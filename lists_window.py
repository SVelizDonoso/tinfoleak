# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lists_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1053, 676)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tbl_header = QtGui.QTableWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_header.sizePolicy().hasHeightForWidth())
        self.tbl_header.setSizePolicy(sizePolicy)
        self.tbl_header.setLineWidth(1)
        self.tbl_header.setShowGrid(False)
        self.tbl_header.setObjectName(_fromUtf8("tbl_header"))
        self.tbl_header.setColumnCount(3)
        self.tbl_header.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_header.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_header.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_header.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tbl_header, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tbl_subscribed = QtGui.QTableWidget(self.tab)
        self.tbl_subscribed.setObjectName(_fromUtf8("tbl_subscribed"))
        self.tbl_subscribed.setColumnCount(17)
        self.tbl_subscribed.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_subscribed.setHorizontalHeaderItem(16, item)
        self.gridLayout_2.addWidget(self.tbl_subscribed, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tbl_ownership = QtGui.QTableWidget(self.tab_2)
        self.tbl_ownership.setObjectName(_fromUtf8("tbl_ownership"))
        self.tbl_ownership.setColumnCount(12)
        self.tbl_ownership.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_ownership.setHorizontalHeaderItem(11, item)
        self.gridLayout_5.addWidget(self.tbl_ownership, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tbl_membership = QtGui.QTableWidget(self.tab_3)
        self.tbl_membership.setObjectName(_fromUtf8("tbl_membership"))
        self.tbl_membership.setColumnCount(12)
        self.tbl_membership.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_membership.setHorizontalHeaderItem(11, item)
        self.gridLayout_6.addWidget(self.tbl_membership, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "User", None))
        item = self.tbl_header.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Image profile", None))
        item = self.tbl_header.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Screen name", None))
        item = self.tbl_header.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Description", None))
        self.label_2.setText(_translate("Dialog", "Lists", None))
        item = self.tbl_subscribed.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID", None))
        item = self.tbl_subscribed.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name", None))
        item = self.tbl_subscribed.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Screen name", None))
        item = self.tbl_subscribed.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Description", None))
        item = self.tbl_subscribed.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Profile image URL", None))
        item = self.tbl_subscribed.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Profile banner URL", None))
        item = self.tbl_subscribed.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Created at", None))
        item = self.tbl_subscribed.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Location", None))
        item = self.tbl_subscribed.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Time zone", None))
        item = self.tbl_subscribed.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Geo enabled", None))
        item = self.tbl_subscribed.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "Followers count", None))
        item = self.tbl_subscribed.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "Friends count", None))
        item = self.tbl_subscribed.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "Statuses count", None))
        item = self.tbl_subscribed.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "Listed count", None))
        item = self.tbl_subscribed.horizontalHeaderItem(14)
        item.setText(_translate("Dialog", "Favourites count", None))
        item = self.tbl_subscribed.horizontalHeaderItem(15)
        item.setText(_translate("Dialog", "User verified", None))
        item = self.tbl_subscribed.horizontalHeaderItem(16)
        item.setText(_translate("Dialog", "User lang", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Subscribed to lists", None))
        item = self.tbl_ownership.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "List ID", None))
        item = self.tbl_ownership.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "List Name", None))
        item = self.tbl_ownership.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "List Description", None))
        item = self.tbl_ownership.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Member count", None))
        item = self.tbl_ownership.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Subscriber count", None))
        item = self.tbl_ownership.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "URI", None))
        item = self.tbl_ownership.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Screen name", None))
        item = self.tbl_ownership.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "User created at", None))
        item = self.tbl_ownership.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "User name", None))
        item = self.tbl_ownership.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "User description", None))
        item = self.tbl_ownership.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "User followers", None))
        item = self.tbl_ownership.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "User friends", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Ownership lists", None))
        item = self.tbl_membership.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "List ID", None))
        item = self.tbl_membership.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "List Name", None))
        item = self.tbl_membership.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "List Description", None))
        item = self.tbl_membership.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Member count", None))
        item = self.tbl_membership.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Subscriber count", None))
        item = self.tbl_membership.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "URI", None))
        item = self.tbl_membership.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Screen name", None))
        item = self.tbl_membership.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "User created at", None))
        item = self.tbl_membership.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "User name", None))
        item = self.tbl_membership.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "User description", None))
        item = self.tbl_membership.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "User followers", None))
        item = self.tbl_membership.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "User friends", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Membership lists", None))

