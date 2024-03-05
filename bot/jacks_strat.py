

class JackStrat:
    def __init__(self):
        self.trusted = []
        self.lib_count = 0
        self.trusted_full = False
    def add_trusted(self, player):
        self.trusted.append(player)

    def check_trusted(self, nominated_pres):
        if nominated_pres in self.trusted:
            return True
        else:
            return False
    def clear_trusted(self):
        print("Game over, Resetting JackStrat trusted.")
        print(f"JackStrat results: trusted players were {self.trusted}" )
        self.trusted.clear()
        self.trusted_full = False
        self.lib_count = 0

    def execute(self, election_result, president, chancellor):
        '''To be exectued in the election clean up until trusted has been filled'''
        if election_result == 'liberal':
            if self.lib_count < 4:
                if president not in self.trusted:
                    self.trusted.append(president)
                    self.lib_count += 1
                if chancellor not in self.trusted:
                    self.trusted.append(chancellor)
                    self.lib_count += 1


            else:
                self.trusted_full = True
    def strat_stats(self, player_list, result):
        correct = 0
        hitler_in_trusted = 0
        for player in player_list:
            print(player.name)

            if player.name in self.trusted:
                print(f"PLAYER IS IN THE TRUSTED LIST WITH ROLE {player.role}")
                if player.role =='Liberal':
                    correct += 1
                if player.role == 'Hitler':
                    hitler_in_trusted = 1
        accuracy = (correct / 4) * 100
        print(f"PLAYERS {player_list} TRUSTED: {self.trusted}" )
        with open("game_stats.txt", "r") as file:
            lines = sum(1 for line in file)
        with open("game_stats.txt", "a") as file:
            game_id = f"game_ {lines}"
            if result == 99:
                game_result = 'game canceled'
            if result == -2:
                game_result = 'facists win by electing hitler'
            if result == -1:
                game_result = "facists win by policies"
            if result == 1:
                game_result = "liberals win by policies"
            if result == 2:
                game_result = "Hitler Killed"
                
            file.write(f"Game ID: {game_id}, Accuracy: {accuracy:.2f}%, Hitler_in_trusted: {hitler_in_trusted} Result: {game_result}\n")


                                    
