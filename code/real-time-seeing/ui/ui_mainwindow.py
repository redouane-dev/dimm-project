# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './code/real-time-seeing/ui/layout.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1032, 1046)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../index.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stars_capture = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stars_capture.sizePolicy().hasHeightForWidth())
        self.stars_capture.setSizePolicy(sizePolicy)
        self.stars_capture.setMinimumSize(QtCore.QSize(640, 480))
        self.stars_capture.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.stars_capture.setMouseTracking(True)
        self.stars_capture.setAutoFillBackground(False)
        self.stars_capture.setFrameShape(QtWidgets.QFrame.Box)
        self.stars_capture.setText("")
        self.stars_capture.setScaledContents(False)
        self.stars_capture.setObjectName("stars_capture")
        self.verticalLayout_3.addWidget(self.stars_capture)
        self.graphicsView = QtWidgets.QGraphicsView(self.widget_2)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_start = QtWidgets.QPushButton(self.widget)
        self.button_start.setEnabled(True)
        self.button_start.setCheckable(False)
        self.button_start.setChecked(False)
        self.button_start.setObjectName("button_start")
        self.verticalLayout_2.addWidget(self.button_start)
        self.button_settings = QtWidgets.QPushButton(self.widget)
        self.button_settings.setObjectName("button_settings")
        self.verticalLayout_2.addWidget(self.button_settings)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.button_simulation = QtWidgets.QPushButton(self.widget)
        self.button_simulation.setObjectName("button_simulation")
        self.verticalLayout_2.addWidget(self.button_simulation)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.button_import = QtWidgets.QPushButton(self.widget)
        self.button_import.setObjectName("button_import")
        self.verticalLayout_2.addWidget(self.button_import)
        self.button_export = QtWidgets.QPushButton(self.widget)
        self.button_export.setEnabled(False)
        self.button_export.setObjectName("button_export")
        self.verticalLayout_2.addWidget(self.button_export)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.button_pause = QtWidgets.QPushButton(self.widget)
        self.button_pause.setEnabled(False)
        self.button_pause.setMinimumSize(QtCore.QSize(0, 35))
        self.button_pause.setObjectName("button_pause")
        self.verticalLayout_2.addWidget(self.button_pause)
        self.enable_seeing = QtWidgets.QCheckBox(self.widget)
        self.enable_seeing.setChecked(True)
        self.enable_seeing.setObjectName("enable_seeing")
        self.verticalLayout_2.addWidget(self.enable_seeing)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.button_roi = QtWidgets.QPushButton(self.widget)
        self.button_roi.setObjectName("button_roi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.button_roi)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineedit_path = QtWidgets.QLineEdit(self.widget)
        self.lineedit_path.setObjectName("lineedit_path")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineedit_path)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineedit_filename = QtWidgets.QLineEdit(self.widget)
        self.lineedit_filename.setObjectName("lineedit_filename")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineedit_filename)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_5)
        self.label_threshold = QtWidgets.QLabel(self.widget)
        self.label_threshold.setObjectName("label_threshold")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_threshold)
        self.slider_threshold = QtWidgets.QSlider(self.widget)
        self.slider_threshold.setMaximum(255)
        self.slider_threshold.setProperty("value", 127)
        self.slider_threshold.setOrientation(QtCore.Qt.Horizontal)
        self.slider_threshold.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_threshold.setTickInterval(16)
        self.slider_threshold.setObjectName("slider_threshold")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.slider_threshold)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinbox_lambda = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_lambda.sizePolicy().hasHeightForWidth())
        self.spinbox_lambda.setSizePolicy(sizePolicy)
        self.spinbox_lambda.setDecimals(9)
        self.spinbox_lambda.setMaximum(999999999.999999)
        self.spinbox_lambda.setSingleStep(1.0)
        self.spinbox_lambda.setProperty("value", 0.5)
        self.spinbox_lambda.setObjectName("spinbox_lambda")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinbox_lambda)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinbox_b = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_b.sizePolicy().hasHeightForWidth())
        self.spinbox_b.setSizePolicy(sizePolicy)
        self.spinbox_b.setDecimals(3)
        self.spinbox_b.setMaximum(999999999.999)
        self.spinbox_b.setProperty("value", 100.0)
        self.spinbox_b.setObjectName("spinbox_b")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinbox_b)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinbox_d = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_d.sizePolicy().hasHeightForWidth())
        self.spinbox_d.setSizePolicy(sizePolicy)
        self.spinbox_d.setDecimals(3)
        self.spinbox_d.setMaximum(999999999.999)
        self.spinbox_d.setProperty("value", 100.0)
        self.spinbox_d.setObjectName("spinbox_d")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.spinbox_d)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinbox_focal = QtWidgets.QDoubleSpinBox(self.widget)
        self.spinbox_focal.setDecimals(9)
        self.spinbox_focal.setMaximum(999999999.999999)
        self.spinbox_focal.setObjectName("spinbox_focal")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.spinbox_focal)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinbox_pwidth = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_pwidth.sizePolicy().hasHeightForWidth())
        self.spinbox_pwidth.setSizePolicy(sizePolicy)
        self.spinbox_pwidth.setDecimals(9)
        self.spinbox_pwidth.setMaximum(999999999.999999)
        self.spinbox_pwidth.setObjectName("spinbox_pwidth")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.spinbox_pwidth)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinbox_pheight = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_pheight.sizePolicy().hasHeightForWidth())
        self.spinbox_pheight.setSizePolicy(sizePolicy)
        self.spinbox_pheight.setDecimals(9)
        self.spinbox_pheight.setMaximum(999999999.999999)
        self.spinbox_pheight.setObjectName("spinbox_pheight")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.spinbox_pheight)
        self.lineedit_star = QtWidgets.QLineEdit(self.widget)
        self.lineedit_star.setText("")
        self.lineedit_star.setObjectName("lineedit_star")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.lineedit_star)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.label_info = QtWidgets.QLabel(self.widget)
        self.label_info.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_info.setLineWidth(2)
        self.label_info.setText("")
        self.label_info.setScaledContents(False)
        self.label_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_info.setWordWrap(True)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_2.addWidget(self.label_info)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 22))
        self.menubar.setObjectName("menubar")
        self.menuStart = QtWidgets.QMenu(self.menubar)
        self.menuStart.setObjectName("menuStart")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionSelect_camera = QtWidgets.QAction(MainWindow)
        self.actionSelect_camera.setObjectName("actionSelect_camera")
        self.actionSimulation = QtWidgets.QAction(MainWindow)
        self.actionSimulation.setObjectName("actionSimulation")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHowTo = QtWidgets.QAction(MainWindow)
        self.actionHowTo.setObjectName("actionHowTo")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionImport_Video_File = QtWidgets.QAction(MainWindow)
        self.actionImport_Video_File.setObjectName("actionImport_Video_File")
        self.actionExport_to_Video_FIle = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Video_FIle.setObjectName("actionExport_to_Video_FIle")
        self.actionEnable_Seeing_Monitoring = QtWidgets.QAction(MainWindow)
        self.actionEnable_Seeing_Monitoring.setCheckable(True)
        self.actionEnable_Seeing_Monitoring.setObjectName("actionEnable_Seeing_Monitoring")
        self.menuStart.addAction(self.actionSelect_camera)
        self.menuStart.addAction(self.actionSimulation)
        self.menuStart.addAction(self.actionEnable_Seeing_Monitoring)
        self.menuStart.addSeparator()
        self.menuStart.addAction(self.actionImport_Video_File)
        self.menuStart.addAction(self.actionExport_to_Video_FIle)
        self.menuStart.addSeparator()
        self.menuStart.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHowTo)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuStart.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionSelect_camera.triggered.connect(self.button_start.click)
        self.actionSimulation.triggered.connect(self.button_simulation.click)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionEnable_Seeing_Monitoring.triggered.connect(self.enable_seeing.click)
        self.actionImport_Video_File.triggered.connect(self.button_import.click)
        self.actionExport_to_Video_FIle.triggered.connect(self.button_export.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seeing Monitor - CRAAG"))
        self.button_start.setToolTip(_translate("MainWindow", "<html><head/><body><p>Start camera and real-time seeing monitoring</p></body></html>"))
        self.button_start.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Start camera and real-time seeing monitoring</p></body></html>"))
        self.button_start.setText(_translate("MainWindow", "▶ Start"))
        self.button_settings.setText(_translate("MainWindow", "⚙Settings"))
        self.button_simulation.setToolTip(_translate("MainWindow", "<html><head/><body><p>Launch simulation with artificial observations</p></body></html>"))
        self.button_simulation.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Launch simulation with artificial observations</p></body></html>"))
        self.button_simulation.setText(_translate("MainWindow", "Simulation"))
        self.button_import.setText(_translate("MainWindow", "Import"))
        self.button_export.setText(_translate("MainWindow", "Export"))
        self.button_pause.setText(_translate("MainWindow", "⏸ Pause"))
        self.enable_seeing.setText(_translate("MainWindow", "Enable seeing monitoring"))
        self.button_roi.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press this button to select the Regions of Interest (where the two star projections are located)</p></body></html>"))
        self.button_roi.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Press this button to select the Regions of Interest (where the two star projections are located)</p></body></html>"))
        self.button_roi.setText(_translate("MainWindow", "Select ROI"))
        self.label_7.setText(_translate("MainWindow", "Saving file path"))
        self.label_8.setText(_translate("MainWindow", "Saving file name"))
        self.label_threshold.setText(_translate("MainWindow", "Pixel Threshold"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Wavelength in micrometers</p></body></html>"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Wavelength in micrometers</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Wavelength (µm)"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Apertures Separation in meters</p></body></html>"))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Apertures Separation in meters</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "B (Apert. Sep.)(mm)"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Apertures Diameter in meters</p></body></html>"))
        self.label_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Apertures Diameter in meters</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "D (Apert. Diam.)(mm)"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Focal Length in millimeters</p></body></html>"))
        self.label_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Focal Length in millimeters</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Focal Length (mm)"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pixel Width in micrometers</p></body></html>"))
        self.label_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Pixel Width in micrometers</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Pixel Width (µm)"))
        self.label_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pixel Height in micrometers</p></body></html>"))
        self.label_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Pixel Height in micrometers</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Pixel Height (µm)"))
        self.lineedit_star.setPlaceholderText(_translate("MainWindow", "Please type star name and characteristics"))
        self.menuStart.setTitle(_translate("MainWindow", "&Start"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionSelect_camera.setText(_translate("MainWindow", "Select &Camera and Start"))
        self.actionSelect_camera.setShortcut(_translate("MainWindow", "F5"))
        self.actionSimulation.setText(_translate("MainWindow", "Si&mulation"))
        self.actionSimulation.setShortcut(_translate("MainWindow", "F6"))
        self.actionExit.setText(_translate("MainWindow", "Exi&t"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionHowTo.setText(_translate("MainWindow", "&HowTo"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionImport_Video_File.setText(_translate("MainWindow", "&Import from Video"))
        self.actionImport_Video_File.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionExport_to_Video_FIle.setText(_translate("MainWindow", "E&xport to Video"))
        self.actionExport_to_Video_FIle.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionEnable_Seeing_Monitoring.setText(_translate("MainWindow", "&Enable Seeing Monitoring"))


