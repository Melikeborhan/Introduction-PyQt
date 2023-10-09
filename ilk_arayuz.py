from PySide6.QtWidgets import QApplication, QPushButton, QWidget

# from PySide6.QtCore import Qt


app = QApplication()


pencere = QWidget
pencere_list = []


def pencere_ac():
    pencere2 = QWidget()
    pencere2.setWindowTitle("ikinci arayüz")
    pencere_list.append(pencere2)
    pencere2.show()


# label = Qlabel("merhabalar",pencere2)


def pencereleri_kapat():
    pencere_list.clear()


button1 = QPushButton("2.pencereyi ac", pencere)
button1.move(200, 100)
button1.clicked.connect(pencere_ac)


button_pencereleri_kapat = QPushButton("Pencereleri kapat", pencere)
button_pencereleri_kapat.move(10, 30)
button_pencereleri_kapat.clicked.connect(pencereleri_kapat)


pencere.show()
app.exec()
