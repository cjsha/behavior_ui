# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameters\parametersUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_parameters(object):
    def setupUi(self, parameters):
        parameters.setObjectName("parameters")
        parameters.resize(334, 977)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(parameters.sizePolicy().hasHeightForWidth())
        parameters.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 28, 2, 1, 1)
        self.songs_per_block_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songs_per_block_spin_box.sizePolicy().hasHeightForWidth())
        self.songs_per_block_spin_box.setSizePolicy(sizePolicy)
        self.songs_per_block_spin_box.setMinimum(1)
        self.songs_per_block_spin_box.setMaximum(255)
        self.songs_per_block_spin_box.setProperty("value", 3)
        self.songs_per_block_spin_box.setObjectName("songs_per_block_spin_box")
        self.gridLayout_2.addWidget(self.songs_per_block_spin_box, 28, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 17, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 13, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 9, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 20, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 13, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 8, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 9, 2, 1, 1)
        self.downloadFromDatabase = QtWidgets.QPushButton(self.centralwidget)
        self.downloadFromDatabase.setObjectName("downloadFromDatabase")
        self.gridLayout_2.addWidget(self.downloadFromDatabase, 36, 0, 1, 3)
        self.submit_push_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_push_button.sizePolicy().hasHeightForWidth())
        self.submit_push_button.setSizePolicy(sizePolicy)
        self.submit_push_button.setObjectName("submit_push_button")
        self.gridLayout_2.addWidget(self.submit_push_button, 34, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 16, 0, 1, 1)
        self.min_divergence_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_divergence_spin_box.sizePolicy().hasHeightForWidth())
        self.min_divergence_spin_box.setSizePolicy(sizePolicy)
        self.min_divergence_spin_box.setMaximum(255)
        self.min_divergence_spin_box.setObjectName("min_divergence_spin_box")
        self.gridLayout_2.addWidget(self.min_divergence_spin_box, 12, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 0, 2, 1)
        self.tone4_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tone4_line_edit.setMaxLength(3)
        self.tone4_line_edit.setObjectName("tone4_line_edit")
        self.gridLayout_3.addWidget(self.tone4_line_edit, 1, 1, 1, 1)
        self.tone2_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tone2_line_edit.sizePolicy().hasHeightForWidth())
        self.tone2_line_edit.setSizePolicy(sizePolicy)
        self.tone2_line_edit.setMaxLength(3)
        self.tone2_line_edit.setObjectName("tone2_line_edit")
        self.gridLayout_3.addWidget(self.tone2_line_edit, 0, 2, 1, 1)
        self.tone3_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tone3_line_edit.setMaxLength(3)
        self.tone3_line_edit.setObjectName("tone3_line_edit")
        self.gridLayout_3.addWidget(self.tone3_line_edit, 0, 3, 1, 1)
        self.tone1_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tone1_line_edit.sizePolicy().hasHeightForWidth())
        self.tone1_line_edit.setSizePolicy(sizePolicy)
        self.tone1_line_edit.setMaxLength(3)
        self.tone1_line_edit.setObjectName("tone1_line_edit")
        self.gridLayout_3.addWidget(self.tone1_line_edit, 0, 1, 1, 1)
        self.tone6_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tone6_line_edit.setMaxLength(3)
        self.tone6_line_edit.setObjectName("tone6_line_edit")
        self.gridLayout_3.addWidget(self.tone6_line_edit, 1, 3, 1, 1)
        self.tone5_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tone5_line_edit.setMaxLength(3)
        self.tone5_line_edit.setObjectName("tone5_line_edit")
        self.gridLayout_3.addWidget(self.tone5_line_edit, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 32, 0, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 7, 0, 1, 1)
        self.licks_per_decision_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.licks_per_decision_spin_box.sizePolicy().hasHeightForWidth())
        self.licks_per_decision_spin_box.setSizePolicy(sizePolicy)
        self.licks_per_decision_spin_box.setMinimum(1)
        self.licks_per_decision_spin_box.setMaximum(255)
        self.licks_per_decision_spin_box.setObjectName("licks_per_decision_spin_box")
        self.gridLayout_2.addWidget(self.licks_per_decision_spin_box, 20, 1, 1, 1)
        self.punishment_air_double_spin_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.punishment_air_double_spin_box.sizePolicy().hasHeightForWidth())
        self.punishment_air_double_spin_box.setSizePolicy(sizePolicy)
        self.punishment_air_double_spin_box.setMaximum(10.0)
        self.punishment_air_double_spin_box.setSingleStep(0.01)
        self.punishment_air_double_spin_box.setObjectName("punishment_air_double_spin_box")
        self.gridLayout_2.addWidget(self.punishment_air_double_spin_box, 17, 1, 1, 1)
        self.max_divergence_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_divergence_spin_box.sizePolicy().hasHeightForWidth())
        self.max_divergence_spin_box.setSizePolicy(sizePolicy)
        self.max_divergence_spin_box.setMaximum(255)
        self.max_divergence_spin_box.setProperty("value", 1)
        self.max_divergence_spin_box.setObjectName("max_divergence_spin_box")
        self.gridLayout_2.addWidget(self.max_divergence_spin_box, 13, 1, 1, 1)
        self.drop_size_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drop_size_spin_box.sizePolicy().hasHeightForWidth())
        self.drop_size_spin_box.setSizePolicy(sizePolicy)
        self.drop_size_spin_box.setMinimum(1)
        self.drop_size_spin_box.setMaximum(255)
        self.drop_size_spin_box.setProperty("value", 7)
        self.drop_size_spin_box.setObjectName("drop_size_spin_box")
        self.gridLayout_2.addWidget(self.drop_size_spin_box, 18, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 18, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 8, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout.addWidget(self.label_21)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_line_edit.sizePolicy().hasHeightForWidth())
        self.name_line_edit.setSizePolicy(sizePolicy)
        self.name_line_edit.setObjectName("name_line_edit")
        self.horizontalLayout_3.addWidget(self.name_line_edit)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 3)
        self.tone_duration_double_spin_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tone_duration_double_spin_box.sizePolicy().hasHeightForWidth())
        self.tone_duration_double_spin_box.setSizePolicy(sizePolicy)
        self.tone_duration_double_spin_box.setMinimum(0.1)
        self.tone_duration_double_spin_box.setMaximum(5.0)
        self.tone_duration_double_spin_box.setSingleStep(0.01)
        self.tone_duration_double_spin_box.setProperty("value", 0.3)
        self.tone_duration_double_spin_box.setObjectName("tone_duration_double_spin_box")
        self.gridLayout_2.addWidget(self.tone_duration_double_spin_box, 8, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_6.addWidget(self.line_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 3)
        self.message_text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_text_browser.setObjectName("message_text_browser")
        self.gridLayout_2.addWidget(self.message_text_browser, 35, 0, 1, 3)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 10, 2, 1, 1)
        self.delay_duration_double_spin_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delay_duration_double_spin_box.sizePolicy().hasHeightForWidth())
        self.delay_duration_double_spin_box.setSizePolicy(sizePolicy)
        self.delay_duration_double_spin_box.setMinimum(1.0)
        self.delay_duration_double_spin_box.setMaximum(10.0)
        self.delay_duration_double_spin_box.setSingleStep(0.01)
        self.delay_duration_double_spin_box.setProperty("value", 3.0)
        self.delay_duration_double_spin_box.setObjectName("delay_duration_double_spin_box")
        self.gridLayout_2.addWidget(self.delay_duration_double_spin_box, 10, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 10, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_2.addWidget(self.label_25)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 14, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 33, 0, 1, 1)
        self.punishment_light_double_spin_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.punishment_light_double_spin_box.sizePolicy().hasHeightForWidth())
        self.punishment_light_double_spin_box.setSizePolicy(sizePolicy)
        self.punishment_light_double_spin_box.setMaximum(10.0)
        self.punishment_light_double_spin_box.setSingleStep(0.01)
        self.punishment_light_double_spin_box.setObjectName("punishment_light_double_spin_box")
        self.gridLayout_2.addWidget(self.punishment_light_double_spin_box, 16, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 3, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setObjectName("label_37")
        self.gridLayout_5.addWidget(self.label_37, 1, 0, 1, 1)
        self.incorrect_encouragement_trials_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.incorrect_encouragement_trials_spin_box.setMinimum(1)
        self.incorrect_encouragement_trials_spin_box.setMaximum(255)
        self.incorrect_encouragement_trials_spin_box.setObjectName("incorrect_encouragement_trials_spin_box")
        self.gridLayout_5.addWidget(self.incorrect_encouragement_trials_spin_box, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)
        self.correct_trials_label2 = QtWidgets.QLabel(self.centralwidget)
        self.correct_trials_label2.setObjectName("correct_trials_label2")
        self.gridLayout_5.addWidget(self.correct_trials_label2, 1, 2, 1, 1)
        self.random_encouragement_trials_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.random_encouragement_trials_spin_box.sizePolicy().hasHeightForWidth())
        self.random_encouragement_trials_spin_box.setSizePolicy(sizePolicy)
        self.random_encouragement_trials_spin_box.setMinimum(1)
        self.random_encouragement_trials_spin_box.setMaximum(255)
        self.random_encouragement_trials_spin_box.setObjectName("random_encouragement_trials_spin_box")
        self.gridLayout_5.addWidget(self.random_encouragement_trials_spin_box, 2, 1, 1, 1)
        self.coinflip_block_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.coinflip_block_spin_box.setMinimum(1)
        self.coinflip_block_spin_box.setMaximum(255)
        self.coinflip_block_spin_box.setProperty("value", 50)
        self.coinflip_block_spin_box.setObjectName("coinflip_block_spin_box")
        self.gridLayout_5.addWidget(self.coinflip_block_spin_box, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_34, 0, 0, 1, 1)
        self.alternate_block_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.alternate_block_spin_box.setMinimum(1)
        self.alternate_block_spin_box.setMaximum(255)
        self.alternate_block_spin_box.setObjectName("alternate_block_spin_box")
        self.gridLayout_5.addWidget(self.alternate_block_spin_box, 0, 1, 1, 1)
        self.correct_trials_label1 = QtWidgets.QLabel(self.centralwidget)
        self.correct_trials_label1.setObjectName("correct_trials_label1")
        self.gridLayout_5.addWidget(self.correct_trials_label1, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 31, 0, 1, 3)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.horizontalWidget)
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addWidget(self.horizontalWidget, 38, 0, 1, 4)
        self.song_volume_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.song_volume_spin_box.sizePolicy().hasHeightForWidth())
        self.song_volume_spin_box.setSizePolicy(sizePolicy)
        self.song_volume_spin_box.setMinimum(1)
        self.song_volume_spin_box.setMaximum(100)
        self.song_volume_spin_box.setProperty("value", 50)
        self.song_volume_spin_box.setObjectName("song_volume_spin_box")
        self.gridLayout_2.addWidget(self.song_volume_spin_box, 33, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 17, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 12, 0, 1, 1)
        self.back_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_push_button.setObjectName("back_push_button")
        self.gridLayout_2.addWidget(self.back_push_button, 37, 0, 1, 3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_5.addWidget(self.label_33)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_5.addWidget(self.line_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 11, 0, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_4.addWidget(self.label_27)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 19, 0, 1, 3)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 7, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 18, 0, 1, 1)
        self.between_tones_duration_double_spin_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.between_tones_duration_double_spin_box.sizePolicy().hasHeightForWidth())
        self.between_tones_duration_double_spin_box.setSizePolicy(sizePolicy)
        self.between_tones_duration_double_spin_box.setMinimum(0.0)
        self.between_tones_duration_double_spin_box.setMaximum(5.0)
        self.between_tones_duration_double_spin_box.setSingleStep(0.01)
        self.between_tones_duration_double_spin_box.setProperty("value", 0.5)
        self.between_tones_duration_double_spin_box.setObjectName("between_tones_duration_double_spin_box")
        self.gridLayout_2.addWidget(self.between_tones_duration_double_spin_box, 9, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 12, 2, 1, 1)
        self.lick_window_duration_double_spin_box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lick_window_duration_double_spin_box.sizePolicy().hasHeightForWidth())
        self.lick_window_duration_double_spin_box.setSizePolicy(sizePolicy)
        self.lick_window_duration_double_spin_box.setMinimum(1.0)
        self.lick_window_duration_double_spin_box.setMaximum(10.0)
        self.lick_window_duration_double_spin_box.setSingleStep(0.01)
        self.lick_window_duration_double_spin_box.setProperty("value", 2.0)
        self.lick_window_duration_double_spin_box.setObjectName("lick_window_duration_double_spin_box")
        self.gridLayout_2.addWidget(self.lick_window_duration_double_spin_box, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 16, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 20, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 28, 0, 1, 1)
        parameters.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parameters)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 21))
        self.menubar.setObjectName("menubar")
        parameters.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parameters)
        self.statusbar.setObjectName("statusbar")
        parameters.setStatusBar(self.statusbar)

        self.retranslateUi(parameters)
        QtCore.QMetaObject.connectSlotsByName(parameters)

    def retranslateUi(self, parameters):
        _translate = QtCore.QCoreApplication.translate
        parameters.setWindowTitle(_translate("parameters", "MainWindow"))
        self.label_2.setText(_translate("parameters", "songs"))
        self.label_10.setText(_translate("parameters", "seconds"))
        self.label_23.setText(_translate("parameters", "Maximum Divergence"))
        self.label_16.setText(_translate("parameters", "Duration Between Tones:"))
        self.label_6.setText(_translate("parameters", "licks"))
        self.label_36.setText(_translate("parameters", "1/2 steps"))
        self.label_15.setText(_translate("parameters", "Tone Duration:"))
        self.label_31.setText(_translate("parameters", "seconds"))
        self.downloadFromDatabase.setText(_translate("parameters", "List Sets of Behavior Task Parameters in Database"))
        self.submit_push_button.setText(_translate("parameters", "Submit"))
        self.label_7.setText(_translate("parameters", "Punishment Light:"))
        self.label_24.setText(_translate("parameters", "Template Song:"))
        self.label_17.setText(_translate("parameters", "Lick Window Duration:"))
        self.label_38.setText(_translate("parameters", "uL"))
        self.label_30.setText(_translate("parameters", "seconds"))
        self.label_21.setText(_translate("parameters", "Trial Structure:"))
        self.label.setText(_translate("parameters", "Name:"))
        self.label_12.setText(_translate("parameters", "Mouse Behavior Task Parameters:"))
        self.label_29.setText(_translate("parameters", "seconds"))
        self.label_14.setText(_translate("parameters", "Delay Duration:"))
        self.label_25.setText(_translate("parameters", "Positive/Negative Feedback:"))
        self.label_3.setText(_translate("parameters", "Song Volume:"))
        self.label_19.setText(_translate("parameters", "percent"))
        self.label_37.setText(_translate("parameters", "Flip Block Chance:"))
        self.label_18.setText(_translate("parameters", "Encouragement Drop After:"))
        self.correct_trials_label2.setText(_translate("parameters", "percent"))
        self.label_20.setText(_translate("parameters", "incorrect trials"))
        self.label_4.setText(_translate("parameters", "Encouragement Drop Chance:"))
        self.label_34.setText(_translate("parameters", "Flip Block After:"))
        self.correct_trials_label1.setText(_translate("parameters", "correct trial(s)"))
        self.label_9.setText(_translate("parameters", "Punishment Air:"))
        self.label_22.setText(_translate("parameters", "Minimum Divergence:"))
        self.back_push_button.setText(_translate("parameters", "Back"))
        self.label_33.setText(_translate("parameters", "Nontemplate Trial Divergence Range:"))
        self.label_27.setText(_translate("parameters", "Training/Miscellaneous:"))
        self.label_32.setText(_translate("parameters", "seconds"))
        self.label_26.setText(_translate("parameters", "Drop Size:"))
        self.label_35.setText(_translate("parameters", "1/2 steps"))
        self.label_8.setText(_translate("parameters", "seconds"))
        self.label_5.setText(_translate("parameters", "Licks Per Decision:"))
        self.label_11.setText(_translate("parameters", "Songs Per Block:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    parameters = QtWidgets.QMainWindow()
    ui = Ui_parameters()
    ui.setupUi(parameters)
    parameters.show()
    sys.exit(app.exec_())
