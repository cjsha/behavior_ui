import json
import logging
import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets
from .taskMainUi import Ui_taskMain as TaskMainUi
from .plots import Plots


class TaskMain(TaskMainUi, QtWidgets.QWidget):

    def __init__(self, mainWidget, session_num, session_suffix, sql_connection,
                 com_connection, cage_number, mouse_number, parameters, save):

        super().__init__()
        super().setupUi(mainWidget)
        self.mouseCageLabel2.setText(cage_number)
        self.mouseIdLabel2.setText(mouse_number)
        self.trainingPhaseLabel2.setText(parameters)
        self.serial_connection = com_connection
        self.comPortLabel2.setText(self.serial_connection.port)
        self.tones_dict = json.loads(open("tonesDict.json").read())
        self.reverse_tones_dict = {value: key for key, value in self.tones_dict.items()}
        self.save = save
        self.sql_connection = sql_connection
        self.session_num = session_num
        self.session_suffix = session_suffix
        self.sql_cursor = self.sql_connection.cursor()
        self.excludeNoLicks.stateChanged.connect(self.update_statistics)
        self.excludeFreeDrops.stateChanged.connect(self.update_statistics)

        # set up performance plots
        self.plots = Plots()
        self.plots.setObjectName("plots")
        self.gridLayout.addWidget(self.plots.view, 0, 0)

        self.sec = 0
        self.lick = 0
        self.alternate_song_text_position = 0

        # timer for reading serial
        self.timerPerformance = QtCore.QTimer()
        self.timerPerformance.timeout.connect(self.read_serial_start_threads)

        self.bytes_dict = {bytes([0x57]): 'pause', bytes([0x58]): 'play', bytes([0x72]): 'delay',
                           bytes([0x77]): 'song', bytes([0x78]): 'lick_window', bytes([0xEE]): 'reset',
                           bytes([0xAC]): 'session_identifier', bytes([0xCA]): 'realtime_identifier',
                           bytes([0x97]): 'left_lick', bytes([0x98]): 'right_lick', bytes([0x37]): 'left_reward',
                           bytes([0x38]): 'right_reward', bytes([0x75]): 'tone_start', bytes([0x7C]): 'tone_end'}
        self.inverse_bytes_dict = {value: key for key, value in self.bytes_dict.items()}

        # self.real_time_save_data = [[0], [0]]
        # self.session_save_data = [[0], [0]]

        self.real_time_plot_delay = [[0], [-1]]
        self.real_time_plot_song = [[0], [-1]]
        self.real_time_plot_tone = [[0], [-1]]
        self.real_time_plot_lick_window = [[0], [-1]]
        self.real_time_plot_pause = [[0], [-1]]
        self.real_time_plot_licks = [[0], [0]]
        self.real_time_plot_reward = [[0], [0]]

        self.session_plot_correct = [[1.0], [0]]
        self.session_plot_incorrect = [[1.0], [0]]
        self.session_plot_free = [[1.0], [0]]
        self.session_plot_diff = [[1.0], [0]]

        self.trial_num = []
        self.lick_direction = []
        self.correctness = []
        self.misc = []
        self.diff = []
        self.free = []

        self.realTimeCheckBoxStateChanged()
        self.performanceCheckBoxStateChanged()
        self.realTimeCheckBox.clicked.connect(self.realTimeCheckBoxStateChanged)
        self.secDoubleSpinBox.valueChanged.connect(self.update_realtime_plots_range)
        self.trialsSpinBox.valueChanged.connect(self.update_trials_plots_range)
        self.performanceCheckBox.clicked.connect(self.performanceCheckBoxStateChanged)
        self.playButton.clicked.connect(self.playButtonPressed)

        logging.basicConfig(filename='debugging_mcu.log', level=logging.DEBUG,
                            format='%(asctime)s:%(levelname)s:%(message)s')

    def read_serial_start_threads(self):
        while self.serial_connection.in_waiting >= 7:
            incoming_char = self.serial_connection.read(1)
            realtime_identifier = bytes([0xCA])
            session_identifier = bytes([0xAC])
            if incoming_char == realtime_identifier:
                realtime_event_byte = self.serial_connection.read(1)
                realtime_timestamp_bytes = self.serial_connection.read(5)
                logging.debug(' '.join([str(incoming_char), str(realtime_event_byte),
                                        str(realtime_timestamp_bytes)]))
                realtime_timestamp = ((realtime_timestamp_bytes[0]) + (realtime_timestamp_bytes[1] << 8)) / 0xFFFF
                realtime_timestamp += ((realtime_timestamp_bytes[2]) + (realtime_timestamp_bytes[3] << 8))
                realtime_timestamp += (realtime_timestamp_bytes[4] << 16)
                realtime_timestamp = realtime_timestamp / 1000
                realtime_info = ' '.join([str(self.session_num), str(self.session_suffix),
                                          self.bytes_dict[realtime_event_byte], str(realtime_timestamp)])
                logging.info(realtime_info)
                print(realtime_info)
                if self.save:
                    # with open('current_session_realtime_data.txt', 'a+') as data_file:
                    #     data_file.write(realtime_info)
                    self.sql_cursor.execute("""INSERT INTO realtimeData (
                                            sessionNumber,
                                            sessionSuffix,
                                            event,
                                            eventTimestamp) 
                                            VALUES (%s, %s, %s, %s)""",
                                            (str(self.session_num),
                                             str(self.session_suffix),
                                             self.bytes_dict[realtime_event_byte],
                                             str(realtime_timestamp)))
                    self.sql_connection.commit()
                if self.bytes_dict[realtime_event_byte] == 'delay':
                    self.real_time_plot_delay[1].extend([-1, 1])
                    self.real_time_plot_delay[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_lick_window[1].extend([1, -1])
                    self.real_time_plot_lick_window[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_licks[1].append(0)
                    self.real_time_plot_licks[0].append(realtime_timestamp)
                elif self.bytes_dict[realtime_event_byte] == 'song':
                    self.real_time_plot_delay[1].extend([1, -1])
                    self.real_time_plot_delay[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_song[1].extend([-1, 1])
                    self.real_time_plot_song[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_licks[1].append(0)
                    self.real_time_plot_licks[0].append(realtime_timestamp)
                elif self.bytes_dict[realtime_event_byte] == 'tone_start':
                    self.real_time_plot_tone[1].extend([-1, 1])
                    self.real_time_plot_tone[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_licks[1].append(0)
                    self.real_time_plot_licks[0].append(realtime_timestamp)
                elif self.bytes_dict[realtime_event_byte] == 'tone_end':
                    self.real_time_plot_tone[1].extend([1, -1])
                    self.real_time_plot_tone[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_licks[1].append(0)
                    self.real_time_plot_licks[0].append(realtime_timestamp)
                elif self.bytes_dict[realtime_event_byte] == 'lick_window':
                    self.real_time_plot_song[1].extend([1, -1])
                    self.real_time_plot_song[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_lick_window[1].extend([-1, 1])
                    self.real_time_plot_lick_window[0].extend([realtime_timestamp, realtime_timestamp + 0.0000001])
                    self.real_time_plot_licks[1].append(0)
                    self.real_time_plot_licks[0].append(realtime_timestamp)
                elif self.bytes_dict[realtime_event_byte] == 'left_lick':
                    self.real_time_plot_licks[1].extend([0, -1, -1, 0])
                    self.real_time_plot_licks[0].extend([realtime_timestamp - 0.0000001, realtime_timestamp])
                    self.real_time_plot_licks[0].extend([realtime_timestamp + 0.0005, realtime_timestamp + 0.0005001])
                elif self.bytes_dict[realtime_event_byte] == 'right_lick':
                    self.real_time_plot_licks[1].extend([0, 1, 1, 0])
                    self.real_time_plot_licks[0].extend([realtime_timestamp - 0.0000001, realtime_timestamp])
                    self.real_time_plot_licks[0].extend([realtime_timestamp + 0.0005, realtime_timestamp + 0.0005001])
                elif self.bytes_dict[realtime_event_byte] == 'pause':
                    self.real_time_plot_pause[1].extend([-1, 1, 1, -1])
                    self.real_time_plot_pause[0].extend([realtime_timestamp - 0.0000001, realtime_timestamp])
                    self.real_time_plot_pause[0].extend([realtime_timestamp + 0.2, realtime_timestamp + 0.200001])
                elif self.bytes_dict[realtime_event_byte] == 'left_reward':
                    self.real_time_plot_reward[1].extend([0, -1, -1, 0])
                    self.real_time_plot_reward[0].extend([realtime_timestamp - 0.0000001, realtime_timestamp])
                    self.real_time_plot_reward[0].extend([realtime_timestamp + 0.3, realtime_timestamp + 0.300001])
                elif self.bytes_dict[realtime_event_byte] == 'right_reward':
                    self.real_time_plot_reward[1].extend([0, 1, 1, 0])
                    self.real_time_plot_reward[0].extend([realtime_timestamp - 0.0000001, realtime_timestamp])
                    self.real_time_plot_reward[0].extend([realtime_timestamp + 0.3, realtime_timestamp + 0.300001])
                self.plots.update_realtime_plots(self.real_time_plot_delay, self.real_time_plot_song,
                                                 self.real_time_plot_tone, self.real_time_plot_lick_window,
                                                 self.real_time_plot_licks, self.real_time_plot_pause,
                                                 self.real_time_plot_reward)
                if self.realTimeCheckBox.isChecked():
                    self.update_realtime_plots_range()
            elif incoming_char == session_identifier:
                while self.serial_connection.in_waiting < 12:
                    pass
                session_info = self.serial_connection.read(12)
                self.trial_num.append((int(session_info[0]) << 8) + int(session_info[1]))
                self.lick_direction.append(int(session_info[2]) - 1)
                self.correctness.append(int(session_info[3]))
                self.misc.append(int(session_info[4]))
                song = (' '.join([self.reverse_tones_dict[int(tone)] for tone in session_info[5:10]])).strip()
                self.diff.append(int(session_info[11]))
                if self.correctness[-1] == 1:
                    self.session_plot_correct[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_correct[1].extend([self.lick_direction[-1], self.lick_direction[-1]])
                    self.session_plot_incorrect[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_incorrect[1].extend([0, 0])
                elif self.correctness[-1] == 0:
                    self.session_plot_correct[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_correct[1].extend([0, 0])
                    self.session_plot_incorrect[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_incorrect[1].extend([0, 0])
                elif self.correctness[-1] == 2:
                    self.session_plot_correct[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_correct[1].extend([0, 0])
                    self.session_plot_incorrect[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_incorrect[1].extend([self.lick_direction[-1], self.lick_direction[-1]])
                self.free.append((self.misc[-1] & 0x0F) - 1)
                if self.free[-1] == -1:
                    self.session_plot_free[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_free[1].extend([-0.5, -0.5])
                elif self.free[-1] == 0:
                    self.session_plot_free[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_free[1].extend([0, 0])
                elif self.free[-1] == 1:
                    self.session_plot_free[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                    self.session_plot_free[1].extend([0.5, 0.5])
                self.session_plot_diff[0].extend([self.trial_num[-1], self.trial_num[-1] + 0.999999])
                self.session_plot_diff[1].extend([self.diff[-1], self.diff[-1]])
                self.plots.update_session_plots(self.session_plot_correct, self.session_plot_incorrect,
                                                self.session_plot_free, self.session_plot_diff)
                self.alternate_song_text_position += 1
                text = pg.TextItem(text=song, color='k')
                self.plots.p1.addItem(text)

                self.update_statistics()

                text.setPos(self.trial_num[-1], 2 + self.alternate_song_text_position % 2)

                if self.performanceCheckBox.isChecked():
                    self.update_trials_plots_range()
                if self.save:
                    # with open('current_session_realtime_data.txt', 'a+') as data_file:
                    #     data_file.write(realtime_info)
                    self.sql_cursor.execute("""INSERT INTO trialData (
                                            sessionNumber,
                                            sessionSuffix,
                                            trialNumber,
                                            lickDirection,
                                            correctness,
                                            freeDrop,
                                            song,
                                            diff) 
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                                            (str(self.session_num),
                                             str(self.session_suffix),
                                             str(self.trial_num[-1]),
                                             str(self.lick_direction[-1]),
                                             str(self.correctness[-1]),
                                             str(self.free[-1]),
                                             str(song),
                                             str(self.diff[-1])))
                    self.sql_connection.commit()
            else:
                self.messageTextBrowser.append("Faulty MCU Message\n")
                self.messageTextBrowser.append(str(incoming_char) + "\n")
                logging.debug(str(incoming_char))

    def performanceCheckBoxStateChanged(self):
        if self.performanceCheckBox.isChecked():
            self.trialsSpinBox.setEnabled(True)
            self.update_trials_plots_range()
            self.plots.p1.hideButtons()
            self.plots.p1.setMouseEnabled(x=False, y=False)
        else:
            self.trialsSpinBox.setEnabled(False)
            self.plots.p1.showButtons()
            self.plots.p1.setMouseEnabled(x=True, y=False)

    def realTimeCheckBoxStateChanged(self):
        if self.realTimeCheckBox.isChecked():
            self.secDoubleSpinBox.setEnabled(True)
            self.update_realtime_plots_range()
            self.plots.p3.hideButtons()
            self.plots.p3.setMouseEnabled(x=False, y=False)
        else:
            self.secDoubleSpinBox.setEnabled(False)
            self.plots.p3.showButtons()
            self.plots.p3.setMouseEnabled(x=True, y=False)

    def playButtonPressed(self):
        if self.playButton.text() == "Play":
            self.serial_connection.write(self.inverse_bytes_dict["play"])
            self.playButton.setText("Pause")
            self.timerPerformance.start(100)
        elif self.playButton.text() == "Pause":
            self.serial_connection.write(self.inverse_bytes_dict["pause"])
            self.playButton.setText("Play")
            self.timerPerformance.stop()

    def update_realtime_plots_range(self):
        most_recent_timestamp = max(self.real_time_plot_delay[0][-1], self.real_time_plot_song[0][-1],
                                    self.real_time_plot_tone[0][-1], self.real_time_plot_lick_window[0][-1],
                                    self.real_time_plot_licks[0][-1], self.real_time_plot_pause[0][-1])
        self.plots.p3.setXRange(most_recent_timestamp - self.secDoubleSpinBox.value(), most_recent_timestamp)

    def update_trials_plots_range(self):
        most_recent_trial = self.session_plot_diff[0][-1]
        self.plots.p1.setXRange(most_recent_trial - self.trialsSpinBox.value(), most_recent_trial)

    def update_statistics(self):
        total_trials = 0
        total_template_trials = 0
        total_nontemplate_trials = 0
        total_no_lick_trials = 0
        total_free_trials = 0
        total_correct_trials = 0
        total_incorrect_trials = 0
        total_reward = 0
        count_no_licks = False if self.excludeNoLicks.isChecked() else True
        count_free_drops = False if self.excludeFreeDrops.isChecked() else True
        for trial in self.trial_num:
            free_drop = bool(self.free[trial - 1])
            no_lick = not bool(self.lick_direction[trial - 1])
            if (count_free_drops or (not free_drop)) and (count_no_licks or (not no_lick)):
                total_trials += 1
                if self.diff[trial - 1] == 0:
                    total_template_trials += 1
                elif self.diff[trial - 1] > 0:
                    total_nontemplate_trials += 1
                if self.lick_direction[trial - 1] == 0:
                    total_no_lick_trials += 1
                if self.free[trial - 1] != 0:
                    total_free_trials += 1
                if self.free[trial - 1] != 0 or self.correctness[trial - 1] == 1:
                    total_reward += 1
                if self.correctness[trial - 1] == 1:
                    total_correct_trials += 1
                if self.correctness[trial - 1] == 2:
                    total_incorrect_trials += 1

        self.toTrStatLabel.setText(str(total_trials))
        self.teTrStatLabel.setText(str(total_template_trials))
        self.noTrStatLabel.setText(str(total_nontemplate_trials))
        self.noLiTrStatLabel.setText(str(total_no_lick_trials))
        self.frDrTrStatLabel.setText(str(total_free_trials))
        self.toDrStatLabel.setText(str(total_reward))
        self.coTrStatLabel.setText(str(total_correct_trials))
        self.inTrStatLabel.setText(str(total_incorrect_trials))
        if total_trials > 0:
            self.coPeStatLabel.setText(''.join([str((total_correct_trials * 100) // total_trials), '%']))
            self.inPeStatLabel.setText(''.join([str((total_incorrect_trials * 100) // total_trials), '%']))
        else:
            self.coPeStatLabel.setText('n/a')
            self.inPeStatLabel.setText('n/a')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    blah = QtWidgets.QWidget()
    ui = TaskMain(blah)
    blah.show()
    sys.exit(app.exec_())
