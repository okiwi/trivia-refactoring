from random import randrange
import oldtrivia
import trivia

__author__ = 'gvincent'

import unittest


class TestTrivia(unittest.TestCase):

    def setUp(self):
        self.game = trivia.Game()
        self.old_game = oldtrivia.Game()
        print '---------------------'

    def test_instance_game(self):
        self.assertTrue(self.game, trivia.Game)

    def test_new_game_has_no_player(self):
        self.assertEqual(0, len(self.game.players))

    def test_add_new_player(self):
        self.game.add("Bob")
        self.assertEqual(1, len(self.game.players))

    def test_roll_raise_exception_if_no_player(self):
        with self.assertRaises(IndexError) as c:
            self.game.roll(randrange(-10, 10))

    def test_random_test(self):
        for i in range(randrange(4) + 1):
            player_name = 'player' + str(i)
            self.game.add(player_name)
            self.old_game.add(player_name)
        self.assertEqual(self.game.__dict__, self.old_game.__dict__)
        for i in range(randrange(20)):
            self.game.roll(i)
            self.old_game.roll(i)
        self.assertEqual(self.game.__dict__, self.old_game.__dict__)

    def test_is_playable(self):
        self.assertFalse(self.game.is_playable())
        self.game.add("Bob")
        self.game.add("Ana")
        self.assertTrue(self.game.is_playable())

    def test_wrong_answer(self):
        self.game.add("Bob")
        self.game.wrong_answer()
        self.assertTrue(self.game.in_penalty_box[0])

    def test_whatever_the_answer_change_player(self):
        self.game.add("Bob")
        self.game.add("Ana")
        self.game.was_correctly_answered()
        self.assertEqual("Ana", self.game.players[self.game.current_player])
        self.game.wrong_answer()
        self.assertEqual("Bob", self.game.players[self.game.current_player])

    def test_roll_modulo_2_stay_in_penalty_box(self):
        self.game.add("Bob")
        self.game.wrong_answer()
        self.game.roll(2)
        self.assertFalse(self.game.is_getting_out_of_penalty_box)

    def test_roll_not_modulo_2_get_out_penalty_box(self):
        self.game.add("Bob")
        self.game.wrong_answer()
        self.game.roll(3)
        self.assertTrue(self.game.is_getting_out_of_penalty_box)

    def test_game_has_12_places(self):
        self.game.add("Bob")
        self.game.wrong_answer()
        self.game.roll(12)
        self.assertEquals(0, self.game.places[0])

    def test_correct_answer_earn_1_coin(self):
        self.game.add("Bob")
        self.game.was_correctly_answered()
        self.assertEqual(1, self.game.purses[0])

    def test_six_good_answer_game_end(self):
        self.game.add("Bob")
        for i in range(6):
            self.assertTrue(self.game._did_player_win())
            self.game.was_correctly_answered()
        self.assertFalse(self.game._did_player_win())

    def test_was_correctly_answered_with_penalty_box(self):
        self.game.add("Bob")
        self.game.wrong_answer()
        self.game.roll(2)
        self.assertTrue(self.game.was_correctly_answered())

if __name__ == '__main__':
    unittest.main()
