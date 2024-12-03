import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from ui_MainWindows import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window's properties
        self.setWindowTitle("PySide6 QMainWindow Example")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        # Add a central widget (QMainWindow requires one)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Add a layout and some widgets
        layout = QVBoxLayout()
        label = QLabel("Welcome to PySide6 QMainWindow!")
        layout.addWidget(label)

        self.central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec())
