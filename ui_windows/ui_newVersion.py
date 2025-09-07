# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newVersionvbtKpM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

import ui_windows.bcg_image_rc as bcg_image_rc
import ui_windows.icons_rc as icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 970)
        font = QFont()
        font.setFamily(u"Niagara Solid")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 80))
        self.header_frame.setStyleSheet(u"\n"
"#header_frame{background-color: qlineargradient(spread:pad, x1:0.61, y1:0.737, \n"
"x2:0.886, y2:0.748, \n"
"stop:0.25 rgba(255, 255, 255, 255), stop:0.255 rgba(56, 63, 66, 255));}")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 250, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_left_frame.sizePolicy().hasHeightForWidth())
        self.header_left_frame.setSizePolicy(sizePolicy)
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Menu_btn = QPushButton(self.header_left_frame)
        self.Menu_btn.setObjectName(u"Menu_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Menu_btn.sizePolicy().hasHeightForWidth())
        self.Menu_btn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.Menu_btn.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/Images for Program/icons/menu_icon1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_btn.setIcon(icon)
        self.Menu_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.Menu_btn)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.header_center_frame.sizePolicy().hasHeightForWidth())
        self.header_center_frame.setSizePolicy(sizePolicy2)
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo_label = QLabel(self.header_center_frame)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setPixmap(QPixmap(u":/icons/Images for Program/icons/64x64Motor_icon.png"))

        self.horizontalLayout_3.addWidget(self.logo_label)

        self.logo_title_label = QLabel(self.header_center_frame)
        self.logo_title_label.setObjectName(u"logo_title_label")
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.logo_title_label.setFont(font2)
        self.logo_title_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.logo_title_label, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header_frame)

        self.mainBody_frame = QFrame(self.centralwidget)
        self.mainBody_frame.setObjectName(u"mainBody_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBody_frame.sizePolicy().hasHeightForWidth())
        self.mainBody_frame.setSizePolicy(sizePolicy3)
        self.mainBody_frame.setFrameShape(QFrame.NoFrame)
        self.mainBody_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBody_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_content_frame = QFrame(self.mainBody_frame)
        self.left_menu_content_frame.setObjectName(u"left_menu_content_frame")
        self.left_menu_content_frame.setMinimumSize(QSize(200, 0))
        self.left_menu_content_frame.setMaximumSize(QSize(30, 16777215))
        self.left_menu_content_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.left_menu_content_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_content_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_content_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        sizePolicy3.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy3)
        self.menu_frame.setMinimumSize(QSize(150, 0))
        self.menu_frame.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        self.menu_frame.setFont(font3)
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Data_input_label = QLabel(self.menu_frame)
        self.Data_input_label.setObjectName(u"Data_input_label")
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(12)
        self.Data_input_label.setFont(font4)
        self.Data_input_label.setMargin(5)

        self.gridLayout.addWidget(self.Data_input_label, 0, 1, 1, 1, Qt.AlignLeft)

        self.Data_sheet_btn = QPushButton(self.menu_frame)
        self.Data_sheet_btn.setObjectName(u"Data_sheet_btn")
        self.Data_sheet_btn.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Images for Program/icons/generator_icon2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Data_sheet_btn.setIcon(icon1)
        self.Data_sheet_btn.setIconSize(QSize(42, 42))

        self.gridLayout.addWidget(self.Data_sheet_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.Data_sheet_label = QLabel(self.menu_frame)
        self.Data_sheet_label.setObjectName(u"Data_sheet_label")
        self.Data_sheet_label.setFont(font4)
        self.Data_sheet_label.setMargin(5)

        self.gridLayout.addWidget(self.Data_sheet_label, 2, 1, 1, 1, Qt.AlignLeft)

        self.calculat_label = QLabel(self.menu_frame)
        self.calculat_label.setObjectName(u"calculat_label")
        self.calculat_label.setFont(font4)
        self.calculat_label.setMargin(5)

        self.gridLayout.addWidget(self.calculat_label, 1, 1, 1, 1, Qt.AlignLeft)

        self.basisdaten_btn = QPushButton(self.menu_frame)
        self.basisdaten_btn.setObjectName(u"basisdaten_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Images for Program/icons/generator_icon1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.basisdaten_btn.setIcon(icon2)
        self.basisdaten_btn.setIconSize(QSize(42, 42))

        self.gridLayout.addWidget(self.basisdaten_btn, 3, 0, 1, 1, Qt.AlignLeft)

        self.calculat_btn = QPushButton(self.menu_frame)
        self.calculat_btn.setObjectName(u"calculat_btn")
        self.calculat_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.calculat_btn.sizePolicy().hasHeightForWidth())
        self.calculat_btn.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/Images for Program/icons/calculator.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calculat_btn.setIcon(icon3)
        self.calculat_btn.setIconSize(QSize(42, 42))

        self.gridLayout.addWidget(self.calculat_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.Basisdaten_label = QLabel(self.menu_frame)
        self.Basisdaten_label.setObjectName(u"Basisdaten_label")
        self.Basisdaten_label.setFont(font4)

        self.gridLayout.addWidget(self.Basisdaten_label, 3, 1, 1, 1, Qt.AlignLeft)

        self.Data_input_btn = QPushButton(self.menu_frame)
        self.Data_input_btn.setObjectName(u"Data_input_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Images for Program/icons/inputs_icon1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Data_input_btn.setIcon(icon4)
        self.Data_input_btn.setIconSize(QSize(42, 42))

        self.gridLayout.addWidget(self.Data_input_btn, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.left_menu_content_frame)

        self.main_body_cont_frame = QFrame(self.mainBody_frame)
        self.main_body_cont_frame.setObjectName(u"main_body_cont_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.main_body_cont_frame.sizePolicy().hasHeightForWidth())
        self.main_body_cont_frame.setSizePolicy(sizePolicy4)
        self.main_body_cont_frame.setMinimumSize(QSize(650, 0))
        self.main_body_cont_frame.setStyleSheet(u"QWidget#main_body_cont_frame{background-image: url(:/bcg_image/Images for Program/png_worldwide.png);}")
        self.main_body_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_cont_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.main_body_cont_frame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.main_body_cont_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"QWidget#stackedWidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0.466, y1:0.494318, x2:0.46, y2:0.5, stop:0 rgba(255, 255, 255, 36), stop:1 rgba(255, 255, 255, 36));\n"
"border-radius:5px;\n"
"}")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.inputsPage = QWidget()
        self.inputsPage.setObjectName(u"inputsPage")
        sizePolicy3.setHeightForWidth(self.inputsPage.sizePolicy().hasHeightForWidth())
        self.inputsPage.setSizePolicy(sizePolicy3)
        self.gridLayout_4 = QGridLayout(self.inputsPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, -1, -1, 9)
        self.Submit1 = QPushButton(self.inputsPage)
        self.Submit1.setObjectName(u"Submit1")
        self.Submit1.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Submit1.sizePolicy().hasHeightForWidth())
        self.Submit1.setSizePolicy(sizePolicy5)
        self.Submit1.setMinimumSize(QSize(100, 35))
        self.Submit1.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.Submit1.setIconSize(QSize(20, 20))
        self.Submit1.setAutoRepeatDelay(300)

        self.gridLayout_4.addWidget(self.Submit1, 3, 0, 1, 1, Qt.AlignRight)

        self.frame_15 = QFrame(self.inputsPage)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy6)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.errorlabel1_5 = QLabel(self.frame_15)
        self.errorlabel1_5.setObjectName(u"errorlabel1_5")
        sizePolicy3.setHeightForWidth(self.errorlabel1_5.sizePolicy().hasHeightForWidth())
        self.errorlabel1_5.setSizePolicy(sizePolicy3)
        self.errorlabel1_5.setMinimumSize(QSize(0, 0))
        self.errorlabel1_5.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_2.addWidget(self.errorlabel1_5, 12, 1, 1, 1, Qt.AlignTop)

        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.label_5, 11, 0, 1, 1, Qt.AlignTop)

        self.label_1 = QLabel(self.frame_15)
        self.label_1.setObjectName(u"label_1")
        sizePolicy3.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.label_1.setFont(font5)
        self.label_1.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.label_1, 3, 0, 1, 1, Qt.AlignTop)

        self.errorlabel1_3 = QLabel(self.frame_15)
        self.errorlabel1_3.setObjectName(u"errorlabel1_3")
        sizePolicy3.setHeightForWidth(self.errorlabel1_3.sizePolicy().hasHeightForWidth())
        self.errorlabel1_3.setSizePolicy(sizePolicy3)
        self.errorlabel1_3.setMinimumSize(QSize(0, 0))
        self.errorlabel1_3.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_2.addWidget(self.errorlabel1_3, 8, 1, 1, 1, Qt.AlignTop)

        self.Tk_lineedit = QLineEdit(self.frame_15)
        self.Tk_lineedit.setObjectName(u"Tk_lineedit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Tk_lineedit.sizePolicy().hasHeightForWidth())
        self.Tk_lineedit.setSizePolicy(sizePolicy7)
        self.Tk_lineedit.setMinimumSize(QSize(0, 25))
        font6 = QFont()
        font6.setFamily(u"Noto Sans")
        font6.setPointSize(10)
        self.Tk_lineedit.setFont(font6)
        self.Tk_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_2.addWidget(self.Tk_lineedit, 7, 1, 1, 2)

        self.label_2 = QLabel(self.frame_15)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1, Qt.AlignTop)

        self.errorlabel1_2 = QLabel(self.frame_15)
        self.errorlabel1_2.setObjectName(u"errorlabel1_2")
        sizePolicy3.setHeightForWidth(self.errorlabel1_2.sizePolicy().hasHeightForWidth())
        self.errorlabel1_2.setSizePolicy(sizePolicy3)
        self.errorlabel1_2.setMinimumSize(QSize(0, 0))
        self.errorlabel1_2.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_2.addWidget(self.errorlabel1_2, 6, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_7 = QLabel(self.frame_15)
        self.errorlabel1_7.setObjectName(u"errorlabel1_7")
        sizePolicy3.setHeightForWidth(self.errorlabel1_7.sizePolicy().hasHeightForWidth())
        self.errorlabel1_7.setSizePolicy(sizePolicy3)
        self.errorlabel1_7.setMinimumSize(QSize(0, 0))
        self.errorlabel1_7.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_2.addWidget(self.errorlabel1_7, 14, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_4 = QLabel(self.frame_15)
        self.errorlabel1_4.setObjectName(u"errorlabel1_4")
        sizePolicy3.setHeightForWidth(self.errorlabel1_4.sizePolicy().hasHeightForWidth())
        self.errorlabel1_4.setSizePolicy(sizePolicy3)
        self.errorlabel1_4.setMinimumSize(QSize(0, 0))
        self.errorlabel1_4.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_2.addWidget(self.errorlabel1_4, 10, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_11 = QLabel(self.frame_15)
        self.errorlabel1_11.setObjectName(u"errorlabel1_11")
        self.errorlabel1_11.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.errorlabel1_11.sizePolicy().hasHeightForWidth())
        self.errorlabel1_11.setSizePolicy(sizePolicy3)
        font7 = QFont()
        font7.setFamily(u"Noto Sans")
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.errorlabel1_11.setFont(font7)
        self.errorlabel1_11.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_2.addWidget(self.errorlabel1_11, 1, 0, 1, 1, Qt.AlignTop)

        self.Browsefile = QPushButton(self.frame_15)
        self.Browsefile.setObjectName(u"Browsefile")
        sizePolicy5.setHeightForWidth(self.Browsefile.sizePolicy().hasHeightForWidth())
        self.Browsefile.setSizePolicy(sizePolicy5)
        self.Browsefile.setMinimumSize(QSize(100, 35))
        font8 = QFont()
        font8.setFamily(u"Siemens Sans Black")
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.Browsefile.setFont(font8)
        self.Browsefile.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.Browsefile.setIconSize(QSize(20, 20))
        self.Browsefile.setAutoRepeatDelay(300)

        self.gridLayout_2.addWidget(self.Browsefile, 0, 2, 1, 1)

        self.VV_Box = QComboBox(self.frame_15)
        self.VV_Box.setObjectName(u"VV_Box")
        self.VV_Box.setMinimumSize(QSize(0, 25))
        self.VV_Box.setMaximumSize(QSize(16777215, 25))
        self.VV_Box.setFont(font6)
        self.VV_Box.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"/*style the borders after opening the box*/\n"
"QComboBox:on{\n"
"	border:3px solid #383f42;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"QComboBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"\n"
"/*Styling the scrollbar*/\n"
"\n"
"            QComboBox QScrollBar:vertical {\n"
"                background-color:transparent  ;\n"
"                width: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"            }\n"
"        \n"
"            QComboBox QScrollBar::handle:vertical {\n"
"                background-color:rgb(56"
                        ", 63, 66) ;\n"
"                min-height: 20px;\n"
"				margin: 16px 2px 16px 2px;\n"
"				border-radius:5px;\n"
"            }\n"
"            QComboBox QScrollBar::handle:vertical:hover {\n"
"                background-color: rgb(255, 205, 0);\n"
"            }\n"
"            QComboBox QScrollBar::handle:vertical:pressed {\n"
"               background-color: rgb(250, 171, 72);\n"
"            }\n"
"            QComboBox QScrollBar::add-line:vertical, QComboBox QScrollBar::sub-line:vertical {\n"
"                background: transparent;\n"
"                height: 15px;\n"
"                width: 15px;\n"
"            }\n"
"        \n"
"            QComboBox QScrollBar::add-page:vertical, QComboBox QScrollBar::sub-page:vertical {\n"
"                background: none;\n"
"                height: 5px;\n"
"                width: 5px;\n"
"            }\n"
"\n"
"			QComboBox QScrollBar::sub-line:vertical:hover, QComboBox QScrollBar::add-line:vertical:hover {\n"
"			background-color:rgb(255, 205, 0);\n"
"			bor"
                        "der-radius:7px;\n"
"            }\n"
"\n"
"			QComboBox QScrollBar::sub-line:vertical:pressed, QComboBox QScrollBar::add-line:vertical:pressed {\n"
"			background-color:rgb(250, 171, 72);\n"
"			border-radius:7px;\n"
"            }\n"
"\n"
"            QComboBox QScrollBar::down-arrow:vertical {\n"
"                background-color: transparent;\n"
"                border: none;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                 /* replace with the path to your custom image */\n"
"				image: url(:/icons/Images for Program/icons/down-arrow.png);\n"
"            }\n"
"\n"
"            QComboBox QScrollBar::up-arrow:vertical{\n"
"                background-color:transparent;\n"
"                border: none;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                 /* replace with the path to your custom image */\n"
"				image: url(:/icons/Images for Program/"
                        "icons/up-arrow.png);\n"
"            }\n"
"        \n"
"            QComboBox QScrollBar::up-arrow:vertical {\n"
"                subcontrol-position: top;\n"
"            }\n"
"        \n"
"            QComboBox QScrollBar::down-arrow:vertical {\n"
"                subcontrol-position: bottom;\n"
"            }")
        self.VV_Box.setEditable(True)
        self.VV_Box.setMaxVisibleItems(6)

        self.gridLayout_2.addWidget(self.VV_Box, 13, 1, 1, 2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radioButton_1 = QRadioButton(self.frame_15)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setFont(font5)
        self.radioButton_1.setLayoutDirection(Qt.RightToLeft)
        self.radioButton_1.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans\";\n"
"\n"
"")
        self.radioButton_1.setChecked(True)

        self.horizontalLayout_11.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.frame_15)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setLayoutDirection(Qt.RightToLeft)
        self.radioButton_2.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans\";")

        self.horizontalLayout_11.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_15)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setLayoutDirection(Qt.RightToLeft)
        self.radioButton_3.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans\";")

        self.horizontalLayout_11.addWidget(self.radioButton_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 9, 1, 1, 2)

        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1, Qt.AlignTop)

        self.Tw_lineedit = QLineEdit(self.frame_15)
        self.Tw_lineedit.setObjectName(u"Tw_lineedit")
        sizePolicy7.setHeightForWidth(self.Tw_lineedit.sizePolicy().hasHeightForWidth())
        self.Tw_lineedit.setSizePolicy(sizePolicy7)
        self.Tw_lineedit.setMinimumSize(QSize(0, 25))
        self.Tw_lineedit.setFont(font6)
        self.Tw_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_2.addWidget(self.Tw_lineedit, 5, 1, 1, 2)

        self.Motoren_box = QComboBox(self.frame_15)
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.addItem("")
        self.Motoren_box.setObjectName(u"Motoren_box")
        self.Motoren_box.setEnabled(False)
        self.Motoren_box.setMinimumSize(QSize(0, 25))
        self.Motoren_box.setMaximumSize(QSize(16777215, 25))
        self.Motoren_box.setFont(font6)
        self.Motoren_box.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border:2px solid #383f42;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"QComboBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"\n"
"\n"
"/*Styling the scrollbar*/\n"
"\n"
"            QComboBox QScrollBar:vertical {\n"
"                background-color:transparent  ;\n"
"                width: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"            }\n"
"        \n"
"            QComboBox QScrollBar::handle:vertical {\n"
"                background-color:rgb(56, 63, 66) ;\n"
"   "
                        "             min-height: 20px;\n"
"				margin: 16px 2px 16px 2px;\n"
"				border-radius:5px;\n"
"            }\n"
"\n"
"            QComboBox QScrollBar::handle:vertical:hover {\n"
"                background-color: rgb(255, 205, 0);\n"
"            }\n"
"\n"
"            QComboBox QScrollBar::handle:vertical:pressed {\n"
"               background-color: rgb(250, 171, 72);\n"
"            }\n"
"\n"
"            QComboBox QScrollBar::add-line:vertical, QComboBox QScrollBar::sub-line:vertical {\n"
"                background: transparent;\n"
"                height: 15px;\n"
"                width: 15px;\n"
"            }\n"
"        \n"
"            QComboBox QScrollBar::add-page:vertical, QComboBox QScrollBar::sub-page:vertical {\n"
"                background: none;\n"
"                height: 5px;\n"
"                width: 5px;\n"
"            }\n"
"\n"
"			QComboBox QScrollBar::sub-line:vertical:hover, QComboBox QScrollBar::add-line:vertical:hover {\n"
"			background-color:rgb(255, 205, 0);\n"
"			border-"
                        "radius:7px;\n"
"            }\n"
"\n"
"			QComboBox QScrollBar::sub-line:vertical:pressed, QComboBox QScrollBar::add-line:vertical:pressed {\n"
"			background-color:rgb(250, 171, 72);\n"
"			border-radius:7px;\n"
"            }\n"
"\n"
"            QComboBox QScrollBar::down-arrow:vertical {\n"
"                background-color: transparent;\n"
"                border: none;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                 /* replace with the path to your custom image */\n"
"				image: url(:/icons/Images for Program/icons/down-arrow.png);\n"
"            }\n"
"\n"
"            QComboBox QScrollBar::up-arrow:vertical{\n"
"                background-color:transparent;\n"
"                border: none;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                 /* replace with the path to your custom image */\n"
"				image: url(:/icons/Images for Program/icon"
                        "s/up-arrow.png);\n"
"            }\n"
"        \n"
"            #Motoren_box QScrollBar::up-arrow:vertical {\n"
"                subcontrol-position: top;\n"
"            }\n"
"        \n"
"            QComboBox QScrollBar::down-arrow:vertical {\n"
"                subcontrol-position: bottom;\n"
"            }\n"
"")
        self.Motoren_box.setMaxVisibleItems(6)
        self.Motoren_box.setInsertPolicy(QComboBox.InsertAtBottom)

        self.gridLayout_2.addWidget(self.Motoren_box, 3, 1, 1, 2)

        self.filelabel = QLineEdit(self.frame_15)
        self.filelabel.setObjectName(u"filelabel")
        self.filelabel.setEnabled(True)
        self.filelabel.setMinimumSize(QSize(500, 25))
        self.filelabel.setMaximumSize(QSize(16777215, 25))
        font9 = QFont()
        font9.setPointSize(10)
        self.filelabel.setFont(font9)
        self.filelabel.setStyleSheet(u"QLineEdit{border-radius:5px;} \n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_2.addWidget(self.filelabel, 0, 0, 1, 2)

        self.errorlabel1_12 = QLabel(self.frame_15)
        self.errorlabel1_12.setObjectName(u"errorlabel1_12")
        self.errorlabel1_12.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.errorlabel1_12.sizePolicy().hasHeightForWidth())
        self.errorlabel1_12.setSizePolicy(sizePolicy3)
        self.errorlabel1_12.setFont(font7)
        self.errorlabel1_12.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_2.addWidget(self.errorlabel1_12, 2, 0, 1, 3, Qt.AlignTop)

        self.label_4 = QLabel(self.frame_15)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.label_4, 9, 0, 2, 1, Qt.AlignTop)

        self.errorlabel1_1 = QLabel(self.frame_15)
        self.errorlabel1_1.setObjectName(u"errorlabel1_1")
        self.errorlabel1_1.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.errorlabel1_1.sizePolicy().hasHeightForWidth())
        self.errorlabel1_1.setSizePolicy(sizePolicy3)
        self.errorlabel1_1.setMinimumSize(QSize(0, 0))
        self.errorlabel1_1.setFont(font7)
        self.errorlabel1_1.setStyleSheet(u"color: rgb(250, 218, 87);\n"
"font: 9pt \"Noto Sans\";")
        self.errorlabel1_1.setWordWrap(False)

        self.gridLayout_2.addWidget(self.errorlabel1_1, 4, 1, 1, 1, Qt.AlignTop)

        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.label_10, 13, 0, 1, 1)

        self.laengeBox = QComboBox(self.frame_15)
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.addItem("")
        self.laengeBox.setObjectName(u"laengeBox")
        self.laengeBox.setEnabled(False)
        self.laengeBox.setMinimumSize(QSize(0, 25))
        self.laengeBox.setMaximumSize(QSize(16777215, 25))
        self.laengeBox.setFont(font6)
        self.laengeBox.setStyleSheet(u"#laengeBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255)\n"
"\n"
"}\n"
"\n"
"/*QComboBox::focus{border: 2px solid #383f42;}*/\n"
"\n"
"#laengeBox::editable:on{\n"
"	border:2px solid #383f42;\n"
"	border-radius:5px;\n"
"	\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"#laengeBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"#laengeBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"#laengeBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*Styling the scrollbar*/\n"
"\n"
"            #laengeBox QScrollBar:vertical {\n"
"                background-color:transparent  ;\n"
"                width: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"            }\n"
"        \n"
"            #laengeBox QS"
                        "crollBar::handle:vertical {\n"
"                background-color:rgb(56, 63, 66) ;\n"
"                min-height: 20px;\n"
"				margin: 16px 2px 16px 2px;\n"
"				border-radius:5px;\n"
"            }\n"
"            #laengeBox QScrollBar::handle:vertical:hover {\n"
"                background-color: rgb(255, 205, 0);\n"
"            }\n"
"            #laengeBox QScrollBar::handle:vertical:pressed {\n"
"               background-color: rgb(250, 171, 72);\n"
"            }\n"
"            #laengeBox QScrollBar::add-line:vertical, QComboBox QScrollBar::sub-line:vertical {\n"
"                background: transparent;\n"
"                height: 15px;\n"
"                width: 15px;\n"
"            }\n"
"        \n"
"            #laengeBox QScrollBar::add-page:vertical, QComboBox QScrollBar::sub-page:vertical {\n"
"                background: none;\n"
"                height: 5px;\n"
"                width: 5px;\n"
"            }\n"
"\n"
"			QComboBox QScrollBar::sub-line:vertical:hover, QComboBox QScrollBar::add"
                        "-line:vertical:hover {\n"
"			background-color:rgb(255, 205, 0);\n"
"			border-radius:7px;\n"
"            }\n"
"\n"
"			QComboBox QScrollBar::sub-line:vertical:pressed, QComboBox QScrollBar::add-line:vertical:pressed {\n"
"			background-color:rgb(250, 171, 72);\n"
"			border-radius:7px;\n"
"            }\n"
"        \n"
"            #laengeBox QScrollBar::down-arrow:vertical {\n"
"                background-color: transparent;\n"
"                border: none;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                 /* replace with the path to your custom image */\n"
"				image: url(:/icons/Images for Program/icons/down-arrow.png);\n"
"            }\n"
"\n"
"            #laengeBox QScrollBar::up-arrow:vertical{\n"
"                background-color:transparent;\n"
"                border: none;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                 /* replace"
                        " with the path to your custom image */\n"
"				image: url(:/icons/Images for Program/icons/up-arrow.png);\n"
"            }\n"
"        \n"
"            #laengeBox QScrollBar::up-arrow:vertical {\n"
"                subcontrol-position: top;\n"
"            }\n"
"        \n"
"            #laengeBox QScrollBar::down-arrow:vertical {\n"
"                subcontrol-position: bottom;\n"
"            }")
        self.laengeBox.setEditable(True)
        self.laengeBox.setMaxVisibleItems(8)

        self.gridLayout_2.addWidget(self.laengeBox, 11, 1, 1, 2)


        self.gridLayout_4.addWidget(self.frame_15, 0, 0, 1, 1)

        self.optionalFrame = QFrame(self.inputsPage)
        self.optionalFrame.setObjectName(u"optionalFrame")
        sizePolicy6.setHeightForWidth(self.optionalFrame.sizePolicy().hasHeightForWidth())
        self.optionalFrame.setSizePolicy(sizePolicy6)
        self.optionalFrame.setMinimumSize(QSize(0, 0))
        self.optionalFrame.setMaximumSize(QSize(16777215, 0))
        self.optionalFrame.setFrameShape(QFrame.StyledPanel)
        self.optionalFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.optionalFrame)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.optionalFrame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_8.addWidget(self.label_7, 2, 0, 1, 1)

        self.Drehzahl_lineedit = QLineEdit(self.optionalFrame)
        self.Drehzahl_lineedit.setObjectName(u"Drehzahl_lineedit")
        sizePolicy7.setHeightForWidth(self.Drehzahl_lineedit.sizePolicy().hasHeightForWidth())
        self.Drehzahl_lineedit.setSizePolicy(sizePolicy7)
        self.Drehzahl_lineedit.setMinimumSize(QSize(0, 25))
        self.Drehzahl_lineedit.setFont(font6)
        self.Drehzahl_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_8.addWidget(self.Drehzahl_lineedit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.optionalFrame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.DeltaTeta_stern_lineedit = QLineEdit(self.optionalFrame)
        self.DeltaTeta_stern_lineedit.setObjectName(u"DeltaTeta_stern_lineedit")
        sizePolicy7.setHeightForWidth(self.DeltaTeta_stern_lineedit.sizePolicy().hasHeightForWidth())
        self.DeltaTeta_stern_lineedit.setSizePolicy(sizePolicy7)
        self.DeltaTeta_stern_lineedit.setMinimumSize(QSize(0, 25))
        self.DeltaTeta_stern_lineedit.setFont(font6)
        self.DeltaTeta_stern_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_8.addWidget(self.DeltaTeta_stern_lineedit, 4, 1, 1, 1)

        self.errorlabel1_6 = QLabel(self.optionalFrame)
        self.errorlabel1_6.setObjectName(u"errorlabel1_6")
        sizePolicy3.setHeightForWidth(self.errorlabel1_6.sizePolicy().hasHeightForWidth())
        self.errorlabel1_6.setSizePolicy(sizePolicy3)
        self.errorlabel1_6.setMinimumSize(QSize(0, 0))
        self.errorlabel1_6.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_8.addWidget(self.errorlabel1_6, 1, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_9 = QLabel(self.optionalFrame)
        self.errorlabel1_9.setObjectName(u"errorlabel1_9")
        sizePolicy3.setHeightForWidth(self.errorlabel1_9.sizePolicy().hasHeightForWidth())
        self.errorlabel1_9.setSizePolicy(sizePolicy3)
        self.errorlabel1_9.setMinimumSize(QSize(0, 0))
        self.errorlabel1_9.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_8.addWidget(self.errorlabel1_9, 5, 1, 1, 1, Qt.AlignTop)

        self.label_9 = QLabel(self.optionalFrame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"font: 12pt \"Noto Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_8.addWidget(self.label_9, 6, 0, 1, 1)

        self.Teta_stern_lineedit = QLineEdit(self.optionalFrame)
        self.Teta_stern_lineedit.setObjectName(u"Teta_stern_lineedit")
        sizePolicy7.setHeightForWidth(self.Teta_stern_lineedit.sizePolicy().hasHeightForWidth())
        self.Teta_stern_lineedit.setSizePolicy(sizePolicy7)
        self.Teta_stern_lineedit.setMinimumSize(QSize(0, 25))
        self.Teta_stern_lineedit.setFont(font6)
        self.Teta_stern_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_8.addWidget(self.Teta_stern_lineedit, 2, 1, 1, 1)

        self.errorlabel1_8 = QLabel(self.optionalFrame)
        self.errorlabel1_8.setObjectName(u"errorlabel1_8")
        sizePolicy3.setHeightForWidth(self.errorlabel1_8.sizePolicy().hasHeightForWidth())
        self.errorlabel1_8.setSizePolicy(sizePolicy3)
        self.errorlabel1_8.setMinimumSize(QSize(0, 0))
        self.errorlabel1_8.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_8.addWidget(self.errorlabel1_8, 3, 1, 1, 1, Qt.AlignTop)

        self.label_8 = QLabel(self.optionalFrame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_8.addWidget(self.label_8, 4, 0, 1, 1)

        self.errorlabel1_10 = QLabel(self.optionalFrame)
        self.errorlabel1_10.setObjectName(u"errorlabel1_10")
        sizePolicy3.setHeightForWidth(self.errorlabel1_10.sizePolicy().hasHeightForWidth())
        self.errorlabel1_10.setSizePolicy(sizePolicy3)
        self.errorlabel1_10.setMinimumSize(QSize(0, 0))
        self.errorlabel1_10.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_8.addWidget(self.errorlabel1_10, 7, 1, 1, 1, Qt.AlignTop)

        self.Pulsdauer_lineedit = QLineEdit(self.optionalFrame)
        self.Pulsdauer_lineedit.setObjectName(u"Pulsdauer_lineedit")
        sizePolicy7.setHeightForWidth(self.Pulsdauer_lineedit.sizePolicy().hasHeightForWidth())
        self.Pulsdauer_lineedit.setSizePolicy(sizePolicy7)
        self.Pulsdauer_lineedit.setMinimumSize(QSize(0, 25))
        self.Pulsdauer_lineedit.setFont(font6)
        self.Pulsdauer_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_8.addWidget(self.Pulsdauer_lineedit, 6, 1, 1, 1)


        self.gridLayout_4.addWidget(self.optionalFrame, 2, 0, 1, 1)

        self.optionalBtn = QPushButton(self.inputsPage)
        self.optionalBtn.setObjectName(u"optionalBtn")
        sizePolicy5.setHeightForWidth(self.optionalBtn.sizePolicy().hasHeightForWidth())
        self.optionalBtn.setSizePolicy(sizePolicy5)
        self.optionalBtn.setMinimumSize(QSize(90, 25))
        font10 = QFont()
        font10.setFamily(u"Noto Sans")
        font10.setPointSize(9)
        self.optionalBtn.setFont(font10)
        self.optionalBtn.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"border-radius:5px;}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(56, 63, 66);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Images for Program/icons/64px-down-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.optionalBtn.setIcon(icon5)
        self.optionalBtn.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.optionalBtn, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.stackedWidget.addWidget(self.inputsPage)
        self.calculationPage = QWidget()
        self.calculationPage.setObjectName(u"calculationPage")
        self.gridLayout_5 = QGridLayout(self.calculationPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.frame_20 = QFrame(self.calculationPage)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy8)
        self.frame_20.setMinimumSize(QSize(0, 0))
        self.frame_20.setMaximumSize(QSize(16777215, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_20)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.gridLayout_11.addWidget(self.label_18, 0, 0, 1, 1, Qt.AlignVCenter)

        self.Strom_lineEdit = QLineEdit(self.frame_20)
        self.Strom_lineEdit.setObjectName(u"Strom_lineEdit")
        self.Strom_lineEdit.setEnabled(True)
        self.Strom_lineEdit.setMinimumSize(QSize(0, 25))
        self.Strom_lineEdit.setFont(font6)
        self.Strom_lineEdit.setStyleSheet(u"QLineEdit{border-radius:5px;} \n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_11.addWidget(self.Strom_lineEdit, 0, 1, 1, 1, Qt.AlignVCenter)

        self.calculat_all_2 = QPushButton(self.frame_20)
        self.calculat_all_2.setObjectName(u"calculat_all_2")
        self.calculat_all_2.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.calculat_all_2.sizePolicy().hasHeightForWidth())
        self.calculat_all_2.setSizePolicy(sizePolicy5)
        self.calculat_all_2.setMinimumSize(QSize(120, 35))
        self.calculat_all_2.setFont(font8)
        self.calculat_all_2.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.calculat_all_2.setIconSize(QSize(20, 20))
        self.calculat_all_2.setAutoRepeatDelay(300)

        self.gridLayout_11.addWidget(self.calculat_all_2, 0, 2, 2, 1, Qt.AlignTop)

        self.errorlabel2_2 = QLabel(self.frame_20)
        self.errorlabel2_2.setObjectName(u"errorlabel2_2")
        self.errorlabel2_2.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_11.addWidget(self.errorlabel2_2, 1, 1, 1, 1, Qt.AlignTop)


        self.gridLayout_5.addWidget(self.frame_20, 6, 0, 1, 1, Qt.AlignTop)

        self.frame_2 = QFrame(self.calculationPage)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy8.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy8)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.errorlabel2_1 = QLabel(self.frame_2)
        self.errorlabel2_1.setObjectName(u"errorlabel2_1")
        sizePolicy7.setHeightForWidth(self.errorlabel2_1.sizePolicy().hasHeightForWidth())
        self.errorlabel2_1.setSizePolicy(sizePolicy7)
        self.errorlabel2_1.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_3.addWidget(self.errorlabel2_1, 1, 0, 1, 1)

        self.calculat_all = QPushButton(self.frame_2)
        self.calculat_all.setObjectName(u"calculat_all")
        self.calculat_all.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.calculat_all.sizePolicy().hasHeightForWidth())
        self.calculat_all.setSizePolicy(sizePolicy5)
        self.calculat_all.setMinimumSize(QSize(120, 35))
        self.calculat_all.setFont(font8)
        self.calculat_all.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.calculat_all.setIconSize(QSize(20, 20))
        self.calculat_all.setAutoRepeatDelay(300)

        self.gridLayout_3.addWidget(self.calculat_all, 2, 1, 1, 1)

        self.errorlabel_20 = QLabel(self.frame_2)
        self.errorlabel_20.setObjectName(u"errorlabel_20")
        self.errorlabel_20.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 8pt \"Noto Sans\";")

        self.gridLayout_3.addWidget(self.errorlabel_20, 6, 1, 1, 1, Qt.AlignTop)

        self.calculat_specific = QPushButton(self.frame_2)
        self.calculat_specific.setObjectName(u"calculat_specific")
        self.calculat_specific.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.calculat_specific.sizePolicy().hasHeightForWidth())
        self.calculat_specific.setSizePolicy(sizePolicy5)
        self.calculat_specific.setMinimumSize(QSize(120, 35))
        self.calculat_specific.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.calculat_specific.setIconSize(QSize(20, 20))
        self.calculat_specific.setAutoRepeatDelay(300)

        self.gridLayout_3.addWidget(self.calculat_specific, 3, 1, 1, 1)

        self.list_to_calculat = QListWidget(self.frame_2)
        self.list_to_calculat.setObjectName(u"list_to_calculat")
        sizePolicy6.setHeightForWidth(self.list_to_calculat.sizePolicy().hasHeightForWidth())
        self.list_to_calculat.setSizePolicy(sizePolicy6)
        self.list_to_calculat.setMinimumSize(QSize(450, 470))
        self.list_to_calculat.setFont(font6)
        self.list_to_calculat.setFocusPolicy(Qt.NoFocus)
        self.list_to_calculat.setStyleSheet(u"border-radius:10px")
        self.list_to_calculat.setInputMethodHints(Qt.ImhNone)
        self.list_to_calculat.setFrameShape(QFrame.VLine)
        self.list_to_calculat.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_to_calculat.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.list_to_calculat.setMovement(QListView.Free)
        self.list_to_calculat.setResizeMode(QListView.Fixed)
        self.list_to_calculat.setLayoutMode(QListView.Batched)
        self.list_to_calculat.setSpacing(2)

        self.gridLayout_3.addWidget(self.list_to_calculat, 2, 0, 6, 1)

        self.GraphsBtn = QPushButton(self.frame_2)
        self.GraphsBtn.setObjectName(u"GraphsBtn")
        self.GraphsBtn.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.GraphsBtn.sizePolicy().hasHeightForWidth())
        self.GraphsBtn.setSizePolicy(sizePolicy5)
        self.GraphsBtn.setMinimumSize(QSize(120, 35))
        self.GraphsBtn.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.GraphsBtn.setIconSize(QSize(20, 20))
        self.GraphsBtn.setAutoRepeatDelay(300)

        self.gridLayout_3.addWidget(self.GraphsBtn, 4, 1, 1, 1)

        self.all_variations_btn = QPushButton(self.frame_2)
        self.all_variations_btn.setObjectName(u"all_variations_btn")
        self.all_variations_btn.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.all_variations_btn.sizePolicy().hasHeightForWidth())
        self.all_variations_btn.setSizePolicy(sizePolicy5)
        self.all_variations_btn.setMinimumSize(QSize(120, 35))
        self.all_variations_btn.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_3.addWidget(self.all_variations_btn, 5, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 3, 0, 1, 1, Qt.AlignTop)

        self.frame_21 = QFrame(self.calculationPage)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy6.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy6)
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_21)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.strom_change_label = QLabel(self.frame_21)
        self.strom_change_label.setObjectName(u"strom_change_label")
        sizePolicy7.setHeightForWidth(self.strom_change_label.sizePolicy().hasHeightForWidth())
        self.strom_change_label.setSizePolicy(sizePolicy7)
        font11 = QFont()
        font11.setFamily(u"Noto Sans")
        font11.setPointSize(11)
        self.strom_change_label.setFont(font11)
        self.strom_change_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.strom_change_label, 1, 0, 1, 1)

        self.Strom_checkBox = QCheckBox(self.frame_21)
        self.Strom_checkBox.setObjectName(u"Strom_checkBox")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.Strom_checkBox.sizePolicy().hasHeightForWidth())
        self.Strom_checkBox.setSizePolicy(sizePolicy9)
        self.Strom_checkBox.setFont(font11)
        self.Strom_checkBox.setStyleSheet(u"QCheckBox{\n"
"color:rgb(255, 255, 255)}\n"
"QCheckBox::indicator{    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"QCheckBox::indicator:checked{image: url(:/icons/Images for Program/icons/tickmark.png) ;}\n"
"\n"
"\n"
"\n"
"")
        self.Strom_checkBox.setIconSize(QSize(16, 16))
        self.Strom_checkBox.setChecked(False)
        self.Strom_checkBox.setTristate(False)

        self.gridLayout_12.addWidget(self.Strom_checkBox, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_21, 5, 0, 1, 1, Qt.AlignTop)

        self.vorlageFrame = QFrame(self.calculationPage)
        self.vorlageFrame.setObjectName(u"vorlageFrame")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.vorlageFrame.sizePolicy().hasHeightForWidth())
        self.vorlageFrame.setSizePolicy(sizePolicy10)
        self.vorlageFrame.setMinimumSize(QSize(0, 0))
        self.vorlageFrame.setFrameShape(QFrame.StyledPanel)
        self.vorlageFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.vorlageFrame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(5)
        self.gridLayout_13.setContentsMargins(-1, 0, 10, -1)
        self.importVorlageBtn = QPushButton(self.vorlageFrame)
        self.importVorlageBtn.setObjectName(u"importVorlageBtn")
        sizePolicy5.setHeightForWidth(self.importVorlageBtn.sizePolicy().hasHeightForWidth())
        self.importVorlageBtn.setSizePolicy(sizePolicy5)
        self.importVorlageBtn.setMinimumSize(QSize(120, 35))
        self.importVorlageBtn.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_13.addWidget(self.importVorlageBtn, 1, 1, 1, 1)

        self.vorlageLabel = QLabel(self.vorlageFrame)
        self.vorlageLabel.setObjectName(u"vorlageLabel")
        font12 = QFont()
        font12.setFamily(u"Noto Sans")
        font12.setPointSize(11)
        font12.setBold(True)
        font12.setWeight(75)
        self.vorlageLabel.setFont(font12)
        self.vorlageLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.vorlageLabel, 0, 0, 1, 1)

        self.errorlabel_21 = QLabel(self.vorlageFrame)
        self.errorlabel_21.setObjectName(u"errorlabel_21")
        self.errorlabel_21.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_13.addWidget(self.errorlabel_21, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.generatDataSheetBtn = QPushButton(self.vorlageFrame)
        self.generatDataSheetBtn.setObjectName(u"generatDataSheetBtn")
        self.generatDataSheetBtn.setEnabled(False)
        self.generatDataSheetBtn.setMinimumSize(QSize(120, 35))
        self.generatDataSheetBtn.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_13.addWidget(self.generatDataSheetBtn, 2, 1, 1, 1)

        self.vorlagePfadLineEdit = QLineEdit(self.vorlageFrame)
        self.vorlagePfadLineEdit.setObjectName(u"vorlagePfadLineEdit")
        self.vorlagePfadLineEdit.setMinimumSize(QSize(0, 25))
        self.vorlagePfadLineEdit.setMaximumSize(QSize(16777215, 25))
        font13 = QFont()
        font13.setFamily(u"Siemens Sans")
        font13.setItalic(True)
        self.vorlagePfadLineEdit.setFont(font13)
        self.vorlagePfadLineEdit.setStyleSheet(u"QLineEdit{border-radius:5px;} \n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_13.addWidget(self.vorlagePfadLineEdit, 1, 0, 1, 1)

        self.errorlabel_22 = QLabel(self.vorlageFrame)
        self.errorlabel_22.setObjectName(u"errorlabel_22")
        self.errorlabel_22.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_13.addWidget(self.errorlabel_22, 3, 0, 1, 1, Qt.AlignTop)


        self.gridLayout_5.addWidget(self.vorlageFrame, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.calculationPage)
        self.ExportPage = QWidget()
        self.ExportPage.setObjectName(u"ExportPage")
        self.gridLayout_6 = QGridLayout(self.ExportPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setContentsMargins(9, 0, 0, 9)
        self.frame_22 = QFrame(self.ExportPage)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy6.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy6)
        self.frame_22.setMinimumSize(QSize(0, 0))
        self.frame_22.setMaximumSize(QSize(16777215, 100))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_22)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(10)
        self.gridLayout_19.setVerticalSpacing(0)
        self.gridLayout_19.setContentsMargins(0, 0, 10, 0)
        self.errorlabel1_41 = QLabel(self.frame_22)
        self.errorlabel1_41.setObjectName(u"errorlabel1_41")
        sizePolicy3.setHeightForWidth(self.errorlabel1_41.sizePolicy().hasHeightForWidth())
        self.errorlabel1_41.setSizePolicy(sizePolicy3)
        self.errorlabel1_41.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_19.addWidget(self.errorlabel1_41, 2, 0, 1, 1, Qt.AlignTop)

        self.creatExcel = QPushButton(self.frame_22)
        self.creatExcel.setObjectName(u"creatExcel")
        self.creatExcel.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.creatExcel.sizePolicy().hasHeightForWidth())
        self.creatExcel.setSizePolicy(sizePolicy5)
        self.creatExcel.setMinimumSize(QSize(100, 35))
        self.creatExcel.setFont(font8)
        self.creatExcel.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_19.addWidget(self.creatExcel, 1, 3, 1, 1, Qt.AlignRight)

        self.label_19 = QLabel(self.frame_22)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font12)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.label_19, 0, 0, 1, 1)

        self.errorlabel1_42 = QLabel(self.frame_22)
        self.errorlabel1_42.setObjectName(u"errorlabel1_42")
        sizePolicy11 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.errorlabel1_42.sizePolicy().hasHeightForWidth())
        self.errorlabel1_42.setSizePolicy(sizePolicy11)
        self.errorlabel1_42.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_19.addWidget(self.errorlabel1_42, 3, 0, 1, 1)

        self.filelabel_3 = QLineEdit(self.frame_22)
        self.filelabel_3.setObjectName(u"filelabel_3")
        self.filelabel_3.setMinimumSize(QSize(0, 25))
        font14 = QFont()
        font14.setFamily(u"Siemens Sans")
        font14.setPointSize(10)
        font14.setItalic(True)
        self.filelabel_3.setFont(font14)
        self.filelabel_3.setStyleSheet(u"QLineEdit{border-radius:5px;} \n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_19.addWidget(self.filelabel_3, 1, 0, 1, 1)

        self.ExcelTemplate = QPushButton(self.frame_22)
        self.ExcelTemplate.setObjectName(u"ExcelTemplate")
        sizePolicy5.setHeightForWidth(self.ExcelTemplate.sizePolicy().hasHeightForWidth())
        self.ExcelTemplate.setSizePolicy(sizePolicy5)
        self.ExcelTemplate.setMinimumSize(QSize(100, 35))
        self.ExcelTemplate.setMaximumSize(QSize(16777215, 16777215))
        self.ExcelTemplate.setFont(font8)
        self.ExcelTemplate.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_19.addWidget(self.ExcelTemplate, 1, 2, 1, 1)


        self.gridLayout_6.addWidget(self.frame_22, 3, 0, 1, 1)

        self.scrollArea = QScrollArea(self.ExportPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(600, 0))
        self.scrollArea.setStyleSheet(u" QWidget#scrollArea  {         \n"
"	background-color: transparent;\n"
"}\n"
"            #scrollArea QScrollBar:vertical {\n"
"                background-color: transparent  ;\n"
"                width: 19px;\n"
"                margin: 0px 0px 0px 0px;\n"
"				border:1px transparent #2A2929 ;\n"
"				border-radius:5;\n"
"\n"
"            }\n"
"			#scrollArea QScrollBar::handle:vertical {\n"
"                background-color:rgb(56, 63, 66) ;\n"
"                min-height: 20px;\n"
"				margin: 20px 5px 20px 5px;\n"
"				border-radius:4px;\n"
"            }\n"
"			\n"
"			#scrollArea QScrollBar::handle:vertical:hover{\n"
"			background-color:rgb(255, 205, 0);\n"
"			}\n"
"\n"
"			#scrollArea QScrollBar::handle:vertical:pressed{\n"
"			background-color:rgb(250, 171, 72);\n"
"			}\n"
"            #scrollArea QScrollBar::add-line:vertical, #scrollArea QScrollBar::sub-line:vertical {\n"
"                background: transparent;\n"
"                height: 18px;\n"
"                width: 18px;\n"
"              "
                        "  margin: 0px 1px 0px 0px\n"
"            }\n"
"        \n"
"            #scrollArea QScrollBar::add-page:vertical, #scrollArea QScrollBar::sub-page:vertical {\n"
"                background: none;\n"
"                height: 0px;\n"
"                width: 0px;\n"
"            }\n"
"\n"
"			#scrollArea QScrollBar::sub-line:vertical:hover, #scrollArea QScrollBar::add-line:vertical:hover {\n"
"			background-color:rgb(255, 205, 0);\n"
"			border-radius:9px;\n"
"            }\n"
"\n"
"			#scrollArea QScrollBar::sub-line:vertical:pressed, #scrollArea QScrollBar::add-line:vertical:pressed {\n"
"			background-color:rgb(250, 171, 72);\n"
"			border-radius:9px;\n"
"            }\n"
"        \n"
"            #scrollArea QScrollBar::down-arrow:vertical {\n"
"                background-color: transparent;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 0px 0px 1px 0px;\n"
"                 /* replace with the path to your custom image */\n"
"				image: url(:/icons/Images for"
                        " Program/icons/down-arrow.png);\n"
"            }\n"
"\n"
"            #scrollArea QScrollBar::up-arrow:vertical{\n"
"                background-color: transparent;\n"
"                width: 15px;\n"
"                height: 15px;\n"
"                margin: 1px 0px 0px 0px;\n"
"                 /* replace with the path to your custom image */\n"
"				image: url(:/icons/Images for Program/icons/up-arrow.png);\n"
"            }\n"
"        \n"
"            #scrollArea QScrollBar::up-arrow:vertical {\n"
"                subcontrol-position: top;\n"
"            }\n"
"        \n"
"            #scrollArea QScrollBar::down-arrow:vertical {\n"
"                subcontrol-position: bottom;\n"
"            }")
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 602, 861))
        sizePolicy6.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy6)
        self.scrollAreaWidgetContents.setStyleSheet(u"/*QWidget#scrollAreaWidgetContents{background-image: url(:/bcg_image/Images for Program/png_worldwide.png);}*/\n"
"/*QWidget#scrollAreaWidgetContents{ background-color:transparent;}\n"
"\n"
"")
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 5, 0)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy6.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy6)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(10)
        self.gridLayout_18.setVerticalSpacing(5)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.errorlabel1_25 = QLabel(self.frame_14)
        self.errorlabel1_25.setObjectName(u"errorlabel1_25")
        sizePolicy3.setHeightForWidth(self.errorlabel1_25.sizePolicy().hasHeightForWidth())
        self.errorlabel1_25.setSizePolicy(sizePolicy3)
        self.errorlabel1_25.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_25, 4, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_30 = QLabel(self.frame_14)
        self.errorlabel1_30.setObjectName(u"errorlabel1_30")
        sizePolicy3.setHeightForWidth(self.errorlabel1_30.sizePolicy().hasHeightForWidth())
        self.errorlabel1_30.setSizePolicy(sizePolicy3)
        self.errorlabel1_30.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_30, 2, 3, 1, 1, Qt.AlignTop)

        self.label_87 = QLabel(self.frame_14)
        self.label_87.setObjectName(u"label_87")
        sizePolicy3.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy3)
        self.label_87.setFont(font12)
        self.label_87.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.label_87, 0, 0, 1, 2, Qt.AlignTop)

        self.label_86 = QLabel(self.frame_14)
        self.label_86.setObjectName(u"label_86")
        sizePolicy3.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy3)
        self.label_86.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_86, 5, 2, 1, 1)

        self.label_79 = QLabel(self.frame_14)
        self.label_79.setObjectName(u"label_79")
        sizePolicy3.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy3)
        self.label_79.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_79, 9, 0, 1, 1)

        self.Encoder_Schnitstelle_comboBox = QComboBox(self.frame_14)
        self.Encoder_Schnitstelle_comboBox.addItem("")
        self.Encoder_Schnitstelle_comboBox.addItem("")
        self.Encoder_Schnitstelle_comboBox.addItem("")
        self.Encoder_Schnitstelle_comboBox.addItem("")
        self.Encoder_Schnitstelle_comboBox.addItem("")
        self.Encoder_Schnitstelle_comboBox.setObjectName(u"Encoder_Schnitstelle_comboBox")
        self.Encoder_Schnitstelle_comboBox.setMinimumSize(QSize(0, 25))
        font15 = QFont()
        font15.setFamily(u"Siemens Sans")
        font15.setPointSize(10)
        self.Encoder_Schnitstelle_comboBox.setFont(font15)
        self.Encoder_Schnitstelle_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border:2px solid #383f42;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"QComboBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"")
        self.Encoder_Schnitstelle_comboBox.setEditable(True)

        self.gridLayout_18.addWidget(self.Encoder_Schnitstelle_comboBox, 11, 1, 1, 1)

        self.Anwendugs_AS_lineedit = QLineEdit(self.frame_14)
        self.Anwendugs_AS_lineedit.setObjectName(u"Anwendugs_AS_lineedit")
        self.Anwendugs_AS_lineedit.setMinimumSize(QSize(0, 25))
        self.Anwendugs_AS_lineedit.setFont(font15)
        self.Anwendugs_AS_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_18.addWidget(self.Anwendugs_AS_lineedit, 5, 1, 1, 1)

        self.label_78 = QLabel(self.frame_14)
        self.label_78.setObjectName(u"label_78")
        sizePolicy3.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy3)
        self.label_78.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_78, 7, 2, 1, 1)

        self.label_81 = QLabel(self.frame_14)
        self.label_81.setObjectName(u"label_81")
        sizePolicy3.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy3)
        self.label_81.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_81, 5, 0, 1, 1)

        self.Encoder_Auswertrichtung_comboBox = QComboBox(self.frame_14)
        self.Encoder_Auswertrichtung_comboBox.addItem("")
        self.Encoder_Auswertrichtung_comboBox.addItem("")
        self.Encoder_Auswertrichtung_comboBox.addItem("")
        self.Encoder_Auswertrichtung_comboBox.setObjectName(u"Encoder_Auswertrichtung_comboBox")
        self.Encoder_Auswertrichtung_comboBox.setMinimumSize(QSize(0, 25))
        self.Encoder_Auswertrichtung_comboBox.setFont(font15)
        self.Encoder_Auswertrichtung_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border:2px solid #383f42;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"QComboBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"")
        self.Encoder_Auswertrichtung_comboBox.setEditable(True)

        self.gridLayout_18.addWidget(self.Encoder_Auswertrichtung_comboBox, 1, 3, 1, 1)

        self.Vorschaltdrossel2_lineedit = QLineEdit(self.frame_14)
        self.Vorschaltdrossel2_lineedit.setObjectName(u"Vorschaltdrossel2_lineedit")
        self.Vorschaltdrossel2_lineedit.setMinimumSize(QSize(0, 25))
        self.Vorschaltdrossel2_lineedit.setFont(font15)
        self.Vorschaltdrossel2_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_18.addWidget(self.Vorschaltdrossel2_lineedit, 9, 3, 1, 1)

        self.Encoder_Bezeichnung_lineedit = QLineEdit(self.frame_14)
        self.Encoder_Bezeichnung_lineedit.setObjectName(u"Encoder_Bezeichnung_lineedit")
        self.Encoder_Bezeichnung_lineedit.setMinimumSize(QSize(0, 25))
        self.Encoder_Bezeichnung_lineedit.setFont(font15)
        self.Encoder_Bezeichnung_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_18.addWidget(self.Encoder_Bezeichnung_lineedit, 5, 3, 1, 1)

        self.Drehzahlbegrenzung2_lineedit = QLineEdit(self.frame_14)
        self.Drehzahlbegrenzung2_lineedit.setObjectName(u"Drehzahlbegrenzung2_lineedit")
        self.Drehzahlbegrenzung2_lineedit.setMinimumSize(QSize(0, 25))
        self.Drehzahlbegrenzung2_lineedit.setFont(font15)
        self.Drehzahlbegrenzung2_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_18.addWidget(self.Drehzahlbegrenzung2_lineedit, 7, 3, 1, 1)

        self.errorlabel1_28 = QLabel(self.frame_14)
        self.errorlabel1_28.setObjectName(u"errorlabel1_28")
        sizePolicy3.setHeightForWidth(self.errorlabel1_28.sizePolicy().hasHeightForWidth())
        self.errorlabel1_28.setSizePolicy(sizePolicy3)
        self.errorlabel1_28.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_28, 10, 1, 1, 1, Qt.AlignTop)

        self.DBL_version_lineedit = QLineEdit(self.frame_14)
        self.DBL_version_lineedit.setObjectName(u"DBL_version_lineedit")
        self.DBL_version_lineedit.setMinimumSize(QSize(0, 25))
        self.DBL_version_lineedit.setFont(font15)
        self.DBL_version_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_18.addWidget(self.DBL_version_lineedit, 1, 1, 1, 1)

        self.errorlabel1_33 = QLabel(self.frame_14)
        self.errorlabel1_33.setObjectName(u"errorlabel1_33")
        sizePolicy7.setHeightForWidth(self.errorlabel1_33.sizePolicy().hasHeightForWidth())
        self.errorlabel1_33.setSizePolicy(sizePolicy7)
        self.errorlabel1_33.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_33, 8, 3, 1, 1, Qt.AlignTop)

        self.errorlabel1_34 = QLabel(self.frame_14)
        self.errorlabel1_34.setObjectName(u"errorlabel1_34")
        sizePolicy7.setHeightForWidth(self.errorlabel1_34.sizePolicy().hasHeightForWidth())
        self.errorlabel1_34.setSizePolicy(sizePolicy7)
        self.errorlabel1_34.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_34, 10, 3, 1, 1, Qt.AlignTop)

        self.label_83 = QLabel(self.frame_14)
        self.label_83.setObjectName(u"label_83")
        sizePolicy3.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy3)
        self.label_83.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_83, 3, 0, 1, 1)

        self.Encoder_Hersteller_comboBox = QComboBox(self.frame_14)
        self.Encoder_Hersteller_comboBox.addItem("")
        self.Encoder_Hersteller_comboBox.addItem("")
        self.Encoder_Hersteller_comboBox.addItem("")
        self.Encoder_Hersteller_comboBox.addItem("")
        self.Encoder_Hersteller_comboBox.setObjectName(u"Encoder_Hersteller_comboBox")
        self.Encoder_Hersteller_comboBox.setMinimumSize(QSize(0, 25))
        self.Encoder_Hersteller_comboBox.setFont(font15)
        self.Encoder_Hersteller_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border:2px solid #383f42;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"QComboBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"")
        self.Encoder_Hersteller_comboBox.setEditable(True)

        self.gridLayout_18.addWidget(self.Encoder_Hersteller_comboBox, 3, 3, 1, 1)

        self.errorlabel1_27 = QLabel(self.frame_14)
        self.errorlabel1_27.setObjectName(u"errorlabel1_27")
        sizePolicy3.setHeightForWidth(self.errorlabel1_27.sizePolicy().hasHeightForWidth())
        self.errorlabel1_27.setSizePolicy(sizePolicy3)
        self.errorlabel1_27.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_27, 8, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_31 = QLabel(self.frame_14)
        self.errorlabel1_31.setObjectName(u"errorlabel1_31")
        sizePolicy3.setHeightForWidth(self.errorlabel1_31.sizePolicy().hasHeightForWidth())
        self.errorlabel1_31.setSizePolicy(sizePolicy3)
        self.errorlabel1_31.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_31, 4, 3, 1, 1, Qt.AlignTop)

        self.label_77 = QLabel(self.frame_14)
        self.label_77.setObjectName(u"label_77")
        sizePolicy3.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy3)
        self.label_77.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_77, 11, 0, 1, 1)

        self.errorlabel1_26 = QLabel(self.frame_14)
        self.errorlabel1_26.setObjectName(u"errorlabel1_26")
        sizePolicy3.setHeightForWidth(self.errorlabel1_26.sizePolicy().hasHeightForWidth())
        self.errorlabel1_26.setSizePolicy(sizePolicy3)
        self.errorlabel1_26.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_26, 6, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_29 = QLabel(self.frame_14)
        self.errorlabel1_29.setObjectName(u"errorlabel1_29")
        sizePolicy3.setHeightForWidth(self.errorlabel1_29.sizePolicy().hasHeightForWidth())
        self.errorlabel1_29.setSizePolicy(sizePolicy3)
        self.errorlabel1_29.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_29, 13, 1, 1, 1, Qt.AlignTop)

        self.DBL_ID_lineedit = QLineEdit(self.frame_14)
        self.DBL_ID_lineedit.setObjectName(u"DBL_ID_lineedit")
        self.DBL_ID_lineedit.setMinimumSize(QSize(0, 25))
        self.DBL_ID_lineedit.setFont(font15)
        self.DBL_ID_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_18.addWidget(self.DBL_ID_lineedit, 3, 1, 1, 1)

        self.sensorTypcomboBox_ANW = QComboBox(self.frame_14)
        self.sensorTypcomboBox_ANW.addItem("")
        self.sensorTypcomboBox_ANW.addItem("")
        self.sensorTypcomboBox_ANW.setObjectName(u"sensorTypcomboBox_ANW")
        self.sensorTypcomboBox_ANW.setMinimumSize(QSize(0, 25))
        self.sensorTypcomboBox_ANW.setFont(font15)
        self.sensorTypcomboBox_ANW.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border:2px solid #383f42;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"QComboBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"")
        self.sensorTypcomboBox_ANW.setEditable(True)

        self.gridLayout_18.addWidget(self.sensorTypcomboBox_ANW, 7, 1, 1, 1)

        self.label_85 = QLabel(self.frame_14)
        self.label_85.setObjectName(u"label_85")
        sizePolicy3.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy3)
        self.label_85.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_85, 1, 2, 1, 1)

        self.Encoder_Strichzahl_lineedit = QLineEdit(self.frame_14)
        self.Encoder_Strichzahl_lineedit.setObjectName(u"Encoder_Strichzahl_lineedit")
        self.Encoder_Strichzahl_lineedit.setMinimumSize(QSize(0, 25))
        self.Encoder_Strichzahl_lineedit.setFont(font15)
        self.Encoder_Strichzahl_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")
        self.Encoder_Strichzahl_lineedit.setInputMethodHints(Qt.ImhPreferUppercase|Qt.ImhTime)

        self.gridLayout_18.addWidget(self.Encoder_Strichzahl_lineedit, 9, 1, 1, 1)

        self.label_80 = QLabel(self.frame_14)
        self.label_80.setObjectName(u"label_80")
        sizePolicy3.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy3)
        self.label_80.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_80, 1, 0, 1, 1)

        self.label_82 = QLabel(self.frame_14)
        self.label_82.setObjectName(u"label_82")
        sizePolicy3.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy3)
        self.label_82.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_82, 7, 0, 1, 1)

        self.label_76 = QLabel(self.frame_14)
        self.label_76.setObjectName(u"label_76")
        sizePolicy3.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy3)
        self.label_76.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_76, 9, 2, 1, 1)

        self.label_84 = QLabel(self.frame_14)
        self.label_84.setObjectName(u"label_84")
        sizePolicy3.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy3)
        self.label_84.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.label_84, 3, 2, 1, 1)

        self.errorlabel1_32 = QLabel(self.frame_14)
        self.errorlabel1_32.setObjectName(u"errorlabel1_32")
        sizePolicy3.setHeightForWidth(self.errorlabel1_32.sizePolicy().hasHeightForWidth())
        self.errorlabel1_32.setSizePolicy(sizePolicy3)
        self.errorlabel1_32.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_32, 6, 3, 1, 1, Qt.AlignTop)

        self.errorlabel1_24 = QLabel(self.frame_14)
        self.errorlabel1_24.setObjectName(u"errorlabel1_24")
        sizePolicy3.setHeightForWidth(self.errorlabel1_24.sizePolicy().hasHeightForWidth())
        self.errorlabel1_24.setSizePolicy(sizePolicy3)
        self.errorlabel1_24.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_18.addWidget(self.errorlabel1_24, 2, 1, 1, 1, Qt.AlignTop)


        self.gridLayout_15.addWidget(self.frame_14, 2, 0, 1, 1)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy10.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy10)
        self.frame_12.setMaximumSize(QSize(16777215, 100))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(10)
        self.gridLayout_16.setVerticalSpacing(20)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.filelabel_4 = QLineEdit(self.frame_12)
        self.filelabel_4.setObjectName(u"filelabel_4")
        self.filelabel_4.setMinimumSize(QSize(0, 25))
        self.filelabel_4.setFont(font14)
        self.filelabel_4.setStyleSheet(u"QLineEdit{border-radius:5px;} \n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_16.addWidget(self.filelabel_4, 3, 0, 1, 1)

        self.wordTemplate = QPushButton(self.frame_12)
        self.wordTemplate.setObjectName(u"wordTemplate")
        sizePolicy5.setHeightForWidth(self.wordTemplate.sizePolicy().hasHeightForWidth())
        self.wordTemplate.setSizePolicy(sizePolicy5)
        self.wordTemplate.setMinimumSize(QSize(100, 25))
        self.wordTemplate.setMaximumSize(QSize(16777215, 16777215))
        font16 = QFont()
        font16.setFamily(u"Siemens Sans Black")
        font16.setPointSize(10)
        font16.setBold(False)
        font16.setItalic(False)
        font16.setWeight(50)
        self.wordTemplate.setFont(font16)
        self.wordTemplate.setStyleSheet(u"QPushButton{\n"
"font: 10pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_16.addWidget(self.wordTemplate, 2, 1, 1, 1)

        self.mot3DateiImport = QPushButton(self.frame_12)
        self.mot3DateiImport.setObjectName(u"mot3DateiImport")
        sizePolicy5.setHeightForWidth(self.mot3DateiImport.sizePolicy().hasHeightForWidth())
        self.mot3DateiImport.setSizePolicy(sizePolicy5)
        self.mot3DateiImport.setMinimumSize(QSize(100, 25))
        self.mot3DateiImport.setMaximumSize(QSize(16777215, 16777215))
        self.mot3DateiImport.setFont(font16)
        self.mot3DateiImport.setStyleSheet(u"QPushButton{\n"
"font: 10pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_16.addWidget(self.mot3DateiImport, 3, 1, 1, 1)

        self.filelabel_2 = QLineEdit(self.frame_12)
        self.filelabel_2.setObjectName(u"filelabel_2")
        self.filelabel_2.setMinimumSize(QSize(0, 25))
        self.filelabel_2.setFont(font14)
        self.filelabel_2.setStyleSheet(u"QLineEdit{border-radius:5px;} \n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_16.addWidget(self.filelabel_2, 2, 0, 1, 1)

        self.errorlabel1_35 = QLabel(self.frame_12)
        self.errorlabel1_35.setObjectName(u"errorlabel1_35")
        sizePolicy3.setHeightForWidth(self.errorlabel1_35.sizePolicy().hasHeightForWidth())
        self.errorlabel1_35.setSizePolicy(sizePolicy3)
        self.errorlabel1_35.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_16.addWidget(self.errorlabel1_35, 4, 0, 1, 1, Qt.AlignTop)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setFont(font12)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_16.addWidget(self.label_14, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy6.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy6)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_13)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(10)
        self.gridLayout_17.setVerticalSpacing(5)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.rotor_ID_lineedit = QLineEdit(self.frame_13)
        self.rotor_ID_lineedit.setObjectName(u"rotor_ID_lineedit")
        self.rotor_ID_lineedit.setMinimumSize(QSize(0, 25))
        self.rotor_ID_lineedit.setFont(font15)
        self.rotor_ID_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")
        self.rotor_ID_lineedit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_17.addWidget(self.rotor_ID_lineedit, 7, 1, 1, 1)

        self.label_64 = QLabel(self.frame_13)
        self.label_64.setObjectName(u"label_64")
        sizePolicy3.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy3)
        self.label_64.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_64, 5, 0, 1, 1)

        self.label_65 = QLabel(self.frame_13)
        self.label_65.setObjectName(u"label_65")
        sizePolicy3.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy3)
        self.label_65.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_65, 3, 0, 1, 1)

        self.motor_AS_lineedit = QLineEdit(self.frame_13)
        self.motor_AS_lineedit.setObjectName(u"motor_AS_lineedit")
        self.motor_AS_lineedit.setMinimumSize(QSize(0, 25))
        self.motor_AS_lineedit.setFont(font15)
        self.motor_AS_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")
        self.motor_AS_lineedit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_17.addWidget(self.motor_AS_lineedit, 11, 1, 1, 1)

        self.errorlabel1_22 = QLabel(self.frame_13)
        self.errorlabel1_22.setObjectName(u"errorlabel1_22")
        sizePolicy3.setHeightForWidth(self.errorlabel1_22.sizePolicy().hasHeightForWidth())
        self.errorlabel1_22.setSizePolicy(sizePolicy3)
        self.errorlabel1_22.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_22, 8, 3, 1, 1, Qt.AlignTop)

        self.label_66 = QLabel(self.frame_13)
        self.label_66.setObjectName(u"label_66")
        sizePolicy3.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy3)
        self.label_66.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_66, 9, 0, 1, 1)

        self.Motortyp_lineedit = QLineEdit(self.frame_13)
        self.Motortyp_lineedit.setObjectName(u"Motortyp_lineedit")
        self.Motortyp_lineedit.setMinimumSize(QSize(0, 25))
        self.Motortyp_lineedit.setFont(font15)
        self.Motortyp_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")
        self.Motortyp_lineedit.setInputMethodHints(Qt.ImhNone)
        self.Motortyp_lineedit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_17.addWidget(self.Motortyp_lineedit, 1, 1, 1, 1)

        self.label_67 = QLabel(self.frame_13)
        self.label_67.setObjectName(u"label_67")
        sizePolicy8.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy8)
        self.label_67.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_67, 1, 2, 1, 1)

        self.errorlabel1_14 = QLabel(self.frame_13)
        self.errorlabel1_14.setObjectName(u"errorlabel1_14")
        sizePolicy3.setHeightForWidth(self.errorlabel1_14.sizePolicy().hasHeightForWidth())
        self.errorlabel1_14.setSizePolicy(sizePolicy3)
        self.errorlabel1_14.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_14, 4, 1, 1, 1, Qt.AlignTop)

        self.errorlabel1_17 = QLabel(self.frame_13)
        self.errorlabel1_17.setObjectName(u"errorlabel1_17")
        sizePolicy3.setHeightForWidth(self.errorlabel1_17.sizePolicy().hasHeightForWidth())
        self.errorlabel1_17.setSizePolicy(sizePolicy3)
        self.errorlabel1_17.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_17, 10, 1, 1, 1)

        self.label_68 = QLabel(self.frame_13)
        self.label_68.setObjectName(u"label_68")
        sizePolicy3.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy3)
        self.label_68.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_68, 11, 0, 1, 1)

        self.errorlabel1_13 = QLabel(self.frame_13)
        self.errorlabel1_13.setObjectName(u"errorlabel1_13")
        sizePolicy3.setHeightForWidth(self.errorlabel1_13.sizePolicy().hasHeightForWidth())
        self.errorlabel1_13.setSizePolicy(sizePolicy3)
        self.errorlabel1_13.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_13, 2, 1, 1, 1, Qt.AlignTop)

        self.label_69 = QLabel(self.frame_13)
        self.label_69.setObjectName(u"label_69")
        sizePolicy8.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy8)
        self.label_69.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_69, 7, 2, 1, 1)

        self.stator_ID_lineedit = QLineEdit(self.frame_13)
        self.stator_ID_lineedit.setObjectName(u"stator_ID_lineedit")
        self.stator_ID_lineedit.setMinimumSize(QSize(0, 25))
        self.stator_ID_lineedit.setFont(font15)
        self.stator_ID_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")
        self.stator_ID_lineedit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_17.addWidget(self.stator_ID_lineedit, 5, 1, 1, 1)

        self.label_70 = QLabel(self.frame_13)
        self.label_70.setObjectName(u"label_70")
        sizePolicy3.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy3)
        self.label_70.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_70, 7, 0, 1, 1)

        self.errorlabel1_18 = QLabel(self.frame_13)
        self.errorlabel1_18.setObjectName(u"errorlabel1_18")
        sizePolicy3.setHeightForWidth(self.errorlabel1_18.sizePolicy().hasHeightForWidth())
        self.errorlabel1_18.setSizePolicy(sizePolicy3)
        self.errorlabel1_18.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_18, 12, 1, 1, 1)

        self.Motor_ID_lineedit = QLineEdit(self.frame_13)
        self.Motor_ID_lineedit.setObjectName(u"Motor_ID_lineedit")
        self.Motor_ID_lineedit.setMinimumSize(QSize(0, 25))
        self.Motor_ID_lineedit.setFont(font15)
        self.Motor_ID_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")
        self.Motor_ID_lineedit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_17.addWidget(self.Motor_ID_lineedit, 3, 1, 1, 1)

        self.motor_DBL_lineedit = QLineEdit(self.frame_13)
        self.motor_DBL_lineedit.setObjectName(u"motor_DBL_lineedit")
        self.motor_DBL_lineedit.setMinimumSize(QSize(0, 25))
        self.motor_DBL_lineedit.setFont(font15)
        self.motor_DBL_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")
        self.motor_DBL_lineedit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_17.addWidget(self.motor_DBL_lineedit, 9, 1, 1, 1)

        self.Trgheitsmoment_lineedit = QLineEdit(self.frame_13)
        self.Trgheitsmoment_lineedit.setObjectName(u"Trgheitsmoment_lineedit")
        self.Trgheitsmoment_lineedit.setMinimumSize(QSize(0, 25))
        self.Trgheitsmoment_lineedit.setFont(font15)
        self.Trgheitsmoment_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_17.addWidget(self.Trgheitsmoment_lineedit, 1, 3, 1, 1)

        self.errorlabel1_15 = QLabel(self.frame_13)
        self.errorlabel1_15.setObjectName(u"errorlabel1_15")
        sizePolicy3.setHeightForWidth(self.errorlabel1_15.sizePolicy().hasHeightForWidth())
        self.errorlabel1_15.setSizePolicy(sizePolicy3)
        self.errorlabel1_15.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_15, 6, 1, 1, 1, Qt.AlignTop)

        self.label_71 = QLabel(self.frame_13)
        self.label_71.setObjectName(u"label_71")
        sizePolicy8.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy8)
        self.label_71.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_71, 5, 2, 1, 1)

        self.errorlabel1_21 = QLabel(self.frame_13)
        self.errorlabel1_21.setObjectName(u"errorlabel1_21")
        sizePolicy3.setHeightForWidth(self.errorlabel1_21.sizePolicy().hasHeightForWidth())
        self.errorlabel1_21.setSizePolicy(sizePolicy3)
        self.errorlabel1_21.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_21, 6, 3, 1, 1, Qt.AlignTop)

        self.Vorschaltdrossel_lineedit = QLineEdit(self.frame_13)
        self.Vorschaltdrossel_lineedit.setObjectName(u"Vorschaltdrossel_lineedit")
        self.Vorschaltdrossel_lineedit.setMinimumSize(QSize(0, 25))
        self.Vorschaltdrossel_lineedit.setFont(font15)
        self.Vorschaltdrossel_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_17.addWidget(self.Vorschaltdrossel_lineedit, 7, 3, 1, 1)

        self.errorlabel1_16 = QLabel(self.frame_13)
        self.errorlabel1_16.setObjectName(u"errorlabel1_16")
        sizePolicy3.setHeightForWidth(self.errorlabel1_16.sizePolicy().hasHeightForWidth())
        self.errorlabel1_16.setSizePolicy(sizePolicy3)
        self.errorlabel1_16.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_16, 8, 1, 1, 1)

        self.errorlabel1_20 = QLabel(self.frame_13)
        self.errorlabel1_20.setObjectName(u"errorlabel1_20")
        sizePolicy3.setHeightForWidth(self.errorlabel1_20.sizePolicy().hasHeightForWidth())
        self.errorlabel1_20.setSizePolicy(sizePolicy3)
        self.errorlabel1_20.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_20, 4, 3, 1, 1, Qt.AlignTop)

        self.label_72 = QLabel(self.frame_13)
        self.label_72.setObjectName(u"label_72")
        sizePolicy8.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy8)
        self.label_72.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_72, 3, 2, 1, 1)

        self.zwischenkreisspannung_lineedit = QLineEdit(self.frame_13)
        self.zwischenkreisspannung_lineedit.setObjectName(u"zwischenkreisspannung_lineedit")
        self.zwischenkreisspannung_lineedit.setMinimumSize(QSize(0, 25))
        self.zwischenkreisspannung_lineedit.setFont(font15)
        self.zwischenkreisspannung_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_17.addWidget(self.zwischenkreisspannung_lineedit, 5, 3, 1, 1)

        self.label_73 = QLabel(self.frame_13)
        self.label_73.setObjectName(u"label_73")
        sizePolicy3.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy3)
        self.label_73.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_73, 1, 0, 1, 1)

        self.errorlabel1_19 = QLabel(self.frame_13)
        self.errorlabel1_19.setObjectName(u"errorlabel1_19")
        sizePolicy3.setHeightForWidth(self.errorlabel1_19.sizePolicy().hasHeightForWidth())
        self.errorlabel1_19.setSizePolicy(sizePolicy3)
        self.errorlabel1_19.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_19, 2, 3, 1, 1, Qt.AlignTop)

        self.Drehzahlbegrenzung_lineedit = QLineEdit(self.frame_13)
        self.Drehzahlbegrenzung_lineedit.setObjectName(u"Drehzahlbegrenzung_lineedit")
        self.Drehzahlbegrenzung_lineedit.setMinimumSize(QSize(0, 25))
        self.Drehzahlbegrenzung_lineedit.setFont(font15)
        self.Drehzahlbegrenzung_lineedit.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_17.addWidget(self.Drehzahlbegrenzung_lineedit, 9, 3, 1, 1)

        self.label_74 = QLabel(self.frame_13)
        self.label_74.setObjectName(u"label_74")
        sizePolicy8.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy8)
        self.label_74.setStyleSheet(u"font: 75 12pt \"Siemens Sans\";\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.label_74, 9, 2, 1, 1)

        self.errorlabel1_23 = QLabel(self.frame_13)
        self.errorlabel1_23.setObjectName(u"errorlabel1_23")
        sizePolicy3.setHeightForWidth(self.errorlabel1_23.sizePolicy().hasHeightForWidth())
        self.errorlabel1_23.setSizePolicy(sizePolicy3)
        self.errorlabel1_23.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_17.addWidget(self.errorlabel1_23, 10, 3, 1, 1, Qt.AlignTop)

        self.label_75 = QLabel(self.frame_13)
        self.label_75.setObjectName(u"label_75")
        sizePolicy3.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy3)
        self.label_75.setFont(font12)
        self.label_75.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_17.addWidget(self.label_75, 0, 0, 1, 2)

        self.sensorTypcomboBox = QComboBox(self.frame_13)
        self.sensorTypcomboBox.addItem("")
        self.sensorTypcomboBox.addItem("")
        self.sensorTypcomboBox.setObjectName(u"sensorTypcomboBox")
        self.sensorTypcomboBox.setMinimumSize(QSize(0, 25))
        self.sensorTypcomboBox.setFont(font15)
        self.sensorTypcomboBox.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border:2px solid #383f42;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*style for dropdown area*/\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"\n"
"/*style drop down arrow*/\n"
"QComboBox::down-arrow{\n"
"	image: url(:/icons/Images for Program/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	margin-right:5px;\n"
"}\n"
"\n"
"/*style for menu list*/\n"
"QComboBox QListView{\n"
"	border:1px solid #383f42;\n"
"	padding:5px;\n"
"	background-color:#fff;\n"
"	outline:0px;\n"
"}\n"
"")
        self.sensorTypcomboBox.setEditable(True)

        self.gridLayout_17.addWidget(self.sensorTypcomboBox, 3, 3, 1, 1)


        self.gridLayout_15.addWidget(self.frame_13, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.Submit2 = QPushButton(self.scrollAreaWidgetContents)
        self.Submit2.setObjectName(u"Submit2")
        sizePolicy5.setHeightForWidth(self.Submit2.sizePolicy().hasHeightForWidth())
        self.Submit2.setSizePolicy(sizePolicy5)
        self.Submit2.setMinimumSize(QSize(120, 35))
        self.Submit2.setFont(font8)
        self.Submit2.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.Submit2.setIconSize(QSize(20, 20))
        self.Submit2.setAutoRepeatDelay(300)

        self.horizontalLayout_2.addWidget(self.Submit2, 0, Qt.AlignLeft)

        self.errorlabel1_36 = QLabel(self.scrollAreaWidgetContents)
        self.errorlabel1_36.setObjectName(u"errorlabel1_36")
        self.errorlabel1_36.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.horizontalLayout_2.addWidget(self.errorlabel1_36)

        self.creatword = QPushButton(self.scrollAreaWidgetContents)
        self.creatword.setObjectName(u"creatword")
        self.creatword.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.creatword.sizePolicy().hasHeightForWidth())
        self.creatword.setSizePolicy(sizePolicy5)
        self.creatword.setMinimumSize(QSize(120, 35))
        self.creatword.setFont(font8)
        self.creatword.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.horizontalLayout_2.addWidget(self.creatword)


        self.gridLayout_15.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.ExportPage)
        self.BasisdatenPage = QWidget()
        self.BasisdatenPage.setObjectName(u"BasisdatenPage")
        self.gridLayout_9 = QGridLayout(self.BasisdatenPage)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(9, -1, -1, -1)
        self.frame_16 = QFrame(self.BasisdatenPage)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy6.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy6)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_16)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_1_page4 = QLabel(self.frame_16)
        self.label_1_page4.setObjectName(u"label_1_page4")
        sizePolicy3.setHeightForWidth(self.label_1_page4.sizePolicy().hasHeightForWidth())
        self.label_1_page4.setSizePolicy(sizePolicy3)
        self.label_1_page4.setFont(font4)
        self.label_1_page4.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_10.addWidget(self.label_1_page4, 5, 0, 1, 1)

        self.Tw_lineedit_page4 = QLineEdit(self.frame_16)
        self.Tw_lineedit_page4.setObjectName(u"Tw_lineedit_page4")
        sizePolicy10.setHeightForWidth(self.Tw_lineedit_page4.sizePolicy().hasHeightForWidth())
        self.Tw_lineedit_page4.setSizePolicy(sizePolicy10)
        self.Tw_lineedit_page4.setMinimumSize(QSize(0, 25))
        self.Tw_lineedit_page4.setFont(font6)
        self.Tw_lineedit_page4.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_10.addWidget(self.Tw_lineedit_page4, 5, 1, 1, 2)

        self.errorlabel1_39 = QLabel(self.frame_16)
        self.errorlabel1_39.setObjectName(u"errorlabel1_39")
        sizePolicy3.setHeightForWidth(self.errorlabel1_39.sizePolicy().hasHeightForWidth())
        self.errorlabel1_39.setSizePolicy(sizePolicy3)
        self.errorlabel1_39.setMinimumSize(QSize(0, 0))
        self.errorlabel1_39.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_10.addWidget(self.errorlabel1_39, 8, 1, 1, 1, Qt.AlignTop)

        self.label_2_page4 = QLabel(self.frame_16)
        self.label_2_page4.setObjectName(u"label_2_page4")
        sizePolicy3.setHeightForWidth(self.label_2_page4.sizePolicy().hasHeightForWidth())
        self.label_2_page4.setSizePolicy(sizePolicy3)
        self.label_2_page4.setFont(font4)
        self.label_2_page4.setStyleSheet(u"\n"
"color:rgb(255, 255, 255)")

        self.gridLayout_10.addWidget(self.label_2_page4, 7, 0, 1, 1)

        self.errorlabel1_37 = QLabel(self.frame_16)
        self.errorlabel1_37.setObjectName(u"errorlabel1_37")
        sizePolicy3.setHeightForWidth(self.errorlabel1_37.sizePolicy().hasHeightForWidth())
        self.errorlabel1_37.setSizePolicy(sizePolicy3)
        self.errorlabel1_37.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_10.addWidget(self.errorlabel1_37, 3, 0, 1, 1, Qt.AlignTop)

        self.progressBar = QProgressBar(self.frame_16)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 25))
        self.progressBar.setMaximumSize(QSize(16777215, 25))
        self.progressBar.setFont(font6)
        self.progressBar.setStyleSheet(u"border-radius:2px")
        self.progressBar.setMaximum(1188)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_10.addWidget(self.progressBar, 10, 0, 1, 3)

        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font12)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignBottom)

        self.Tk_lineedit_page4 = QLineEdit(self.frame_16)
        self.Tk_lineedit_page4.setObjectName(u"Tk_lineedit_page4")
        sizePolicy10.setHeightForWidth(self.Tk_lineedit_page4.sizePolicy().hasHeightForWidth())
        self.Tk_lineedit_page4.setSizePolicy(sizePolicy10)
        self.Tk_lineedit_page4.setMinimumSize(QSize(0, 25))
        self.Tk_lineedit_page4.setFont(font6)
        self.Tk_lineedit_page4.setStyleSheet(u"QLineEdit{border-radius:5px;}\n"
"\n"
"QLineEdit:focus{border: 2px solid #383f42;border-radius:5px;}")

        self.gridLayout_10.addWidget(self.Tk_lineedit_page4, 7, 1, 1, 2)

        self.BrowsFile_basisdaten1 = QPushButton(self.frame_16)
        self.BrowsFile_basisdaten1.setObjectName(u"BrowsFile_basisdaten1")
        self.BrowsFile_basisdaten1.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.BrowsFile_basisdaten1.sizePolicy().hasHeightForWidth())
        self.BrowsFile_basisdaten1.setSizePolicy(sizePolicy5)
        self.BrowsFile_basisdaten1.setMinimumSize(QSize(100, 35))
        self.BrowsFile_basisdaten1.setMaximumSize(QSize(16777215, 16777215))
        self.BrowsFile_basisdaten1.setFont(font8)
        self.BrowsFile_basisdaten1.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_10.addWidget(self.BrowsFile_basisdaten1, 1, 2, 1, 1)

        self.filelabel_page4_1 = QLineEdit(self.frame_16)
        self.filelabel_page4_1.setObjectName(u"filelabel_page4_1")
        self.filelabel_page4_1.setMinimumSize(QSize(400, 25))
        self.filelabel_page4_1.setFont(font15)
        self.filelabel_page4_1.setStyleSheet(u"QLineEdit{border-radius:5px;} \n"
"QLineEdit:focus{border: 2px solid #383f42; border-radius:5px;}")

        self.gridLayout_10.addWidget(self.filelabel_page4_1, 1, 0, 1, 2)

        self.errorlabel1_38 = QLabel(self.frame_16)
        self.errorlabel1_38.setObjectName(u"errorlabel1_38")
        sizePolicy3.setHeightForWidth(self.errorlabel1_38.sizePolicy().hasHeightForWidth())
        self.errorlabel1_38.setSizePolicy(sizePolicy3)
        self.errorlabel1_38.setMinimumSize(QSize(0, 0))
        self.errorlabel1_38.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_10.addWidget(self.errorlabel1_38, 6, 1, 1, 1, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_10.addItem(self.verticalSpacer, 12, 1, 1, 1)

        self.progressBarLabel = QLabel(self.frame_16)
        self.progressBarLabel.setObjectName(u"progressBarLabel")
        self.progressBarLabel.setFont(font11)
        self.progressBarLabel.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.gridLayout_10.addWidget(self.progressBarLabel, 9, 0, 1, 2, Qt.AlignBottom)


        self.gridLayout_9.addWidget(self.frame_16, 0, 0, 1, 3)

        self.Submit_basisdaten = QPushButton(self.BasisdatenPage)
        self.Submit_basisdaten.setObjectName(u"Submit_basisdaten")
        sizePolicy5.setHeightForWidth(self.Submit_basisdaten.sizePolicy().hasHeightForWidth())
        self.Submit_basisdaten.setSizePolicy(sizePolicy5)
        self.Submit_basisdaten.setMinimumSize(QSize(120, 35))
        self.Submit_basisdaten.setFont(font8)
        self.Submit_basisdaten.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")
        self.Submit_basisdaten.setIconSize(QSize(20, 20))
        self.Submit_basisdaten.setAutoRepeatDelay(300)

        self.gridLayout_9.addWidget(self.Submit_basisdaten, 1, 0, 1, 1)

        self.errorlabel1_40 = QLabel(self.BasisdatenPage)
        self.errorlabel1_40.setObjectName(u"errorlabel1_40")
        self.errorlabel1_40.setStyleSheet(u"color: rgb(251, 215, 69);\n"
"font: 9pt \"Noto Sans\";")

        self.gridLayout_9.addWidget(self.errorlabel1_40, 1, 1, 1, 1, Qt.AlignRight)

        self.exportBasisdaten_btn = QPushButton(self.BasisdatenPage)
        self.exportBasisdaten_btn.setObjectName(u"exportBasisdaten_btn")
        self.exportBasisdaten_btn.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.exportBasisdaten_btn.sizePolicy().hasHeightForWidth())
        self.exportBasisdaten_btn.setSizePolicy(sizePolicy5)
        self.exportBasisdaten_btn.setMinimumSize(QSize(120, 35))
        self.exportBasisdaten_btn.setFont(font8)
        self.exportBasisdaten_btn.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Siemens Sans Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 63, 66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 205, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(250, 171, 72);\n"
"}")

        self.gridLayout_9.addWidget(self.exportBasisdaten_btn, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.BasisdatenPage)

        self.gridLayout_7.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.main_body_cont_frame)

        self.right_frame = QFrame(self.mainBody_frame)
        self.right_frame.setObjectName(u"right_frame")
        sizePolicy3.setHeightForWidth(self.right_frame.sizePolicy().hasHeightForWidth())
        self.right_frame.setSizePolicy(sizePolicy3)
        self.right_frame.setMinimumSize(QSize(100, 0))
        self.right_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.right_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.stackedWidget_2 = QStackedWidget(self.right_frame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy3.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy3)
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.inputData_hinweise = QWidget()
        self.inputData_hinweise.setObjectName(u"inputData_hinweise")
        self.verticalLayout_17 = QVBoxLayout(self.inputData_hinweise)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_3 = QFrame(self.inputData_hinweise)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.hinweis_icon_label = QLabel(self.frame_4)
        self.hinweis_icon_label.setObjectName(u"hinweis_icon_label")
        sizePolicy5.setHeightForWidth(self.hinweis_icon_label.sizePolicy().hasHeightForWidth())
        self.hinweis_icon_label.setSizePolicy(sizePolicy5)
        self.hinweis_icon_label.setTextFormat(Qt.AutoText)
        self.hinweis_icon_label.setPixmap(QPixmap(u":/icons/Images for Program/icons/exclamationMark.png"))

        self.horizontalLayout_12.addWidget(self.hinweis_icon_label)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)
        font17 = QFont()
        font17.setFamily(u"Noto Sans")
        font17.setPointSize(14)
        font17.setBold(True)
        font17.setWeight(75)
        self.label_11.setFont(font17)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.verticalLayout_14.addWidget(self.frame_4)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setFont(font11)
        self.label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label)


        self.verticalLayout_15.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.stackedWidget_2.addWidget(self.inputData_hinweise)
        self.calculation_hinweise = QWidget()
        self.calculation_hinweise.setObjectName(u"calculation_hinweise")
        self.verticalLayout_2 = QVBoxLayout(self.calculation_hinweise)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.calculation_hinweise)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_7)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.hinweis_icon_label_2 = QLabel(self.frame_8)
        self.hinweis_icon_label_2.setObjectName(u"hinweis_icon_label_2")
        sizePolicy5.setHeightForWidth(self.hinweis_icon_label_2.sizePolicy().hasHeightForWidth())
        self.hinweis_icon_label_2.setSizePolicy(sizePolicy5)
        self.hinweis_icon_label_2.setTextFormat(Qt.AutoText)
        self.hinweis_icon_label_2.setPixmap(QPixmap(u":/icons/Images for Program/icons/exclamationMark.png"))

        self.horizontalLayout_13.addWidget(self.hinweis_icon_label_2)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setFont(font17)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_19.addWidget(self.frame_8)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setFont(font11)
        self.label_13.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setTextFormat(Qt.RichText)
        self.label_13.setScaledContents(True)
        self.label_13.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_13)


        self.verticalLayout_18.addWidget(self.frame_7, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.stackedWidget_2.addWidget(self.calculation_hinweise)
        self.Export_hinweise = QWidget()
        self.Export_hinweise.setObjectName(u"Export_hinweise")
        self.verticalLayout_34 = QVBoxLayout(self.Export_hinweise)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_9 = QFrame(self.Export_hinweise)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_9)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_10)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.hinweis_icon_label_3 = QLabel(self.frame_11)
        self.hinweis_icon_label_3.setObjectName(u"hinweis_icon_label_3")
        sizePolicy5.setHeightForWidth(self.hinweis_icon_label_3.sizePolicy().hasHeightForWidth())
        self.hinweis_icon_label_3.setSizePolicy(sizePolicy5)
        self.hinweis_icon_label_3.setTextFormat(Qt.AutoText)
        self.hinweis_icon_label_3.setPixmap(QPixmap(u":/icons/Images for Program/icons/exclamationMark.png"))

        self.horizontalLayout_14.addWidget(self.hinweis_icon_label_3)

        self.label_38 = QLabel(self.frame_11)
        self.label_38.setObjectName(u"label_38")
        sizePolicy5.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy5)
        self.label_38.setFont(font17)

        self.horizontalLayout_14.addWidget(self.label_38)

        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)


        self.verticalLayout_33.addWidget(self.frame_11)

        self.label_39 = QLabel(self.frame_10)
        self.label_39.setObjectName(u"label_39")
        sizePolicy3.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy3)
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setFont(font11)
        self.label_39.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_39.setLayoutDirection(Qt.LeftToRight)
        self.label_39.setTextFormat(Qt.RichText)
        self.label_39.setScaledContents(True)
        self.label_39.setWordWrap(True)

        self.verticalLayout_33.addWidget(self.label_39)


        self.verticalLayout_27.addWidget(self.frame_10, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_34.addWidget(self.frame_9)

        self.stackedWidget_2.addWidget(self.Export_hinweise)
        self.Basisdaten_hinweise = QWidget()
        self.Basisdaten_hinweise.setObjectName(u"Basisdaten_hinweise")
        self.verticalLayout_3 = QVBoxLayout(self.Basisdaten_hinweise)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_17 = QFrame(self.Basisdaten_hinweise)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy3.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy3)
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_17)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMinimumSize(QSize(0, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.hinweis_icon_label_4 = QLabel(self.frame_19)
        self.hinweis_icon_label_4.setObjectName(u"hinweis_icon_label_4")
        sizePolicy5.setHeightForWidth(self.hinweis_icon_label_4.sizePolicy().hasHeightForWidth())
        self.hinweis_icon_label_4.setSizePolicy(sizePolicy5)
        self.hinweis_icon_label_4.setTextFormat(Qt.AutoText)
        self.hinweis_icon_label_4.setPixmap(QPixmap(u":/icons/Images for Program/icons/exclamationMark.png"))

        self.horizontalLayout_15.addWidget(self.hinweis_icon_label_4)

        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setFont(font17)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)


        self.verticalLayout_21.addWidget(self.frame_19)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setMinimumSize(QSize(0, 0))
        self.label_17.setFont(font11)
        self.label_17.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_17.setLayoutDirection(Qt.LeftToRight)
        self.label_17.setTextFormat(Qt.RichText)
        self.label_17.setScaledContents(True)
        self.label_17.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_17)


        self.verticalLayout_20.addWidget(self.frame_18, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_17)

        self.stackedWidget_2.addWidget(self.Basisdaten_hinweise)

        self.verticalLayout_16.addWidget(self.stackedWidget_2)

        self.frame = QFrame(self.right_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_back = QPushButton(self.frame)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setEnabled(False)
        self.pushButton_back.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Images for Program/icons/arrow-left-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_back.setIcon(icon6)
        self.pushButton_back.setIconSize(QSize(32, 32))
        self.pushButton_back.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.pushButton_back, 0, Qt.AlignRight)

        self.pushButton_next = QPushButton(self.frame)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Images for Program/icons/arrow-right-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_next.setIcon(icon7)
        self.pushButton_next.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.pushButton_next, 0, Qt.AlignLeft)


        self.verticalLayout_16.addWidget(self.frame)


        self.horizontalLayout_8.addWidget(self.right_frame)


        self.verticalLayout.addWidget(self.mainBody_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMinimumSize(QSize(0, 75))
        self.footer_frame.setStyleSheet(u"/*#footer_frame{background-color: qlineargradient(spread:pad, x0:0, y0:0, x0:0, y0:0, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));}*/\n"
"\n"
"#footer_frame{background-color:qlineargradient(spread:pad, x1:0.250, y1:0.477591, x2:0.375, y2:0.482, stop:0.25 rgba(255, 255, 255, 255), stop:0.255 rgba(56, 63, 66, 255))}")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 5, 5)
        self.fotter_left_frame = QFrame(self.footer_frame)
        self.fotter_left_frame.setObjectName(u"fotter_left_frame")
        self.fotter_left_frame.setFrameShape(QFrame.StyledPanel)
        self.fotter_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fotter_left_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(200, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.footer_logo = QLabel(self.fotter_left_frame)
        self.footer_logo.setObjectName(u"footer_logo")
        self.footer_logo.setMaximumSize(QSize(65, 60))
        self.footer_logo.setPixmap(QPixmap(u":/icons/Images for Program/icons/logo.png"))
        self.footer_logo.setScaledContents(True)
        self.footer_logo.setAlignment(Qt.AlignCenter)
        self.footer_logo.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.footer_logo, 0, Qt.AlignBottom)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_5.addWidget(self.fotter_left_frame)

        self.footer_label = QLabel(self.footer_frame)
        self.footer_label.setObjectName(u"footer_label")
        font18 = QFont()
        font18.setFamily(u"Barlow")
        font18.setPointSize(11)
        self.footer_label.setFont(font18)
        self.footer_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.footer_label, 0, Qt.AlignBottom)

        self.horizontalSpacer_10 = QSpacerItem(200, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.version_label = QLabel(self.footer_frame)
        self.version_label.setObjectName(u"version_label")
        font19 = QFont()
        font19.setFamily(u"Barlow")
        font19.setPointSize(8)
        font19.setBold(False)
        font19.setItalic(False)
        font19.setWeight(50)
        self.version_label.setFont(font19)
        self.version_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.version_label, 0, Qt.AlignBottom)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.footer_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Browsefile, self.filelabel)
        QWidget.setTabOrder(self.filelabel, self.Motoren_box)
        QWidget.setTabOrder(self.Motoren_box, self.Tw_lineedit)
        QWidget.setTabOrder(self.Tw_lineedit, self.Tk_lineedit)
        QWidget.setTabOrder(self.Tk_lineedit, self.radioButton_1)
        QWidget.setTabOrder(self.radioButton_1, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.VV_Box)
        QWidget.setTabOrder(self.VV_Box, self.Data_input_btn)
        QWidget.setTabOrder(self.Data_input_btn, self.calculat_btn)
        QWidget.setTabOrder(self.calculat_btn, self.Data_sheet_btn)
        QWidget.setTabOrder(self.Data_sheet_btn, self.calculat_all)
        QWidget.setTabOrder(self.calculat_all, self.calculat_specific)
        QWidget.setTabOrder(self.calculat_specific, self.wordTemplate)
        QWidget.setTabOrder(self.wordTemplate, self.filelabel_2)
        QWidget.setTabOrder(self.filelabel_2, self.Motortyp_lineedit)
        QWidget.setTabOrder(self.Motortyp_lineedit, self.Motor_ID_lineedit)
        QWidget.setTabOrder(self.Motor_ID_lineedit, self.stator_ID_lineedit)
        QWidget.setTabOrder(self.stator_ID_lineedit, self.rotor_ID_lineedit)
        QWidget.setTabOrder(self.rotor_ID_lineedit, self.motor_DBL_lineedit)
        QWidget.setTabOrder(self.motor_DBL_lineedit, self.motor_AS_lineedit)
        QWidget.setTabOrder(self.motor_AS_lineedit, self.Trgheitsmoment_lineedit)
        QWidget.setTabOrder(self.Trgheitsmoment_lineedit, self.sensorTypcomboBox)
        QWidget.setTabOrder(self.sensorTypcomboBox, self.zwischenkreisspannung_lineedit)
        QWidget.setTabOrder(self.zwischenkreisspannung_lineedit, self.Vorschaltdrossel_lineedit)
        QWidget.setTabOrder(self.Vorschaltdrossel_lineedit, self.Drehzahlbegrenzung_lineedit)
        QWidget.setTabOrder(self.Drehzahlbegrenzung_lineedit, self.DBL_version_lineedit)
        QWidget.setTabOrder(self.DBL_version_lineedit, self.DBL_ID_lineedit)
        QWidget.setTabOrder(self.DBL_ID_lineedit, self.Anwendugs_AS_lineedit)
        QWidget.setTabOrder(self.Anwendugs_AS_lineedit, self.sensorTypcomboBox_ANW)
        QWidget.setTabOrder(self.sensorTypcomboBox_ANW, self.Encoder_Strichzahl_lineedit)
        QWidget.setTabOrder(self.Encoder_Strichzahl_lineedit, self.Encoder_Auswertrichtung_comboBox)
        QWidget.setTabOrder(self.Encoder_Auswertrichtung_comboBox, self.Encoder_Bezeichnung_lineedit)
        QWidget.setTabOrder(self.Encoder_Bezeichnung_lineedit, self.Drehzahlbegrenzung2_lineedit)
        QWidget.setTabOrder(self.Drehzahlbegrenzung2_lineedit, self.Vorschaltdrossel2_lineedit)
        QWidget.setTabOrder(self.Vorschaltdrossel2_lineedit, self.Submit2)
        QWidget.setTabOrder(self.Submit2, self.creatword)
        QWidget.setTabOrder(self.creatword, self.Menu_btn)
        QWidget.setTabOrder(self.Menu_btn, self.scrollArea)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.VV_Box.setCurrentIndex(-1)
        self.Motoren_box.setCurrentIndex(-1)
        self.laengeBox.setCurrentIndex(-1)
        self.Encoder_Schnitstelle_comboBox.setCurrentIndex(0)
        self.Encoder_Auswertrichtung_comboBox.setCurrentIndex(-1)
        self.Encoder_Hersteller_comboBox.setCurrentIndex(0)
        self.sensorTypcomboBox_ANW.setCurrentIndex(-1)
        self.sensorTypcomboBox.setCurrentIndex(-1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Menu_btn.setText("")
        self.logo_label.setText("")
        self.logo_title_label.setText(QCoreApplication.translate("MainWindow", u"DATA SHEET MANAGER", None))
        self.Data_input_label.setText(QCoreApplication.translate("MainWindow", u"Data Input", None))
        self.Data_sheet_btn.setText("")
        self.Data_sheet_label.setText(QCoreApplication.translate("MainWindow", u"Data sheet", None))
        self.calculat_label.setText(QCoreApplication.translate("MainWindow", u"Calculation", None))
        self.basisdaten_btn.setText("")
        self.calculat_btn.setText("")
        self.Basisdaten_label.setText(QCoreApplication.translate("MainWindow", u" Basisdaten", None))
        self.Data_input_btn.setText("")
        self.Submit1.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.errorlabel1_5.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Die L\u00e4nge X in mm: * ", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Den Motor XXXHX oder XXXUHX: *", None))
        self.errorlabel1_3.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.Tk_lineedit.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Die max. Wicklungstemperatur in \u00b0C: *", None))
        self.errorlabel1_2.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.errorlabel1_7.setText(QCoreApplication.translate("MainWindow", u"* Motor \u00e4ndern", None))
        self.errorlabel1_4.setText(QCoreApplication.translate("MainWindow", u"* Bitte Spannung eingeben", None))
        self.errorlabel1_11.setText(QCoreApplication.translate("MainWindow", u"* Bitte, w\u00e4helen Sie das SCV Datei !", None))
        self.Browsefile.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"400", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"425", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Die K\u00fchlungstemperatur in \u00b0C: *", None))
        self.Tw_lineedit.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.Motoren_box.setItemText(0, QCoreApplication.translate("MainWindow", u"200HX", None))
        self.Motoren_box.setItemText(1, QCoreApplication.translate("MainWindow", u"200UHX", None))
        self.Motoren_box.setItemText(2, QCoreApplication.translate("MainWindow", u"240HX", None))
        self.Motoren_box.setItemText(3, QCoreApplication.translate("MainWindow", u"240UHX", None))
        self.Motoren_box.setItemText(4, QCoreApplication.translate("MainWindow", u"310HX", None))
        self.Motoren_box.setItemText(5, QCoreApplication.translate("MainWindow", u"310UHX", None))
        self.Motoren_box.setItemText(6, QCoreApplication.translate("MainWindow", u"360UHX", None))
        self.Motoren_box.setItemText(7, QCoreApplication.translate("MainWindow", u"410HX", None))
        self.Motoren_box.setItemText(8, QCoreApplication.translate("MainWindow", u"410UHX", None))
        self.Motoren_box.setItemText(9, QCoreApplication.translate("MainWindow", u"564HX", None))

        self.Motoren_box.setCurrentText("")
        self.errorlabel1_12.setText(QCoreApplication.translate("MainWindow", u"* Der ausgew\u00e4hle Motor hat keine Verschaltungsvarianten, W\u00e4hlen Sie einen anderen Motor aus", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"W\u00e4hlen Sie einen Spannungswert aus: *", None))
        self.errorlabel1_1.setText(QCoreApplication.translate("MainWindow", u"* Bitte, Motorname eingeben", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Die Verschaltungsvarianten: *", None))
        self.laengeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"25", None))
        self.laengeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"50", None))
        self.laengeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"75", None))
        self.laengeBox.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))
        self.laengeBox.setItemText(4, QCoreApplication.translate("MainWindow", u"125", None))
        self.laengeBox.setItemText(5, QCoreApplication.translate("MainWindow", u"150", None))
        self.laengeBox.setItemText(6, QCoreApplication.translate("MainWindow", u"175", None))
        self.laengeBox.setItemText(7, QCoreApplication.translate("MainWindow", u"200", None))
        self.laengeBox.setItemText(8, QCoreApplication.translate("MainWindow", u"225", None))
        self.laengeBox.setItemText(9, QCoreApplication.translate("MainWindow", u"250", None))
        self.laengeBox.setItemText(10, QCoreApplication.translate("MainWindow", u"275", None))
        self.laengeBox.setItemText(11, QCoreApplication.translate("MainWindow", u"300", None))

        self.laengeBox.setCurrentText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Wicklgstemp.Beginn \u0398* in [\u00b0C]:", None))
        self.Drehzahl_lineedit.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Die gew\u00fcnschte Nenndrehzahl in [1/min]: *", None))
        self.DeltaTeta_stern_lineedit.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.errorlabel1_6.setText(QCoreApplication.translate("MainWindow", u"*ung\u00fcltiger Wert", None))
        self.errorlabel1_9.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Die gew\u00fcnschte Pulsdauer t_p in [s]:", None))
        self.Teta_stern_lineedit.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.errorlabel1_8.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Temperatur erh\u00f6hung \u0394\u0398* in [K]: ", None))
        self.errorlabel1_10.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.Pulsdauer_lineedit.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.optionalBtn.setText(QCoreApplication.translate("MainWindow", u"Optional:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Der Strom in [A]:", None))
        self.Strom_lineEdit.setText("")
        self.calculat_all_2.setText(QCoreApplication.translate("MainWindow", u"Calculat all", None))
        self.errorlabel2_2.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltige Wert!", None))
        self.errorlabel2_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>* Sie haben nichts aus der Liste ausgew\u00e4hlt!</p></body></html>", None))
        self.calculat_all.setText(QCoreApplication.translate("MainWindow", u"All Data", None))
        self.errorlabel_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>* Bitte, Dateiverzeichnis</p><p>ausw\u00e4hlen !</p></body></html>", None))
        self.calculat_specific.setText(QCoreApplication.translate("MainWindow", u"Selected Data", None))
        self.GraphsBtn.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.all_variations_btn.setText(QCoreApplication.translate("MainWindow", u"All-variations", None))
        self.strom_change_label.setText(QCoreApplication.translate("MainWindow", u"Bitte aktivieren Sie das Check-k\u00e4stchen, wenn Sie den Wert des Stroms \u00e4ndern m\u00f6chten!", None))
        self.Strom_checkBox.setText(QCoreApplication.translate("MainWindow", u"Strom \u00e4ndern", None))
        self.importVorlageBtn.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.vorlageLabel.setText(QCoreApplication.translate("MainWindow", u"Datenblatt-Ersteller:", None))
        self.errorlabel_21.setText(QCoreApplication.translate("MainWindow", u"Bitte, die Datenblatt-Vorlage ausw\u00e4hlen !", None))
        self.generatDataSheetBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.vorlagePfadLineEdit.setInputMask("")
        self.vorlagePfadLineEdit.setText(QCoreApplication.translate("MainWindow", u"Bitte, die Datenblatt-Vorlage ausw\u00e4hlen:", None))
        self.errorlabel_22.setText(QCoreApplication.translate("MainWindow", u"\"Bitte w\u00e4hlen Sie einen Speicherpfad f\u00fcr das exportierte Datenblatt aus!", None))
        self.errorlabel1_41.setText(QCoreApplication.translate("MainWindow", u"* Bitte Template ausw\u00e4hlen!", None))
        self.creatExcel.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"4- Excel Vorlage ausw\u00e4hlen:", None))
        self.errorlabel1_42.setText(QCoreApplication.translate("MainWindow", u"* Bitte, Dateiverzeichnis ausw\u00e4hlen !", None))
        self.filelabel_3.setText(QCoreApplication.translate("MainWindow", u"HH-VorlageMM3.xlsx ausw\u00e4hlen", None))
        self.ExcelTemplate.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.errorlabel1_25.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert ", None))
        self.errorlabel1_30.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"3- Anwendungsspezifische Daten:", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Encoder-Bezeichnung", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Encoder-Strichzahl", None))
        self.Encoder_Schnitstelle_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1Vss", None))
        self.Encoder_Schnitstelle_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"EnDat 2.1", None))
        self.Encoder_Schnitstelle_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"EnDat 2.2", None))
        self.Encoder_Schnitstelle_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"EnDat 2.2 FS", None))
        self.Encoder_Schnitstelle_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"SSI", None))

        self.Anwendugs_AS_lineedit.setText(QCoreApplication.translate("MainWindow", u"9876", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Mech. Drehzahlbegrenzung", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Motor-AS", None))
        self.Encoder_Auswertrichtung_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"+", None))
        self.Encoder_Auswertrichtung_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"-", None))
        self.Encoder_Auswertrichtung_comboBox.setItemText(2, "")

        self.Vorschaltdrossel2_lineedit.setText(QCoreApplication.translate("MainWindow", u"1.3", None))
        self.Encoder_Bezeichnung_lineedit.setText(QCoreApplication.translate("MainWindow", u"RCN471", None))
        self.Drehzahlbegrenzung2_lineedit.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.errorlabel1_28.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.DBL_version_lineedit.setText(QCoreApplication.translate("MainWindow", u"02", None))
        self.errorlabel1_33.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert ", None))
        self.errorlabel1_34.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"DBL-ID 205", None))
        self.Encoder_Hersteller_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Heidenhain", None))
        self.Encoder_Hersteller_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Amo", None))
        self.Encoder_Hersteller_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Zettlex", None))
        self.Encoder_Hersteller_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"L&B", None))

        self.errorlabel1_27.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.errorlabel1_31.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Encoder-Schnitstelle", None))
        self.errorlabel1_26.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.errorlabel1_29.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert ", None))
        self.DBL_ID_lineedit.setText(QCoreApplication.translate("MainWindow", u"1234", None))
        self.sensorTypcomboBox_ANW.setItemText(0, QCoreApplication.translate("MainWindow", u"PT1000", None))
        self.sensorTypcomboBox_ANW.setItemText(1, QCoreApplication.translate("MainWindow", u"KTY 84-130", None))

        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Encoder-Auswertrichtung", None))
        self.Encoder_Strichzahl_lineedit.setText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"DBL-Version", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Typ Temperatursensor", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Vorschaltdrossel [mH]", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Encoder-Hersteller", None))
        self.errorlabel1_32.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.errorlabel1_24.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.filelabel_4.setText(QCoreApplication.translate("MainWindow", u"motor_oem.mot3 Datei ausw\u00e4hlen:", None))
        self.wordTemplate.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.mot3DateiImport.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.filelabel_2.setText(QCoreApplication.translate("MainWindow", u"Siemens, HH, Fanuc oder Rexroth Vorlage ausw\u00e4hlen:", None))
        self.errorlabel1_35.setText(QCoreApplication.translate("MainWindow", u"* Bitte Template ausw\u00e4hlen!", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"1- Vorlage ausw\u00e4hlen:", None))
        self.rotor_ID_lineedit.setText(QCoreApplication.translate("MainWindow", u"3333", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Stator-ID 166-", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Motor-ID 166-", None))
        self.motor_AS_lineedit.setText(QCoreApplication.translate("MainWindow", u"0815", None))
        self.errorlabel1_22.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert ", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Motor-DBL-Version", None))
        self.Motortyp_lineedit.setText(QCoreApplication.translate("MainWindow", u"RMHS 564-250", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Tr\u00e4gheitsmoment [kgm\u00b2]", None))
        self.errorlabel1_14.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert ", None))
        self.errorlabel1_17.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Motor-AS", None))
        self.errorlabel1_13.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Vorschaltdrossel [mH]", None))
        self.stator_ID_lineedit.setText(QCoreApplication.translate("MainWindow", u"2222", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Rotor-ID 166-", None))
        self.errorlabel1_18.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert ", None))
        self.Motor_ID_lineedit.setText(QCoreApplication.translate("MainWindow", u"1111", None))
        self.motor_DBL_lineedit.setText(QCoreApplication.translate("MainWindow", u"01", None))
        self.Trgheitsmoment_lineedit.setText(QCoreApplication.translate("MainWindow", u"1.5", None))
        self.errorlabel1_15.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Zwischenkreisspannung", None))
        self.errorlabel1_21.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.Vorschaltdrossel_lineedit.setText(QCoreApplication.translate("MainWindow", u"5.5", None))
        self.errorlabel1_16.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.errorlabel1_20.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Typ Temperatursensor", None))
        self.zwischenkreisspannung_lineedit.setText(QCoreApplication.translate("MainWindow", u"600", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Motortyp", None))
        self.errorlabel1_19.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.Drehzahlbegrenzung_lineedit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Elec. Drehzahlbegrenzung", None))
        self.errorlabel1_23.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"2- Angaben zum Motor:", None))
        self.sensorTypcomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"PT1000", None))
        self.sensorTypcomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"KTY 84-130", None))

        self.Submit2.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.errorlabel1_36.setText(QCoreApplication.translate("MainWindow", u"* Bitte, Dateiverzeichnis ausw\u00e4hlen !", None))
        self.creatword.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_1_page4.setText(QCoreApplication.translate("MainWindow", u"Die max. Wicklungstemperatur in \u00b0C: *", None))
        self.Tw_lineedit_page4.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.errorlabel1_39.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.label_2_page4.setText(QCoreApplication.translate("MainWindow", u"Die K\u00fchlungstemperatur in \u00b0C: *", None))
        self.errorlabel1_37.setText(QCoreApplication.translate("MainWindow", u"* Bitte Template ausw\u00e4hlen!", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1- CSV-Datei ausw\u00e4hlen:", None))
        self.Tk_lineedit_page4.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.BrowsFile_basisdaten1.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.errorlabel1_38.setText(QCoreApplication.translate("MainWindow", u"* ung\u00fcltiger Wert", None))
        self.progressBarLabel.setText(QCoreApplication.translate("MainWindow", u"Please don't click on the program interface! Calculation in progress ... ", None))
        self.Submit_basisdaten.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.errorlabel1_40.setText(QCoreApplication.translate("MainWindow", u"* Bitte, Dateiverzeichnis ausw\u00e4hlen !", None))
        self.exportBasisdaten_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.hinweis_icon_label.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Hinweise:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Noto Sans','sans-serif';\">Geben Sie alle folgenden Daten ein.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Bitte nur Ziefern in den Felder eingeben.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Bei der Auswahl von Motoren, die noch keine Verschaltungnsvarianten bzw. keine vollst\u00e4ndigen daten haben, das Programm kann die Berechnung nicht ausf\u00fchren und eine Fehlermeldung wird angezeigt um einen anderen Motor aus zu w\u00e4hlen.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">\u00a0Wenn Sie in einigen Eingabefeldern keine Daten zur Eingabe haben, lassen Sie bitte die zuvor eingegebenen Daten in dem Feld.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Nachdem Sie alle Felder ausgef\u00fcllt haben, klicken Sie auf Submit.</span></p></body></html>", None))
        self.hinweis_icon_label_2.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Hinweise:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Noto Sans','sans-serif';\">Die Berechnungen sind erst m\u00f6glich nach dem Ausf\u00fcllen der vorherigen Felder und dem Submit-Klick.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Um alle berechneten Ergebnisse in einer Tabelle anzuzeigen, klicken Sie auf &quot;All Data&quot;.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Um bestimmte berechnete Ergebnisse in einer Tabelle anzuzeigen, w\u00e4hlen Sie die zu berechnenden Werte aus der Liste daneben aus und klicken Sie dann auf \u00a0&quot;Selected Data&quot;.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Nach einem Klick auf .&quot;All Data / Selected Data&quot; erscheint die Tabelle mit den Ergebnissen, die \u00fcber die \u201eOptions\u201c in der Men\u00fcleiste in eine Excel-Datei exportiert werden k\u00f6nnen. </span></p><p>Wenn Sie die Daten f\u00fcr den ausgew\u00e4hlten Motor f\u00fcr alle verf\u00fcgbaren Verschaltungsvarianten in Excel e"
                        "xportieren m\u00f6chten, klicken Sie bitte auf &quot;Alle-Variations&quot;</p></body></html>", None))
        self.hinweis_icon_label_3.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Hinweise:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Noto Sans','sans-serif';\">Cliken Sie auf &quot;Browse File&quot; und w\u00e4hlen Sie eien Vorlage.</span>geben Sie alle Angaben zum Motor und die Anwendungsspezifische Daten ein, beachten Sie die Dezimalzahlen mit einem Punkt einzugeben. Sie k\u00f6nnen <span style=\" font-family:'Noto Sans','sans-serif';\">die zuvor eingegebenen Daten in dem Feld als Beispiel verwenden.</span></p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Wenn Sie in einigen Eingabefeldern keine Daten zur Eingabe haben, l\u00f6chen Sie bitte die zuvor eingegebenen Daten in dem Feld. Nachdem Sie die Felder ausgef\u00fcllt haben, klicken Sie auf Submit dann auf Export</span></p><p>Um die Daten in der Excel-Datei &quot;HH-VorlageMM3&quot; einzutragen, folgen Sie bitte diesen Schritten:</p><p>Klicken Sie nach dem Klick auf &quot;Submit&quot; auf &quot;Browse file&quot; unten auf der Seite.</p><p>W\u00e4hlen Sie die &quot;HH-VorlageMM3&quot; Excel-Datei aus.</p><p>Zum Abschluss klic"
                        "ken Sie bitte unten rechts auf &quot;Export&quot;.</p></body></html>", None))
        self.hinweis_icon_label_4.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Hinweise:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Noto Sans','sans-serif';\">Cliken Sie auf &quot;Browse File&quot; und w\u00e4hlen Sie die TechnoTab Datei.</span></p><p>Geben Sie die max. Wicklungstemperatur und die K\u00fchlungstemperatur ein, beachten Sie die Dezimalzahlen mit einem Punkt einzugebennicht mit komma.</p><p><span style=\" font-family:'Noto Sans','sans-serif';\">Nachdem Sie die Felder ausgef\u00fcllt haben, klicken Sie auf 'Submit'; </span>Bitte warten Sie, w\u00e4hrend die Berechnung durchgef\u00fchrt wird. Eine Fortschrittsanzeige zeigt den Ladefortschritt an. Bitte vermeiden Sie es, w\u00e4hrend des Ladevorgangs mit der Programmoberfl\u00e4che zu interagieren.</p><p>Nachdem die Fortschrittsanzeige erfolgreich geladen wurde, k\u00f6nnen Sie die Ergebnisse exportieren, indem Sie auf  &quot;Export&quot; klicken. W\u00e4hlen Sie den Speicherort aus, an dem Sie die exportierten Ergebnisse speichern m\u00f6chten.</p></body></html>", None))
        self.pushButton_back.setText("")
        self.pushButton_next.setText("")
        self.footer_logo.setText("")
        self.footer_label.setText(QCoreApplication.translate("MainWindow", u"MOTORTECHNIK GMBH 2024", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"Version: 1.0 | Copyrright MOTORTECHNIK.de", None))
    # retranslateUi

