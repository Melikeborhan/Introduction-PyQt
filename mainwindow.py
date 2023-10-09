# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)

class Ui_txtEmail(object):
    def setupUi(self, txtEmail):
        if not txtEmail.objectName():
            txtEmail.setObjectName(u"txtEmail")
        txtEmail.resize(800, 600)
        txtEmail.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget = QWidget(txtEmail)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 60, 391, 341))
        self.frame.setStyleSheet(u" \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.password = QTextBrowser(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 200, 91, 21))
        self.txt_password = QTextBrowser(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(30, 230, 271, 41))
        self.email_txt = QTextBrowser(self.frame)
        self.email_txt.setObjectName(u"email_txt")
        self.email_txt.setGeometry(QRect(30, 140, 271, 41))
        self.email_txt.setStyleSheet(u"alternate-background-color: rgb(255, 255, 0);\n"
"border-bottom-color: rgb(255, 255, 255);")
        self.Email = QTextBrowser(self.frame)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(30, 110, 121, 21))
        self.Email.setStyleSheet(u"selection-background-color: rgb(255, 255, 255);")
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(80, 290, 191, 41))
        self.btn_login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"font: 600 9pt \"Segoe UI Variable Text Semibold\";")
        self.photo1 = QLabel(self.frame)
        self.photo1.setObjectName(u"photo1")
        self.photo1.setGeometry(QRect(100, 0, 181, 91))
        self.photo1.setPixmap(QPixmap(u"../../Downloads/user-2160923_1280.png"))
        self.photo1.setScaledContents(True)
        txtEmail.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(txtEmail)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        txtEmail.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(txtEmail)
        self.statusbar.setObjectName(u"statusbar")
        txtEmail.setStatusBar(self.statusbar)

        self.retranslateUi(txtEmail)

        QMetaObject.connectSlotsByName(txtEmail)
    # setupUi

    def retranslateUi(self, txtEmail):
        txtEmail.setWindowTitle(QCoreApplication.translate("txtEmail", u"MainWindow", None))
        self.password.setHtml(QCoreApplication.translate("txtEmail", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Password</span></p></body></html>", None))
        self.Email.setHtml(QCoreApplication.translate("txtEmail", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Email ID</span></p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("txtEmail", u"Login", None))
        self.photo1.setText("")
    # retranslateUi

