# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organizer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(895, 697)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(142, 159, 250, 255), stop:1 rgba(116, 35, 255, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lbl_title = QLabel(self.frame)
        self.lbl_title.setObjectName(u"lbl_title")

        self.verticalLayout.addWidget(self.lbl_title)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_path = QLineEdit(self.frame_2)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(0, 29))
        font = QFont()
        font.setPointSize(11)
        self.txt_path.setFont(font)
        self.txt_path.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_path)

        self.btn_open = QPushButton(self.frame_2)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setEnabled(True)
        self.btn_open.setMinimumSize(QSize(120, 29))
        self.btn_open.setFont(font)
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-top-right-radius:15px;\n"
"	color:rgb(0,109,159);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(0, 157, 235)\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_open)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_organize = QPushButton(self.frame)
        self.btn_organize.setObjectName(u"btn_organize")
        self.btn_organize.setMinimumSize(QSize(160, 30))
        self.btn_organize.setFont(font)
        self.btn_organize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_organize.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	color:rgb(0,109,159);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(0, 157, 235)\n"
"	\n"
"}")

        self.verticalLayout.addWidget(self.btn_organize, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/icons/pngegg.png\"/></p><p align=\"center\"><span style=\" font-size:16pt;\">ORGANIZADOR DE ARQUIVOS</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta -->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btn_organize.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
    # retranslateUi

