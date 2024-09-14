import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class GasBillCalculator(QMainWindow):
    def __init__(self):
        super(GasBillCalculator).__init__()
        self.load_ui()

        # Connect the Calculate button to the calculation method
        self.ui.pushCalculate.clicked.connect(self.calculate_gas_bill)

    def load_ui(self):
        loader = QUiLoader()
        ui_file = QFile("GasCal.ui")  # Load your GasCal.ui file
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

    def calculate_gas_bill(self):
        try:
            # Retrieve the input values from the GUI
            previous_reading = int(self.ui.preReading.text())
            current_reading = int(self.ui.curReading.text())
            factor = float(self.ui.factor.text())
            gcv = float(self.ui.gcv.text())
            fix = float(self.ui.fixCharg.text())
            meter_rent = float(self.ui.meterRent.text())

            # Calculate the difference
            difference = current_reading - previous_reading
            hm3 = (difference * factor) / 100000
            mmbtu = (hm3 * gcv) / 281.7385

            # Gas Tarif slabs
            s1 = 500 / 0.25
            s2 = 850 / 0.60
            s3 = 1250 / 1.0
            s4 = 1450 / 1.5
            s5 = 1900 / 2
            s6 = 3300 / 3
            s7 = 3800 / 4
            s8 = 4200

            # Determine the rate based on mmbtu slab
            if hm3 <= 0.25:
                rate = s1
            elif 0.25 < hm3 <= 0.60:
                rate = s2
            elif 0.60 < hm3 <= 1.0:
                rate = s3
            elif 1.0 < hm3 <= 1.5:
                rate = s4
            elif 1.5 < hm3 <= 2.0:
                rate = s5
            elif 2.0 < hm3 <= 3.0:
                rate = s6
            elif 3.0 < hm3 <= 4.0:
                rate = s7
            else:
                rate = s8

            # Calculate the gas charges and GST
            gst = (rate + meter_rent + fix) * 0.18  # GST is 18%
            final_amount = rate + meter_rent + fix + gst

            # Output the results in the PlainTextEdit widget
            self.ui.totAmount.setPlainText(f"Gas charges: {rate}\nGST: {gst}\nFinal Amount: {final_amount}")

        except ValueError:
            self.ui.totAmount.setPlainText("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GasBillCalculator()
    window.show()
    sys.exit(app.exec())
