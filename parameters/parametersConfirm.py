from PyQt5 import QtCore, QtGui, QtWidgets
from .parametersConfirmUi import Ui_parametersConfirm as ParametersConfirmUi

class ParametersConfirm(ParametersConfirmUi, QtWidgets.QDialog):
  
    def __init__(self, widget):

        ## call init function from QWidget
        super().__init__()

        super().setupUi(widget)
        
        self.confirmation_button_box.accepted.connect(widget.accept)
        self.confirmation_button_box.rejected.connect(widget.reject)


    def pass_objects(self, name, lick_window, tone,
                     between_tones, delay_duration,
                     min_div, max_div,
                     punish_light, punish_air, drop_size,
                     licks_per_decision, songs_per_block,
                     alternate_block, coinflip_block,
                     random_encourage, incorrect_encourage,
                     template_song, song_volume):
        self.name_label.setText(str(name))
        self.lick_window_duration_label.setText(str(lick_window))
        self.tone_duration_label.setText(str(tone))
        self.between_tones_duration_label.setText(str(between_tones))
        self.min_divergence_label.setText(str(min_div))
        self.max_divergence_label.setText(str(max_div))
        self.punishment_light_label.setText(str(punish_light))
        self.punishment_air_label.setText(str(punish_air))
        self.drop_size_label.setText(str(delay_duration))
        self.delay_duration_label.setText(str(drop_size))
        self.licks_per_decision_label.setText(str(licks_per_decision))
        self.songs_per_block_label.setText(str(songs_per_block))
        self.alternate_block_label.setText(str(alternate_block))
        self.coinflip_block_label.setText(str(coinflip_block))
        self.random_encouragement_trials_label.setText(str(random_encourage))
        self.incorrect_encouragement_trials_label.setText(str(incorrect_encourage))
        self.template_song_label.setText(str(template_song))
        self.song_volume_label.setText(str(song_volume))

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = mouse(widget)
    widget.show()
    sys.exit(app.exec_())

