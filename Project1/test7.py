# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test5.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Adafruit_DHT
import time
sensor = Adafruit_DHT.DHT22
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
str1='! ALERT !\n'
str2= 'Temperature high'
def values( ):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Sucessful reading') 
    else:
        print('Check Connections, failed')
        sys.exit(1)
    ui.thtUi(MainWindow)
def log():
    tem=[]
    hum=[]
    avg_tem=0.0
    avg_hum=0.0
    for i in range(0,10):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        tem.append(temperature)
        hum.append(humidity)
        avg_tem=avg_tem+tem[i]
        avg_hum=avg_hum+hum[i]
        time.sleep(1)
    avg_tem=avg_tem/10
    avg_hum=avg_hum/10
    print('Average Temperature is {0:0.1f}*C and Average Humidity is ={1:0.1f}%'.format(avg_tem,avg_hum))
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Temperature = QtWidgets.QTextBrowser(self.centralwidget)
        self.Temperature.setGeometry(QtCore.QRect(90, 40, 256, 71))
        self.Temperature.setObjectName("Temperature")
        self.Humidity = QtWidgets.QTextBrowser(self.centralwidget)
        self.Humidity.setGeometry(QtCore.QRect(460, 40, 256, 71))
        self.Humidity.setObjectName("Humidity")
        self.PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton.setGeometry(QtCore.QRect(364, 470, 81, 23))
        self.PushButton.setObjectName("PushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 530, 81, 16))
        self.label.setObjectName("label")
        self.TimeDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.TimeDisplay.setGeometry(QtCore.QRect(250, 201, 331, 91))
        self.TimeDisplay.setObjectName("TimeDisplay")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 140, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(516, 130, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(376, 300, 81, 20))
        self.label_4.setObjectName("label_4")
        self.Alert = QtWidgets.QTextBrowser(self.centralwidget)
        self.Alert.setGeometry(QtCore.QRect(60, 360, 256, 192))
        self.Alert.setObjectName("Alert")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionSave_2)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.PushButton.clicked.connect(values)
        self.actionClose.triggered.connect(MainWindow.close)
        self.actionClear.triggered.connect(self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "test5"))
        self.PushButton.setText(_translate("MainWindow", "Ask for Data"))
        self.label.setText(_translate("MainWindow", "Random"))
        self.label_2.setText(_translate("MainWindow", "Temperature"))
        self.label_3.setText(_translate("MainWindow", "Humidity"))
        self.label_4.setText(_translate("MainWindow", "Time"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionSave_2.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
    def thtUi(self,MainWindow):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if temperature>21:
            self.Alert.setText(str1)
            msg=QtWidgets.QMessageBox()
            msg.warning(msg,str1,str2)
        else:
             self.Alert.setText(' ')
        self.Temperature.setText(str(temperature))
        self.Humidity.setText(str(humidity))
        self.TimeDisplay.setText(str(time.gmtime()))
	
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  

if __name__ == "__main__":
    import sys
    if temperature is None or humidity is None:
        print('Check Connections, failed')
        sys.exit(1)
    log()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
