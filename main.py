from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime
import sys
import ctypes
from multiprocessing import Process,Pipe
from datetime import datetime,timedelta
import os
import numpy as np


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.timer = QtCore.QTimer(self)               
        self.timer.start(1000)                
        self.timer.timeout.connect(self.setTime)   

    def setupUi(self):
        self.program_height = ctypes.windll.user32.GetSystemMetrics(1) - 70
        self.program_width = ctypes.windll.user32.GetSystemMetrics(0)
        self.setObjectName("MainWindow")
        self.setFixedSize(self.program_width, self.program_height)
        self.setWindowTitle("강릉 산불 지능형 시스템")
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QtCore.QRect(0,0,self.program_width,self.program_height))
        self.centralwidget.setStyleSheet("background-color: white")

        self.headerWidget = QtWidgets.QWidget(self.centralwidget)
        self.headerWidget.setGeometry(QtCore.QRect(0,0,self.program_width,self.program_height*0.05))
        self.headerWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));")

        self.titleWidget = QtWidgets.QLabel(self.headerWidget)
        self.titleWidget.setGeometry(QtCore.QRect(30,5,250,45))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(15)
        self.titleWidget.setFont(font)
        self.titleWidget.setStyleSheet("color:white; background-color: rgba(0,0,0,0);")
        self.titleWidget.setText("강릉 산불 지능형 시스템")

        self.weatherWidget_1 = QtWidgets.QWidget(self.headerWidget)
        self.weatherWidget_1.setGeometry(QtCore.QRect(350,7,160,35))
        self.weatherWidget_1.setStyleSheet("background-color:#8B008B;\n border-radius:15px;")
        self.weatherWidget_1_1 = QtWidgets.QLabel(self.weatherWidget_1)
        self.weatherWidget_1_1.setGeometry(QtCore.QRect(7,5,27,27))
        self.weatherWidget_1_1.setPixmap(QtGui.QPixmap("weather_icon_direction-wind.png"))
        self.weatherWidget_1_2 = QtWidgets.QLabel(self.weatherWidget_1)
        self.weatherWidget_1_2.setGeometry(QtCore.QRect(45,3,110,30))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.weatherWidget_1_2.setFont(font)
        self.weatherWidget_1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherWidget_1_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);")
        self.weatherWidget_1_2.setText("풍향 : 북북동")

        self.weatherWidget_2 = QtWidgets.QWidget(self.headerWidget)
        self.weatherWidget_2.setGeometry(QtCore.QRect(520,7,160,35))
        self.weatherWidget_2.setStyleSheet("background-color:#8B008B;\n border-radius:15px;")
        self.weatherWidget_2_1 = QtWidgets.QLabel(self.weatherWidget_2)
        self.weatherWidget_2_1.setGeometry(QtCore.QRect(7,5,27,27))
        self.weatherWidget_2_1.setPixmap(QtGui.QPixmap("weather_icon_humidity.png"))
        self.weatherWidget_2_2 = QtWidgets.QLabel(self.weatherWidget_2)
        self.weatherWidget_2_2.setGeometry(QtCore.QRect(45,3,110,30))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.weatherWidget_2_2.setFont(font)
        self.weatherWidget_2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherWidget_2_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);")
        self.weatherWidget_2_2.setText("습도 : 15%")

        self.weatherWidget_3 = QtWidgets.QWidget(self.headerWidget)
        self.weatherWidget_3.setGeometry(QtCore.QRect(690,7,160,35))
        self.weatherWidget_3.setStyleSheet("background-color:#8B008B;\n border-radius:15px;")
        self.weatherWidget_3_1 = QtWidgets.QLabel(self.weatherWidget_3)
        self.weatherWidget_3_1.setGeometry(QtCore.QRect(7,5,27,27))
        self.weatherWidget_3_1.setPixmap(QtGui.QPixmap("weather_icon_rainfall.png"))
        self.weatherWidget_3_2 = QtWidgets.QLabel(self.weatherWidget_3)
        self.weatherWidget_3_2.setGeometry(QtCore.QRect(45,3,110,30))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.weatherWidget_3_2.setFont(font)
        self.weatherWidget_3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherWidget_3_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);")
        self.weatherWidget_3_2.setText("강수량 : 0mm")

        self.weatherWidget_4 = QtWidgets.QWidget(self.headerWidget)
        self.weatherWidget_4.setGeometry(QtCore.QRect(860,7,160,35))
        self.weatherWidget_4.setStyleSheet("background-color:#8B008B;\n border-radius:15px;")
        self.weatherWidget_4_1 = QtWidgets.QLabel(self.weatherWidget_4)
        self.weatherWidget_4_1.setGeometry(QtCore.QRect(7,5,27,27))
        self.weatherWidget_4_1.setPixmap(QtGui.QPixmap("weather_icon_rainform.png"))
        self.weatherWidget_4_2 = QtWidgets.QLabel(self.weatherWidget_4)
        self.weatherWidget_4_2.setGeometry(QtCore.QRect(45,3,110,30))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.weatherWidget_4_2.setFont(font)
        self.weatherWidget_4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherWidget_4_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);")
        self.weatherWidget_4_2.setText("강수형태 : 없음")\

        self.weatherWidget_5 = QtWidgets.QWidget(self.headerWidget)
        self.weatherWidget_5.setGeometry(QtCore.QRect(1030,7,160,35))
        self.weatherWidget_5.setStyleSheet("background-color:#8B008B;\n border-radius:15px;")
        self.weatherWidget_5_1 = QtWidgets.QLabel(self.weatherWidget_5)
        self.weatherWidget_5_1.setGeometry(QtCore.QRect(7,5,27,27))
        self.weatherWidget_5_1.setPixmap(QtGui.QPixmap("weather_icon_temperature.png"))
        self.weatherWidget_5_2 = QtWidgets.QLabel(self.weatherWidget_5)
        self.weatherWidget_5_2.setGeometry(QtCore.QRect(45,3,110,30))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.weatherWidget_5_2.setFont(font)
        self.weatherWidget_5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherWidget_5_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);")
        self.weatherWidget_5_2.setText("기온 : 20°C")

        self.weatherWidget_6 = QtWidgets.QWidget(self.headerWidget)
        self.weatherWidget_6.setGeometry(QtCore.QRect(1200,7,160,35))
        self.weatherWidget_6.setStyleSheet("background-color:#8B008B;\n border-radius:15px;")
        self.weatherWidget_6_1 = QtWidgets.QLabel(self.weatherWidget_6)
        self.weatherWidget_6_1.setGeometry(QtCore.QRect(7,5,27,27))
        self.weatherWidget_6_1.setPixmap(QtGui.QPixmap("weather_icon_wind-speed.png"))
        self.weatherWidget_6_2 = QtWidgets.QLabel(self.weatherWidget_6)
        self.weatherWidget_6_2.setGeometry(QtCore.QRect(45,3,110,30))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.weatherWidget_6_2.setFont(font)
        self.weatherWidget_6_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherWidget_6_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);")
        self.weatherWidget_6_2.setText("풍속 : 10Km/h")

        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(0,self.program_height*0.05, self.program_width, self.program_height*0.9))

        self.mainWidget_1 = QtWidgets.QWidget(self.mainWidget)
        self.mainWidget_1.setGeometry(QtCore.QRect(0,0,self.program_width*0.5,self.program_height*0.45))
        self.mainWidget_1.setStyleSheet("border : 1px solid white; background-color: #9370DB;")

        self.mainWidget_2 = QtWidgets.QWidget(self.mainWidget)
        self.mainWidget_2.setGeometry(QtCore.QRect(self.program_width*0.5,0,self.program_width*0.5,self.program_height*0.45))
        self.mainWidget_2.setStyleSheet("border : 1px solid white; background-color: #9370DB;")

        self.mainWidget_3 = QtWidgets.QWidget(self.mainWidget)
        self.mainWidget_3.setGeometry(QtCore.QRect(0,self.program_height*0.45,self.program_width*0.5,self.program_height*0.45))
        self.mainWidget_3.setStyleSheet("border : 1px solid white; background-color: #9370DB;")

        self.mainWidget_4 = QtWidgets.QWidget(self.mainWidget)
        self.mainWidget_4.setGeometry(QtCore.QRect(self.program_width*0.5,self.program_height*0.45,self.program_width*0.5,self.program_height*0.45))
        self.mainWidget_4.setStyleSheet("border : 1px solid white; background-color: #9370DB;")
        
        self.bottomWidget = QtWidgets.QWidget(self.centralwidget)
        self.bottomWidget.setGeometry(QtCore.QRect(0,self.program_height*0.95,self.program_width,self.program_height*0.05))
        self.bottomWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 #483D8B, stop:1 #6A5ACD);")

        self.logoWidget = QtWidgets.QLabel(self.bottomWidget)
        self.logoWidget.setGeometry(QtCore.QRect(40,7,210,35))
        self.logoImage = QtGui.QImage("logo-fireguard.png").scaled(QtCore.QSize(210,35))
        self.logoWidget.setPixmap(QtGui.QPixmap(self.logoImage))

        self.timeWiget = QtWidgets.QLabel(self.bottomWidget)
        self.timeWiget.setGeometry(QtCore.QRect(300,8,280,35))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.timeWiget.setFont(font)
        self.timeWiget.setStyleSheet("color:white; background-color: #0A1931; border-radius:15px;")
        self.timeWiget.setAlignment(QtCore.Qt.AlignCenter)
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.timeWiget.setText(now.toString(QtCore.Qt.DefaultLocaleLongDate)+' '+time.toString())

    def setTime(self):
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.timeWiget.setText(now.toString(QtCore.Qt.DefaultLocaleLongDate)+' '+time.toString())
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()

    sys.exit(app.exec_())