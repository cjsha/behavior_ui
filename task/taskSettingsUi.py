# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task\taskSettingsUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_taskSettings(object):
    def setupUi(self, taskSettings):
        taskSettings.setObjectName("taskSettings")
        taskSettings.resize(267, 429)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(taskSettings.sizePolicy().hasHeightForWidth())
        taskSettings.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(taskSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.go_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_push_button.setEnabled(False)
        self.go_push_button.setObjectName("go_push_button")
        self.gridLayout_4.addWidget(self.go_push_button, 6, 0, 1, 1)
        self.mouse_widget = QtWidgets.QWidget(self.centralwidget)
        self.mouse_widget.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouse_widget.sizePolicy().hasHeightForWidth())
        self.mouse_widget.setSizePolicy(sizePolicy)
        self.mouse_widget.setObjectName("mouse_widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.mouse_widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.massLineEdit = QtWidgets.QLineEdit(self.mouse_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.massLineEdit.sizePolicy().hasHeightForWidth())
        self.massLineEdit.setSizePolicy(sizePolicy)
        self.massLineEdit.setObjectName("massLineEdit")
        self.gridLayout_5.addWidget(self.massLineEdit, 2, 1, 1, 1)
        self.massLabel = QtWidgets.QLabel(self.mouse_widget)
        self.massLabel.setObjectName("massLabel")
        self.gridLayout_5.addWidget(self.massLabel, 2, 0, 1, 1)
        self.mouseInfoLabel = QtWidgets.QLabel(self.mouse_widget)
        self.mouseInfoLabel.setObjectName("mouseInfoLabel")
        self.gridLayout_5.addWidget(self.mouseInfoLabel, 0, 0, 1, 2)
        self.mouseLabel = QtWidgets.QLabel(self.mouse_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouseLabel.sizePolicy().hasHeightForWidth())
        self.mouseLabel.setSizePolicy(sizePolicy)
        self.mouseLabel.setObjectName("mouseLabel")
        self.gridLayout_5.addWidget(self.mouseLabel, 1, 0, 1, 1)
        self.gramsLabel = QtWidgets.QLabel(self.mouse_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gramsLabel.sizePolicy().hasHeightForWidth())
        self.gramsLabel.setSizePolicy(sizePolicy)
        self.gramsLabel.setObjectName("gramsLabel")
        self.gridLayout_5.addWidget(self.gramsLabel, 2, 2, 1, 1)
        self.mouse_combo_box = QtWidgets.QComboBox(self.mouse_widget)
        self.mouse_combo_box.setObjectName("mouse_combo_box")
        self.gridLayout_5.addWidget(self.mouse_combo_box, 1, 1, 1, 2)
        self.gridLayout_4.addWidget(self.mouse_widget, 3, 0, 1, 1)
        self.serialWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialWidget.sizePolicy().hasHeightForWidth())
        self.serialWidget.setSizePolicy(sizePolicy)
        self.serialWidget.setObjectName("serialWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.serialWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.refresh_push_button = QtWidgets.QPushButton(self.serialWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_push_button.sizePolicy().hasHeightForWidth())
        self.refresh_push_button.setSizePolicy(sizePolicy)
        self.refresh_push_button.setObjectName("refresh_push_button")
        self.gridLayout_2.addWidget(self.refresh_push_button, 1, 0, 1, 1)
        self.com_combo_box = QtWidgets.QComboBox(self.serialWidget)
        self.com_combo_box.setObjectName("com_combo_box")
        self.gridLayout_2.addWidget(self.com_combo_box, 1, 1, 1, 1)
        self.serial_push_button = QtWidgets.QPushButton(self.serialWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serial_push_button.sizePolicy().hasHeightForWidth())
        self.serial_push_button.setSizePolicy(sizePolicy)
        self.serial_push_button.setObjectName("serial_push_button")
        self.gridLayout_2.addWidget(self.serial_push_button, 1, 2, 1, 1)
        self.serialLabel = QtWidgets.QLabel(self.serialWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialLabel.sizePolicy().hasHeightForWidth())
        self.serialLabel.setSizePolicy(sizePolicy)
        self.serialLabel.setObjectName("serialLabel")
        self.gridLayout_2.addWidget(self.serialLabel, 0, 0, 1, 3)
        self.gridLayout_4.addWidget(self.serialWidget, 0, 0, 1, 1)
        self.message_text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_text_browser.setObjectName("message_text_browser")
        self.gridLayout_4.addWidget(self.message_text_browser, 5, 0, 1, 1)
        self.backPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPushButton.setObjectName("backPushButton")
        self.gridLayout_4.addWidget(self.backPushButton, 7, 0, 1, 1)
        self.save_data_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.save_data_check_box.setEnabled(False)
        self.save_data_check_box.setChecked(False)
        self.save_data_check_box.setObjectName("save_data_check_box")
        self.gridLayout_4.addWidget(self.save_data_check_box, 2, 0, 1, 1)
        self.parameters_widget = QtWidgets.QWidget(self.centralwidget)
        self.parameters_widget.setEnabled(False)
        self.parameters_widget.setObjectName("parameters_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.parameters_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.parameters_widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.parameters_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.parameters_combo_box = QtWidgets.QComboBox(self.parameters_widget)
        self.parameters_combo_box.setObjectName("parameters_combo_box")
        self.gridLayout.addWidget(self.parameters_combo_box, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.parameters_widget, 1, 0, 1, 1)
        taskSettings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(taskSettings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 267, 21))
        self.menubar.setObjectName("menubar")
        taskSettings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(taskSettings)
        self.statusbar.setObjectName("statusbar")
        taskSettings.setStatusBar(self.statusbar)

        self.retranslateUi(taskSettings)
        QtCore.QMetaObject.connectSlotsByName(taskSettings)

    def retranslateUi(self, taskSettings):
        _translate = QtCore.QCoreApplication.translate
        taskSettings.setWindowTitle(_translate("taskSettings", "MainWindow"))
        self.go_push_button.setText(_translate("taskSettings", "Go"))
        self.massLabel.setText(_translate("taskSettings", "Mass:"))
        self.mouseInfoLabel.setText(_translate("taskSettings", "Enter Mouse Information:"))
        self.mouseLabel.setText(_translate("taskSettings", "Mouse:"))
        self.gramsLabel.setText(_translate("taskSettings", "grams"))
        self.refresh_push_button.setText(_translate("taskSettings", "Refresh"))
        self.serial_push_button.setText(_translate("taskSettings", "Connect"))
        self.serialLabel.setText(_translate("taskSettings", "Establish Serial Connection:"))
        self.backPushButton.setText(_translate("taskSettings", "Back"))
        self.save_data_check_box.setText(_translate("taskSettings", "Save Behavior Task Data"))
        self.label.setText(_translate("taskSettings", "Select Behavior Task Parameters:"))
        self.label_2.setText(_translate("taskSettings", "Parameters:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    taskSettings = QtWidgets.QMainWindow()
    ui = Ui_taskSettings()
    ui.setupUi(taskSettings)
    taskSettings.show()
    sys.exit(app.exec_())
