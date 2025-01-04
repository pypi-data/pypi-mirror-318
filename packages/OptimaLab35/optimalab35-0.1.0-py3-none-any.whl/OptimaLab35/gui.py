import sys
import os
from datetime import datetime

from optima35.core import OptimaManager
from OptimaLab35.utils.utility import Utilities
from OptimaLab35.ui.main_window import Ui_MainWindow
from OptimaLab35.ui.exif_handler_window import ExifEditor
from OptimaLab35.ui.simple_dialog import SimpleDialog  # Import the SimpleDialog class
from OptimaLab35 import __version__

from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QMessageBox,
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QFileDialog,
    QHBoxLayout,
    QSpinBox,
)

class OptimaLab35(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(OptimaLab35, self).__init__()
        self.name = "OptimaLab35"
        self.version = __version__
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.o = OptimaManager()
        self.u = Utilities()
        self.u.program_configs()
        self.exif_file = os.path.expanduser("~/.config/OptimaLab35/exif.yaml")
        self.available_exif_data = None
        self.settings = {}
        self.setWindowTitle(f"{self.name} v{self.version}")
        self._default_ui_layout()
        self._define_gui_interaction()

        self.sd = SimpleDialog()
        self._change_statusbar(f"Using {self.o.name} v{self.o.version}", 5000)

    def _default_ui_layout(self):
        self.ui.png_quality_spinBox.setVisible(False)

    def _define_gui_interaction(self):
        self.ui.input_folder_button.clicked.connect(self._browse_input_folder)
        self.ui.output_folder_button.clicked.connect(self._browse_output_folder)
        self.ui.start_button.clicked.connect(self._process)
        self.ui.image_type.currentIndexChanged.connect(self._update_quality_options)

        self.ui.exif_checkbox.stateChanged.connect(
            lambda state: self._handle_checkbox_state(state, 2, self._populate_exif)
        )
        self.ui.tabWidget.currentChanged.connect(self._on_tab_changed)
        self.ui.edit_exif_button.clicked.connect(self._open_exif_editor)

        self.ui.actionInfo.triggered.connect(self._info_window)

    def _info_window(self):
        self.sd.show_dialog(f"{self.name} v{self.version}", f"{self.name} v{self.version} is a GUI for {self.o.name} (v{self.o.version})")

    def _process(self):
        self.ui.start_button.setEnabled(False)
        self._update_settings() # Get all user selected data
        input_folder_valid = os.path.exists(self.settings["input_folder"])
        output_folder_valid = os.path.exists(self.settings["output_folder"])
        if not input_folder_valid or not output_folder_valid:
            QMessageBox.warning(self, "Warning", f"Input location {input_folder_valid}\nOutput folder {output_folder_valid}...")
            return

        input_folder = self.settings["input_folder"]
        output_folder = self.settings["output_folder"]

        image_files = [
            f for f in os.listdir(input_folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
        ]
        i = 1
        for image_file in image_files:
            input_path = os.path.join(input_folder, image_file)
            if self.settings["new_file_names"] != False:
                image_name = self.u.append_number_to_name(self.settings["new_file_names"], i, len(image_files), self.settings["invert_image_order"])
            else:
                image_name = os.path.splitext(image_file)[0]
            output_path = os.path.join(output_folder, image_name)

            self.o.process_image(
                image_input_file = input_path,
                image_output_file = output_path,
                file_type = self.settings["file_format"],
                quality = self.settings["jpg_quality"],
                compressing = self.settings["png_compression"],
                optimize = self.ui.optimize_checkBox.isChecked(),
                resize = self.settings["resize"],
                watermark = self.settings["watermark"],
                font_size = self.settings["font_size"],
                grayscale = self.settings["grayscale"],
                brightness = self.settings["brightness"],
                contrast = self.settings["contrast"],
                dict_for_exif = self.user_selected_exif,
                gps = self.settings["gps"],
                copy_exif = self.settings["copy_exif"])
            self._handle_qprogressbar(i, len(image_files))
            i += 1

        QMessageBox.information(self, "Information", "Finished")
        self.ui.start_button.setEnabled(True)
        self.ui.progressBar.setValue(0)

    def _open_exif_editor(self):
        """Open the EXIF Editor."""
        self.exif_editor = ExifEditor(self.available_exif_data)
        self.exif_editor.exif_data_updated.connect(self._update_exif_data)
        self.exif_editor.show()

    def _update_exif_data(self, updated_exif_data):
        """Update the EXIF data."""
        self.exif_data = updated_exif_data
        self._populate_exif()

    def _handle_checkbox_state(self, state, desired_state, action):
        """Perform an action based on the checkbox state and a desired state. Have to use lambda when calling."""
        if state == desired_state:
            action()

    def _on_tab_changed(self, index):
        """Handle tab changes."""
        # chatgpt
        if index == 1:  # EXIF Tab
            self._handle_exif_file("read")
        elif index == 0:  # Main Tab
            self._handle_exif_file("write")

    def _handle_exif_file(self, do):
        if do == "read":
            self.available_exif_data = self.u.read_yaml(self.exif_file)
        elif do == "write":
            self.u.write_yaml(self.exif_file, self.available_exif_data)

    def _populate_exif(self):
        # partly chatGPT
        # Mapping of EXIF fields to comboboxes in the UI
        combo_mapping = {
            "make": self.ui.make_comboBox,
            "model": self.ui.model_comboBox,
            "lens": self.ui.lens_comboBox,
            "iso": self.ui.iso_comboBox,
            "image_description": self.ui.image_description_comboBox,
            "user_comment": self.ui.user_comment_comboBox,
            "artist": self.ui.artist_comboBox,
            "copyright_info": self.ui.copyright_info_comboBox,
        }
        self._populate_comboboxes(combo_mapping)

    def _populate_comboboxes(self, combo_mapping):
        """Populate comboboxes with EXIF data."""
        # ChatGPT
        for field, comboBox in combo_mapping.items():
            comboBox.clear()  # Clear existing items
            comboBox.addItems(map(str, self.available_exif_data.get(field, [])))

    def _update_quality_options(self):
            """Update visibility of quality settings based on selected format."""
            # ChatGPT
            selected_format = self.ui.image_type.currentText()
            # Hide all quality settings
            self.ui.png_quality_spinBox.setVisible(False)
            self.ui.jpg_quality_spinBox.setVisible(False)
            # Show relevant settings
            if selected_format == "jpg":
                self.ui.jpg_quality_spinBox.setVisible(True)
            elif selected_format == "webp":
                self.ui.jpg_quality_spinBox.setVisible(True)
            elif selected_format == "png":
                self.ui.png_quality_spinBox.setVisible(True)

    def _browse_input_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Input Folder")
        if folder:
            self.ui.input_path.setText(folder)

    def _browse_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.ui.output_path.setText(folder)

    def _change_statusbar(self, msg, timeout = 500):
        self.ui.statusBar.showMessage(msg, timeout)

    def _handle_qprogressbar(self, current, total):
        progress = int((100 / total) * current)
        self.ui.progressBar.setValue(progress)

    def _get_checkbox_value(self, checkbox, default=None):
        """Helper function to get the value of a checkbox or a default value."""
        return checkbox.isChecked() if checkbox else default

    def _get_spinbox_value(self, spinbox, default=None):
        """Helper function to get the value of a spinbox and handle empty input."""
        return int(spinbox.text()) if spinbox.text() else default

    def _get_combobox_value(self, combobox, default=None):
        """Helper function to get the value of a combobox."""
        return combobox.currentIndex() + 1 if combobox.currentIndex() != -1 else default

    def _get_text_value(self, lineedit, default=None):
        """Helper function to get the value of a text input field."""
        return lineedit.text() if lineedit.text() else default

    def _get_selected_exif(self):
        """Collect selected EXIF data and handle date and GPS if necessary."""
        selected_exif = self._collect_selected_exif() if self.ui.exif_checkbox.isChecked() else None
        if selected_exif:
            if self.ui.add_date_checkBox.isChecked():
                selected_exif["date_time_original"] = self._get_date()
        if self.ui.gps_checkBox.isChecked():
            self.settings["gps"] = [self.ui.lat_lineEdit.text(), self.ui.long_lineEdit.text()]
        else:
            self.settings["gps"] = None
        return selected_exif

    def _update_settings(self):
        """Update .settings from all GUI elements."""
        # General settings
        self.settings["input_folder"] = self._get_text_value(self.ui.input_path)
        self.settings["output_folder"] = self._get_text_value(self.ui.output_path)
        self.settings["file_format"] = self.ui.image_type.currentText()
        self.settings["jpg_quality"] = self._get_spinbox_value(self.ui.jpg_quality_spinBox)
        self.settings["png_compression"] = self._get_spinbox_value(self.ui.png_quality_spinBox)
        self.settings["invert_image_order"] = self._get_checkbox_value(self.ui.revert_checkbox)
        self.settings["grayscale"] = self._get_checkbox_value(self.ui.grayscale_checkBox)
        self.settings["copy_exif"] = self._get_checkbox_value(self.ui.exif_copy_checkBox)
        self.settings["own_exif"] = self._get_checkbox_value(self.ui.exif_checkbox)
        self.settings["font_size"] = self._get_combobox_value(self.ui.font_size_comboBox)
        self.settings["optimize"] = self._get_checkbox_value(self.ui.optimize_checkBox)
        self.settings["own_date"] = self._get_checkbox_value(self.ui.add_date_checkBox)

        # Conditional settings with logic
        self.settings["resize"] = self._get_spinbox_value(self.ui.resize_spinBox) if self.ui.resize_checkbox.isChecked() else None
        self.settings["brightness"] = self._get_spinbox_value(self.ui.brightness_spinBox) if self.ui.brightness_checkbox.isChecked() else None
        self.settings["contrast"] = self._get_spinbox_value(self.ui.contrast_spinBox) if self.ui.contrast_checkbox.isChecked() else None

        self.settings["new_file_names"] = self._get_text_value(self.ui.filename, False) if self.ui.rename_checkbox.isChecked() else False
        self.settings["watermark"] = self._get_text_value(self.ui.watermark_lineEdit) if self.ui.watermark_checkbox.isChecked() else None

        # Handle EXIF data selection
        if self.settings["own_exif"]:
            self.user_selected_exif = self._get_selected_exif()
        else:
            self.user_selected_exif = None
            self.settings["gps"] = None

    def _get_date(self):
        date_input = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        new_date = datetime.strptime(date_input, "%Y-%m-%d")
        return new_date.strftime("%Y:%m:%d 00:00:00")

    def _collect_selected_exif(self):
        user_data = {}
        user_data["make"] = self.ui.make_comboBox.currentText()
        user_data["model"] = self.ui.model_comboBox.currentText()
        user_data["lens"] = self.ui.lens_comboBox.currentText()
        user_data["iso"] = self.ui.iso_comboBox.currentText()
        user_data["image_description"] = self.ui.image_description_comboBox.currentText()
        user_data["user_comment"] = self.ui.user_comment_comboBox.currentText()
        user_data["artist"] = self.ui.artist_comboBox.currentText()
        user_data["copyright_info"] = self.ui.copyright_info_comboBox.currentText()
        user_data["software"] = f"{self.o.name} {self.o.version}"
        return user_data

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = OptimaLab35()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
