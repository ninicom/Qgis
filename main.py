import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_MainWindows import Ui_MainWindow  # Ensure this file exists and is correctly generated

class MainWindow(QMainWindow):  # Inherit from QMainWindow
    def __init__(self, parent=None):
        super().__init__(parent)  # Initialize QMainWindow
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Setup the UI on this QMainWindow instance
        self.show()  # Show the main window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())  # Start the event loop
