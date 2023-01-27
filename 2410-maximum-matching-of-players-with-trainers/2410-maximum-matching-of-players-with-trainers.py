class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        player_pointer = 0
        trainer_pointer = 0
        play_size = len(players)
        train_size = len(trainers)
        counter = 0
        while player_pointer < play_size and trainer_pointer < train_size:
            if players[player_pointer] <= trainers[trainer_pointer]:
                counter += 1
                player_pointer += 1
                trainer_pointer += 1
            else:
                trainer_pointer += 1
        return counter
        