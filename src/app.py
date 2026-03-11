import sys
import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from API import fetch_data

class Ui_MainWindow(object):
    def __init__(self, temp, h_temp, l_temp):
        self._temp = temp
        self._h_temp = h_temp
        self._l_temp = l_temp

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 630)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Maintains the Picture property
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(0, 0, 531, 611))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap(":/assets/bg.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")

        # === START OF ALL TEXT PROPERT and LAYOUT ===
        # After MainWindow, I added vertical layout to better display values
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 70, 251, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # This section is part of the vertical layout
        self.temp_property = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.temp_property.setContentsMargins(0, 0, 0, 0)
        self.temp_property.setObjectName("temp_property")

        # Property to change the city text templet
        self.cityName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cityName.setStyleSheet("font: 20pt \"Sans Serif\";\n"
                                    "color: rgb(255, 255, 255)")
        self.cityName.setAlignment(QtCore.Qt.AlignCenter)
        self.cityName.setObjectName("cityName")

        # Property to change tempeature text templet
        self.temp_property.addWidget(self.cityName)
        self.temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.temp.setStyleSheet("font: 28pt \"Sans Serif\";\n"
                                "color: rgb(255, 255, 255)")
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")
        self.temp_property.addWidget(self.temp)
        
        # The Horizontal layout is part of the Vertical layout to display High and Low tempeature next to each other
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # High tempeature text templet
        self.high_temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.high_temp.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 12pt \"Sans Serif\";")
        self.high_temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.high_temp.setObjectName("high_temp")
        
        # Separates the high by itself
        self.horizontalLayout.addWidget(self.high_temp)

        # Low tempeature text templet
        self.low_temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.low_temp.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"Sans Serif\";")
        self.low_temp.setObjectName("low_temp")

        # Separates the low by itself
        self.horizontalLayout.addWidget(self.low_temp)

        self.temp_property.addLayout(self.horizontalLayout)

        # === END OF ALL TEXT PROPERT and LAYOUT ===

        #IDK what this is ... don't touch
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Wrap all widgets here
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cityName.setText(_translate("MainWindow", "Dallas")) # ============ For now Hardcoded city name  TO BE UPDATED!!!
        self.temp.setText(_translate("MainWindow", f"{self._temp}°"))
        self.high_temp.setText(_translate("MainWindow", f"H: {self._h_temp}° "))
        self.low_temp.setText(_translate("MainWindow", f"L: {self._l_temp}° "))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    temp, h_temp, l_temp = fetch_data()
    
    # Added error handling before app is executed
    if type(temp) != float:
        raise ValueError("Main tempeature must be a valid tempeature value")
    
    if type(h_temp) != int:
        raise ValueError("High tempeature must be a valid tempeature value")
    
    if type(l_temp) != int:
        raise ValueError("Low Tempeature must be a valid tempeature value")
    
    ui = Ui_MainWindow(temp, h_temp, l_temp)
    ui.setupUi(MainWindow)

    MainWindow.show()
    
    sys.exit(app.exec_())
