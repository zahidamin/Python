 
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import QEvent
from ui_widget import Ui_widget
import webbrowser

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Modern Calculator")
        self.setMaximumHeight(500)
        self.setMaximumWidth(800)

        # Connect the "Calculate" button to the gasCal 
        self.pushCalculate.clicked.connect(self.gasCal)

        # Connect the "OnlineBill" button to the onlineBill 
        self.pushOnlineBill.clicked.connect(self.onlineBill)

        # Variables to track active input fields
        self.active_field = None  # Track which field is active (preReading or curReading)

        # Connect keypad buttons
        self.push_0.clicked.connect(self.keypad)
        self.push_1.clicked.connect(self.keypad)
        self.push_2.clicked.connect(self.keypad)
        self.push_3.clicked.connect(self.keypad)
        self.push_4.clicked.connect(self.keypad)
        self.push_5.clicked.connect(self.keypad)
        self.push_6.clicked.connect(self.keypad)
        self.push_7.clicked.connect(self.keypad)
        self.push_8.clicked.connect(self.keypad)
        self.push_9.clicked.connect(self.keypad)
        self.push_c.clicked.connect(self.keypad)
        self.push_dot.clicked.connect(self.keypad)

        # Set focus handlers for both input fields
        self.preReading.installEventFilter(self)
        self.curReading.installEventFilter(self)
        self.factor.installEventFilter(self)
        self.gcv.installEventFilter(self)
        self.fixCharg.installEventFilter(self)
        self.meterRent.installEventFilter(self)

    def eventFilter(self, source, event):
        """ Detects which input field is focused (active) """
        if event.type() == QEvent.FocusIn:  # Use QEvent.FocusIn
            if source == self.preReading:
                self.active_field = 'preReading'
            elif source == self.curReading:
                self.active_field = 'curReading'
            elif source == self.factor:
                self.active_field = 'factor'
            elif source == self.gcv:
                self.active_field = 'gcv'
            elif source == self.fixCharg:
                self.active_field = 'fixCharg'
            elif source == self.meterRent:
                self.active_field = 'meterRent'

        return super(Widget, self).eventFilter(source, event)

    def keypad(self):
        button = self.sender()

        # For the "C" button (Clear)
        if button.text() == "C":
            self.preReading.setText("0")
            self.curReading.setText("0")
            self.factor.setText("0")
            self.gcv.setText("0")
            self.fixCharg.setText("0")
            self.meterRent.setText("0")
            return  # Exit the method after clearing

        # If the button pressed is "=" to evaluate an expression
        if button.text() == "=":
            try:
                # Evaluate based on the active field
                if self.active_field == 'preReading':
                    result_pre = str(eval(self.preReading.text()))
                    self.preReading.setText(result_pre)
                elif self.active_field == 'curReading':
                    result_cur = str(eval(self.curReading.text()))
                    self.curReading.setText(result_cur)
                elif self.active_field == 'factor':
                    result_factor = str(eval(self.factor.text()))
                    self.factor.setText(result_factor)
                elif self.active_field == 'gcv':
                    result_gcv = str(eval(self.gcv.text()))
                    self.gcv.setText(result_gcv)
                elif self.active_field == 'fixCharg':
                    result_fixcharg = str(eval(self.fixCharg.text()))
                    self.fixCharg.setText(result_fixcharg)
                elif self.active_field == 'meterRent':
                    result_meter = str(eval(self.meterRent.text()))
                    self.meterRent.setText(result_meter)

            except ZeroDivisionError:
                if self.active_field == 'preReading':
                    self.preReading.setText("Error")
                elif self.active_field == 'curReading':
                    self.curReading.setText("Error")
                elif self.active_field == 'factor':
                    self.factor.setText("Error")
                elif self.active_field == 'gcv':
                    self.gcv.setText("Error")
                elif self.active_field == 'fixCharg':
                    self.fixCharg.setText("Error")
                elif self.active_field == 'meterRent':
                    self.meterRent.setText("Error")

            except Exception:
                if self.active_field == 'preReading':
                    self.preReading.setText("Invalid entry")
                elif self.active_field == 'curReading':
                    self.curReading.setText("Invalid entry")
                elif self.active_field == 'factor':
                    self.factor.setText("Invalid entry")
                elif self.active_field == 'gcv':
                    self.gcv.setText("Invalid entry")
                elif self.active_field == 'fixCharg':
                    self.fixCharg.setText("Invalid entry")
                elif self.active_field == 'meterRent':
                    self.meterRent.setText("Invalid entry")

        # For numeric and dot buttons
        else:
            # Handle input for the active field only
            if self.active_field == 'preReading':
                current_text_pre = self.preReading.text()
                if current_text_pre == "0":  # Replace "0" with the pressed button
                    current_text_pre = ""
                self.preReading.setText(current_text_pre + button.text())

            elif self.active_field == 'curReading':
                current_text_cur = self.curReading.text()
                if current_text_cur == "0":  # Replace "0" with the pressed button
                    current_text_cur = ""
                self.curReading.setText(current_text_cur + button.text())

            elif self.active_field == 'factor':
                current_text_fac = self.factor.text()
                if current_text_fac == "0":  # Replace "0" with the pressed button
                    current_text_fac = ""
                self.factor.setText(current_text_fac + button.text())
            elif self.active_field == 'gcv':
                current_text_gcv = self.gcv.text()
                if current_text_gcv == "0":  # Replace "0" with the pressed button
                    current_text_gcv = ""
                self.gcv.setText(current_text_gcv + button.text())

            elif self.active_field == 'fixCharg':
                current_text_fixCharg = self.fixCharg.text()
                if current_text_fixCharg == "0":  # Replace "0" with the pressed button
                    current_text_fixCharg = ""
                self.fixCharg.setText(current_text_fixCharg + button.text())

            elif self.active_field == 'meterRent':
                current_text_rent = self.meterRent.text()
                if current_text_rent == "0":  # Replace "0" with the pressed button
                    current_text_rent = ""
                self.meterRent.setText(current_text_rent + button.text())


# Gas Calculation 


    def gasCal(self):
        try:
            # Input readings from the form
            previous_reading = int(self.preReading.text())
            current_reading = int(self.curReading.text())
            difference = current_reading - previous_reading

            # Input factors from the form
            factor = float(self.factor.text())
            gcv = float(self.gcv.text())
            fix = float(self.fixCharg.text())
            meter_rent = float(self.meterRent.text())

            # Calculate hm3 and mmbtu
            hm3 = (difference * factor) / 100000
            mmbtu = (hm3 * gcv) / 281.7385

            # Gas Tarif slabs
            s1 = 500 / 0.25
            s2 = 850 / 0.60
            s3 = 1250 / 1.0
            s4 = 1450 / 1.5
            s5 = 1900 / 2.0
            s6 = 3300 / 3.0
            s7 = 3800 / 4.0
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

            # Calculate GST
            gst = (rate + meter_rent + fix) * 0.18  # GST is 18%

            # Calculate final amount
            final_amount = rate + meter_rent + fix + gst

            # Output the results in the PlainTextEdit widget
            self.totAmount.setPlainText(f"Gas charges: {rate}\nGST: {gst}\nFinal Amount: {final_amount}")
        
        except ValueError:
            self.totAmount.setPlainText("Invalid input! Please enter numeric values.")

    def onlineBill(self):
        # Open the online bill webpage
        webbrowser.open("https://www.sngpl.com.pk/login.jsp?mdids=85")
        