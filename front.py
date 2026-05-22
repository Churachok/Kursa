import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGridLayout,
                             QPushButton, QMessageBox, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from back import GameLogic


class PuzzleGUI(QMainWindow):
    """Главное окно игры Пятнашки"""

    def __init__(self):
        super().__init__()
        self.game = GameLogic()
        self.moves = 0

        self.init_ui()
        self.new_game()

    def init_ui(self):
        """Настройка интерфейса"""
        self.setWindowTitle("Пятнашки")
        self.setFixedSize(500, 550)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Верхняя панель со счётчиком ходов
        info_layout = QHBoxLayout()
        self.moves_label = QLabel("Ходы: 0")
        self.moves_label.setFont(QFont("Arial", 14))
        info_layout.addWidget(self.moves_label, alignment=Qt.AlignCenter)
        main_layout.addLayout(info_layout)

        # Игровое поле
        self.game_widget = QWidget()
        self.game_layout = QGridLayout(self.game_widget)
        self.game_layout.setSpacing(8)
        main_layout.addWidget(self.game_widget, alignment=Qt.AlignCenter)

        self.buttons = []

    def new_game(self):
        """Начать новую игру"""
        self.game = GameLogic()
        self.game.start_game()
        self.moves = 0
        self.update_moves_display()
        self.update_ui()

    def update_moves_display(self):
        """Обновить отображение ходов"""
        self.moves_label.setText(f"Ходы: {self.moves}")

    def update_ui(self):
        """Обновить игровое поле"""
        # Очищаем старые кнопки
        for btn in self.buttons:
            btn.deleteLater()
        self.buttons.clear()

        # Очищаем layout
        while self.game_layout.count():
            child = self.game_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Создаём новые кнопки
        for i in range(9):
            row, col = divmod(i, 3)
            value = self.game.board[i]

            if value == 0:
                btn = QPushButton(" ")
                btn.setEnabled(False)
                btn.setStyleSheet("background-color: #cccccc;")
            else:
                btn = QPushButton(str(value))
                btn.clicked.connect(lambda checked, v=value: self.on_tile_click(v))
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #4CAF50;
                        color: white;
                        font-size: 24px;
                        font-weight: bold;
                        border-radius: 8px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                """)

            btn.setFixedSize(100, 100)
            self.game_layout.addWidget(btn, row, col)
            self.buttons.append(btn)

        # Проверка победы
        if self.game.win():
            QMessageBox.information(
                self,
                "Победа!",
                f"Вы собрали пятнашки!\nКоличество ходов: {self.moves}"
            )
            self.close()

    def on_tile_click(self, value):
        """Обработка клика по плитке"""
        if self.game.is_moving(value):
            self.moves += 1
            self.update_moves_display()
            self.update_ui()
        else:
            QMessageBox.warning(self, "Ошибка", "Эту плитку нельзя переместить")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PuzzleGUI()
    window.show()
    sys.exit(app.exec_())
