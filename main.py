import sys
from PyQt5.QtWidgets import QApplication , QMainWindow,QLabel ,QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon,QPixmap,QFont,QFontDatabase
from PyQt5.QtCore import QTimer,Qt,QTime


class Mainwindows(QWidget):
    def __init__(self):
        super().__init__()      
        self.time_label=QLabel(self)
        self.Timer=QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,500,150)
        self.setWindowIcon(QIcon("pic//25d6cd5a-26c9-47cb-b005-d7976c1fe2c5.jpg"))

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setStyleSheet("background-color: black;" "color : green;" "font-size : 150px; padding:20px;")
        
        Font_id= QFontDatabase.addApplicationFont(r"digital clock\DIGITALDREAMFAT.ttf")
        font_family=QFontDatabase.applicationFontFamilies(Font_id)[0]
        my_font=QFont(font_family,150)
        self.time_label.setFont(my_font)#setting font in python

        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.Timer.timeout.connect(self.updtime)
        self.Timer.start(1000)
        self.updtime()

    def updtime(self):
        currect_time=QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(currect_time)
        


def Main():
    app=QApplication(sys.argv)
    windows=Mainwindows()
    windows.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    Main()