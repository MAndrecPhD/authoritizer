# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importauthority.ui'
#
# Created: Tue Oct  6 13:21:25 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImportAuthDialog(object):
    def setupUi(self, ImportAuthDialog):
        ImportAuthDialog.setObjectName(_fromUtf8("ImportAuthDialog"))
        ImportAuthDialog.resize(390, 274)
        self.buttonBox = QtGui.QDialogButtonBox(ImportAuthDialog)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setGeometry(QtCore.QRect(10, 230, 361, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(ImportAuthDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 358, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.column_list = QtGui.QListWidget(self.layoutWidget)
        self.column_list.setEnabled(False)
        self.column_list.setObjectName(_fromUtf8("column_list"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.column_list)
        self.layoutWidget1 = QtGui.QWidget(ImportAuthDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 332, 32))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.selectfile_button = QtGui.QPushButton(self.layoutWidget1)
        self.selectfile_button.setObjectName(_fromUtf8("selectfile_button"))
        self.horizontalLayout_2.addWidget(self.selectfile_button)
        self.filename_label = QtGui.QLabel(self.layoutWidget1)
        self.filename_label.setObjectName(_fromUtf8("filename_label"))
        self.horizontalLayout_2.addWidget(self.filename_label)

        self.retranslateUi(ImportAuthDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportAuthDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportAuthDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportAuthDialog)

    def retranslateUi(self, ImportAuthDialog):
        ImportAuthDialog.setWindowTitle(_translate("ImportAuthDialog", "Import Authorities", None))
        self.label_4.setText(_translate("ImportAuthDialog", "Select column:", None))
        self.selectfile_button.setText(_translate("ImportAuthDialog", "Select authority file...", None))
        self.filename_label.setText(_translate("ImportAuthDialog", "(No file selected)", None))

