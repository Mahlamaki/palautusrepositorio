import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_players_of_team(self):
        players = self.stats.team("EDM")
        #testataan, että tiimin koko on oikein
        self.assertEqual(len(players), 3)

    def test_search_player(self):
        player = self.stats.search("Semenko")
        #tarkistetaan että löytyy haluttu pelaaja
        self.assertEqual(player.name, "Semenko")

    def test_top_sorted_by_points(self):
        players = self.stats.top(2,SortBy.POINTS)
        #testataan, että antaa top listan oikein, sortattu kokonaispisteillä
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[-1].name, "Lemieux")

    def test_top_sorted_by_goals(self):
        players = self.stats.top(2,SortBy.GOALS)
        #testataan, että antaa top listan oikein, sortattu maaleilla
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[-1].name, "Yzerman")
    def test_top_sorted_by_poinst(self):

        players = self.stats.top(2,SortBy.ASSISTS)
        #testataan, että antaa top listan oikein,sortattu syötöillä
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[-1].name, "Yzerman")

    def test_search_none(self):
        player = self.stats.search("supersusu")      
        #testataan että toimii kun etsitään olemattomalla pelaajalla
        self.assertEqual(player, None)
