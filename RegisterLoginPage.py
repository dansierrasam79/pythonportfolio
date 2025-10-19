# I really like PyQt over Tkinter... just a preference!
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QStackedWidget
)
from PyQt5.QtCore import Qt

class RegisterPage(QWidget):
    def __init__(self, switch_to_login_callback, user_db):
        super().__init__()
        self.switch_to_login = switch_to_login_callback
        self.user_db = user_db
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("<h2>Register</h2>")
        self.label.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.register_btn = QPushButton("Register")
        self.register_btn.clicked.connect(self.register)

        self.login_switch_btn = QPushButton("Already have an account? Login")
        self.login_switch_btn.clicked.connect(self.switch_to_login)

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_btn)
        layout.addWidget(self.login_switch_btn)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter username and password.")
            return

        if username in self.user_db:
            QMessageBox.warning(self, "Error", "Username already exists.")
            return

        self.user_db[username] = password
        QMessageBox.information(self, "Success", "Registration successful!")
        self.switch_to_login()


class LoginPage(QWidget):
    def __init__(self, switch_to_register_callback, user_db):
        super().__init__()
        self.switch_to_register = switch_to_register_callback
        self.user_db = user_db
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("<h2>Login</h2>")
        self.label.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.login)

        self.register_switch_btn = QPushButton("Don't have an account? Register")
        self.register_switch_btn.clicked.connect(self.switch_to_register)

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.register_switch_btn)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.user_db.get(username) == password:
            QMessageBox.information(self, "Success", f"Welcome back, {username}!")
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.user_db = {}  # Simple in-memory user "database"

        self.login_page = LoginPage(self.show_register_page, self.user_db)
        self.register_page = RegisterPage(self.show_login_page, self.user_db)

        self.addWidget(self.login_page)     # Index 0
        self.addWidget(self.register_page)  # Index 1

        self.setWindowTitle("Register and Login")
        self.setFixedSize(300, 250)

        self.show_login_page()

    def show_login_page(self):
        self.setCurrentIndex(0)

    def show_register_page(self):
        self.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
