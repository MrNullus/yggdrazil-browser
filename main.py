# Import Libs
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *


# Main Class
class MainWindow(QMainWindow):
    def go_home(self):
        self.browser.setUrl(QUrl('https://google.com'))


    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def update_url(self, url):
        self.url_bar.setText(url.toString())


    def __init__(self):
        super(MainWindow, self).__init__()

        #--=== Initial Config
        #-- Instanciate web engine view
        self.browser = QWebEngineView()
        #-- Define default URL browser
        self.browser.setUrl(QUrl('https://google.com'))
        #-- At initialize the windows stay in central widget
        self.setCentralWidget(self.browser)


        #--=== Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #-- Button Preview
        btn_preview = QAction('<-', self)
        btn_preview.triggered.connect(self.browser.back)
        navbar.addAction(btn_preview)

        #-- Button Next
        btn_next = QAction('->', self)
        btn_next.triggered.connect(self.browser.forward)
        navbar.addAction(btn_next)

        #-- Button Refresh
        btn_refresh = QAction('Recaregar', self)
        btn_refresh.triggered.connect(self.browser.reload)
        navbar.addAction(btn_refresh)

        #-- Button Home
        btn_home = QAction('Home', self)
        btn_home.triggered.connect(self.go_home)
        navbar.addAction(btn_home)

        #-- Search Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)


# Create App
app = QApplication(sys.argv)
QApplication.setApplicationName('Yggdrazil')

windows = MainWindow()


# Run Browser
app.exec()
