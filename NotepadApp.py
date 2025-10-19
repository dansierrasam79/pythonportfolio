import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox, QLabel, QListWidget
)
from PyQt5.QtCore import Qt

class NotepadApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Notepad")
        self.setGeometry(600, 300, 700, 500)
        self.current_file = None
        self.files_directory = os.path.join(os.getcwd(), "notes")
        os.makedirs(self.files_directory, exist_ok=True)

        self.init_ui()
        self.load_file_list()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Left panel: File list and buttons
        left_panel = QVBoxLayout()
        self.file_list = QListWidget()
        self.file_list.itemClicked.connect(self.load_selected_file)

        btn_new = QPushButton("New File")
        btn_new.clicked.connect(self.new_file)

        btn_delete = QPushButton("Delete File")
        btn_delete.clicked.connect(self.delete_file)

        btn_refresh = QPushButton("Refresh List")
        btn_refresh.clicked.connect(self.load_file_list)

        left_panel.addWidget(QLabel("Files:"))
        left_panel.addWidget(self.file_list)
        left_panel.addWidget(btn_new)
        left_panel.addWidget(btn_delete)
        left_panel.addWidget(btn_refresh)

        # Right panel: Text editor and save button
        right_panel = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Create or open a text file...")

        btn_save = QPushButton("Save")
        btn_save.clicked.connect(self.save_file)

        right_panel.addWidget(self.text_edit)
        right_panel.addWidget(btn_save)

        main_layout.addLayout(left_panel, 1)
        main_layout.addLayout(right_panel, 3)

        self.setLayout(main_layout)

    def load_file_list(self):
        self.file_list.clear()
        try:
            files = [f for f in os.listdir(self.files_directory) if f.endswith(".txt")]
            self.file_list.addItems(files)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load file list:\n{e}")

    def load_selected_file(self, item):
        filename = item.text()
        filepath = os.path.join(self.files_directory, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_edit.setPlainText(content)
            self.current_file = filepath
            self.setWindowTitle(f"PyQt Notepad - {filename}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load file:\n{e}")

    def new_file(self):
        self.text_edit.clear()
        self.current_file = None
        self.setWindowTitle("PyQt Notepad - New File")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
                QMessageBox.information(self, "Saved", "File saved successfully.")
                self.load_file_list()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save file:\n{e}")
        else:
            # Save as new file
            filename, _ = QFileDialog.getSaveFileName(
                self, "Save File", self.files_directory, "Text Files (*.txt)"
            )
            if filename:
                # Ensure extension
                if not filename.endswith(".txt"):
                    filename += ".txt"
                try:
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(self.text_edit.toPlainText())
                    self.current_file = filename
                    self.setWindowTitle(f"PyQt Notepad - {os.path.basename(filename)}")
                    QMessageBox.information(self, "Saved", "File saved successfully.")
                    self.load_file_list()
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to save file:\n{e}")

    def delete_file(self):
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Delete File", "Please select a file to delete.")
            return

        filename = selected_items[0].text()
        filepath = os.path.join(self.files_directory, filename)

        reply = QMessageBox.question(
            self, "Delete File",
            f"Are you sure you want to delete '{filename}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                os.remove(filepath)
                QMessageBox.information(self, "Deleted", f"File '{filename}' deleted.")
                self.load_file_list()
                # Clear editor if deleted file was open
                if self.current_file == filepath:
                    self.text_edit.clear()
                    self.current_file = None
                    self.setWindowTitle("PyQt Notepad")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to delete file:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotepadApp()
    window.show()
    sys.exit(app.exec_())
