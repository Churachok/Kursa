import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGridLayout,
                             QPushButton, QMessageBox, QWidget)
from back import GameLogic


class PuzzleGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = GameLogic()
        self.game.start_game()

        self.setWindowTitle("Пятнашки")
        self.setFixedSize(400, 400)
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E3440;
            }
        """)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.layout.setSpacing(5)

        self.buttons = []
        self.update_ui()

    def update_ui(self):
        for btn in self.buttons:
            btn.deleteLater()
        self.buttons.clear()

        for i in range(9):
            row, col = divmod(i, 3)
            value = self.game.board[i]

            if value == 0:
                btn = QPushButton(" ")
                btn.setEnabled(False)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #4C566A;
                        border-radius: 8px;
                    }
                """)
            else:
                btn = QPushButton(str(value))
                btn.clicked.connect(lambda checked, v=value: self.on_tile_click(v))
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #88C0D0;
                        color: #2E3440;
                        font-size: 24px;
                        font-weight: bold;
                        border-radius: 8px;
                    }
                    QPushButton:hover {
                        background-color: #81A1C1;
                    }
                    QPushButton:pressed {
                        background-color: #5E81AC;
                    }
                """)

            btn.setFixedSize(100, 100)
            self.layout.addWidget(btn, row, col)
            self.buttons.append(btn)

        if self.game.win():
            QMessageBox.information(self, "Победа!", "Вы собрали пятнашки!")
            self.close()

    def on_tile_click(self, value):
        if self.game.is_moving(value):
            self.update_ui()
        else:
            QMessageBox.warning(self, "Ошибка", "Эту плитку нельзя переместить")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PuzzleGUI()
    window.show()
    sys.exit(app.exec_())
