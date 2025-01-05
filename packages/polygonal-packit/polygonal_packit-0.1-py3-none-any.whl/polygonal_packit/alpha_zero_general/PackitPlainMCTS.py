import logging
import math

import numpy as np

EPS = 1e-8

log = logging.getLogger(__name__)


class PlainMCTS:
    """
    This class handles the Plain MCTS tree.
    """

    def __init__(self, game, nnet, args):
        self.game = game
        self.nnet = nnet
        self.args = args
        self.Qsa = {}  # stores Q values for s,a (as defined in the paper)
        self.Nsa = {}  # stores #times edge s,a was visited
        self.Ns = {}  # stores #times board s was visited
        self.Ps = {}  # stores initial policy (returned by neural net)

        self.Es = {}  # stores game.getGameEnded ended for board s
        self.Vs = {}  # stores game.getValidMoves for board s

    def getActionProb(self, canonicalBoard, turn, temp=1):
        """
        This function performs numMCTSSims simulations of MCTS starting from
        canonicalBoard.

        Returns:
            probs: a policy vector where the probability of the ith action is
                   proportional to Nsa[(s,a)]**(1./temp)
        """
        for _ in range(self.args.numMCTSSims):
            self.search(canonicalBoard, turn)

        s = self.game.stringRepresentation(canonicalBoard)
        counts = [self.Nsa[(s, a)] if (s, a) in self.Nsa else 0 for a in range(self.game.getActionSize())]

        if temp == 0:
            bestAs = np.array(np.argwhere(counts == np.max(counts))).flatten()
            bestA = np.random.choice(bestAs)
            probs = [0] * len(counts)
            probs[bestA] = 1
            return probs

        counts = [x ** (1. / temp) for x in counts]
        counts_sum = float(sum(counts))
        probs = [x / counts_sum for x in counts]
        # print("sum of probs: ", np.sum(probs))
        return probs

    def search(self, canonicalBoard):
        """
        Perform one iteration of MCTS. Recursively called until a leaf node is found.
        Value and policy are derived from rollouts or heuristics.
        """
        s = self.game.stringRepresentation(canonicalBoard)

        if s not in self.Es:
            self.Es[s] = self.game.getGameEnded(canonicalBoard, 1)
        if self.Es[s] != 0:
            # Terminal node
            return -self.Es[s]

        if s not in self.Ps:
            # Leaf node
            valids = self.game.getValidMoves(canonicalBoard, 1)
            self.Ps[s] = valids / np.sum(valids)  # Uniform probabilities for valid moves
            self.Vs[s] = valids

            # Estimate value using rollouts or heuristics
            v = self.rollout(canonicalBoard)
            self.Ns[s] = 0
            return -v

        valids = self.Vs[s]
        cur_best = -float('inf')
        best_act = -1

        # Pick the action with the highest UCB
        for a in range(self.game.getActionSize()):
            if valids[a]:
                if (s, a) in self.Qsa:
                    u = self.Qsa[(s, a)] + self.args.cpuct * self.Ps[s][a] * math.sqrt(self.Ns[s]) / (
                            1 + self.Nsa[(s, a)])
                else:
                    u = self.args.cpuct * self.Ps[s][a] * math.sqrt(self.Ns[s] + EPS)

                if u > cur_best:
                    cur_best = u
                    best_act = a

        a = best_act
        next_s, next_player = self.game.getNextState(canonicalBoard, 1, a)
        next_s = self.game.getCanonicalForm(next_s, next_player)

        v = self.search(next_s)

        if (s, a) in self.Qsa:
            self.Qsa[(s, a)] = (self.Nsa[(s, a)] * self.Qsa[(s, a)] + v) / (self.Nsa[(s, a)] + 1)
            self.Nsa[(s, a)] += 1
        else:
            self.Qsa[(s, a)] = v
            self.Nsa[(s, a)] = 1

        self.Ns[s] += 1
        return -v

    def rollout(self, canonicalBoard):
        """
        Perform a random simulation from the current board state until the game ends.
        """
        curBoard = canonicalBoard
        curPlayer = 1

        while True:
            valids = self.game.getValidMoves(curBoard, curPlayer)
            actions = np.where(valids)[0]
            action = np.random.choice(actions)

            next_state, next_player = self.game.getNextState(curBoard, curPlayer, action)
            curBoard = self.game.getCanonicalForm(next_state, next_player)
            curPlayer = next_player

            game_result = self.game.getGameEnded(curBoard, curPlayer)
            if game_result != 0:
                return game_result

