import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QTextEdit, QMainWindow, QAction, QMessageBox, QComboBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class HosgeldinEkranı(QWidget): # Hoş Geldin Ekranı
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seyahat Planlama")
        self.setFixedSize(600, 500)
        self.setStyleSheet("""
            background-color: #f0f0f0;
        """)
        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()

        welcome_label = QLabel("Hoş Geldiniz")
        welcome_label.setFont(QFont("Arial", 24))
        layout.addWidget(welcome_label, alignment=Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("background-color: #333333; padding: 10px; color:white;")

        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.jpg")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        login_button = QPushButton("Giriş Yap")
        login_button.setFont(QFont("Arial", 18))
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #367b34;
            }
        """)
        login_button.clicked.connect(self.open_main_window)
        layout.addWidget(login_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def open_main_window(self):
        self.main_window = SeyahatPlanlama()
        self.main_window.show()
        self.close()


class SeyahatPlanlama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seyahat Planlama")
        self.setGeometry(660, 300, 600, 450)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-family: Arial;
                font-size: 18px;
            }
            QLineEdit, QTextEdit {
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                font-size: 18px;
                border-radius: 5px;
                padding: 5px 12px;
                background-color: #4CAF50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #367b34;
            }
            #rota_bilgi_button, #konaklama_bilgi_button { /* Bilgi Al butonları */
               background-color: #333333; 
                color: white;
            }
            #temizle_button {
                background-color: red;
                color: white;
                margin-top : 17px;
            }
            QMenuBar {
                background-color: #87CEEB; /* Su mavisi */
                font-size: 19px;
                font-family: Arial;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 10px 23px;
                border-radius: 50%;
            }
            QMenuBar::item:selected {
                background-color: #79bdea;
            }
            QMessageBox {
                background-color: #f0f8ff; /* Alice Blue */
                color: #000000; /* Black */
            }
        """)
        self.setWindowIcon(QIcon('logo.jpg'))
        self.initialize_ui()

    def initialize_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.rota_label = QLabel("Seyahat Rotası")
        self.rota_input = QLineEdit()
        self.rota_input.setFixedWidth(280)
        self.rota_ekle_button = QPushButton("Rota Ekle")
        self.rota_ekle_button.setFixedWidth(100)
        self.rota_ekle_button.clicked.connect(self.rota_ekle)
        self.rota_bilgi_button = QPushButton("Bilgi Al")
        self.rota_bilgi_button.setFixedWidth(100)
        self.rota_bilgi_button.clicked.connect(self.show_rota_guide)
        self.rota_bilgi_button.setObjectName("rota_bilgi_button")

        self.konaklama_label = QLabel("Konaklama Tesisi")
        self.konaklama_input = QComboBox() # Değişiklik: QLineEdit yerine QComboBox
        self.konaklama_input.addItems(["Dias Hotel", "Hilton Koyatağı", "Address İstanbul","Anemon Galata","Cityloft 161","Plaza İstanbul","Suit Hotel","İstanbul Gonen Hotel"]) # Örnek veri
        self.konaklama_input.setFixedWidth(250)
        self.fiyat_label = QLabel("Fiyat")
        self.fiyat_input = QLineEdit()
        self.fiyat_input.setFixedWidth(250)
        self.konaklama_ekle_button = QPushButton("Konaklama Ekle")
        self.konaklama_ekle_button.setFixedWidth(150)
        self.konaklama_ekle_button.clicked.connect(self.konaklama_ekle)
        self.konaklama_bilgi_button = QPushButton("Bilgi Al")
        self.konaklama_bilgi_button.setFixedWidth(100)
        self.konaklama_bilgi_button.clicked.connect(self.show_konaklama_guide)
        self.konaklama_bilgi_button.setObjectName("konaklama_bilgi_button")

        self.rota_listesi = QTextEdit()
        self.rota_listesi.setReadOnly(True)

        self.temizle_button = QPushButton("Temizle")
        self.temizle_button.setMinimumWidth(100)
        self.temizle_button.clicked.connect(self.temizle)
        self.temizle_button.setObjectName("temizle_button")

        vbox = QVBoxLayout()
        vbox.addWidget(self.rota_label)
        vbox.addWidget(self.rota_input)
        vbox.addWidget(self.rota_ekle_button)
        vbox.addWidget(self.rota_bilgi_button)
        vbox.addWidget(self.konaklama_label)
        vbox.addWidget(self.konaklama_input)
        vbox.addWidget(self.fiyat_label)
        vbox.addWidget(self.fiyat_input)
        vbox.addWidget(self.konaklama_ekle_button)
        vbox.addWidget(self.konaklama_bilgi_button)
        vbox.addWidget(self.temizle_button)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.rota_listesi)

        self.central_widget.setLayout(hbox)

        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        # Dosya ve Yardım menülerini kaldırma
        menubar.setNativeMenuBar(False)

        # Çıkış ve Kılavuz menüleri
        file_menu = menubar.addMenu('Çıkış')

        exit_action = QAction(QIcon('carpi.png'), 'Çıkış', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setFont(QFont("Arial", 11))
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        yardim_menuleri = menubar.addMenu('Kılavuz')

        guide_action = QAction(QIcon('klavuz_simge.png'), 'Kılavuz', self)
        guide_action.setFont(QFont("Arial", 12))
        guide_action.triggered.connect(self.show_guide)

        yardim_menuleri.addAction(guide_action)

    def show_guide(self): # Kılavuz alanı
        guide_text = """
Kılavuz

- Seyahat Rotası eklemek için "Seyahat Rotası" metin kutusuna rotanızı yazın ve "Rota Ekle" düğmesine tıklayın.

- Konaklama eklemek için "Konaklama Tesisi Adı" ve "Fiyat" metin kutularına bilgileri girin ve "Konaklama Ekle" düğmesine tıklayın.

- Eklenen rotalar ve konaklamalar sağ taraftaki listede görüntülenecektir.

- Listeden öğeleri temizlemek için "Temizle" düğmesine tıklayın.

- Çıkış yapmak için menüden "Dosya" > "Çıkış" seçeneğini kullanabilirsiniz.
        """
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Kılavuz")
        message_box.setStyleSheet("""
            background-color: #d0e1e0; /* Alice Blue */
            color: #000000; /* Black */
        """)
        message_box.setText(guide_text)
        message_box.exec_()

    def show_rota_guide(self): #Seyehat rotası Bilgi kısmı
        rota_guide_text = """
        Seyahat Rotası Hakkında Bilgi

- Seyahat rotası eklemek için buraya rotanızı yazın. Örneğin: İstanbul - Antalya.
- Eklemek için "Rota Ekle" düğmesine tıklayın.
        """
        QMessageBox.information(self, "Rota Bilgi", rota_guide_text)

    def show_konaklama_guide(self):#Konaklama rehberi yani Bilgi yeri
        konaklama_guide_text = """
        Konaklama Tesisi Hakkında Bilgi

- Konaklamak istediğiniz Tesisi yazın ardından Fiyat belirtin.
- Eklemek için "Konaklama Ekle" düğmesine tıklayın.
        """
        QMessageBox.information(self, "Konaklama Bilgi", konaklama_guide_text)

    def rota_ekle(self): # Rota Ekleme kısmı
        rota = self.rota_input.text()
        if not rota:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir rota adı girin!")
            return
        self.rota_listesi.append(rota)
        self.rota_input.clear()

    def konaklama_ekle(self): # Konaklama Ekleme kısmı
        konaklama = self.konaklama_input.currentText() # Değişiklik: Seçilen öğeyi al
        fiyat = self.fiyat_input.text()
        if not konaklama or not fiyat:
            QMessageBox.warning(self, "Uyarı", "Lütfen konaklama adı ve fiyatı girin!")
            return
        self.rota_listesi.append(f"{konaklama} - {fiyat} TL")
        self.konaklama_input.setCurrentIndex(0) # Açılır menüyü sıfırla
        self.fiyat_input.clear()

    def temizle(self):
        self.rota_listesi.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_screen = HosgeldinEkranı()
    welcome_screen.show()
    sys.exit(app.exec_())
