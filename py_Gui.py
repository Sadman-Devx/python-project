# pyQt5 introduction example
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First PyQt5 App')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icone.jpg'))  # Ensure you have an 'icon.png' file in the same directory
        
        

        label_image = QLabel(self)
        pixmap = QPixmap('icone.jpg')  # Ensure you have an 'icon.png' file in the same directory
        label_image.setPixmap(pixmap)
        label_image.setGeometry(0,0, 800, 600)
        label_image.setScaledContents(True)

        label = QLabel('Hello, PyQt5!', self)
        label.setGeometry(0, 0, 200, 200)
        label.setFont(QFont('Arial', 20))
        label.adjustSize()
        label.setStyleSheet("color: #57ab6d;"
                            "background-color: #000000;"
                            "font-weight: bold;"
                            "text-align: center;")
        # label.move(350, 280)
        label.setAlignment(Qt.AlignCenter) # Center the label in the window

        
        # Add a button
        button = QPushButton('Click Me', self)
        button.setGeometry(330, 500, 100, 50)
        button.setStyleSheet("background-color: #57ab6d; color: white; font-weight: bold;")
        button.clicked.connect(self.on_click)

        self.show()
        
    def on_click(self):
        print("Button clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    