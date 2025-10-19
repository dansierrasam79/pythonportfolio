import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTabWidget, QMessageBox
)

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unit Converter")
        self.setFixedSize(350, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        tabs = QTabWidget()
        tabs.addTab(self.temperature_tab_ui(), "Temperature")
        tabs.addTab(self.distance_tab_ui(), "Distance")
        tabs.addTab(self.weight_tab_ui(), "Weight")

        layout.addWidget(tabs)
        self.setLayout(layout)

    # Temperature conversion tab
    def temperature_tab_ui(self):
        tab = QWidget()
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.temp_input = QLineEdit()
        self.temp_input.setPlaceholderText("Enter temperature")
        input_layout.addWidget(self.temp_input)

        self.temp_unit_label = QLabel("Celsius/Fahrenheit")
        input_layout.addWidget(self.temp_unit_label)

        btn_layout = QHBoxLayout()
        self.btn_c_to_f = QPushButton("Celsius → Fahrenheit")
        self.btn_f_to_c = QPushButton("Fahrenheit → Celsius")

        self.btn_c_to_f.clicked.connect(self.celsius_to_fahrenheit)
        self.btn_f_to_c.clicked.connect(self.fahrenheit_to_celsius)

        btn_layout.addWidget(self.btn_c_to_f)
        btn_layout.addWidget(self.btn_f_to_c)

        self.temp_result = QLabel("")
        layout.addLayout(input_layout)
        layout.addLayout(btn_layout)
        layout.addWidget(self.temp_result)

        tab.setLayout(layout)
        return tab

    def celsius_to_fahrenheit(self):
        try:
            c = float(self.temp_input.text())
            f = (c * 9/5) + 32
            self.temp_result.setText(f"{c} °C = {f:.2f} °F")
        except ValueError:
            self.show_error("Please enter a valid number for temperature.")

    def fahrenheit_to_celsius(self):
        try:
            f = float(self.temp_input.text())
            c = (f - 32) * 5/9
            self.temp_result.setText(f"{f} °F = {c:.2f} °C")
        except ValueError:
            self.show_error("Please enter a valid number for temperature.")

    # Distance conversion tab
    def distance_tab_ui(self):
        tab = QWidget()
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.dist_input = QLineEdit()
        self.dist_input.setPlaceholderText("Enter distance")
        input_layout.addWidget(self.dist_input)

        self.dist_unit_label = QLabel("Kilometers/Miles")
        input_layout.addWidget(self.dist_unit_label)

        btn_layout = QHBoxLayout()
        self.btn_km_to_miles = QPushButton("Kilometers → Miles")
        self.btn_miles_to_km = QPushButton("Miles → Kilometers")

        self.btn_km_to_miles.clicked.connect(self.km_to_miles)
        self.btn_miles_to_km.clicked.connect(self.miles_to_km)

        btn_layout.addWidget(self.btn_km_to_miles)
        btn_layout.addWidget(self.btn_miles_to_km)

        self.dist_result = QLabel("")
        layout.addLayout(input_layout)
        layout.addLayout(btn_layout)
        layout.addWidget(self.dist_result)

        tab.setLayout(layout)
        return tab

    def km_to_miles(self):
        try:
            km = float(self.dist_input.text())
            miles = km * 0.621371
            self.dist_result.setText(f"{km} km = {miles:.2f} miles")
        except ValueError:
            self.show_error("Please enter a valid number for distance.")

    def miles_to_km(self):
        try:
            miles = float(self.dist_input.text())
            km = miles / 0.621371
            self.dist_result.setText(f"{miles} miles = {km:.2f} km")
        except ValueError:
            self.show_error("Please enter a valid number for distance.")

    # Weight conversion tab
    def weight_tab_ui(self):
        tab = QWidget()
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Enter weight")
        input_layout.addWidget(self.weight_input)

        self.weight_unit_label = QLabel("Kilograms/Pounds")
        input_layout.addWidget(self.weight_unit_label)

        btn_layout = QHBoxLayout()
        self.btn_kg_to_lb = QPushButton("Kilograms → Pounds")
        self.btn_lb_to_kg = QPushButton("Pounds → Kilograms")

        self.btn_kg_to_lb.clicked.connect(self.kg_to_pounds)
        self.btn_lb_to_kg.clicked.connect(self.pounds_to_kg)

        btn_layout.addWidget(self.btn_kg_to_lb)
        btn_layout.addWidget(self.btn_lb_to_kg)

        self.weight_result = QLabel("")
        layout.addLayout(input_layout)
        layout.addLayout(btn_layout)
        layout.addWidget(self.weight_result)

        tab.setLayout(layout)
        return tab

    def kg_to_pounds(self):
        try:
            kg = float(self.weight_input.text())
            pounds = kg * 2.20462
            self.weight_result.setText(f"{kg} kg = {pounds:.2f} lbs")
        except ValueError:
            self.show_error("Please enter a valid number for weight.")

    def pounds_to_kg(self):
        try:
            pounds = float(self.weight_input.text())
            kg = pounds / 2.20462
            self.weight_result.setText(f"{pounds} lbs = {kg:.2f} kg")
        except ValueError:
            self.show_error("Please enter a valid number for weight.")

    def show_error(self, message):
        QMessageBox.warning(self, "Input Error", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())
