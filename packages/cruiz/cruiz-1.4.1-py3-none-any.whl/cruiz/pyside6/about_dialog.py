# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLayout, QSizePolicy, QWidget)

class Ui_AboutCruiz(object):
    def setupUi(self, AboutCruiz):
        if not AboutCruiz.objectName():
            AboutCruiz.setObjectName(u"AboutCruiz")
        AboutCruiz.resize(246, 160)
        AboutCruiz.setModal(True)
        self.gridLayout = QGridLayout(AboutCruiz)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.label_4 = QLabel(AboutCruiz)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_2 = QLabel(AboutCruiz)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.python = QLabel(AboutCruiz)
        self.python.setObjectName(u"python")

        self.gridLayout.addWidget(self.python, 3, 1, 1, 1)

        self.version = QLabel(AboutCruiz)
        self.version.setObjectName(u"version")

        self.gridLayout.addWidget(self.version, 1, 1, 1, 1)

        self.python_version = QLabel(AboutCruiz)
        self.python_version.setObjectName(u"python_version")

        self.gridLayout.addWidget(self.python_version, 4, 1, 1, 1)

        self.pyside_version = QLabel(AboutCruiz)
        self.pyside_version.setObjectName(u"pyside_version")

        self.gridLayout.addWidget(self.pyside_version, 5, 1, 1, 1)

        self.cruiz = QLabel(AboutCruiz)
        self.cruiz.setObjectName(u"cruiz")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.cruiz.sizePolicy().hasHeightForWidth())
        self.cruiz.setSizePolicy(sizePolicy)
        self.cruiz.setMaximumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.cruiz, 0, 0, 6, 1)


        self.retranslateUi(AboutCruiz)

        QMetaObject.connectSlotsByName(AboutCruiz)
    # setupUi

    def retranslateUi(self, AboutCruiz):
        AboutCruiz.setWindowTitle(QCoreApplication.translate("AboutCruiz", u"About cruiz", None))
        self.label_4.setText(QCoreApplication.translate("AboutCruiz", u"Author: Mark Final (c) 2020-2024", None))
        self.label_2.setText(QCoreApplication.translate("AboutCruiz", u"cruiz: Conan recipe user interface", None))
        self.python.setText(QCoreApplication.translate("AboutCruiz", u"Python executable: unknown", None))
        self.version.setText(QCoreApplication.translate("AboutCruiz", u"Version: unknown", None))
        self.python_version.setText(QCoreApplication.translate("AboutCruiz", u"Python version: unknown", None))
        self.pyside_version.setText(QCoreApplication.translate("AboutCruiz", u"PySide version: unknown", None))
    # retranslateUi

