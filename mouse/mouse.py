from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import json
import pathlib
import datetime
import csv
from .mouseUi import Ui_mouse as mouseUi
from .newMouseConfirm import NewMouseConfirm
from .oldMouseConfirm import OldMouseConfirm


class Mouse(mouseUi, QtWidgets.QWidget):
    back_pressed = QtCore.pyqtSignal()

    def __init__(self, widget, sql_connection):

# call init function from QWidget
        super().__init__()
        self.sql_connection = sql_connection
# set up the ui, starting with code inherited from mouseUi.py
# mouseUi.ui is to be converted to mouseUi.py using pyuic5 command
        super().setupUi(widget)

# connect slots to signals, i.e. when pushbutton is clicked (signal), call a method in response (slot)
        self.submitPushButton.clicked.connect(self.submit_clicked)
        self.list_mice_push_button.clicked.connect(self.list_mice)
        self.backPushButton.clicked.connect(self.back_pressed.emit)
        self.newMouseRadioButton.clicked.connect(self.new_mice_clicked)
        self.oldMouseRadioButton.clicked.connect(self.old_mice_clicked)
        self.refresh_mouse_options()

    def submit_clicked(self):

        submit = True
        input_error = ""

        try:

            if self.newMouseRadioButton.isChecked():

                submit, input_error = self.check_cage_input(submit, input_error)
                submit, input_error = self.check_mouse_id_input(submit, input_error)
                if submit:
                    submit, input_error = self.check_duplicate_mouse(submit, input_error)
                submit, input_error = self.check_mass(submit, input_error)
                submit, input_error = self.check_birthday(submit, input_error)
                submit, input_error = self.check_breed(submit, input_error)
                submit, input_error = self.check_sex(submit, input_error)
                submit, input_error = self.check_misc(submit, input_error)
                if submit:
                    ## set up the dialog ui
                    new_mouse_dialog = QtWidgets.QDialog()
                    new_mouse = NewMouseConfirm(new_mouse_dialog)
                    new_mouse.pass_objects(self.cageLineEdit.text(),
                                           self.mouseIdLineEdit.text(),
                                           self.massLineEdit.text(),
                                           self.birthdayLineEdit.text(),
                                           self.breedLineEdit.text(),
                                           self.sexLineEdit.text(),
                                           self.miscTextEdit.toPlainText())
                    if new_mouse_dialog.exec_():
                        sql_cursor = self.sql_connection.cursor()
                        sql_cursor.execute("""INSERT INTO mouseInfo (
                                                cageNumber,
                                                mouseNumber,
                                                baselineMass,
                                                birthday,
                                                breed,
                                                sex,
                                                miscellaneous,
                                                retired)
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, FALSE)""",
                                           (int(self.cageLineEdit.text()),
                                            int(self.mouseIdLineEdit.text()),
                                            float(self.massLineEdit.text()),
                                            str(self.birthdayLineEdit.text()),
                                            str(self.breedLineEdit.text()).lower(),
                                            str(self.sexLineEdit.text()).lower(),
                                            str(self.miscTextEdit.toPlainText())))
                        self.sql_connection.commit()
                        sql_cursor.close()
                        self.messageTextBrowser.append("Submission Successful\n")
                    else:
                        self.messageTextBrowser.append("Submission Cancelled\n")
                else:
                    self.messageTextBrowser.append("Submission Unsuccessful\n" + input_error)

            elif self.oldMouseRadioButton.isChecked():
                if str(self.mouse_combo_box.currentText()) != "Select mouse...":
                    try:
                        old_mouse_dialog = QtWidgets.QDialog()
                        old_mouse = OldMouseConfirm(old_mouse_dialog)
                        old_mouse.pass_objects(str(self.mouse_combo_box.currentText()))
                        if old_mouse_dialog.exec_():
                            sql_cursor = self.sql_connection.cursor()
                            mouse = str(self.mouse_combo_box.currentText()).split(" ")
                            sql_cursor.execute("""UPDATE mouseInfo SET retired = TRUE
                                                    WHERE cageNumber = %s AND mouseNumber = %s""",
                                               (int(mouse[1]),
                                                int(mouse[4])))
                            self.sql_connection.commit()
                            self.refresh_mouse_options()
                            sql_cursor.close()
                            self.messageTextBrowser.append("Submission Successful\n")
                        else:
                            self.messageTextBrowser.append("Submission Cancelled\n")
                    except Exception as error:
                        self.messageTextBrowser.append("Submission Unsuccessful\n" + str(error))
                else:
                    self.messageTextBrowser.append("Submission Unsuccessful\nYou must choose a valid mouse\n")
        except Exception as error:

            self.messageTextBrowser.append("Submission Unsuccessful\n" + str(error))

# if mouse information input is determined valid by our checks yet still raises an exception,
# log mouse information input so that we can fix that later
            if submit:
                self.write_error_log(error)

    def list_mice(self):

        try:
            sql_cursor = self.sql_connection.cursor()
            sql_cursor.execute("SELECT * FROM mouseInfo;")
            with open("./mouse/behaviorMice.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in sql_cursor.description])  # write headers
                csv_writer.writerows(sql_cursor)
            sql_cursor.close()
            self.messageTextBrowser.append("File (behaviorMice.csv) saved successfully to the following directory:\n" +
                                           os.getcwd() + "\mouse\n")
        except Exception as error:
            print(error)
            self.messageTextBrowser.append("File saved unsuccessfully\n" + str(error))

    def old_mice_clicked(self):
        self.cageLineEdit.setEnabled(False)
        self.mouseIdLineEdit.setEnabled(False)
        self.massLineEdit.setEnabled(False)
        self.birthdayLineEdit.setEnabled(False)
        self.breedLineEdit.setEnabled(False)
        self.sexLineEdit.setEnabled(False)
        self.miscTextEdit.setEnabled(False)
        self.refresh_mouse_options()
        self.mouse_combo_box.setEnabled(True)

    def new_mice_clicked(self):
        self.cageLineEdit.setEnabled(True)
        self.mouseIdLineEdit.setEnabled(True)
        self.massLineEdit.setEnabled(True)
        self.birthdayLineEdit.setEnabled(True)
        self.breedLineEdit.setEnabled(True)
        self.sexLineEdit.setEnabled(True)
        self.miscTextEdit.setEnabled(True)
        self.mouse_combo_box.setEnabled(False)

    def check_cage_input(self, submit, input_error):
        if not str(self.cageLineEdit.text()):
            input_error = input_error + "Cage input cannot be empty\n"
            submit = False
        elif not str(self.cageLineEdit.text()).isdigit():
            input_error = input_error + "Cage input must contain only digits\n"
            submit = False
        elif int(self.cageLineEdit.text()) > 2147483647:
            input_error = input_error + "Cage input must be less than 2147483647\n"
            submit = False
        return submit, input_error

    def check_mouse_id_input(self, submit, input_error):
        if not str(self.mouseIdLineEdit.text()):
            input_error = input_error + "Mouse ID input cannot be empty\n"
            submit = False
        elif not str(self.mouseIdLineEdit.text()).isdigit():
            input_error = input_error + "Mouse ID input must contain only digits\n"
            submit = False
        elif int(self.mouseIdLineEdit.text()) > 127:
            input_error = input_error + "mouse ID input must be between 0 and 127\n"
            submit = False
        return submit, input_error

    def check_duplicate_mouse(self, submit, input_error):
        try:
            sql_cursor = self.sql_connection.cursor()
            sql_cursor.execute("SELECT cageNumber, mouseNumber FROM mouseInfo;")
            for (cageNumber, mouseNumber) in sql_cursor:
                if str(cageNumber) == str(self.cageLineEdit.text()) and str(mouseNumber) == str(
                        self.mouseIdLineEdit.text()):
                    submit = False
                    input_error = input_error + "Mouse already exists in database\n"
            sql_cursor.close()

        except Exception as error:
            print(error)

        return submit, input_error

    def check_mass(self, submit, input_error):
        if not str(self.massLineEdit.text()):
            input_error = input_error + "Baseline Mass input cannot be empty\n"
            submit = False
        elif not str(self.massLineEdit.text()).replace(".", "1", 1).isdigit():
            input_error = input_error + "Baseline Mass input must contain only digits and optionally one period\n"
            submit = False
        elif len(str(self.massLineEdit.text()).split(".")) > 1:
            if len(str(self.massLineEdit.text()).split(".")[0]) > 6 or len(
                    str(self.massLineEdit.text()).split(".")[1]) > 4:
                input_error = input_error + \
                              "Baseline Mass input contains too many digits before or after the decimal point\n"
                submit = False
        elif len(str(self.massLineEdit.text()).split(".")) > 6:
            input_error = input_error + "Baseline Mass input contains too many digits after the decimal point\n"
            submit = False

        return submit, input_error

    def check_birthday(self, submit, input_error):
        birthday_string_split = str(self.birthdayLineEdit.text()).split("-")
        now = datetime.datetime.now()
        if not str(self.birthdayLineEdit.text()):
            input_error = input_error + "Birthday input cannot be empty\n"
            submit = False
        elif len(birthday_string_split) != 3:
            input_error = input_error + "Birthday input must have format YYYY-MM-DD\n"
            submit = False
        elif len(birthday_string_split[0]) != 4 or len(birthday_string_split[1]) != 2 or len(
                birthday_string_split[2]) != 2:
            input_error = input_error + "Birthday input must have format YYYY-MM-DD\n"
            submit = False
        elif int(birthday_string_split[0]) > int(now.year) or int(birthday_string_split[0]) < int(now.year) - 5:
            input_error = input_error + "Year of birth cannot exceed than the current year or be more than five years ago\n"
            submit = False
        else:
            try:
                datetime.datetime.strptime(self.birthdayLineEdit.text(), '%Y-%m-%d')
            except Exception as error:
                input_error = input_error + "Birthday input must be a valid date\n"
                submit = False
        return submit, input_error

    def check_breed(self, submit, input_error):
        if not str(self.breedLineEdit.text()):
            input_error = input_error + "Breed input cannot be empty\n"
            submit = False
        elif len(str(self.breedLineEdit.text())) > 20:
            input_error = input_error + "Breed input must contain less than 20 characters\n"
            submit = False
        return submit, input_error

    def check_sex(self, submit, input_error):
        sex_input = str(self.sexLineEdit.text()).lower()
        if not sex_input:
            input_error = input_error + "Sex input cannot be empty\n"
            submit = False
        elif len(sex_input) != 1:
            input_error = input_error + "Sex input must contain exactly one character, either 'm' or 'f'\n"
            submit = False
        elif not (sex_input == "m" or sex_input == "f"):
            input_error = input_error + "Sex input must be either 'm' or 'f'\n"
            submit = False
        return submit, input_error

    def check_misc(self, submit, input_error):
        if len(str(self.miscTextEdit.toPlainText())) > 8000:
            input_error = input_error + "Miscellaneous input must contain less then 8000 characters\n"
            submit = False
        return submit, input_error

    def refresh_mouse_options(self):
        try:
            sql_cursor = self.sql_connection.cursor()
            sql_cursor.execute("SELECT cageNumber, mouseNumber FROM mouseInfo WHERE retired = 0;")
            self.mouse_combo_box.clear()
            self.mouse_combo_box.addItem("Select mouse...")
            for (cageNumber, mouseNumber) in sql_cursor:
                self.mouse_combo_box.addItem("Cage: " + str(cageNumber) + "  Mouse: " + str(mouseNumber))
            sql_cursor.close()
        except Exception as error:
            print(error)

    def write_error_log(self, error):
        error_file_exist = True
        i = -1
        while error_file_exist:
            i = i + 1
            error_file = pathlib.Path("./mouse/errorLogs/error{0}.json".format(i))
            error_file_exist = error_file.is_file()
        with open("./mouse/errorLogs/error{0}.json".format(i), 'w+') as error_file:
            mouseDict = {"cage": self.cageLineEdit.text(),
                         "mouse": self.mouseIdLineEdit.text(),
                         "mass": self.massLineEdit.text(),
                         "birthday": self.birthdayLineEdit.text(),
                         "breed": self.breedLineEdit.text(),
                         "sex": self.sexLineEdit.text(),
                         "miscellaneous": self.miscTextEdit.toPlainText(),
                         "error": str(error)}
            json.dump(mouseDict, error_file)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Mouse(widget, "what the butt")
    widget.show()
    sys.exit(app.exec_())
