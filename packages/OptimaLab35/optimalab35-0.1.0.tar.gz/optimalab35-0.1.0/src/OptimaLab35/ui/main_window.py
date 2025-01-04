# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 708)
        MainWindow.setMinimumSize(QSize(350, 677))
        MainWindow.setMaximumSize(QSize(500, 1000))
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(500, 16777215))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_10 = QVBoxLayout(self.tab_1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.folder_group = QFrame(self.tab_1)
        self.folder_group.setObjectName(u"folder_group")
        self.folder_group.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_5 = QGridLayout(self.folder_group)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.input_path = QLineEdit(self.folder_group)
        self.input_path.setObjectName(u"input_path")

        self.gridLayout_5.addWidget(self.input_path, 0, 0, 1, 1)

        self.output_path = QLineEdit(self.folder_group)
        self.output_path.setObjectName(u"output_path")

        self.gridLayout_5.addWidget(self.output_path, 0, 1, 1, 1)

        self.input_folder_button = QPushButton(self.folder_group)
        self.input_folder_button.setObjectName(u"input_folder_button")

        self.gridLayout_5.addWidget(self.input_folder_button, 1, 0, 1, 1)

        self.output_folder_button = QPushButton(self.folder_group)
        self.output_folder_button.setObjectName(u"output_folder_button")

        self.gridLayout_5.addWidget(self.output_folder_button, 1, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.folder_group)

        self.groupBox = QGroupBox(self.tab_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.resize_checkbox = QCheckBox(self.groupBox)
        self.resize_checkbox.setObjectName(u"resize_checkbox")

        self.gridLayout_4.addWidget(self.resize_checkbox, 0, 0, 1, 1)

        self.resize_spinBox = QSpinBox(self.groupBox)
        self.resize_spinBox.setObjectName(u"resize_spinBox")
        self.resize_spinBox.setEnabled(False)
        self.resize_spinBox.setMinimum(1)
        self.resize_spinBox.setMaximum(200)
        self.resize_spinBox.setSingleStep(1)
        self.resize_spinBox.setValue(80)

        self.gridLayout_4.addWidget(self.resize_spinBox, 0, 1, 1, 1)

        self.image_type = QComboBox(self.groupBox)
        self.image_type.addItem(u"jpg")
        self.image_type.addItem(u"png")
        self.image_type.addItem(u"webp")
        self.image_type.setObjectName(u"image_type")

        self.gridLayout_4.addWidget(self.image_type, 1, 0, 1, 1)

        self.jpg_quality_spinBox = QSpinBox(self.groupBox)
        self.jpg_quality_spinBox.setObjectName(u"jpg_quality_spinBox")
        self.jpg_quality_spinBox.setMinimum(1)
        self.jpg_quality_spinBox.setMaximum(100)
        self.jpg_quality_spinBox.setValue(80)

        self.gridLayout_4.addWidget(self.jpg_quality_spinBox, 1, 1, 1, 1)

        self.png_quality_spinBox = QSpinBox(self.groupBox)
        self.png_quality_spinBox.setObjectName(u"png_quality_spinBox")
        self.png_quality_spinBox.setEnabled(True)
        self.png_quality_spinBox.setMinimum(1)
        self.png_quality_spinBox.setMaximum(9)
        self.png_quality_spinBox.setValue(6)

        self.gridLayout_4.addWidget(self.png_quality_spinBox, 1, 2, 1, 1)

        self.optimize_checkBox = QCheckBox(self.groupBox)
        self.optimize_checkBox.setObjectName(u"optimize_checkBox")

        self.gridLayout_4.addWidget(self.optimize_checkBox, 0, 2, 1, 1)

        self.png_quality_spinBox.raise_()
        self.resize_checkbox.raise_()
        self.resize_spinBox.raise_()
        self.image_type.raise_()
        self.jpg_quality_spinBox.raise_()
        self.optimize_checkBox.raise_()

        self.verticalLayout_10.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.watermark_lineEdit = QLineEdit(self.groupBox_2)
        self.watermark_lineEdit.setObjectName(u"watermark_lineEdit")
        self.watermark_lineEdit.setEnabled(False)

        self.gridLayout_3.addWidget(self.watermark_lineEdit, 3, 0, 1, 3)

        self.brightness_checkbox = QCheckBox(self.groupBox_2)
        self.brightness_checkbox.setObjectName(u"brightness_checkbox")

        self.gridLayout_3.addWidget(self.brightness_checkbox, 0, 0, 1, 1)

        self.grayscale_checkBox = QCheckBox(self.groupBox_2)
        self.grayscale_checkBox.setObjectName(u"grayscale_checkBox")

        self.gridLayout_3.addWidget(self.grayscale_checkBox, 0, 2, 1, 1)

        self.contrast_spinBox = QSpinBox(self.groupBox_2)
        self.contrast_spinBox.setObjectName(u"contrast_spinBox")
        self.contrast_spinBox.setEnabled(False)
        self.contrast_spinBox.setMinimum(-100)
        self.contrast_spinBox.setMaximum(100)
        self.contrast_spinBox.setValue(10)

        self.gridLayout_3.addWidget(self.contrast_spinBox, 1, 1, 1, 1)

        self.watermark_checkbox = QCheckBox(self.groupBox_2)
        self.watermark_checkbox.setObjectName(u"watermark_checkbox")

        self.gridLayout_3.addWidget(self.watermark_checkbox, 2, 0, 1, 1)

        self.brightness_spinBox = QSpinBox(self.groupBox_2)
        self.brightness_spinBox.setObjectName(u"brightness_spinBox")
        self.brightness_spinBox.setEnabled(False)
        self.brightness_spinBox.setMinimum(-100)
        self.brightness_spinBox.setMaximum(100)
        self.brightness_spinBox.setValue(-10)

        self.gridLayout_3.addWidget(self.brightness_spinBox, 0, 1, 1, 1)

        self.contrast_checkbox = QCheckBox(self.groupBox_2)
        self.contrast_checkbox.setObjectName(u"contrast_checkbox")

        self.gridLayout_3.addWidget(self.contrast_checkbox, 1, 0, 1, 1)

        self.font_size_comboBox = QComboBox(self.groupBox_2)
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.setObjectName(u"font_size_comboBox")

        self.gridLayout_3.addWidget(self.font_size_comboBox, 2, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.rename_group = QGroupBox(self.tab_1)
        self.rename_group.setObjectName(u"rename_group")
        self.rename_group.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_6 = QGridLayout(self.rename_group)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.rename_checkbox = QCheckBox(self.rename_group)
        self.rename_checkbox.setObjectName(u"rename_checkbox")

        self.gridLayout_6.addWidget(self.rename_checkbox, 0, 0, 1, 1)

        self.revert_checkbox = QCheckBox(self.rename_group)
        self.revert_checkbox.setObjectName(u"revert_checkbox")

        self.gridLayout_6.addWidget(self.revert_checkbox, 0, 1, 1, 1)

        self.filename = QLineEdit(self.rename_group)
        self.filename.setObjectName(u"filename")
        self.filename.setEnabled(False)

        self.gridLayout_6.addWidget(self.filename, 1, 0, 1, 2)


        self.verticalLayout_10.addWidget(self.rename_group)

        self.widget_9 = QWidget(self.tab_1)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(400, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressBar = QProgressBar(self.widget_9)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.start_button = QPushButton(self.widget_9)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.start_button)


        self.verticalLayout_10.addWidget(self.widget_9)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.exif_group = QGroupBox(self.tab_2)
        self.exif_group.setObjectName(u"exif_group")
        self.horizontalLayout = QHBoxLayout(self.exif_group)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exif_checkbox = QCheckBox(self.exif_group)
        self.exif_checkbox.setObjectName(u"exif_checkbox")
        self.exif_checkbox.setEnabled(True)

        self.horizontalLayout.addWidget(self.exif_checkbox)

        self.exif_copy_checkBox = QCheckBox(self.exif_group)
        self.exif_copy_checkBox.setObjectName(u"exif_copy_checkBox")

        self.horizontalLayout.addWidget(self.exif_copy_checkBox)

        self.edit_exif_button = QPushButton(self.exif_group)
        self.edit_exif_button.setObjectName(u"edit_exif_button")
        self.edit_exif_button.setEnabled(False)

        self.horizontalLayout.addWidget(self.edit_exif_button)


        self.verticalLayout_9.addWidget(self.exif_group)

        self.exif_options_group = QGroupBox(self.tab_2)
        self.exif_options_group.setObjectName(u"exif_options_group")
        self.exif_options_group.setEnabled(False)
        self.gridLayout_7 = QGridLayout(self.exif_options_group)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_7 = QWidget(self.exif_options_group)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.artist_comboBox = QComboBox(self.widget_7)
        self.artist_comboBox.setObjectName(u"artist_comboBox")

        self.verticalLayout_7.addWidget(self.artist_comboBox)


        self.gridLayout_7.addWidget(self.widget_7, 3, 0, 1, 1)

        self.widget_4 = QWidget(self.exif_options_group)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.iso_comboBox = QComboBox(self.widget_4)
        self.iso_comboBox.setObjectName(u"iso_comboBox")

        self.verticalLayout_4.addWidget(self.iso_comboBox)


        self.gridLayout_7.addWidget(self.widget_4, 1, 1, 1, 1)

        self.widget_6 = QWidget(self.exif_options_group)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.user_comment_comboBox = QComboBox(self.widget_6)
        self.user_comment_comboBox.setObjectName(u"user_comment_comboBox")

        self.verticalLayout_6.addWidget(self.user_comment_comboBox)


        self.gridLayout_7.addWidget(self.widget_6, 2, 1, 1, 1)

        self.widget_2 = QWidget(self.exif_options_group)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lens_comboBox = QComboBox(self.widget_2)
        self.lens_comboBox.setObjectName(u"lens_comboBox")

        self.verticalLayout_2.addWidget(self.lens_comboBox)


        self.gridLayout_7.addWidget(self.widget_2, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.exif_options_group)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.image_description_comboBox = QComboBox(self.widget_5)
        self.image_description_comboBox.setObjectName(u"image_description_comboBox")

        self.verticalLayout_5.addWidget(self.image_description_comboBox)


        self.gridLayout_7.addWidget(self.widget_5, 2, 0, 1, 1)

        self.widget = QWidget(self.exif_options_group)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.make_comboBox = QComboBox(self.widget)
        self.make_comboBox.setObjectName(u"make_comboBox")

        self.verticalLayout.addWidget(self.make_comboBox)


        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.exif_options_group)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.model_comboBox = QComboBox(self.widget_3)
        self.model_comboBox.setObjectName(u"model_comboBox")

        self.verticalLayout_3.addWidget(self.model_comboBox)


        self.gridLayout_7.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget_8 = QWidget(self.exif_options_group)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_8 = QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.copyright_info_comboBox = QComboBox(self.widget_8)
        self.copyright_info_comboBox.setObjectName(u"copyright_info_comboBox")

        self.verticalLayout_8.addWidget(self.copyright_info_comboBox)


        self.gridLayout_7.addWidget(self.widget_8, 3, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.exif_options_group)

        self.gps_groupBox = QGroupBox(self.tab_2)
        self.gps_groupBox.setObjectName(u"gps_groupBox")
        self.gps_groupBox.setEnabled(False)
        self.horizontalLayout_4 = QHBoxLayout(self.gps_groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gps_checkBox = QCheckBox(self.gps_groupBox)
        self.gps_checkBox.setObjectName(u"gps_checkBox")

        self.horizontalLayout_4.addWidget(self.gps_checkBox)

        self.lat_lineEdit = QLineEdit(self.gps_groupBox)
        self.lat_lineEdit.setObjectName(u"lat_lineEdit")
        self.lat_lineEdit.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.lat_lineEdit)

        self.long_lineEdit = QLineEdit(self.gps_groupBox)
        self.long_lineEdit.setObjectName(u"long_lineEdit")
        self.long_lineEdit.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.long_lineEdit)


        self.verticalLayout_9.addWidget(self.gps_groupBox)

        self.date_groupBox = QGroupBox(self.tab_2)
        self.date_groupBox.setObjectName(u"date_groupBox")
        self.date_groupBox.setEnabled(False)
        self.horizontalLayout_2 = QHBoxLayout(self.date_groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_date_checkBox = QCheckBox(self.date_groupBox)
        self.add_date_checkBox.setObjectName(u"add_date_checkBox")

        self.horizontalLayout_2.addWidget(self.add_date_checkBox)

        self.dateEdit = QDateEdit(self.date_groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setEnabled(False)
        self.dateEdit.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_2.addWidget(self.dateEdit)


        self.verticalLayout_9.addWidget(self.date_groupBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 450, 27))
        self.menuInfo = QMenu(self.menuBar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuInfo.menuAction())
        self.menuInfo.addAction(self.actionInfo)

        self.retranslateUi(MainWindow)
        self.resize_checkbox.toggled.connect(self.resize_spinBox.setEnabled)
        self.brightness_checkbox.toggled.connect(self.brightness_spinBox.setEnabled)
        self.contrast_checkbox.toggled.connect(self.contrast_spinBox.setEnabled)
        self.watermark_checkbox.toggled.connect(self.watermark_lineEdit.setEnabled)
        self.rename_checkbox.toggled.connect(self.filename.setEnabled)
        self.exif_checkbox.toggled.connect(self.exif_options_group.setEnabled)
        self.exif_checkbox.toggled.connect(self.exif_copy_checkBox.setDisabled)
        self.exif_copy_checkBox.toggled.connect(self.exif_checkbox.setDisabled)
        self.exif_checkbox.toggled.connect(self.edit_exif_button.setEnabled)
        self.add_date_checkBox.toggled.connect(self.dateEdit.setEnabled)
        self.exif_checkbox.toggled.connect(self.date_groupBox.setEnabled)
        self.exif_checkbox.toggled.connect(self.gps_groupBox.setEnabled)
        self.gps_checkBox.toggled.connect(self.lat_lineEdit.setEnabled)
        self.gps_checkBox.toggled.connect(self.long_lineEdit.setEnabled)

        self.tabWidget.setCurrentIndex(0)
        self.font_size_comboBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OPTIMA-35", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.input_path.setText("")
        self.input_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter input folder", None))
        self.output_path.setText("")
        self.output_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter output folder", None))
        self.input_folder_button.setText(QCoreApplication.translate("MainWindow", u"input", None))
        self.output_folder_button.setText(QCoreApplication.translate("MainWindow", u"output", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Essential group", None))
        self.resize_checkbox.setText(QCoreApplication.translate("MainWindow", u"Resize", None))

        self.optimize_checkBox.setText(QCoreApplication.translate("MainWindow", u"optimize", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Extra stuff", None))
        self.watermark_lineEdit.setText("")
        self.watermark_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Watermark", None))
        self.brightness_checkbox.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.grayscale_checkBox.setText(QCoreApplication.translate("MainWindow", u"Grayscale", None))
        self.watermark_checkbox.setText(QCoreApplication.translate("MainWindow", u"Watermark", None))
        self.contrast_checkbox.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.font_size_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Tiny", None))
        self.font_size_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Small", None))
        self.font_size_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.font_size_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Large", None))
        self.font_size_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Huge", None))

        self.font_size_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.rename_group.setTitle(QCoreApplication.translate("MainWindow", u"files", None))
        self.rename_checkbox.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.revert_checkbox.setText(QCoreApplication.translate("MainWindow", u"Revert order", None))
        self.filename.setText("")
        self.filename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter file name", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Main", None))
        self.exif_group.setTitle(QCoreApplication.translate("MainWindow", u"EXIF EXPERIMENTAL", None))
        self.exif_checkbox.setText(QCoreApplication.translate("MainWindow", u"own exif", None))
        self.exif_copy_checkBox.setText(QCoreApplication.translate("MainWindow", u"copy exif", None))
        self.edit_exif_button.setText(QCoreApplication.translate("MainWindow", u"edit exif", None))
        self.exif_options_group.setTitle(QCoreApplication.translate("MainWindow", u"Must", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Scanner", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lens", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Film", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Make", None))
        self.make_comboBox.setCurrentText("")
        self.make_comboBox.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Copyright", None))
        self.gps_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.gps_checkBox.setText(QCoreApplication.translate("MainWindow", u"add gps", None))
        self.lat_lineEdit.setText("")
        self.lat_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"latitude [S, N]", None))
        self.long_lineEdit.setText("")
        self.long_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"longitude [W, E]", None))
        self.date_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Optional", None))
        self.add_date_checkBox.setText(QCoreApplication.translate("MainWindow", u"add date", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"EXIF", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

