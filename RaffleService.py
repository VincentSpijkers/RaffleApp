import random

from WriterService import WriterService


class RaffleService:
    def __init__(self, raffle_pool_name):
        self.writer_service = WriterService(raffle_pool_name)

    def handle_raffle(self, players):
        raffled_player = self.raffle(players)
        self.update_pool_chances(raffled_player, players)
        return raffled_player

    def raffle(self, players):
        raffle_index = random.randint(0, len(players)-1)
        raffled_player = players[raffle_index]

        return raffled_player

    def update_pool_chances(self, raffled_player, players):
        self.writer_service.reset_player(raffled_player, players)

    def raffle_chance(self, player_name, players):
        players_amount = len(players)
        current_player_occurrence = players.count(player_name)

        return round(current_player_occurrence / players_amount * 100)

    def raffle_amount(self, player_name, players):
        return players.count(player_name)