# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GasCal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 350)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushCalculate = QPushButton(self.frame)
        self.pushCalculate.setObjectName(u"pushCalculate")
        self.pushCalculate.setGeometry(QRect(5, 155, 471, 26))
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(5, 30, 471, 124))
        self.gridLayout_3 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gcv = QLineEdit(self.formLayoutWidget)
        self.gcv.setObjectName(u"gcv")

        self.gridLayout_3.addWidget(self.gcv, 2, 3, 1, 1)

        self.fixCharg = QLineEdit(self.formLayoutWidget)
        self.fixCharg.setObjectName(u"fixCharg")

        self.gridLayout_3.addWidget(self.fixCharg, 4, 1, 1, 1)

        self.preReading = QLineEdit(self.formLayoutWidget)
        self.preReading.setObjectName(u"preReading")

        self.gridLayout_3.addWidget(self.preReading, 0, 1, 1, 1)

        self.curReading = QLineEdit(self.formLayoutWidget)
        self.curReading.setObjectName(u"curReading")

        self.gridLayout_3.addWidget(self.curReading, 0, 3, 1, 1)

        self.meterRentLabel = QLabel(self.formLayoutWidget)
        self.meterRentLabel.setObjectName(u"meterRentLabel")

        self.gridLayout_3.addWidget(self.meterRentLabel, 4, 2, 1, 1)

        self.meterRent = QLineEdit(self.formLayoutWidget)
        self.meterRent.setObjectName(u"meterRent")

        self.gridLayout_3.addWidget(self.meterRent, 4, 3, 1, 1)

        self.currentLabel = QLabel(self.formLayoutWidget)
        self.currentLabel.setObjectName(u"currentLabel")

        self.gridLayout_3.addWidget(self.currentLabel, 0, 2, 1, 1)

        self.factorLabel = QLabel(self.formLayoutWidget)
        self.factorLabel.setObjectName(u"factorLabel")

        self.gridLayout_3.addWidget(self.factorLabel, 2, 0, 1, 1)

        self.previousLabel = QLabel(self.formLayoutWidget)
        self.previousLabel.setObjectName(u"previousLabel")

        self.gridLayout_3.addWidget(self.previousLabel, 0, 0, 1, 1)

        self.gCVLabel = QLabel(self.formLayoutWidget)
        self.gCVLabel.setObjectName(u"gCVLabel")

        self.gridLayout_3.addWidget(self.gCVLabel, 2, 2, 1, 1)

        self.factor = QLineEdit(self.formLayoutWidget)
        self.factor.setObjectName(u"factor")

        self.gridLayout_3.addWidget(self.factor, 2, 1, 1, 1)

        self.fixChargesLabel = QLabel(self.formLayoutWidget)
        self.fixChargesLabel.setObjectName(u"fixChargesLabel")

        self.gridLayout_3.addWidget(self.fixChargesLabel, 4, 0, 1, 1)

        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(490, 30, 181, 161))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.push_7 = QPushButton(self.gridLayoutWidget)
        self.push_7.setObjectName(u"push_7")

        self.gridLayout_4.addWidget(self.push_7, 0, 0, 1, 1)

        self.push_1 = QPushButton(self.gridLayoutWidget)
        self.push_1.setObjectName(u"push_1")

        self.gridLayout_4.addWidget(self.push_1, 2, 0, 1, 1)

        self.push_5 = QPushButton(self.gridLayoutWidget)
        self.push_5.setObjectName(u"push_5")

        self.gridLayout_4.addWidget(self.push_5, 1, 1, 1, 1)

        self.push_4 = QPushButton(self.gridLayoutWidget)
        self.push_4.setObjectName(u"push_4")

        self.gridLayout_4.addWidget(self.push_4, 1, 0, 1, 1)

        self.push_2 = QPushButton(self.gridLayoutWidget)
        self.push_2.setObjectName(u"push_2")

        self.gridLayout_4.addWidget(self.push_2, 2, 1, 1, 1)

        self.push_6 = QPushButton(self.gridLayoutWidget)
        self.push_6.setObjectName(u"push_6")

        self.gridLayout_4.addWidget(self.push_6, 1, 2, 1, 1)

        self.push_8 = QPushButton(self.gridLayoutWidget)
        self.push_8.setObjectName(u"push_8")

        self.gridLayout_4.addWidget(self.push_8, 0, 1, 1, 1)

        self.push_9 = QPushButton(self.gridLayoutWidget)
        self.push_9.setObjectName(u"push_9")

        self.gridLayout_4.addWidget(self.push_9, 0, 2, 1, 1)

        self.push_3 = QPushButton(self.gridLayoutWidget)
        self.push_3.setObjectName(u"push_3")

        self.gridLayout_4.addWidget(self.push_3, 2, 2, 1, 1)

        self.push_dot = QPushButton(self.gridLayoutWidget)
        self.push_dot.setObjectName(u"push_dot")

        self.gridLayout_4.addWidget(self.push_dot, 3, 2, 1, 1)

        self.push_0 = QPushButton(self.gridLayoutWidget)
        self.push_0.setObjectName(u"push_0")

        self.gridLayout_4.addWidget(self.push_0, 3, 0, 1, 2)

        self.totAmount = QPlainTextEdit(self.frame)
        self.totAmount.setObjectName(u"totAmount")
        self.totAmount.setGeometry(QRect(5, 185, 471, 70))
        self.header = QLabel(self.frame)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(180, 250, 331, 41))
        self.header.setMaximumSize(QSize(16777202, 16777202))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.header.setFont(font)
        self.pushOnlineBill = QPushButton(self.frame)
        self.pushOnlineBill.setObjectName(u"pushOnlineBill")
        self.pushOnlineBill.setGeometry(QRect(515, 205, 121, 41))
        self.footer = QLabel(self.frame)
        self.footer.setObjectName(u"footer")
        self.footer.setGeometry(QRect(210, 0, 271, 26))
        self.footer.setMaximumSize(QSize(16777202, 16777202))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.footer.setFont(font1)

        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.meterRentLabel.setText(QCoreApplication.translate("MainWindow", u"Meter Rent", None))
        self.currentLabel.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.factorLabel.setText(QCoreApplication.translate("MainWindow", u"Factor", None))
        self.previousLabel.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.gCVLabel.setText(QCoreApplication.translate("MainWindow", u"GCV", None))
        self.fixChargesLabel.setText(QCoreApplication.translate("MainWindow", u"Fix Charges", None))
        self.push_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.push_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.push_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.push_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.push_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.push_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.push_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.push_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.push_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.push_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.push_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.push_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.push_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.push_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.push_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.push_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.push_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.push_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.push_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.push_dot.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.push_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.push_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.totAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.header.setText(QCoreApplication.translate("MainWindow", u"Sui Northern Gas Pipelines Limited (SNGPL)", None))
        self.pushOnlineBill.setText(QCoreApplication.translate("MainWindow", u"Online Bill", None))
        self.footer.setText(QCoreApplication.translate("MainWindow", u"Gas Bill Calculator (SNGPL)", None))
    # retranslateUi

