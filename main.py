# Import Libs
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *

# Main Class
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #-- Instanciate web engine view
        self.browser = QWebEngineView()
        #-- Define default URL browser
        self.browser.setUrl(QUrl('https://google.com'))
        #-- At initialize the windows stay in central of widget
        self.setCentralWidget(self.browser)
        #-- The window in show the aperence is maximized
        self.showMaximized()

        #-- Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        #-- Button Preview
        btn_preview = QAction('<-', self)
        btn_preview.triggered.connect(self.browser.back)
        navbar.addAction(btn_preview)

        #-- Button Refresh
        btn_refresh = QAction('Recaregar', self)
        btn_refresh.triggered.connect(self.browser.reload)
        navbar.addAction(btn_refresh)


# Create App
app = QApplication(sys.argv)
QApplication.setApplicationName('Yggdrazil')

windows = MainWindow()


# Run Browser
app.exec()
