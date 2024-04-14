# -*- coding: UTF-8 -*-
import sys
import os

from PyQt6.QtWebEngineCore import QWebEnginePage
"""
pip install PyQt6-WebEngine
"""
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtWebEngineWidgets import  QWebEngineView
import asyncio
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from colorama import Fore, Back, Style


class MWebPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        filename = os.path.basename(str(sourceID))
        if level == QWebEnginePage.JavaScriptConsoleMessageLevel.InfoMessageLevel:
            print(f"{filename}:{lineNumber} => {Fore.GREEN}{message}{Style.RESET_ALL}")
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel:
            print(f"{filename}:{lineNumber} => \033[38;5;214m {message} \033[m")
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel:
            print(f"{filename}:{lineNumber} => {Fore.RED}{message}{Style.RESET_ALL}")

class JSDemo(QMainWindow):
    def __init__(self):
        self._app = QApplication(sys.argv)
        super(JSDemo, self).__init__()
        self.initUI()
        self.init()
       
    # 初始化信号
    def init(self):
        self._loop = asyncio.get_event_loop()
        def _startapp():
            os.system('clear')
            self._loop.run_until_complete(self.appmain())
        self.browser.loadFinished.connect(_startapp)
    
    # 调用js函数
    async def call(self,funcstr):
        _result = -1
        def call_back(res):
            nonlocal _result
            _result = res
        self.browser.page().runJavaScript(funcstr,call_back)
        while _result == -1:
            QApplication.processEvents()

        return _result


    # 程序入口
    async def appmain(self):
        pass

    # 初始化部件
    def initUI(self):
        self.browser = QWebEngineView()
        self.browser.setPage(MWebPage(self.browser))

    # 加载html
    def loadHtml(self,html):
        #self.browser.setPage(WebPage())
        self.browser.load(QUrl.fromLocalFile(html))

    # 加载url
    def loadUrl(self,url):
        self.browser.load(QUrl(url))

    # 启动app
    def startApp(self):
        sys.exit(self._app.exec())
    
    # 退出程序
    def quitApp(self):
        self._app.quit()

if __name__ == '__main__':
    js = JSDemo()
    url = os.getcwd() + '/app.html'
    js.loadHtml(url)
    js.startApp()
