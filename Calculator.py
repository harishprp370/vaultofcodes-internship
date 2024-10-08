# Requirements PyQt5 package
# pip install pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        self.layout = QVBoxLayout()

        # Adding user details at the top
        self.add_user_details()

        # Input fields for numbers
        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText('Enter the first number')
        self.layout.addWidget(self.num1_input)

        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText('Enter the second number')
        self.layout.addWidget(self.num2_input)

        # Operator buttons layout
        self.operator_layout = QHBoxLayout()

        self.add_btn = QPushButton('+', self)
        self.add_btn.clicked.connect(lambda: self.perform_calculation('+'))
        self.operator_layout.addWidget(self.add_btn)

        self.sub_btn = QPushButton('-', self)
        self.sub_btn.clicked.connect(lambda: self.perform_calculation('-'))
        self.operator_layout.addWidget(self.sub_btn)

        self.mul_btn = QPushButton('*', self)
        self.mul_btn.clicked.connect(lambda: self.perform_calculation('*'))
        self.operator_layout.addWidget(self.mul_btn)

        self.div_btn = QPushButton('/', self)
        self.div_btn.clicked.connect(lambda: self.perform_calculation('/'))
        self.operator_layout.addWidget(self.div_btn)

        self.pow_btn = QPushButton('^', self)
        self.pow_btn.clicked.connect(lambda: self.perform_calculation('^'))
        self.operator_layout.addWidget(self.pow_btn)

        # Adding operator buttons layout to the main layout
        self.layout.addLayout(self.operator_layout)

        # Result label
        self.result_label = QLabel('Result:', self)
        self.layout.addWidget(self.result_label)

        # Error label for invalid input or division by zero
        self.error_label = QLabel('', self)
        self.error_label.setStyleSheet("color: red;")
        self.layout.addWidget(self.error_label)

        # Clear button
        self.clear_btn = QPushButton('Clear', self)
        self.clear_btn.clicked.connect(self.clear_fields)
        self.layout.addWidget(self.clear_btn)

        # Exit button
        self.exit_btn = QPushButton('Exit', self)
        self.exit_btn.clicked.connect(self.close)
        self.layout.addWidget(self.exit_btn)

        # Set main layout
        self.setLayout(self.layout)
        self.setWindowTitle('Basic Calculator')

    def add_user_details(self):
        # Adding name, email, GitHub, and intern details
        self.name_label = QLabel("HARISH N", self)
        self.layout.addWidget(self.name_label)

        # Gmail label with icon
        self.gmail_layout = QHBoxLayout()
        self.gmail_icon = QLabel(self)
        self.gmail_icon.setPixmap(QPixmap("gmail_logo.png"))  # Add the path to your Gmail logo file
        self.gmail_layout.addWidget(self.gmail_icon)

        self.gmail_label = QLabel("harishprp370@gmail.com", self)
        self.gmail_layout.addWidget(self.gmail_label)
        self.layout.addLayout(self.gmail_layout)

        # GitHub label with icon
        self.github_layout = QHBoxLayout()
        self.github_icon = QLabel(self)
        self.github_icon.setPixmap(QPixmap("github_logo.png"))  # Add the path to your GitHub logo file
        self.github_layout.addWidget(self.github_icon)

        self.github_label = QLabel('<a href="https://github.com/harishprp370/">https://github.com/harishprp370/</a>', self)
        self.github_label.setOpenExternalLinks(True)
        self.github_layout.addWidget(self.github_label)
        self.layout.addLayout(self.github_layout)

        # Internship details
        self.intern_label = QLabel("AI and PE intern at Vaultofcodes", self)
        self.layout.addWidget(self.intern_label)

    def perform_calculation(self, operation):
        # Clear previous error messages
        self.error_label.setText('')
        try:
            # Read input
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())

            # Perform the calculation based on the operation
            if operation == '+':
                result = self.add(num1, num2)
            elif operation == '-':
                result = self.subtract(num1, num2)
            elif operation == '*':
                result = self.multiply(num1, num2)
            elif operation == '/':
                result = self.divide(num1, num2)
            elif operation == '^':
                result = self.power(num1, num2)

            # Display result
            self.result_label.setText(f'Result: {result}')

        except ValueError:
            self.error_label.setText('Error: Invalid input. Please enter numbers.')
        except ZeroDivisionError:
            self.error_label.setText('Error: Division by zero is not allowed.')

    def clear_fields(self):
        # Clear all input fields and reset labels
        self.num1_input.clear()
        self.num2_input.clear()
        self.result_label.setText('Result:')
        self.error_label.setText('')

    # Basic operation functions
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

    def power(self, a, b):
        return a ** b

# Running the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
