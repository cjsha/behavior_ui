from PyQt5 import QtCore, QtWidgets
import serial
import serial.tools.list_ports
import fnmatch
import json
from .taskSettingsConfirm import TaskSettingsConfirm
from .taskSettingsUi import Ui_taskSettings as TaskSettingsUi


class TaskSettings(TaskSettingsUi, QtWidgets.QWidget):
    back_pressed = QtCore.pyqtSignal()
    open_task = QtCore.pyqtSignal(object, object, object, object, object, object, object, object)

    def __init__(self, widget, sql_connection):

        super().__init__()
        super().setupUi(widget)
        self.sql_connection = sql_connection
        self.refresh_push_button.clicked.connect(self.refresh_com_port_options)
        self.save_data_check_box.clicked.connect(self.save_data)
        self.serial_push_button.clicked.connect(self.serial_pushed)
        self.parameters_combo_box.activated.connect(self.check_that_all_is_ready)
        self.mouse_combo_box.activated.connect(self.check_that_all_is_ready)
        self.backPushButton.clicked.connect(self.back_pressed.emit)
        self.go_push_button.clicked.connect(self.go_clicked)
        self.refresh_com_port_options()
        self.refresh_mouse_options()
        self.refresh_parameters_options()
        self.tones_dict = json.loads(open("tonesDict.json").read())
        self.serial_connection = 1

    def refresh_com_port_options(self):
        self.com_combo_box.clear()
        self.com_combo_box.addItem("Select COM Port...")
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            self.com_combo_box.addItem(str(p))
            if "USB Serial Device" in str(p):
                self.com_combo_box.addItem(str(p))

    def save_data(self):
        if self.save_data_check_box.isChecked():
            self.mouse_widget.setEnabled(True)
        elif not self.save_data_check_box.isChecked():
            self.mouse_widget.setEnabled(False)
        self.check_that_all_is_ready()

    def refresh_mouse_options(self):
        try:
            sql_cursor = self.sql_connection.cursor()
            sql_cursor.execute("SELECT cageNumber, mouseNumber FROM mouseInfo WHERE retired = 0;")
            self.mouse_combo_box.clear()
            self.mouse_combo_box.addItem("Select Mouse...")
            for (cageNumber, mouseNumber) in sql_cursor:
                self.mouse_combo_box.addItem("Cage: " + str(cageNumber) + "  Mouse: " + str(mouseNumber))
            sql_cursor.close()
        except Exception as error:
            self.message_text_browser.append("Refresh unsuccessful\n" + str(error) + "\n")

    def refresh_parameters_options(self):
        try:
            sql_cursor = self.sql_connection.cursor()
            sql_cursor.execute("SELECT name FROM taskParameters;")
            self.parameters_combo_box.addItem("Select Behavior Task Parameters...")
            for name in sql_cursor:
                self.parameters_combo_box.addItem(str(name[0]))
            sql_cursor.close()
        except Exception as error:
            self.message_text_browser.append("Refresh unsuccessful\n" + str(error) + "\n")

    def serial_pushed(self):
        if self.serial_push_button.text() == "Connect":
            if self.com_combo_box.currentText() == "Select COM Port...":
                self.message_text_browser.append("Serial Connection Unsuccessful\nYou must choose a valid COM port\n")
            else:
                try:
                    serial_port = str(
                        fnmatch.filter([str(self.com_combo_box.currentText()).split(' ', 1)[0]], 'COM?*')[0])
                    self.serial_connection = serial.Serial(serial_port, baudrate=115200)
                    self.message_text_browser.append("Serial Connection Successful\n")
                    self.serial_push_button.setText("Disconnect")
                    self.parameters_widget.setEnabled(True)
                    self.save_data_check_box.setEnabled(True)
                    self.mouse_widget.setEnabled(self.save_data_check_box.isChecked())
                    self.com_combo_box.setEnabled(False)
                except Exception as error:
                    self.message_text_browser.append("Serial Connection Unsuccessful\n" + str(error) + "\n")
        elif self.serial_push_button.text() == "Disconnect":
            try:
                self.serial_connection.close()
                self.message_text_browser.append("Serial Disconnection Successful\n")
                self.serial_push_button.setText("Connect")
                self.parameters_widget.setEnabled(False)
                self.save_data_check_box.setEnabled(False)
                self.mouse_widget.setEnabled(False)
                self.com_combo_box.setEnabled(True)
            except Exception as error:
                self.message_text_browser.append("Serial Disconnection Unsuccessful\n" + str(error) + "\n")
        self.check_that_all_is_ready()

    def check_that_all_is_ready(self):
        if self.parameters_combo_box.currentText() != "Select Behavior Task Parameters..." and \
                self.serial_push_button.text() == "Disconnect" and ((not self.save_data_check_box.isChecked()) or (
                self.save_data_check_box.isChecked() and str(self.mouse_combo_box.currentText()) != "Select Mouse...")):
            self.go_push_button.setEnabled(True)
        else:
            self.go_push_button.setEnabled(False)

    def send_parameters(self, input_error):

        sql_cursor = self.sql_connection.cursor(dictionary=True)
        query = "SELECT * FROM taskParameters WHERE name = '" + \
                str(self.parameters_combo_box.currentText()).strip() + "'"
        sql_cursor.execute(query)
        parameters = sql_cursor.fetchone()

        template_song_notes = (str(parameters['templateSong']).strip()).split(" ")

        template_song_ints = [None] * 6
        for index, values in enumerate(template_song_ints):
            if index < len(template_song_notes):
                template_song_ints[index] = int(self.tones_dict[template_song_notes[index]])
            else:
                template_song_ints[index] = int(255)

        config = bytearray([0x11,
                            int(parameters['lickWindowDuration'] * 1000 // 256),  # 0
                            int(parameters['lickWindowDuration'] * 1000 % 256),  # 1
                            int(parameters['toneDuration'] * 1000 // 256),  # 2
                            int(parameters['toneDuration'] * 1000 % 256),  # 3
                            int(parameters['betweenToneDuration'] * 1000 // 256),  # 4
                            int(parameters['betweenToneDuration'] * 1000 % 256),  # 5
                            int(parameters['delayDuration'] * 1000 // 256),  # 6
                            int(parameters['delayDuration'] * 1000 % 256),  # 7
                            int(parameters['minDivergence']),  # 8
                            int(parameters['maxDivergence']),  # 9
                            int(parameters['punishmentLight'] * 1000 // 256),  # 10
                            int(parameters['punishmentLight'] * 1000 % 256),  # 11
                            int(parameters['punishmentAir'] * 1000 // 256),  # 12
                            int(parameters['punishmentAir'] * 1000 % 256),  # 12
                            int(parameters['dropSize']),  # 14
                            int(parameters['licksPerDecision']),  # 15
                            int(parameters['songsPerBlock']),  # 16
                            int(parameters['alternateBlock']),  # 17
                            int(parameters['blockFlipChance']),  # 18
                            int(parameters['encourageWrong']),  # 19
                            int(parameters['encourageRandom']),  # 20
                            template_song_ints[0],  # 21
                            template_song_ints[1],  # 22
                            template_song_ints[2],  # 23
                            template_song_ints[3],  # 24
                            template_song_ints[4],  # 25
                            template_song_ints[5],  # 26
                            int(parameters['songVolume'])])  # 27

        check_sum = sum(bytearray(config[1:]))
        config.extend((int(check_sum // 256), int(check_sum % 256)))  # 28 #29
        self.serial_connection.timeout = 2
        self.serial_connection.write(config)
        print(config)
        pause_byte = bytes([0x57])
        confirmation_byte = self.serial_connection.read()
        if not confirmation_byte:
            successful_mcu_communication = False
            input_error = input_error + "MCU did not respond to parameters message.\n"
        elif confirmation_byte != pause_byte:
            successful_mcu_communication = False
            input_error = input_error + "MCU did not return the correct checksum.\n"
            print(pause_byte)
            print(confirmation_byte)
        else:
            successful_mcu_communication = True

        return successful_mcu_communication, input_error

    def go_clicked(self):
        # reset_byte = bytes([0xEE])
        # self.serial_connection.write(reset_byte)
        try:

            submit = True
            input_error = ""
            current_session_number = 0
            current_session_suffix = 0
            if not self.save_data_check_box.isChecked():
                mouse_string = "Practice Session"
                mass_string = "Data will not be saved"
                cage_number = "n/a"
                mouse_number = "n/a"
            else:
                mouse_split = str(self.mouse_combo_box.currentText()).split(" ")
                cage_number = mouse_split[1]
                mouse_number = mouse_split[4]
                sql_cursor = self.sql_connection.cursor()
                sql_cursor.execute("""SELECT sessionNumber, sessionSuffix, mass, timeSubmitted FROM sessionData 
                                        WHERE cageNumber = %s AND mouseNumber = %s AND 
                                        timeSubmitted > DATE_SUB(NOW(), INTERVAL 5 HOUR)""",
                                   (int(cage_number), int(mouse_number)))
                sessions_today = sql_cursor.fetchall()
                number_sessions_today = len(sessions_today)

                if number_sessions_today == 0:
                    if not str(self.massLineEdit.text()):
                        input_error = "Mass input cannot be empty (unless the mouse has started a session in the last five hours)\n"
                        submit = False
                    elif not str(self.massLineEdit.text()).replace(".", "1", 1).isdigit():
                        input_error = "Mass input must contain only digits and optionally one period (unless the mouse has started a session in the last five hours)\n"
                        submit = False
                    elif len(str(self.massLineEdit.text()).split(".")) > 1:
                        if len(str(self.massLineEdit.text()).split(".")[0]) > 6 or len(
                                str(self.massLineEdit.text()).split(".")[1]) > 4:
                            input_error = "Mass input contains too many digits before or after the decimal point\n"
                            submit = False
                    elif len(str(self.massLineEdit.text()).split(".")) > 6:
                        input_error = "Mass input contains too many digits after the decimal point\n"
                        submit = False
                    mass = float(self.massLineEdit.text())
                    mass_string = "Mass: " + str(mass) + " grams"
                    mouse_string = str(self.mouse_combo_box.currentText())
                    sql_cursor.execute("""SELECT sessionNumber FROM sessionData WHERE 
                                          id = (SELECT max(id) FROM sessionData)""")
                    session_number = sql_cursor.fetchone()
                    if not session_number:
                        current_session_number = 0
                    else:
                        current_session_number = int(session_number[0]) + 1
                    current_session_suffix = "A"

                else:
                    session_number = list()
                    session_suffix = list()
                    for session_data_rows in sessions_today:
                        session_number.append(session_data_rows[0])
                        session_suffix.append(ord(session_data_rows[1]))
                    mass_index = max(enumerate(session_suffix), key=lambda x: x[1])[0]
                    mass = float(sessions_today[mass_index][2])
                    mouse_string = str(
                        self.mouse_combo_box.currentText()) + " started a session less than five hours ago."
                    mass_string = "Mass (" + str(mass) + " g) will be taken from this mouse's previous session."
                    current_session_number = int(max(session_number))
                    current_session_suffix = chr(max(session_suffix) + 1)

            if submit:
                parameters = str(self.parameters_combo_box.currentText())
                parameters_string = "Parameters: " + parameters
                com_string = str(fnmatch.filter([str(self.com_combo_box.currentText()).split(' ', 1)[0]], 'COM?*')[0])
                task_settings_confirm_dialog = QtWidgets.QDialog()
                task_settings_confirm = TaskSettingsConfirm(task_settings_confirm_dialog)
                task_settings_confirm.pass_objects(com_string, parameters_string, mouse_string, mass_string)

                if task_settings_confirm_dialog.exec_():
                    successful_mcu_communication, input_error = self.send_parameters(input_error)
                    if successful_mcu_communication:
                        if self.save_data_check_box.isChecked():
                            sql_cursor.execute("""INSERT INTO sessionData (
                                                sessionNumber,
                                                sessionSuffix,
                                                cageNumber,
                                                mouseNumber,
                                                mass,
                                                parametersName,
                                                comPort) 
                                                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                                               (current_session_number,
                                                current_session_suffix,
                                                cage_number,
                                                mouse_number,
                                                mass,
                                                parameters,
                                                com_string))
                            self.sql_connection.commit()
                            sql_cursor.close()

                        self.open_task.emit(current_session_number, current_session_suffix, self.sql_connection,
                                            self.serial_connection, cage_number, mouse_number, parameters,
                                            self.save_data_check_box.isChecked())
                    else:
                        self.message_text_browser.append("Submission Failed\n" + input_error + "\n")
                else:
                    self.message_text_browser.append("Submission Cancelled\n")
            else:
                self.message_text_browser.append("Submission Unsuccessful\n" + input_error + "\n")

        except Exception as error:
            self.message_text_browser.append("Submission Unsuccessful\n" + str(error) + "\n")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWidget = QtWidgets.QWidget()
    ui = TaskSettings(mainWidget)
    mainWidget.show()
    sys.exit(app.exec_())
