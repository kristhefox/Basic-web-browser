import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView



class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        back_button = QAction('Go back', self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)

        forward_button = QAction('Go forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        reload_button = QAction('Reload page', self)
        reload_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(reload_button)

        home_button = QAction('Home page', self)
        home_button.triggered.connect(self.navigate_home)
        navigation_bar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


application = QApplication(sys.argv)
QApplication.setApplicationName('Basic browser purely in Python')
window = Browser()
application.exec_()
