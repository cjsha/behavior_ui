from PyQt5 import QtCore, QtWidgets
import sys
import os
import pathlib
import json
import csv
from .parametersUi import Ui_parameters as ParametersUi
from .parametersConfirm import ParametersConfirm


class Parameters(ParametersUi, QtWidgets.QWidget):
    back_pressed = QtCore.pyqtSignal()

    def __init__(self, widget, sql_connection):

        ## call init function from QWidget
        super().__init__()
        self.sql_connection = sql_connection
        ## call UiMainWindow's setupUi function
        super().setupUi(widget)
        ## connect slots to signals, i.e. when pushbutton is clicked (signal), call a method in response (slot)

        self.submit_push_button.clicked.connect(self.submit_clicked)
        self.back_push_button.clicked.connect(self.back_pressed.emit)
        self.downloadFromDatabase.clicked.connect(self.list_parameters)
        self.tones_dict = json.loads(open("tonesDict.json", "r").read())

    def submit_clicked(self):

        submit = True
        input_error = ""

        try:
            submit, input_error = self.check_name(submit, input_error)
            if submit:
                submit, input_error = self.check_duplicate_name(submit, input_error)
            submit, input_error = self.check_tone_durations(submit, input_error)
            submit, input_error = self.check_divergences(submit, input_error)
            submit, input_error = self.check_template_song(submit, input_error)
            submit, input_error = self.check_song_volume(submit, input_error)

            if submit:
                ## set up the dialog ui
                parameters_confirm_dialog = QtWidgets.QDialog()
                parameters_confirm = ParametersConfirm(parameters_confirm_dialog)
                parameters_confirm.pass_objects(self.name_line_edit.text(),
                                                self.lick_window_duration_double_spin_box.value(),
                                                self.tone_duration_double_spin_box.value(),
                                                self.between_tones_duration_double_spin_box.value(),
                                                self.delay_duration_double_spin_box.value(),
                                                self.min_divergence_spin_box.value(),
                                                self.max_divergence_spin_box.value(),
                                                self.punishment_light_double_spin_box.value(),
                                                self.punishment_air_double_spin_box.value(),
                                                self.drop_size_spin_box.value(),
                                                self.licks_per_decision_spin_box.value(),
                                                self.songs_per_block_spin_box.value(),
                                                self.alternate_block_spin_box.value(),
                                                self.coinflip_block_spin_box.value(),
                                                self.random_encouragement_trials_spin_box.value(),
                                                self.incorrect_encouragement_trials_spin_box.value(),
                                                str(self.tone1_line_edit.text()) + " " +
                                                str(self.tone2_line_edit.text()) + " " +
                                                str(self.tone3_line_edit.text()) + " " +
                                                str(self.tone4_line_edit.text()) + " " +
                                                str(self.tone5_line_edit.text()) + " " +
                                                str(self.tone6_line_edit.text()),
                                                self.song_volume_spin_box.value())

                if parameters_confirm_dialog.exec_():
                    sql_cursor = self.sql_connection.cursor()
                    template_song = str(self.tone1_line_edit.text()) + " " +\
                                    str(self.tone2_line_edit.text()) + " " +\
                                    str(self.tone3_line_edit.text()) + " " +\
                                    str(self.tone4_line_edit.text()) + " " +\
                                    str(self.tone5_line_edit.text()) + " " +\
                                    str(self.tone6_line_edit.text())
                    template_song = template_song.strip()
                    sql_cursor.execute("""INSERT INTO taskParameters (
                                            name,
                                            lickWindowDuration,
                                            toneDuration,
                                            betweenToneDuration,
                                            delayDuration,
                                            minDivergence,
                                            maxDivergence,
                                            punishmentLight,
                                            punishmentAir,
                                            dropSize,                                        
                                            encourageRandom,
                                            encourageWrong,
                                            songsPerBlock,
                                            licksPerDecision,
                                            alternateBlock,
                                            coinFlipBlock,
                                            templateSong,
                                            songVolume)
                                            VALUES (%s, %s, %s,
                                            %s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s)""",
                                       (str(self.name_line_edit.text()),
                                        float(self.lick_window_duration_double_spin_box.value()),
                                        float(self.tone_duration_double_spin_box.value()),
                                        float(self.between_tones_duration_double_spin_box.value()),
                                        float(self.delay_duration_double_spin_box.value()),
                                        int(self.min_divergence_spin_box.value()),
                                        int(self.max_divergence_spin_box.value()),
                                        float(self.punishment_light_double_spin_box.value()),
                                        float(self.punishment_air_double_spin_box.value()),
                                        int(self.drop_size_spin_box.value()),
                                        int(self.random_encouragement_trials_spin_box.value()),
                                        int(self.incorrect_encouragement_trials_spin_box.value()),
                                        int(self.songs_per_block_spin_box.value()),
                                        int(self.licks_per_decision_spin_box.value()),
                                        int(self.alternate_block_spin_box.value()),
                                        int(self.coinflip_block_spin_box.value()),
                                        template_song,
                                        int(self.song_volume_spin_box.value())))
                    self.sql_connection.commit()
                    sql_cursor.close()
                    self.message_text_browser.append("Submission Successful\n")
                else:
                    self.message_text_browser.append("Submission Cancelled\n")
            else:
                self.message_text_browser.append("Submission Unsuccessful\n" + input_error)



        except Exception as error:

            self.message_text_browser.append("Submission Unsuccessful\n" + str(error))

            ## if mouse information input is determined valid by our checks yet still raises an exception,
            ## log mouse information input so that we can fix that later 
            if submit:
                self.write_error_log(error)

    def check_name(self, submit, input_error):
        if not str(self.name_line_edit.text()):
            input_error = input_error + "Name input cannot be empty\n"
            submit = False
        return submit, input_error

    def check_duplicate_name(self, submit, input_error):
        try:
            sql_cursor = self.sql_connection.cursor()
            sql_cursor.execute("SELECT name FROM taskParameters;")
            for name in sql_cursor:
                if str(name[0]) == str(self.name_line_edit.text()):
                    submit = False
                    input_error = input_error + str(name[0]) + " already exists in database\n"
            sql_cursor.close()
        except Exception as error:
            print(error)

        return submit, input_error

    def check_tone_durations(self, submit, input_error):
        if self.between_tones_duration_double_spin_box.value() <= self.tone_duration_double_spin_box.value():
            input_error = input_error + "Duration Between Tones cannot exceed or be equal to Duration Of Tones\n"
            submit = False
        return submit, input_error

    def check_divergences(self, submit, input_error):
        if self.max_divergence_spin_box.value() <= self.min_divergence_spin_box.value():
            input_error = input_error + "Maximum Divergence cannot exceed or be equal to Minimum Divergence\n"
            submit = False
        return submit, input_error

    def check_template_song(self, submit, input_error):
        empty_space = False

        if not str(self.tone1_line_edit.text()):
            input_error = input_error + self.tone1_line_edit.text() + "First tone field cannot be empty\n"
            submit = False
        elif self.tone1_line_edit.text() not in self.tones_dict:
            input_error = input_error + self.tone1_line_edit.text() + " is not a valid tone\n"
            submit = False

        if str(self.tone2_line_edit.text()):
            if str(self.tone2_line_edit.text()) not in self.tones_dict:
                input_error = input_error + self.tone2_line_edit.text() + " is not a valid tone\n"
                submit = False
        else:
            empty_space = True

        if str(self.tone3_line_edit.text()):
            if empty_space:
                input_error = input_error + "Empty template song fields between filled template song " +\
                              "fields are not allowed\n"
                submit = False
            elif self.tone3_line_edit.text() not in self.tones_dict:
                input_error = input_error + self.tone3_line_edit.text() + " is not a valid tone\n"
                submit = False
        else:
            empty_space = True

        if str(self.tone4_line_edit.text()):
            if empty_space:
                input_error = input_error + "Empty template song fields between filled template song " +\
                              "fields are not allowed\n"
                submit = False
            elif self.tone4_line_edit.text() not in self.tones_dict:
                input_error = input_error + self.tone4_line_edit.text() + " is not a valid tone\n"
                submit = False
        else:
            empty_space = True

        if str(self.tone5_line_edit.text()):
            if empty_space:
                input_error = input_error + "Empty template song fields between filled template song " +\
                              "fields are not allowed\n"
                submit = False
            elif self.tone5_line_edit.text() not in self.tones_dict:
                input_error = input_error + self.tone5_line_edit.text() + " is not a valid tone\n"
                submit = False
        else:
            empty_space = True

        if str(self.tone6_line_edit.text()):
            if empty_space:
                input_error = input_error + "Empty template song fields between filled template song " +\
                              "fields are not allowed\n"
                submit = False
            elif self.tone6_line_edit.text() not in self.tones_dict:
                input_error = input_error + self.tone6_line_edit.text() + " is not a valid tone\n"
                submit = False

        return submit, input_error

    def check_song_volume(self, submit, input_error):
        if int(self.song_volume_spin_box.value()) <= 0 or int(self.song_volume_spin_box.value()) > 100:
            input_error = input_error + "Song Volume must be between 0 and 100\n"
            submit = False
        return submit, input_error

    def write_error_log(self, error):
        print(error)
        errorFileExist = True
        i = -1
        while errorFileExist:
            i = i + 1
            errorFile = pathlib.Path("./parameters/errorLogs/error{0}.json".format(i))
            errorFileExist = errorFile.is_file()
        with open("./parameters/errorLogs/error{0}.json".format(i), 'w+') as errorFile:
            parametersDict = dict(name=self.name_line_edit.text(),
                                  lickWindow=self.lick_window_duration_double_spin_box.value(),
                                  tones=self.tone_duration_double_spin_box.value(),
                                  betweenTones=self.between_tones_duration_double_spin_box.value(),
                                  delay=self.delay_duration_double_spin_box.value(),
                                  minDiv=self.min_divergence_spin_box.value(),
                                  maxDiv=self.max_divergence_spin_box.value(),
                                  punishLight=self.punishment_light_double_spin_box.value(),
                                  punishAir=self.punishment_light_double_spin_box.value(),
                                  dropSize=self.drop_size_spin_box.value(),
                                  licksPerDecision=self.licks_per_decision_spin_box.value(),
                                  songsPerBlock=self.songs_per_block_spin_box.value(),
                                  alternateBlock=self.alternate_block_spin_box.value(),
                                  coinFlipBlock=self.coinflip_block_spin_box.value(),
                                  randomEncouragement=self.random_encouragement_trials_spin_box.value(),
                                  incorrectEncouragement=self.incorrect_encouragement_trials_spin_box.value(),
                                  templateSong=str(self.tone1_line_edit.text()) + " " +
                                               str(self.tone2_line_edit.text()) + " " +
                                               str(self.tone3_line_edit.text()) + " " +
                                               str(self.tone4_line_edit.text()) + " " +
                                               str(self.tone5_line_edit.text()) + " " +
                                               str(self.tone6_line_edit.text()),
                                  error=str(error),
                                  songVolume=self.song_volume_spin_box.value())
            json.dump(parametersDict, errorFile)

    def list_parameters(self):
        try:
            sql_cursor = self.sql_connection.cursor()
            sql_cursor.execute("SELECT * FROM taskParameters;")
            with open("./parameters/parameters.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in sql_cursor.description])  # write headers
                csv_writer.writerows(sql_cursor)
            sql_cursor.close()
            self.message_text_browser.append("File (parameters.csv) saved successfully to the following directory:\n" +
                                           os.getcwd() + "\parameters\n")
        except Exception as error:
            print(error)
            self.message_text_browser.append("File saved unsuccessfully\n" + str(error))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = sql(widget)
    widget.show()
    sys.exit(app.exec_())
