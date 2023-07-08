import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Login")
        self.setGeometry(100, 100, 300, 200)

        # Membuat widget utama
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Membuat layout vertikal
        self.layout = QVBoxLayout(self.central_widget)

        # Membuat label dan menambahkannya ke layout
        self.label_username = QLabel("Username:", self)
        self.layout.addWidget(self.label_username)

        # Membuat line edit untuk input username
        self.line_edit_username = QLineEdit(self)
        self.layout.addWidget(self.line_edit_username)

        # Membuat label dan menambahkannya ke layout
        self.label_password = QLabel("Password:", self)
        self.layout.addWidget(self.label_password)

        # Membuat line edit untuk input password
        self.line_edit_password = QLineEdit(self)
        self.line_edit_password.setEchoMode(QLineEdit.Password)  # Menyembunyikan karakter password
        self.layout.addWidget(self.line_edit_password)

        # Membuat tombol login
        self.button_login = QPushButton("Login", self)
        self.button_login.clicked.connect(self.login)
        self.layout.addWidget(self.button_login)

    def login(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()

        if username == "PTI" and password == "sobatkreatif":
            print("Login berhasil!")
        else:
            print("Login gagal!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())
