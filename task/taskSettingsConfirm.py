from PyQt5 import QtWidgets
from .taskSettingsConfirmUi import Ui_TaskSettingsConfirm as TaskSettingConfirmUi


class TaskSettingsConfirm(TaskSettingConfirmUi, QtWidgets.QDialog):

    def __init__(self, widget):
        # call init function from QWidget
        super().__init__()

        super().setupUi(widget)

        self.confirmation_button_box.accepted.connect(widget.accept)
        self.confirmation_button_box.rejected.connect(widget.reject)

    def pass_objects(self, com_port, parameters, mouse_identifier, mass):
        self.com_port_label.setText(com_port)
        self.parameters_label.setText(parameters)
        self.mouse_label.setText(mouse_identifier)
        self.mass_label.setText(mass)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    ui = TaskSettingsConfirm(widget)
    widget.show()
    sys.exit(app.exec_())
