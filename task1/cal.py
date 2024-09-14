import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gas Calculator")

        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Form layout for input fields
        self.form_layout = QFormLayout()
        self.previous_reading_input = QLineEdit()
        self.current_reading_input = QLineEdit()
        self.factor_input = QLineEdit()
        self.gcv_input = QLineEdit()
        self.fix_input = QLineEdit()
        self.meter_rent_input = QLineEdit()
        
        self.form_layout.addRow("Previous Reading:", self.previous_reading_input)
        self.form_layout.addRow("Current Reading:", self.current_reading_input)
        self.form_layout.addRow("Factor:", self.factor_input)
        self.form_layout.addRow("GCV:", self.gcv_input)
        self.form_layout.addRow("Fix:", self.fix_input)
        self.form_layout.addRow("Meter Rent:", self.meter_rent_input)

        # Calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        # Output labels
        self.result_label = QLabel("Results will appear here")

        # Add widgets to layout
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

    def calculate(self):
        try:
            previous_reading = int(self.previous_reading_input.text())
            current_reading = int(self.current_reading_input.text())
            factor = float(self.factor_input.text())
            gcv = float(self.gcv_input.text())
            fix = float(self.fix_input.text())
            meter_rent = float(self.meter_rent_input.text())

            difference = current_reading - previous_reading
            hm3 = difference * factor / 100000
            mmbtu = hm3 * gcv / 281.7385

            if mmbtu <= 0.25:
                price = 500
            elif mmbtu <= 0.60:
                price = 850
            elif mmbtu <= 1.0:
                price = 1250
            elif mmbtu <= 1.5:
                price = 1450
            elif mmbtu <= 2:
                price = 1900
            elif mmbtu <= 3:
                price = 3300
            elif mmbtu <= 4:
                price = 3800
            else:
                price = 4200 

            total = hm3 * price
            gst = total * 0.25
            final_amount = total + gst + meter_rent

            result = (f"Difference: {difference}\n"
                      f"HM3: {hm3:.4f}\n"
                      f"MMBTU: {mmbtu:.4f}\n"
                      f"Total: {total:.2f}\n"
                      f"GST: {gst:.2f}\n"
                      f"Amount: {final_amount:.2f}")

            self.result_label.setText(result)
        except ValueError:
            self.result_label.setText("Please enter valid numbers in all fields.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
