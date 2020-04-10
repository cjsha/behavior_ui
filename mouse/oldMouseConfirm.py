from PyQt5 import QtCore, QtGui, QtWidgets
from .oldMouseConfirmUi import Ui_OldMouseConfirm as OldMouseConfirmUi

class OldMouseConfirm(OldMouseConfirmUi, QtWidgets.QDialog):
  
    def __init__(self, widget):

        ## call init function from QWidget
        super().__init__()

        super().setupUi(widget)
        
        self.confirmation_button_box.accepted.connect(widget.accept)
        self.confirmation_button_box.rejected.connect(widget.reject)


    def pass_objects(self, mouse_identifier):
        self.which_mouse_label.setText(mouse_identifier)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = mouse(widget)
    widget.show()
    sys.exit(app.exec_())

