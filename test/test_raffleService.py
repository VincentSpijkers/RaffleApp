import unittest

from RaffleService import RaffleService


class TestRaffleService(unittest.TestCase):

    def setUp(self):
        self.test_pool = ['__TestName__']
        self.raffle_service = RaffleService('test_pool.txt')

    def test_raffle_withSingleItemList_toBeTestValue(self):
        #act
        raffled_player = self.raffle_service.raffle(self.test_pool)
        expected = '__TestName__'
        #assert
        self.assertEqual(raffled_player, expected)

    def test_raffle_chance_withSingleItemList_toBe100PerCent(self):
        # act
        raffle_chance = self.raffle_service.raffle_chance('__TestName__', self.test_pool)
        expected = 100

        # assert
        self.assertEqual(raffle_chance, expected)

    def test_raffle_amount_withSingleItemList_toBeOne(self):
        # act
        raffle_amount = self.raffle_service.raffle_amount('__TestName__', self.test_pool)
        expected = 1

        # assert
        self.assertEqual(raffle_amount, expected)