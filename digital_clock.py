# python PyQt5 digital clock

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont,QFontDatabase

class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.vabox = QVBoxLayout()

        self.iniUI()


    def iniUI(self):
        self.setWindowTitle("digital clock")
        self.setGeometry(600,400,300,100)
        
        self.vabox.addWidget(self.time_label)
        self.setLayout(self.vabox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet(
            "color: #04cf18;"
            "background-color: #000000;"
            "font-size: 30px;"
            "font-weight: bold;"      
        )

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF") # Load custom font
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0] # Get the font family name
        my_font = QFont(font_families, 50) # Set font size to 50
        self.time_label.setFont(my_font) # Apply the custom font to the label
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss AP') # Format time as HH:MM:SS AM/PM
        self.time_label.setText(current_time)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Digital_clock()
    clock.show()
    sys.exit(app.exec_())

