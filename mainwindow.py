# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Oct 14 15:56:16 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1110, 545)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 681, 441))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 439))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.match_table = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.match_table.setGeometry(QtCore.QRect(0, 0, 671, 431))
        self.match_table.setLineWidth(1)
        self.match_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.match_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.match_table.setAlternatingRowColors(False)
        self.match_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.match_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.match_table.setShowGrid(True)
        self.match_table.setRowCount(10)
        self.match_table.setColumnCount(2)
        self.match_table.setObjectName(_fromUtf8("match_table"))
        item = QtGui.QTableWidgetItem()
        self.match_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.match_table.setHorizontalHeaderItem(1, item)
        self.match_table.horizontalHeader().setVisible(True)
        self.match_table.horizontalHeader().setDefaultSectionSize(309)
        self.match_table.verticalHeader().setDefaultSectionSize(30)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(750, 40, 341, 426))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tophit_list = QtGui.QListWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tophit_list.setFont(font)
        self.tophit_list.setObjectName(_fromUtf8("tophit_list"))
        self.verticalLayout.addWidget(self.tophit_list)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.new_authority = QtGui.QLineEdit(self.layoutWidget)
        self.new_authority.setEnabled(True)
        self.new_authority.setObjectName(_fromUtf8("new_authority"))
        self.horizontalLayout.addWidget(self.new_authority)
        self.createAuthority_button = QtGui.QPushButton(self.layoutWidget)
        self.createAuthority_button.setObjectName(_fromUtf8("createAuthority_button"))
        self.horizontalLayout.addWidget(self.createAuthority_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.deleteAuthority_button = QtGui.QPushButton(self.layoutWidget)
        self.deleteAuthority_button.setObjectName(_fromUtf8("deleteAuthority_button"))
        self.verticalLayout.addWidget(self.deleteAuthority_button)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1110, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuRun = QtGui.QMenu(self.menuBar)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionImport_auth = QtGui.QAction(MainWindow)
        self.actionImport_auth.setObjectName(_fromUtf8("actionImport_auth"))
        self.actionExport_CSV = QtGui.QAction(MainWindow)
        self.actionExport_CSV.setEnabled(False)
        self.actionExport_CSV.setObjectName(_fromUtf8("actionExport_CSV"))
        self.actionSave_Project = QtGui.QAction(MainWindow)
        self.actionSave_Project.setEnabled(False)
        self.actionSave_Project.setObjectName(_fromUtf8("actionSave_Project"))
        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setEnabled(False)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.actionClose_Project = QtGui.QAction(MainWindow)
        self.actionClose_Project.setEnabled(False)
        self.actionClose_Project.setObjectName(_fromUtf8("actionClose_Project"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setEnabled(True)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionImport_messy = QtGui.QAction(MainWindow)
        self.actionImport_messy.setObjectName(_fromUtf8("actionImport_messy"))
        self.actionRun_matching = QtGui.QAction(MainWindow)
        self.actionRun_matching.setEnabled(False)
        self.actionRun_matching.setObjectName(_fromUtf8("actionRun_matching"))
        self.menuFile.addAction(self.actionImport_auth)
        self.menuFile.addAction(self.actionImport_messy)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionClose_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRun.addAction(self.actionRun_matching)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuRun.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.new_authority, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.createAuthority_button.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Authoritizer", None))
        item = self.match_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nonstandard term", None))
        item = self.match_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Authority term", None))
        self.label.setText(_translate("MainWindow", "Matched authorities (double-click to assign):", None))
        self.label_2.setText(_translate("MainWindow", "Create new authority:", None))
        self.createAuthority_button.setText(_translate("MainWindow", "Create", None))
        self.deleteAuthority_button.setText(_translate("MainWindow", "Delete authority assignment", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuRun.setTitle(_translate("MainWindow", "Run", None))
        self.actionImport_auth.setText(_translate("MainWindow", "Import Authorities...", None))
        self.actionExport_CSV.setText(_translate("MainWindow", "Export CSV...", None))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project...", None))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project...", None))
        self.actionClose_Project.setText(_translate("MainWindow", "Close Project", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences...", None))
        self.actionImport_messy.setText(_translate("MainWindow", "Import Nonstandard Terms...", None))
        self.actionRun_matching.setText(_translate("MainWindow", "Match...", None))

