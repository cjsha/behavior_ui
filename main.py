from PyQt5 import QtWidgets
import sys
from sql.sql import Sql
from mouse.mouse import Mouse
from parameters.parameters import Parameters
from task.taskSettings import TaskSettings
from task.taskMain import TaskMain


# last-3) threads
# last-2) fix mySql timezone?
# last-1) figure out slot decorators and lambdas (more pythonic code?)
# last) follow pep8, fix naming convention

class Main:

    def __init__(self):
        self.sqlUi = QtWidgets.QMainWindow()
        self.sql = Sql(self.sqlUi)
        self.sql.mouse_toggled.connect(self.show_mouse)
        self.sql.parameters_toggled.connect(self.show_parameters)
        self.sql.task_toggled.connect(self.show_task_settings)

        attribute_placeholder = 1
        self.mouseUi = QtWidgets.QMainWindow()
        self.mouse = attribute_placeholder
        self.parametersUi = QtWidgets.QMainWindow()
        self.parameters = attribute_placeholder
        self.taskSettingsUi = QtWidgets.QMainWindow()
        self.task_settings = attribute_placeholder
        self.taskMainUi = QtWidgets.QWidget()
        self.task_main = attribute_placeholder

    def show_sql(self):
        self.mouseUi.close()
        self.parametersUi.close()
        self.taskSettingsUi.close()
        self.sqlUi.show()

    def show_mouse(self, sql_connection):
        self.mouse = Mouse(self.mouseUi, sql_connection)
        self.mouse.back_pressed.connect(self.show_sql)
        self.sqlUi.hide()
        self.mouseUi.show()

    def show_parameters(self, sql_connection):
        self.parameters = Parameters(self.parametersUi, sql_connection)
        self.parameters.back_pressed.connect(self.show_sql)
        self.sqlUi.hide()
        self.parametersUi.show()

    def show_plots(self):
        pass

    def show_task_settings(self, sql_connection):
        self.task_settings = TaskSettings(self.taskSettingsUi, sql_connection)
        self.task_settings.back_pressed.connect(self.show_sql)
        self.task_settings.open_task.connect(self.show_task)
        self.sqlUi.hide()
        self.taskSettingsUi.show()

    def show_task(self, session_num, session_suffix, sql_connection, com_connection,
                  cage_number, mouse_number, parameters, save_data):
        self.task_main = TaskMain(self.taskMainUi, session_num, session_suffix, sql_connection,
                                  com_connection, cage_number, mouse_number, parameters, save_data)
        self.taskSettingsUi.hide()
        self.taskMainUi.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show_sql()
    sys.exit(app.exec_())
