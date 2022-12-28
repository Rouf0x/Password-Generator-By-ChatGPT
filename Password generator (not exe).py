import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QClipboard

# List of characters to include in the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

# Function to generate a random password
def generate_password(length):
  password = ""
  for i in range(length):
    password += random.choice(characters)
  return password

# Create the main window
app = QApplication([])
window = QWidget()
window.setWindowTitle("Password generator")

# Set the window size
window.setGeometry(100, 100, 400, 100)

# Create a label and line edit for the password length
length_label = QLabel("Password length:")
length_edit = QLineEdit()

# Create a button to generate the password
generate_button = QPushButton("Generate")

# Create a button to copy the password
copy_button = QPushButton("Copy")

# Create a label to display the generated password
password_label = QLabel()

# Define a function to generate the password and update the password label
def generate_password_clicked():
  # Get the password length from the line edit
  length = int(length_edit.text())
  # Generate the password
  password = generate_password(length)
  # Update the password label
  password_label.setText(password)

# Define a function to copy the password to the clipboard
def copy_password_clicked():
  # Get the text of the password label
  password = password_label.text()
  # Get the system clipboard
  clipboard = QApplication.clipboard()
  # Set the text of the clipboard
  clipboard.setText(password)

# Connect the buttons' clicked signals to the functions
generate_button.clicked.connect(generate_password_clicked)
copy_button.clicked.connect(copy_password_clicked)

# Create the layout and add the widgets
layout = QVBoxLayout()
layout.addWidget(length_label)
layout.addWidget(length_edit)
layout.addWidget(generate_button)
layout.addWidget(copy_button)
layout.addWidget(password_label)

# Set the layout of the main window
window.setLayout(layout)

# Show the window and run the app
window.show()
app.exec_()
