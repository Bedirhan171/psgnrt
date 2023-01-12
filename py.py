#Kütüphaneler
#----------------------------------------------------
import sys
from PyQt5 import QtWidgets, QtGui
import random
import string
#----------------------------------------------------

#class 
#----------------------------------------------------
class PasswordGenerator(QtWidgets.QWidget):
    #----------------------------------------------------
    def __init__(self):
        super().__init__()
        self.length = 16
        self.setWindowTitle("Password Generator")
        self.setGeometry(50, 50, 300, 100)

        #widget oluşturuldu.    
        #----------------------------------------------------
        self.length_label = QtWidgets.QLabel("Length:")
        self.length_spinbox = QtWidgets.QSpinBox()
        self.length_spinbox.setValue(self.length)
        self.length_spinbox.valueChanged.connect(self.update_length)
        self.generate_button = QtWidgets.QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_password)
        self.password_label = QtWidgets.QLabel("Password:")
        self.password_lineedit = QtWidgets.QLineEdit()
        self.password_lineedit.setReadOnly(True)
        #----------------------------------------------------

        #layout oluşturuldu.
        #----------------------------------------------------   
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.length_label, 0, 0)
        layout.addWidget(self.length_spinbox, 0, 1)
        layout.addWidget(self.generate_button, 0, 2)
        layout.addWidget(self.password_label, 1, 0)
        layout.addWidget(self.password_lineedit, 1, 1, 1, 2)
        self.setLayout(layout)
        #----------------------------------------------------


    #----------------------------------------------------
    def update_length(self, value):
        self.length = value
    #----------------------------------------------------

    #----------------------------------------------------
    def generate_password(self):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(self.length))
        self.password_lineedit.setText(password)
    #----------------------------------------------------


#----------------------------------------------------        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())
#----------------------------------------------------    
