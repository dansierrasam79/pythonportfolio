import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt5.QtCore import Qt

DB_NAME = "contacts.db"

class ContactsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contacts App")
        self.setGeometry(600, 300, 600, 400)
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()
        self.init_ui()
        self.load_contacts()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def init_ui(self):
        layout = QVBoxLayout()

        # Form to add/edit contacts
        form_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(self.email_input)

        layout.addLayout(form_layout)

        # Buttons for add, update, delete
        btn_layout = QHBoxLayout()

        self.btn_add = QPushButton("Add Contact")
        self.btn_add.clicked.connect(self.add_contact)

        self.btn_update = QPushButton("Update Contact")
        self.btn_update.clicked.connect(self.update_contact)
        self.btn_update.setEnabled(False)

        self.btn_delete = QPushButton("Delete Contact")
        self.btn_delete.clicked.connect(self.delete_contact)
        self.btn_delete.setEnabled(False)

        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_delete)

        layout.addLayout(btn_layout)

        # Table to display contacts
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.hideColumn(0)  # Hide ID column

        self.table.cellClicked.connect(self.load_contact_into_form)

        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_contacts(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacts ORDER BY name")
        rows = cursor.fetchall()
        self.table.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                if col_idx == 0:  # ID column
                    item.setFlags(Qt.ItemFlag.NoItemFlags)  # Make ID not selectable/editable
                self.table.setItem(row_idx, col_idx, item)

        self.clear_form()
        self.btn_update.setEnabled(False)
        self.btn_delete.setEnabled(False)

    def clear_form(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.table.clearSelection()

    def add_contact(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Validation Error", "Name cannot be empty.")
            return

        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email)
        )
        self.conn.commit()
        self.load_contacts()
        QMessageBox.information(self, "Success", "Contact added successfully.")

    def load_contact_into_form(self, row, column):
        self.selected_contact_id = int(self.table.item(row, 0).text())
        self.name_input.setText(self.table.item(row, 1).text())
        self.phone_input.setText(self.table.item(row, 2).text())
        self.email_input.setText(self.table.item(row, 3).text())

        self.btn_update.setEnabled(True)
        self.btn_delete.setEnabled(True)

    def update_contact(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Validation Error", "Name cannot be empty.")
            return

        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
            (name, phone, email, self.selected_contact_id)
        )
        self.conn.commit()
        self.load_contacts()
        QMessageBox.information(self, "Success", "Contact updated successfully.")

    def delete_contact(self):
        confirm = QMessageBox.question(
            self, "Delete Contact",
            "Are you sure you want to delete this contact?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM contacts WHERE id=?", (self.selected_contact_id,))
            self.conn.commit()
            self.load_contacts()
            QMessageBox.information(self, "Deleted", "Contact deleted successfully.")

    def closeEvent(self, event):
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactsApp()
    window.show()
    sys.exit(app.exec_())
