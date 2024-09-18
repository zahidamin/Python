# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(652, 500)
        self.gridLayoutWidget = QWidget(widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(510, 60, 242, 161))
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

        self.gridLayout_4.addWidget(self.push_0, 3, 1, 1, 1)

        self.push_c = QPushButton(self.gridLayoutWidget)
        self.push_c.setObjectName(u"push_c")

        self.gridLayout_4.addWidget(self.push_c, 3, 0, 1, 1)

        self.formLayoutWidget = QWidget(widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 60, 471, 124))
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


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.push_7.setText(QCoreApplication.translate("widget", u"7", None))
#if QT_CONFIG(shortcut)
        self.push_7.setShortcut(QCoreApplication.translate("widget", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.push_1.setText(QCoreApplication.translate("widget", u"1", None))
#if QT_CONFIG(shortcut)
        self.push_1.setShortcut(QCoreApplication.translate("widget", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.push_5.setText(QCoreApplication.translate("widget", u"5", None))
#if QT_CONFIG(shortcut)
        self.push_5.setShortcut(QCoreApplication.translate("widget", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.push_4.setText(QCoreApplication.translate("widget", u"4", None))
#if QT_CONFIG(shortcut)
        self.push_4.setShortcut(QCoreApplication.translate("widget", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.push_2.setText(QCoreApplication.translate("widget", u"2", None))
#if QT_CONFIG(shortcut)
        self.push_2.setShortcut(QCoreApplication.translate("widget", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.push_6.setText(QCoreApplication.translate("widget", u"6", None))
#if QT_CONFIG(shortcut)
        self.push_6.setShortcut(QCoreApplication.translate("widget", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.push_8.setText(QCoreApplication.translate("widget", u"8", None))
#if QT_CONFIG(shortcut)
        self.push_8.setShortcut(QCoreApplication.translate("widget", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.push_9.setText(QCoreApplication.translate("widget", u"9", None))
#if QT_CONFIG(shortcut)
        self.push_9.setShortcut(QCoreApplication.translate("widget", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.push_3.setText(QCoreApplication.translate("widget", u"3", None))
#if QT_CONFIG(shortcut)
        self.push_3.setShortcut(QCoreApplication.translate("widget", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.push_dot.setText(QCoreApplication.translate("widget", u".", None))
#if QT_CONFIG(shortcut)
        self.push_dot.setShortcut(QCoreApplication.translate("widget", u".", None))
#endif // QT_CONFIG(shortcut)
        self.push_0.setText(QCoreApplication.translate("widget", u"0", None))
#if QT_CONFIG(shortcut)
        self.push_0.setShortcut(QCoreApplication.translate("widget", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.push_c.setText(QCoreApplication.translate("widget", u"C", None))
#if QT_CONFIG(shortcut)
        self.push_c.setShortcut(QCoreApplication.translate("widget", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.meterRentLabel.setText(QCoreApplication.translate("widget", u"Meter Rent", None))
        self.currentLabel.setText(QCoreApplication.translate("widget", u"Current", None))
        self.factorLabel.setText(QCoreApplication.translate("widget", u"Factor", None))
        self.previousLabel.setText(QCoreApplication.translate("widget", u"Previous", None))
        self.gCVLabel.setText(QCoreApplication.translate("widget", u"GCV", None))
        self.fixChargesLabel.setText(QCoreApplication.translate("widget", u"Fix Charges", None))
    # retranslateUi

