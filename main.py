from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime
import sys
import ctypes

weather_data  = {
    'day1': {'direction':'북북동','huminity':'15%','rainfall':'0mm','rainform':'없음','temperature':'20°C','windspeed':'6Km/h'},
    'day2': {'direction':'서','huminity':'13%','rainfall':'21mm','rainform':'비','temperature':'17°C','windspeed':'3Km/h'},
    'day3': {'direction':'남동','huminity':'12%','rainfall':'64mm','rainform':'소나기','temperature':'24°C','windspeed':'5Km/h'},
    'day4': {'direction':'북북서','huminity':'17%','rainfall':'0mm','rainform':'없음','temperature':'23°C','windspeed':'7Km/h'},
    'day5': {'direction':'남서','huminity':'19%','rainfall':'0mm','rainform':'없음','temperature':'22°C','windspeed':'8Km/h'},
    'day6': {'direction':'북서','huminity':'20%','rainfall':'0mm','rainform':'없음','temperature':'21°C','windspeed':'9Km/h'},
    'day7': {'direction':'남남동','huminity':'7%','rainfall':'17mm','rainform':'비','temperature':'20°C','windspeed':'10Km/h'},
}


class Ui_MainWindow(QtWidgets.QMainWindow):

    global weather_data

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.timer = QtCore.QTimer(self)               
        self.timer.start(1000)                
        self.timer.timeout.connect(self.setTime)
        self.timer2 = QtCore.QTimer(self)               
        self.timer2.start(60000)                
        self.timer2.timeout.connect(self.setWeather)
        self.weather_count= 1
        self.log = ''
        self.on_alam = False
        self.blink = True
        self.blink_count = 0
        self.blink_timer = None

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

        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(0,self.program_height*0.05, self.program_width, self.program_height*0.9))

        self.mainWidget_1 = QtWidgets.QWidget(self.mainWidget)
        self.mainWidget_1.setGeometry(QtCore.QRect(0,0,self.program_width*0.8,self.program_height*0.8))
        self.mainWidget_1.setStyleSheet("border : 1px solid black;")

        self.mainWidget_2 = QtWidgets.QLabel(self.mainWidget)
        self.mainWidget_2.setGeometry(QtCore.QRect(self.program_width*0.8,0,self.program_width*0.2,self.program_height*0.9))
        self.mainWidget_2.setStyleSheet("border : 1px solid black;")
        
        self.logWidget = QtWidgets.QLabel(self.mainWidget_2)
        self.logWidget.setGeometry(QtCore.QRect(20,20,self.program_width*0.2 - 40,self.program_height*0.9 - 40))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(20)
        self.logWidget.setFont(font)
        self.logWidget.setAlignment(QtCore.Qt.AlignTop)
        self.logWidget.setStyleSheet("border-radius : 20px;")

        self.mainWidget_3 = QtWidgets.QWidget(self.mainWidget)
        self.mainWidget_3.setGeometry(QtCore.QRect(0,self.program_height*0.8,self.program_width*0.8,self.program_height*0.1))
        self.mainWidget_3.setStyleSheet("border : 1px solid black;")

        self.weatherWidget_1 = QtWidgets.QWidget(self.mainWidget_3)
        self.weatherWidget_1.setGeometry(QtCore.QRect(100,30,160,35))
        self.weatherWidget_1.setStyleSheet("background-color:#8B008B;\n border-radius:15px;border:none;")
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
        self.weatherWidget_1_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0); border:none;")
        self.weatherWidget_1_2.setText("풍향 : 북북동")

        self.weatherWidget_2 = QtWidgets.QWidget(self.mainWidget_3)
        self.weatherWidget_2.setGeometry(QtCore.QRect(320,30,160,35))
        self.weatherWidget_2.setStyleSheet("background-color:#8B008B;\n border-radius:15px;border:none;")
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
        self.weatherWidget_2_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);border:none;")
        self.weatherWidget_2_2.setText("습도 : 15%")

        self.weatherWidget_3 = QtWidgets.QWidget(self.mainWidget_3)
        self.weatherWidget_3.setGeometry(QtCore.QRect(540,30,160,35))
        self.weatherWidget_3.setStyleSheet("background-color:#8B008B;\n border-radius:15px;border:none;")
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
        self.weatherWidget_3_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);border:none;")
        self.weatherWidget_3_2.setText("강수량 : 0mm")

        self.weatherWidget_4 = QtWidgets.QWidget(self.mainWidget_3)
        self.weatherWidget_4.setGeometry(QtCore.QRect(760,30,160,35))
        self.weatherWidget_4.setStyleSheet("background-color:#8B008B;\n border-radius:15px;border:none;")
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
        self.weatherWidget_4_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);border:none;")
        self.weatherWidget_4_2.setText("강수형태 : 없음")

        self.weatherWidget_5 = QtWidgets.QWidget(self.mainWidget_3)
        self.weatherWidget_5.setGeometry(QtCore.QRect(980,30,160,35))
        self.weatherWidget_5.setStyleSheet("background-color:#8B008B;\n border-radius:15px;border:none;")
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
        self.weatherWidget_5_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);border:none;")
        self.weatherWidget_5_2.setText("기온 : 20°C")

        self.weatherWidget_6 = QtWidgets.QWidget(self.mainWidget_3)
        self.weatherWidget_6.setGeometry(QtCore.QRect(1200,30,160,35))
        self.weatherWidget_6.setStyleSheet("background-color:#8B008B;\n border-radius:15px;border:none;")
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
        self.weatherWidget_6_2.setStyleSheet("color:white; background-color: rgba(0,0,0,0);border:none;")
        self.weatherWidget_6_2.setText("풍속 : 10Km/h")

        
        self.bottomWidget = QtWidgets.QWidget(self.centralwidget)
        self.bottomWidget.setGeometry(QtCore.QRect(0,self.program_height*0.95,self.program_width,self.program_height*0.05))
        self.bottomWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 #483D8B, stop:1 #6A5ACD);")

        self.logoWidget = QtWidgets.QLabel(self.bottomWidget)
        self.logoWidget.setGeometry(QtCore.QRect(40,7,160,32))
        self.logoImage = QtGui.QImage("logo-fireguard.png").scaled(QtCore.QSize(160,32))
        self.logoWidget.setPixmap(QtGui.QPixmap(self.logoImage))

        self.timeWiget = QtWidgets.QLabel(self.bottomWidget)
        self.timeWiget.setGeometry(QtCore.QRect(250,8,280,35))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(11)
        self.timeWiget.setFont(font)
        self.timeWiget.setStyleSheet("color:white; background-color: #0A1931; border-radius:15px;")
        self.timeWiget.setAlignment(QtCore.Qt.AlignCenter)
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.timeWiget.setText(now.toString(QtCore.Qt.DefaultLocaleLongDate)+' '+time.toString())

        self.alam = QtWidgets.QLabel(self.centralwidget)
        self.alam.setGeometry(QtCore.QRect(self.program_width*0.25,self.program_height*0.4,self.program_width*0.5,self.program_height*0.2))
        self.alam.setStyleSheet("color:yellow; background-color: red; border:3px solid black; border-radius:20px;")
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(50)
        self.alam.setFont(font)
        self.alam.setAlignment(QtCore.Qt.AlignCenter)
        self.alam.setText('산  불  발  생')
        self.alam.hide()

        

    def setTime(self):
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.timeWiget.setText(now.toString(QtCore.Qt.DefaultLocaleLongDate)+' '+time.toString())

    def setWeather(self):
        day = ''
        if self.weather_count == 1:
            day = 'day1'
        elif self.weather_count == 2:
            day = 'day2'
        elif self.weather_count == 3:
            day = 'day3'
        elif self.weather_count == 4:
            day = 'day4'
        elif self.weather_count == 5:
            day = 'day5'
        elif self.weather_count == 6:
            day = 'day6'
        elif self.weather_count == 7:
            day = 'day7'
        wd = weather_data[day]
        self.weatherWidget_1_2.setText("풍향 : "+wd['direction'])
        self.weatherWidget_2_2.setText("습도 : "+wd['huminity'])
        self.weatherWidget_3_2.setText("강수량 : "+wd['rainfall'])
        self.weatherWidget_4_2.setText("강수형태 : "+wd['rainform'])
        self.weatherWidget_5_2.setText("기온 : "+wd['temperature'])
        self.weatherWidget_6_2.setText("풍속 : "+wd['windspeed'])
        self.weather_count = self.weather_count + 1

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            self.onAlam()
        
    def onAlam(self):
        if self.on_alam == False:
            self.on_alam = True
            time = QTime.currentTime()
            self.log = self.log + time.toString()+' : 산불 발생\n'
            self.logWidget.setText(self.log)
            self.alam.show()
            self.blink = False
            self.blink_timer = QtCore.QTimer(self)
            self.blink_timer.timeout.connect(self.blinkAlam)
            self.blink_timer.start(1000)

    def blinkAlam(self):
        if self.blink == False:
            self.alam.hide()
            self.blink = True
        else:
            self.alam.show()
            self.blink = False
        if self.blink_count <5:
            self.blink_count = self.blink_count + 1
        else:
            self.blink_timer.stop()
            self.blink_count = 0
            self.on_alam = False
            self.alam.hide()
            self.blink = True

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()

    sys.exit(app.exec_())