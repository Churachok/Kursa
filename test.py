import unittest
from back import GameLogic


class TestGameLogic(unittest.TestCase):
    
    def setUp(self):
        self.game = GameLogic()
    
    def test_init(self):
        self.assertEqual(self.game.is_win, [1, 2, 3, 4, 5, 6, 7, 8, 0])
        self.assertEqual(self.game.board, [])
        self.assertEqual(self.game.empty_index, 8)
        print("Инициализация - есть")
    
    def test_is_win_cp(self):
        win_copy = self.game.is_win_cp()
        self.assertEqual(win_copy, [1, 2, 3, 4, 5, 6, 7, 8, 0])
        self.assertIsNot(win_copy, self.game.is_win)  
        print("Тест копии выигрыша - есть")
    
    def test_rules(self):
        self.game.board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
        self.game.empty_index = 6
        self.game.rules()
        self.assertEqual(self.game.board, [1, 2, 3, 4, 5, 6, 7, 8, 0])
        self.assertEqual(self.game.empty_index, 8)
        print("Начальное состояние - есть")
    
    def test_possible_moves_center(self):
        self.game.board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
        self.game.empty_index = 4
        moves = self.game.possible_moves()
        expected_moves = [1, 7, 3, 5]  
        self.assertEqual(sorted(moves), sorted(expected_moves))
        print("Возможные ходы из центра - есть")
    
    def test_possible_moves_corner(self):
        self.game.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.game.empty_index = 0
        moves = self.game.possible_moves()
        expected_moves = [3, 1]  
        self.assertEqual(sorted(moves), sorted(expected_moves))
        print("Возможные ходы из угла - есть")
    
    def test_possible_moves_edge(self):
        self.game.board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        self.game.empty_index = 7
        moves = self.game.possible_moves()
        expected_moves = [4, 6, 8]  
        self.assertEqual(sorted(moves), sorted(expected_moves))
        print("Возможные ходы с края - есть")
    
    def test_swap(self):
        self.game.board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.game.empty_index = 8
        self.game.swap(7)
        self.assertEqual(self.game.board, [1, 2, 3, 4, 5, 6, 7, 0, 8])
        self.assertEqual(self.game.empty_index, 7)
        print("Перемещение элементов - есть")
    
    def test_start_game(self):
        self.game.start_game()
        self.assertEqual(len(self.game.board), 9)
        self.assertEqual(sorted(self.game.board), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.game.board[self.game.empty_index], 0)
        print("Начало игры - есть")
    
    def test_start_game_randomness(self):
        boards = []
        for i in range(10):
            game = GameLogic()
            game.start_game()
            boards.append(game.board.copy())
        unique_boards = set(tuple(board) for board in boards)
        self.assertGreater(len(unique_boards), 1)
        print("Тест случайного начального места - есть")
    
    def test_is_moving_valid(self):
        self.game.board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        self.game.empty_index = 7
        result = self.game.is_moving(8)
        self.assertTrue(result)
        self.assertEqual(self.game.empty_index, 8)
        self.assertEqual(self.game.board[7], 8)
        print("Корректность перемещения - есть")
    
    def test_is_moving_invalid(self):
        self.game.board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
        self.game.empty_index = 4
        result = self.game.is_moving(1)
        self.assertFalse(result)
        print("Некорректность перемещения - есть")
    
    def test_is_moving_out_of_range(self):
        self.game.board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.game.empty_index = 8
        result = self.game.is_moving(0)
        self.assertFalse(result)
        result = self.game.is_moving(9)
        self.assertFalse(result)
        print("Перемещение вне диапозона - есть")

    def test_win_condition(self):
        self.game.board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertTrue(self.game.win())
        self.game.board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
        self.assertFalse(self.game.win())
        print("Проверка выигрыша - есть")
    
    def test_scenario(self):
        self.game.board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        self.game.empty_index = 7
        self.assertTrue(self.game.is_moving(8))
        self.assertEqual(self.game.board, [1, 2, 3, 4, 5, 6, 7, 8, 0])
        self.assertTrue(self.game.win())
        self.game.rules()
        self.assertEqual(self.game.board, self.game.is_win)
        print("Сценарий игры - есть")


def run_tests():
    print("ТЕСТИРОВАНИЕ ИГРЫ \"ПЯТНАШКИ\"")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGameLogic)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print("ИТОГОВЫЙ ОТЧЁТ")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    if result.wasSuccessful():
        print("\nВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("\nЕСТЬ ПРОВАЛЕННЫЕ ТЕСТЫ!")
        if result.failures:
            print("\nПроваленные тесты:")
            for test, traceback in result.failures:
                print(f"  - {test}")
        if result.errors:
            print("\nТесты с ошибками:")
            for test, traceback in result.errors:
                print(f"  - {test}")
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
