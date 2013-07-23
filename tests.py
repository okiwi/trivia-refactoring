import trivia
import unittest

GAME_DICT = {
    'sports_questions': [
        'Sports Question 0', 'Sports Question 1', 'Sports Question 2', 'Sports Question 3', 'Sports Question 4', 'Sports Question 5', 'Sports Question 6', 'Sports Question 7', 'Sports Question 8', 'Sports Question 9', 'Sports Question 10', 'Sports Question 11', 'Sports Question 12', 'Sports Question 13', 'Sports Question 14', 'Sports Question 15', 'Sports Question 16', 'Sports Question 17', 'Sports Question 18', 'Sports Question 19', 'Sports Question 20', 'Sports Question 21', 'Sports Question 22', 'Sports Question 23', 'Sports Question 24', 'Sports Question 25', 'Sports Question 26', 'Sports Question 27', 'Sports Question 28', 'Sports Question 29', 'Sports Question 30', 'Sports Question 31', 'Sports Question 32', 'Sports Question 33', 'Sports Question 34', 'Sports Question 35', 'Sports Question 36', 'Sports Question 37', 'Sports Question 38', 'Sports Question 39', 'Sports Question 40', 'Sports Question 41', 'Sports Question 42', 'Sports Question 43', 'Sports Question 44', 'Sports Question 45', 'Sports Question 46', 'Sports Question 47', 'Sports Question 48', 'Sports Question 49'], 'places': [0, 0, 0, 0, 0, 0], 'rock_questions': ['Rock Question 0', 'Rock Question 1', 'Rock Question 2', 'Rock Question 3', 'Rock Question 4', 'Rock Question 5', 'Rock Question 6', 'Rock Question 7', 'Rock Question 8', 'Rock Question 9', 'Rock Question 10', 'Rock Question 11', 'Rock Question 12', 'Rock Question 13', 'Rock Question 14', 'Rock Question 15', 'Rock Question 16', 'Rock Question 17', 'Rock Question 18', 'Rock Question 19', 'Rock Question 20', 'Rock Question 21', 'Rock Question 22', 'Rock Question 23', 'Rock Question 24', 'Rock Question 25', 'Rock Question 26', 'Rock Question 27', 'Rock Question 28', 'Rock Question 29', 'Rock Question 30', 'Rock Question 31', 'Rock Question 32', 'Rock Question 33', 'Rock Question 34', 'Rock Question 35', 'Rock Question 36', 'Rock Question 37', 'Rock Question 38', 'Rock Question 39', 'Rock Question 40', 'Rock Question 41', 'Rock Question 42', 'Rock Question 43', 'Rock Question 44', 'Rock Question 45', 'Rock Question 46', 'Rock Question 47', 'Rock Question 48', 'Rock Question 49'], 'science_questions': ['Science Question 0', 'Science Question 1', 'Science Question 2', 'Science Question 3', 'Science Question 4', 'Science Question 5', 'Science Question 6', 'Science Question 7', 'Science Question 8', 'Science Question 9', 'Science Question 10', 'Science Question 11', 'Science Question 12', 'Science Question 13', 'Science Question 14', 'Science Question 15', 'Science Question 16', 'Science Question 17', 'Science Question 18', 'Science Question 19', 'Science Question 20', 'Science Question 21', 'Science Question 22', 'Science Question 23', 'Science Question 24', 'Science Question 25', 'Science Question 26', 'Science Question 27', 'Science Question 28', 'Science Question 29', 'Science Question 30', 'Science Question 31', 'Science Question 32', 'Science Question 33', 'Science Question 34', 'Science Question 35', 'Science Question 36', 'Science Question 37', 'Science Question 38', 'Science Question 39', 'Science Question 40', 'Science Question 41', 'Science Question 42', 'Science Question 43', 'Science Question 44', 'Science Question 45', 'Science Question 46', 'Science Question 47', 'Science Question 48', 'Science Question 49'], 'purses': [0, 0, 0, 0, 0, 0], 'players': [], 'current_player': 0, 'is_getting_out_of_penalty_box': False, 'in_penalty_box': [0, 0, 0, 0, 0, 0], 'pop_questions': ['Pop Question 0', 'Pop Question 1', 'Pop Question 2', 'Pop Question 3', 'Pop Question 4', 'Pop Question 5', 'Pop Question 6', 'Pop Question 7', 'Pop Question 8', 'Pop Question 9', 'Pop Question 10', 'Pop Question 11', 'Pop Question 12', 'Pop Question 13', 'Pop Question 14', 'Pop Question 15', 'Pop Question 16', 'Pop Question 17', 'Pop Question 18', 'Pop Question 19', 'Pop Question 20', 'Pop Question 21', 'Pop Question 22', 'Pop Question 23', 'Pop Question 24', 'Pop Question 25', 'Pop Question 26', 'Pop Question 27', 'Pop Question 28', 'Pop Question 29', 'Pop Question 30', 'Pop Question 31', 'Pop Question 32', 'Pop Question 33', 'Pop Question 34', 'Pop Question 35', 'Pop Question 36', 'Pop Question 37', 'Pop Question 38', 'Pop Question 39', 'Pop Question 40', 'Pop Question 41', 'Pop Question 42', 'Pop Question 43', 'Pop Question 44', 'Pop Question 45', 'Pop Question 46', 'Pop Question 47', 'Pop Question 48', 'Pop Question 49']}

class TestGame(unittest.TestCase):
    def test_instance(self):
        game = trivia.Game()
        self.assertTrue(game, trivia.Game)

    def test_create_game_with_no_players(self):
        game = trivia.Game()
        self.assertEqual(len(game.players), 0)

    def test_create_game_with_six_places(self):
        game = trivia.Game()
        self.assertEqual(len(game.places), 6)

    def test_add_player(self):
        game = trivia.Game()
        game.add('Pierre')
        self.assertEqual(len(game.players), 1)
        game.add('sam')
        self.assertEqual(len(game.players), 2)

    def test_wrong_answer_put_current_player_in_penalty_box(self):
        game = trivia.Game()
        game.add('Pierre')
        game.wrong_answer()
        self.assertTrue(game.in_penalty_box[game.current_player])
        
    def test_first_added_player_is_current_player(self):
        game = trivia.Game()
        game.add('Pierre')
        game.add('Paul')
        self.assertEqual(game.current_player, 0)  
        
    def test_alternate_players(self):
        game = trivia.Game()
        game.add('Pierre')
        game.add('Paul')
        game.roll(5)
        self.assertEqual(game.current_player, 0)
        game.was_correctly_answered()
        self.assertEqual(game.current_player, 1)
       
unittest.main()
