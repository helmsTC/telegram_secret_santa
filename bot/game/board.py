# Board.py

from constants.Cards import playerSets
from constants.Cards import policies
import random
from game.State import State

class Board(object):
    def __init__(self, playercount, game):
        self.state = State()
        self.num_players = playercount
        self.naughtist_track_actions = playerSets[self.num_players]["track"]
        self.policies = random.sample(policies, len(policies))
        self.game = game
        self.discards = []
        self.previous = []
    def reset_policies(self, game_policies):
        if len(game_policies) == 0:
            game_policies = random.sample(policies, len(policies))
        return game_policies
        
    def print_board(self):
        board = "--- Niceist acts ---\n"
        for i in range(5):
            if i < self.state.niceist_track:
                board += u"\u2716\uFE0F" + " " #X
            elif i >= self.state.niceist_track and i == 4:
                board += u"\U0001F54A" + " " #dove
            else:
                board += u"\u25FB\uFE0F" + " " #empty
        board += "\n--- Naughtist acts ---\n"
        for i in range(6):
            if i < self.state.naughtist_track:
                board += u"\u2716\uFE0F" + " " #X
            else:
                action = self.naughtist_track_actions[i]
                if action == None:
                    board += u"\u25FB\uFE0F" + " "  # empty
                elif action == "policy":
                    board += u"\U0001F52E" + " " # crystal
                elif action == "inspect":
                    board += u"\U0001F50E" + " " # inspection glass
                elif action == "kill":
                    board += u"\U0001F5E1" + " " # knife
                elif action == "win":
                    board += u"\u2620" + " " # skull
                elif action == "choose":
                    board += u"\U0001F454" + " " # tie

        board += "\n--- Election counter ---\n"
        for i in range(3):
            if i < self.state.failed_votes:
                board += u"\u2716\uFE0F" + " " #X
            else:
                board += u"\u25FB\uFE0F" + " " #empty

        board += "\n--- Presidential order  ---\n"
        for player in self.game.player_sequence:
            board += player.name + " " + u"\u27A1\uFE0F" + " "
        board = board[:-3]
        board += u"\U0001F501"
        board += "\n\nThere are " + str(len(self.policies)) + " policies left on the pile."
        if self.state.naughtist_track >= 3:
            board += "\n\n" + u"\u203C\uFE0F" + " Beware: If Santa gets elected as Chancellor the naughtists win the game! " + u"\u203C\uFE0F"
        if len(self.state.not_santas) > 0:
            board += "\n\nWe know that the following players are not Santa because they got elected as Chancellor after 3 naughtist policies:\n"
            for nh in self.state.not_santas:
                board += nh.name + ", "
            board = board[:-2]
        return board