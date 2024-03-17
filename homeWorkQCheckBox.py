import sys
from PyQt5.QtWidgets import (QApplication, 
                            QWidget, 
                            QLineEdit, 
                            QRadioButton, 
                            QPushButton, 
                            QFormLayout, 
                            QComboBox, 
                            QSpinBox,
                        )

class Sorovnoma(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Student")

        self.ism_input = QLineEdit(self)
        self.sharif_input = QLineEdit(self)

        self.yoshi_spinbox = QSpinBox(self)
        self.yoshi_spinbox.setMinimum(0)
        self.yoshi_spinbox.setMaximum(45)

        self.jins_radio_erkak = QRadioButton('Erkak', self)
        self.jins_radio_ayol = QRadioButton('Ayol', self)

        self.mamlakat_combobox = QComboBox(self)
        self.mamlakat_combobox.addItems(["Toshkent", 'Andijon', 'Namangan', "Samarqand", 
                                        "Farg'ona", "Jizzax", "Xorazim", "Surxandaryo",
                                        "Qasgqadaryo", "Nukus", "Buxoro", "Sirdaryo"])
        
        self.tel_num_input = QLineEdit(self)
        self.tel_num_input.setInputMask('+999_99_990_99_99')

        self.fakultutet_input = QLineEdit(self)

        self.kursi_combobox = QComboBox(self)
        self.kursi_combobox.addItems(['1', '2', '3', '4'])

        self.saqlash_btn = QPushButton("Ma'lumotlarni faylga yozish", self)
        self.saqlash_btn.clicked.connect(self.saqlash)

        layout = QFormLayout()
        layout.addRow('Ism:', self.ism_input)
        layout.addRow('Sharif:', self.sharif_input)
        layout.addRow('Jins:', self.jins_radio_ayol)
        layout.addRow('', self.jins_radio_erkak)
        layout.addRow('Yoshi:', self.yoshi_spinbox)
        layout.addRow('Manzili:', self.mamlakat_combobox)
        layout.addRow('Telefon raqami:', self.tel_num_input)
        layout.addRow('Fakultuteti:', self.fakultutet_input)
        layout.addRow('Kursi:', self.kursi_combobox)
        layout.addRow('', self.saqlash_btn)

        self.setLayout(layout)

    def saqlash(self):
        ism = self.ism_input.text()
        sharif = self.sharif_input.text()
        jins = 'Erkak' if self.jins_radio_erkak.isChecked() else 'Ayol'
        yoshi = self.yoshi_spinbox.value()
        mamlakat = self.mamlakat_combobox.currentText()
        tel_num = self.tel_num_input.text()
        fakultutet = self.fakultutet_input.text()
        kursi = self.kursi_combobox.currentText()

        fayl_nomi = f"{ism} {sharif}.txt"
        with open(fayl_nomi, 'w') as file:
            file.write(f'Ism: {ism}\nSharif: {sharif}\nJins: {jins}\nYoshi: {yoshi}\nMamlakat: {mamlakat}\nTelefon raqami: {tel_num}\nfakultuteti: {fakultutet}\nKursi: {kursi}')

        self.close()


app = QApplication([])
oyna = Sorovnoma()
oyna.show()
app.exec_()

sys.exit()
