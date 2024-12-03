# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowsLBXpUC.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTableView, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Left_menu_widget = QWidget(self.centralwidget)
        self.Left_menu_widget.setObjectName(u"Left_menu_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Left_menu_widget.sizePolicy().hasHeightForWidth())
        self.Left_menu_widget.setSizePolicy(sizePolicy1)
        self.Left_menu_widget.setAutoFillBackground(False)
        self.Left_menu_widget.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.verticalLayout = QVBoxLayout(self.Left_menu_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.Left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(32, 32))
        self.label_10.setMaximumSize(QSize(32, 32))
        self.label_10.setPixmap(QPixmap(u":/Icons/dashboard.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.horizontalLayout_6.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.Left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setFont(font)

        self.verticalLayout_3.addWidget(self.label_12)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.comboBox)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/Icons/interest-rate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setMaximumSize(QSize(16777215, 50))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/pie-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setMaximumSize(QSize(16777215, 50))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/line-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy4)
        self.pushButton_4.setMaximumSize(QSize(16777215, 50))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/bar-chart2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.Left_menu_widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy6)
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.Left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.frame_7)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.header_frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy7)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.label_3 = QLabel(self.header_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.header_frame)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.header_frame)

        self.header_nav = QFrame(self.frame_7)
        self.header_nav.setObjectName(u"header_nav")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.header_nav.sizePolicy().hasHeightForWidth())
        self.header_nav.setSizePolicy(sizePolicy8)
        self.header_nav.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.header_nav)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_8 = QPushButton(self.header_nav)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy7.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy7)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/minus-sign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.pushButton_8)

        self.pushButton_2 = QPushButton(self.header_nav)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy7.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy7)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/full-screen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_9 = QPushButton(self.header_nav)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy7.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy7)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.pushButton_9)


        self.horizontalLayout.addWidget(self.header_nav)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.PercentageChart = QWidget()
        self.PercentageChart.setObjectName(u"PercentageChart")
        self.verticalLayout_12 = QVBoxLayout(self.PercentageChart)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_16 = QFrame(self.PercentageChart)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_11.addWidget(self.label_6)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.PercentageChart)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy2.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy2)
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout = QGridLayout(self.frame_17)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_12.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.PercentageChart)
        self.NestedChart = QWidget()
        self.NestedChart.setObjectName(u"NestedChart")
        self.verticalLayout_14 = QVBoxLayout(self.NestedChart)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_18 = QFrame(self.NestedChart)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.NestedChart)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy2.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy2)
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_2 = QGridLayout(self.frame_19)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_14.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.NestedChart)
        self.LineChart = QWidget()
        self.LineChart.setObjectName(u"LineChart")
        self.verticalLayout_16 = QVBoxLayout(self.LineChart)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_20 = QFrame(self.LineChart)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_15 = QVBoxLayout(self.frame_20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.frame_20)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_15.addWidget(self.label_8)


        self.verticalLayout_16.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.LineChart)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
        self.frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_3 = QGridLayout(self.frame_21)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout_16.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.LineChart)
        self.BarChart = QWidget()
        self.BarChart.setObjectName(u"BarChart")
        self.verticalLayout_18 = QVBoxLayout(self.BarChart)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_22 = QFrame(self.BarChart)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_9 = QLabel(self.frame_22)
        self.label_9.setObjectName(u"label_9")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy9)
        self.label_9.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_9)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_17.addWidget(self.frame_24)


        self.verticalLayout_18.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.BarChart)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_23 = QFrame(self.frame_13)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy2.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy2)
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_4 = QGridLayout(self.frame_23)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_11 = QLabel(self.frame_23)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_23)

        self.tableView = QTableView(self.frame_13)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_10.addWidget(self.tableView)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.frame_9.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.verticalLayout_8.addWidget(self.label_5)


        self.horizontalLayout_5.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy5.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy5)
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.size_grid = QFrame(self.frame_15)
        self.size_grid.setObjectName(u"size_grid")
        self.size_grid.setGeometry(QRect(130, 30, 120, 80))
        self.size_grid.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_5.addWidget(self.frame_15)


        self.verticalLayout_6.addWidget(self.frame_9)


        self.horizontalLayout_2.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"B\u1ea3ng th\u1ed1ng k\u00ea", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"H\u00e0m th\u1ed1ng k\u00ea", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Nested Donut Chart", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Line Chart", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t d\u1eef li\u1ec7u ra file", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"B\u1ea3ng th\u1ed1ng k\u00ea", None))
        self.pushButton_8.setText("")
        self.pushButton_2.setText("")
        self.pushButton_9.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nested Donut Chart", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Line Chart", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"B\u1ea3ng d\u1eef li\u1ec7u k\u1ebft qu\u1ea3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Copyrighsts Nhom 2", None))
    # retranslateUi

