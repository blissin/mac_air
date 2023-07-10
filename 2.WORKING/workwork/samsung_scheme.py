import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton, QLineEdit

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Samsung-inspired Dark Mode Application updated")
        self.setGeometry(100, 100, 600, 800)

        # Set the menubar and status bar color to black
        self.setStyleSheet("""
            QMenuBar {
                background-color: #000000;
                color: #FFFFFF;
            }
            QStatusBar {
                background-color: #000000;
                color: #FFFFFF;
            }
        """)

        # Create a central widget and set it as the main window's central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Create and add labels to the layout
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # Create and add line edits to the layout
        line_edit1 = QLineEdit()
        line_edit2 = QLineEdit()
        line_edit3 = QLineEdit()
        layout.addWidget(line_edit1)
        layout.addWidget(line_edit2)
        layout.addWidget(line_edit3)

        # Create and add push buttons to the layout
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # Apply Samsung-inspired dark mode color scheme to the labels, line edits, and push buttons
        self.setStyleSheet("""
            QLabel {
                background-color: #001933;
                color: #FFFFFF;
                padding: 10px;
                font-size: 18px;
                border-radius: 8px;
            }
            QLineEdit {
                background-color: #003366;
                color: #FFFFFF;
                padding: 10px;
                font-size: 18px;
                border-radius: 8px;
            }
            QPushButton {
                background-color: #001933;
                color: #FFFFFF;
                padding: 10px;
                font-size: 18px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #FF6600;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
