from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mysql.connector
import json
import pathlib
from .sqlUi import Ui_sql


class Sql(Ui_sql, QtWidgets.QWidget):
    mouse_toggled = QtCore.pyqtSignal(object)
    parameters_toggled = QtCore.pyqtSignal(object)
    task_toggled = QtCore.pyqtSignal(object)

    def __init__(self, widget):

        # call init function from QWidget
        super().__init__()
        # set up objects to be used later
        self.sqlConnected = False
        # call UiMainWindow's setupUi function
        self.setupUi(widget)
        # check if settings.json exists
        settingsFile = pathlib.Path("./sql/settings.json")
        settingsFileExist = settingsFile.is_file()
        # if settings.json exists, populate database fields with information from that file
        if settingsFileExist:
            with open("sql/settings.json") as settingsFile:
                settingsJson = json.loads(settingsFile.read())
                self.serverAddressLineEdit.setText(settingsJson["serverAddress"])
                self.usernameLineEdit.setText(settingsJson["username"])
                self.passwordLineEdit.setText(settingsJson["password"])
        # connect slots to signals, i.e. when pushbutton is clicked (signal), call a method in response (slot)
        self.sqlPushButton.clicked.connect(self.sqlClicked)
        self.goPushButton.clicked.connect(self.goClicked)

    def sqlClicked(self):

        # if we're not connected to database, try to connect
        if not self.sqlConnected:
            # if user's input is such we're not able to connect to our sql db,
            # an error will occur. for that reason, we put this code in a try-catch block
            try:
                ## connect to database
                self.sqlConnection = mysql.connector.connect(user=self.usernameLineEdit.text(),
                                                             password=self.passwordLineEdit.text(),
                                                             host=self.serverAddressLineEdit.text(),
                                                             database="salk")
                # if connection is successful, this code will execute
                # otherwise, code goes to the except block
                self.sqlConnected = True
                self.sqlPushButton.setText("Disconnect")
                self.goWidget.setEnabled(True)
                self.serverAddressLineEdit.setEnabled(False)
                self.usernameLineEdit.setEnabled(False)
                self.passwordLineEdit.setEnabled(False)
                self.messageTextBrowser.append("Connection Successful\n")
                # if connection is successful, user's input is saved to settings.json
                # so that the GUI can automatically load that information for next time
                with open("sql/settings.json", "w+") as settingsFile:
                    settingsDict = {"username": self.usernameLineEdit.text(),
                                    "password": self.passwordLineEdit.text(),
                                    "serverAddress": self.serverAddressLineEdit.text()}
                    json.dump(settingsDict, settingsFile)
            # this is what happens if connection to database is unsuccessful
            except Exception as error:
                self.messageTextBrowser.append("Connection Unsuccessful\n")
                print(str(error))
        # if we're connected to database, try to disconnect

        elif self.sqlConnected:

            # if we're not, for some reason, able to disconenct from db,
            # an error will occur. hence, we put this code in a try-catch block
            try:

                # if disconnection is successful, this code will execute
                # otherwise, connection goes to the except block
                self.sqlConnection.close()
                self.sqlConnected = False
                self.goWidget.setEnabled(False)
                self.serverAddressLineEdit.setEnabled(True)
                self.usernameLineEdit.setEnabled(True)
                self.passwordLineEdit.setEnabled(True)
                self.sqlPushButton.setText("Connect")
                self.messageTextBrowser.append("Disconnection Successful\n")

            # this is what happens if disconnection to database is unsuccessful
            except Exception as error:
                self.messageTextBrowser.append("Disconnection Unsuccessful\n")
                print(str(error))

    def goClicked(self):
        if self.mouseInfoRadioButton.isChecked():
            self.mouse_toggled.emit(self.sqlConnection)
        elif self.trialParametersRadioButton.isChecked():
            self.parameters_toggled.emit(self.sqlConnection)
        elif self.behaviorTaskRadioButton.isChecked():
            self.task_toggled.emit(self.sqlConnection)
        else:
            widget.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = sql(widget)
    widget.show()
    sys.exit(app.exec_())
