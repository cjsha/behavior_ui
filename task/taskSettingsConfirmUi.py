# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task\taskSettingsConfirmUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskSettingsConfirm(object):
    def setupUi(self, TaskSettingsConfirm):
        TaskSettingsConfirm.setObjectName("TaskSettingsConfirm")
        TaskSettingsConfirm.setEnabled(True)
        TaskSettingsConfirm.resize(405, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskSettingsConfirm.sizePolicy().hasHeightForWidth())
        TaskSettingsConfirm.setSizePolicy(sizePolicy)
        TaskSettingsConfirm.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(TaskSettingsConfirm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.confirmation_label = QtWidgets.QLabel(TaskSettingsConfirm)
        self.confirmation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmation_label.setWordWrap(False)
        self.confirmation_label.setObjectName("confirmation_label")
        self.verticalLayout.addWidget(self.confirmation_label)
        self.com_port_label = QtWidgets.QLabel(TaskSettingsConfirm)
        self.com_port_label.setText("")
        self.com_port_label.setAlignment(QtCore.Qt.AlignCenter)
        self.com_port_label.setObjectName("com_port_label")
        self.verticalLayout.addWidget(self.com_port_label)
        self.parameters_label = QtWidgets.QLabel(TaskSettingsConfirm)
        self.parameters_label.setText("")
        self.parameters_label.setAlignment(QtCore.Qt.AlignCenter)
        self.parameters_label.setObjectName("parameters_label")
        self.verticalLayout.addWidget(self.parameters_label)
        self.mouse_label = QtWidgets.QLabel(TaskSettingsConfirm)
        self.mouse_label.setText("")
        self.mouse_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mouse_label.setObjectName("mouse_label")
        self.verticalLayout.addWidget(self.mouse_label)
        self.mass_label = QtWidgets.QLabel(TaskSettingsConfirm)
        self.mass_label.setText("")
        self.mass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mass_label.setObjectName("mass_label")
        self.verticalLayout.addWidget(self.mass_label)
        self.confirmation_button_box = QtWidgets.QDialogButtonBox(TaskSettingsConfirm)
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

        self.retranslateUi(TaskSettingsConfirm)
        QtCore.QMetaObject.connectSlotsByName(TaskSettingsConfirm)

    def retranslateUi(self, TaskSettingsConfirm):
        _translate = QtCore.QCoreApplication.translate
        TaskSettingsConfirm.setWindowTitle(_translate("TaskSettingsConfirm", "Confirmation"))
        self.confirmation_label.setText(_translate("TaskSettingsConfirm", "The Mouse Behavior Task will start using the following parameters:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskSettingsConfirm = QtWidgets.QDialog()
    ui = Ui_TaskSettingsConfirm()
    ui.setupUi(TaskSettingsConfirm)
    TaskSettingsConfirm.show()
    sys.exit(app.exec_())
