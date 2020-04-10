from PyQt5 import QtWidgets
import sys
import numpy as np
import pyqtgraph as pg


class Plots(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # configure plots visuals
        # pg.setConfigOptions(antialias=False)
        pg.setConfigOptions(antialias=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.view = pg.GraphicsLayoutWidget()
        self.view.addLabel('Trial Data Plots')

        # set up p1 and p2 performance plots
        self.view.nextRow()
        self.p1 = self.view.addPlot()
        # self.p1.setDownsampling(auto=True)
        # self.p1.setClipToView(True)
        self.p1.setMenuEnabled(False)
        self.p1.hideButtons()
        self.p1.setYRange(-1, 3)
        self.p1Ticks = self.p1.getAxis('left')
        self.p1Ticks.setTicks([[(-1, 'Left'), (0, 'No Lick'), (1, 'Right'), (2, 'Song')]])
        self.p1.setMouseEnabled(x=False, y=False)
        self.curve_correct_trials = self.p1.plot(pen='k', width=0, brush='g', fillLevel=0.0)
        self.curve_incorrect_trials = self.p1.plot(pen='k', width=0, brush='r', fillLevel=0.0)
        self.curve_free_trials = self.p1.plot(pen='k', width=0, brush='b', fillLevel=0.0)
        self.view.nextRow()

        self.view.nextRow()
        self.p2 = self.view.addPlot()
        # self.p2.setDownsampling(auto=True)
        # self.p2.setClipToView(True)
        self.p2.setMenuEnabled(False)
        self.p2.hideButtons()
        self.p2.setYRange(0, 100)
        self.p2Ticks = self.p2.getAxis('left')
        self.p2.setMouseEnabled(x=False, y=False)
        self.curve_diff = self.p2.plot(pen='k')

        self.p1.sigXRangeChanged.connect(self.update_difficulty_plot_range)

        self.view.nextRow()
        self.view.addLabel('Real Time Data Plot')

        # set up p3 real time data plots
        self.view.nextRow()
        self.p3 = self.view.addPlot()
        # self.p3.setDownsampling(auto=True)
        # self.p3.setClipToView(True)
        self.p3.setMenuEnabled(False)
        self.p3.hideButtons()
        self.p3.setYRange(-1, 1)
        self.p3Ticks = self.p3.getAxis('left')
        self.p3Ticks.setTicks([[(-1, 'Left'), (0, 'No Lick'), (1, 'Right')]])
        self.p3.setMouseEnabled(x=False, y=False)
        self.curve_delay = self.p3.plot(pen='w', width=0, brush=(230, 255, 255), fillLevel=-1.0)
        self.curve_song = self.p3.plot(pen='w', width=0, brush=(255, 255, 230), fillLevel=-1.0)
        self.curve_tone = self.p3.plot(pen='w', width=0, brush=(255, 225, 75), fillLevel=-1.0)
        self.curve_lick_window = self.p3.plot(pen='w', width=0, brush=(255, 230, 255), fillLevel=-1.0)
        self.curve_pause = self.p3.plot(pen='w', width=1, brush='k', fillLevel=-1.0)
        self.curve_reward = self.p3.plot(pen='g', width=1, brush='g', fillLevel=0.0)
        self.curve_licks = self.p3.plot(pen='b', width=1, brush='b', fillLevel=0.0)

    def update_session_plots(self, correct_trials, incorrect_trials, free_trials, diff):
        self.curve_free_trials.setData(x=np.array(free_trials[0]), y=np.array(free_trials[1]))
        self.curve_correct_trials.setData(x=np.array(correct_trials[0]), y=np.array(correct_trials[1]))
        self.curve_incorrect_trials.setData(x=np.array(incorrect_trials[0]), y=np.array(incorrect_trials[1]))
        self.curve_diff.setData(x=np.array(diff[0]), y=np.array(diff[1]))

    def update_realtime_plots(self, delay, song, tone, lick_window, licks, pause, reward):
        self.curve_delay.setData(x=np.array(delay[0]), y=np.array(delay[1]))
        self.curve_song.setData(x=np.array(song[0]), y=np.array(song[1]))
        self.curve_tone.setData(x=np.array(tone[0]), y=np.array(tone[1]))
        self.curve_lick_window.setData(x=np.array(lick_window[0]), y=np.array(lick_window[1]))
        self.curve_pause.setData(x=np.array(pause[0]), y=np.array(pause[1]))
        self.curve_licks.setData(x=np.array(licks[0]), y=np.array(licks[1]))
        self.curve_reward.setData(x=np.array(reward[0]), y=np.array(reward[1]))

    def update_difficulty_plot_range(self):
        x_range = self.p1.viewRange()[0]
        self.p2.setXRange(x_range[0], x_range[1], padding=0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    plots = Plots()
    widget.show()
    sys.exit(app.exec_())
