# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Mon May 30 16:08:07 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(942, 693)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/PyffLogoNeu.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.hboxlayout.addWidget(self.lineEdit)
        self.toolButton_clearFilter = QtGui.QToolButton(self.centralwidget)
        self.toolButton_clearFilter.setObjectName(_fromUtf8("toolButton_clearFilter"))
        self.hboxlayout.addWidget(self.toolButton_clearFilter)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.vboxlayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/saveas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon3)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionPlay = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon4)
        self.actionPlay.setObjectName(_fromUtf8("actionPlay"))
        self.actionPause = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon5)
        self.actionPause.setObjectName(_fromUtf8("actionPause"))
        self.actionGet = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/get.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGet.setIcon(icon6)
        self.actionGet.setObjectName(_fromUtf8("actionGet"))
        self.actionSendInit = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sendinit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSendInit.setIcon(icon7)
        self.actionSendInit.setObjectName(_fromUtf8("actionSendInit"))
        self.actionSendAll = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sendall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSendAll.setIcon(icon8)
        self.actionSendAll.setObjectName(_fromUtf8("actionSendAll"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon9)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionChangeFeedbackController = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangeFeedbackController.setIcon(icon10)
        self.actionChangeFeedbackController.setObjectName(_fromUtf8("actionChangeFeedbackController"))
        self.actionClearFilter = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearFilter.setIcon(icon11)
        self.actionClearFilter.setObjectName(_fromUtf8("actionClearFilter"))
        self.actionSendModified = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sendmodified.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSendModified.setIcon(icon12)
        self.actionSendModified.setObjectName(_fromUtf8("actionSendModified"))
        self.actionStop = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon13)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGet)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionChangeFeedbackController)
        self.toolBar.addAction(self.actionSendInit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pyff", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open an Existing File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGet.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGet.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh varialbes from Feedback", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSendInit.setText(QtGui.QApplication.translate("MainWindow", "SendInit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSendAll.setText(QtGui.QApplication.translate("MainWindow", "Send All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChangeFeedbackController.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearFilter.setText(QtGui.QApplication.translate("MainWindow", "clearFilter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSendModified.setText(QtGui.QApplication.translate("MainWindow", "Send Modified", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
