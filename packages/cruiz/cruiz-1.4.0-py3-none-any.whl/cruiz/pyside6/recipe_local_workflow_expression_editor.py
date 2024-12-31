# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_local_workflow_expression_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ExpressionEditor(object):
    def setupUi(self, ExpressionEditor):
        if not ExpressionEditor.objectName():
            ExpressionEditor.setObjectName(u"ExpressionEditor")
        ExpressionEditor.resize(268, 263)
        self.verticalLayout = QVBoxLayout(ExpressionEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.expression = QLineEdit(ExpressionEditor)
        self.expression.setObjectName(u"expression")
        self.expression.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.expression)

        self.evaluatedExpression = QLabel(ExpressionEditor)
        self.evaluatedExpression.setObjectName(u"evaluatedExpression")
        self.evaluatedExpression.setFrameShape(QFrame.Panel)
        self.evaluatedExpression.setFrameShadow(QFrame.Sunken)
        self.evaluatedExpression.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.evaluatedExpression)

        self.line = QFrame(ExpressionEditor)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.groupBox = QGroupBox(ExpressionEditor)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.profileMacro = QLabel(self.groupBox)
        self.profileMacro.setObjectName(u"profileMacro")

        self.gridLayout.addWidget(self.profileMacro, 3, 1, 1, 1)

        self.buildtypelcMacro = QLabel(self.groupBox)
        self.buildtypelcMacro.setObjectName(u"buildtypelcMacro")

        self.gridLayout.addWidget(self.buildtypelcMacro, 6, 1, 1, 1)

        self.nameMacro = QLabel(self.groupBox)
        self.nameMacro.setObjectName(u"nameMacro")

        self.gridLayout.addWidget(self.nameMacro, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.buildtypeMacro = QLabel(self.groupBox)
        self.buildtypeMacro.setObjectName(u"buildtypeMacro")

        self.gridLayout.addWidget(self.buildtypeMacro, 5, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.versionMacro = QLabel(self.groupBox)
        self.versionMacro.setObjectName(u"versionMacro")

        self.gridLayout.addWidget(self.versionMacro, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ExpressionEditor)

        QMetaObject.connectSlotsByName(ExpressionEditor)
    # setupUi

    def retranslateUi(self, ExpressionEditor):
        ExpressionEditor.setWindowTitle(QCoreApplication.translate("ExpressionEditor", u"Expression Editor", None))
        self.evaluatedExpression.setText(QCoreApplication.translate("ExpressionEditor", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("ExpressionEditor", u"Available macros", None))
        self.profileMacro.setText(QCoreApplication.translate("ExpressionEditor", u"TextLabel", None))
        self.buildtypelcMacro.setText(QCoreApplication.translate("ExpressionEditor", u"TextLabel", None))
        self.nameMacro.setText(QCoreApplication.translate("ExpressionEditor", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("ExpressionEditor", u"${build_type_lc}", None))
        self.label_3.setText(QCoreApplication.translate("ExpressionEditor", u"${build_type}", None))
        self.buildtypeMacro.setText(QCoreApplication.translate("ExpressionEditor", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("ExpressionEditor", u"${name}", None))
        self.label.setText(QCoreApplication.translate("ExpressionEditor", u"${profile}", None))
        self.label_2.setText(QCoreApplication.translate("ExpressionEditor", u"${version}", None))
        self.versionMacro.setText(QCoreApplication.translate("ExpressionEditor", u"TextLabel", None))
    # retranslateUi

