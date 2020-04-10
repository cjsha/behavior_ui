# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mouse\oldMouseConfirmUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OldMouseConfirm(object):
    def setupUi(self, OldMouseConfirm):
        OldMouseConfirm.setObjectName("OldMouseConfirm")
        OldMouseConfirm.setEnabled(True)
        OldMouseConfirm.resize(405, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OldMouseConfirm.sizePolicy().hasHeightForWidth())
        OldMouseConfirm.setSizePolicy(sizePolicy)
        OldMouseConfirm.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(OldMouseConfirm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.confirmation_label = QtWidgets.QLabel(OldMouseConfirm)
        self.confirmation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmation_label.setWordWrap(False)
        self.confirmation_label.setObjectName("confirmation_label")
        self.verticalLayout.addWidget(self.confirmation_label)
        self.which_mouse_label = QtWidgets.QLabel(OldMouseConfirm)
        self.which_mouse_label.setText("")
        self.which_mouse_label.setAlignment(QtCore.Qt.AlignCenter)
        self.which_mouse_label.setObjectName("which_mouse_label")
        self.verticalLayout.addWidget(self.which_mouse_label)
        self.confirmation_button_box = QtWidgets.QDialogButtonBox(OldMouseConfirm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmation_button_box.sizePolicy().hasHeightForWidth())
        self.confirmation_button_box.setSizePolicy(sizePolicy)
        self.confirmation_button_box.setOrientation(QtCore.Qt.Horizontal)
        self.confirmation_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.confirmation_button_box.setCenterButtons(True)
        self.confirmation_button_box.setObjectName("confirmation_button_box")
        self.verticalLayout.addWidget(self.confirmation_button_box)

        self.retranslateUi(OldMouseConfirm)
        QtCore.QMetaObject.connectSlotsByName(OldMouseConfirm)

    def retranslateUi(self, OldMouseConfirm):
        _translate = QtCore.QCoreApplication.translate
        OldMouseConfirm.setWindowTitle(_translate("OldMouseConfirm", "Confirmation"))
        self.confirmation_label.setText(_translate("OldMouseConfirm", "Is the following mouse out of comission?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OldMouseConfirm = QtWidgets.QDialog()
    ui = Ui_OldMouseConfirm()
    ui.setupUi(OldMouseConfirm)
    OldMouseConfirm.show()
    sys.exit(app.exec_())
