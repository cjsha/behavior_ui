from PyQt5 import QtCore, QtGui, QtWidgets
from .newMouseConfirmUi import Ui_NewMouseConfirm as NewMouseConfirmUi

class NewMouseConfirm(NewMouseConfirmUi, QtWidgets.QDialog):
  
    def __init__(self, widget):

        ## call init function from QWidget
        super().__init__()

        super().setupUi(widget)
        
        self.confirmation_button_box.accepted.connect(widget.accept)
        self.confirmation_button_box.rejected.connect(widget.reject)


    def pass_objects(self, cage, mouse_id, weight, birthday, breed, sex, misc):
        self.cageLabel2.setText(cage)
        self.mouseIdLabel2.setText(mouse_id)
        self.weightLabel2.setText(weight)
        self.birthdayLabel2.setText(birthday)
        self.breedLabel2.setText(breed)
        self.sexLabel2.setText(sex)
        self.miscTextBrowser.setText(misc)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = mouse(widget)
    widget.show()
    sys.exit(app.exec_())

