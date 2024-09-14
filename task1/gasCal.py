from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox)
import sys

class GasChargeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()

        # Input fields
        self.prev_reading_label = QLabel("Previous Reading:")
        self.prev_reading_input = QLineEdit()
        layout.addWidget(self.prev_reading_label)
        layout.addWidget(self.prev_reading_input)

        self.curr_reading_label = QLabel("Current Reading:")
        self.curr_reading_input = QLineEdit()
        layout.addWidget(self.curr_reading_label)
        layout.addWidget(self.curr_reading_input)

        self.factor_label = QLabel("Factor:")
        self.factor_input = QLineEdit()
        layout.addWidget(self.factor_label)
        layout.addWidget(self.factor_input)

        self.gcv_label = QLabel("GCV:")
        self.gcv_input = QLineEdit()
        layout.addWidget(self.gcv_label)
        layout.addWidget(self.gcv_input)

        self.fix_label = QLabel("Fix:")
        self.fix_input = QLineEdit()
        layout.addWidget(self.fix_label)
        layout.addWidget(self.fix_input)

        self.meter_rent_label = QLabel("Meter Rent:")
        self.meter_rent_input = QLineEdit()
        layout.addWidget(self.meter_rent_label)
        layout.addWidget(self.meter_rent_input)

        # Calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        # Output fields
        self.difference_label = QLabel("Difference: ")
        layout.addWidget(self.difference_label)

        self.hm3_label = QLabel("HM3: ")
        layout.addWidget(self.hm3_label)

        self.mmbtu_label = QLabel("MMBTU: ")
        layout.addWidget(self.mmbtu_label)

        self.gas_charges_label = QLabel("Gas Charges: ")
        layout.addWidget(self.gas_charges_label)

        self.gst_label = QLabel("GST: ")
        layout.addWidget(self.gst_label)

        self.final_amount_label = QLabel("Final Amount: ")
        layout.addWidget(self.final_amount_label)

        # Set main layout
        self.setLayout(layout)
        self.setWindowTitle("Gas Charge Calculator")

    def calculate(self):
        try:
            # Input readings
            previous_reading = int(self.prev_reading_input.text())
            current_reading = int(self.curr_reading_input.text())
            difference = current_reading - previous_reading
            self.difference_label.setText(f"Difference: {difference}")

            # Input factors
            factor = float(self.factor_input.text())
            gcv = float(self.gcv_input.text())
            fix = float(self.fix_input.text())
            meter_rent = float(self.meter_rent_input.text())

            # Calculate hm3 and mmbtu
            hm3 = (difference * factor) / 100000
            self.hm3_label.setText(f"HM3: {hm3:.2f}")

            mmbtu = (hm3 * gcv) / 281.7385
            self.mmbtu_label.setText(f"MMBTU: {mmbtu:.2f}")

            # Gas Tarif
            s1 = (500 / 0.25)
            s2 = (850 / 0.60)
            s3 = (1250 / 1.0)
            s4 = (1450 / 1.5)
            s5 = (1900 / 2)
            s6 = (3300 / 3)
            s7 = (3800 / 4)
            s8 = 4200

            # Determine price based on hm3 slab
            if hm3 <= 0.25:
                rate = s1
            elif hm3 > 0.25 and hm3 <= 0.60:
                rate = s2
            elif hm3 > 0.60 and hm3 <= 1.0:
                rate = s3
            elif hm3 > 1.0 and hm3 <= 1.5:
                rate = s4
            elif hm3 > 1.5 and hm3 <= 2:
                rate = s5
            elif hm3 > 2.0 and hm3 <= 3:
                rate = s6
            elif hm3 > 3.0 and hm3 <= 4:
                rate = s7
            else:
                rate = s8

            self.gas_charges_label.setText(f"Gas Charges: {rate:.2f}")

            # Calculate GST
            gst = (rate + meter_rent + fix) * 0.18  # GST is 18%
            self.gst_label.setText(f"GST: {gst:.2f}")

            # Calculate final amount
            final_amount = rate + meter_rent + fix + gst
            self.final_amount_label.setText(f"Final Amount: {final_amount:.2f}")

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers.")

# Main execution
app = QApplication(sys.argv)
window = GasChargeCalculator()
window.resize(500, 400)
window.show()
sys.exit(app.exec())
