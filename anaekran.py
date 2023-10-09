from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_txtEmail

app = QApplication()



class Pencere(QMainWindow, Ui_txtEmail):
    def __init__(self):
        super().__init__()  # super demek ebeveyınımın ınıtını de calıstır demek
        self.setupUi(self)

        self.btn_login.clicked.connect(self.parola_kontrol_et)

    def parola_kontrol_et(self):
        email = self.email_txt.text()
        parola = self.txt_password.text()

        if email == sistem_email and parola == sistem_parola

        print("Parola kontrol et")
        self.email_txt.setVisible(False)
        self.email_txt.setVisible(False)
        self.email_txt.setVisible(False)
        self.email_txt.setVisible(False)





pencere = Pencere()
pencere.show()

app.exec()
