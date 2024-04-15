import sys
import os

from PyQt6.QtWebEngineCore import QWebEnginePage
"""
pip install PyQt6-WebEngine
"""
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtWebEngineWidgets import  QWebEngineView
from AppJavaScriptLoader import AppJavaScriptLoader
import asyncio
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from colorama import Fore, Back, Style


class MWebPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        filename = os.path.basename(str(sourceID))
        if level == QWebEnginePage.JavaScriptConsoleMessageLevel.InfoMessageLevel:
            print(f"js.info: => {Fore.GREEN}{message}{Style.RESET_ALL}")
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel:
            print(f"js.wran => \033[38;5;214m {message} \033[m")
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel:
            print(f"js.error => {Fore.RED}{message}{Style.RESET_ALL}")

class JSDemo(QMainWindow):
    def __init__(self,JavaScript: AppJavaScriptLoader):
        self._app = QApplication(sys.argv)
        self._JavaScript = JavaScript
        super(JSDemo, self).__init__()
        self.initUI()
        self.init()

    # 初始化信号
    def init(self):
        self._loop = asyncio.get_event_loop()
        def _startapp():
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
        print("javascipt 加载完成")
        aweme_id = "7356672812599299343"
        cursor = 0
        count = 20
        msToken = "vZHoRDPsiJAL5cowL1pLFbhppUtOUixaLQGLB9b-3J6uWJtIwwqZisXsqzBUq21QT3qatSR5xEzUqrbUf89OJgU-CyxqyAWr8fAs-W_t5vnM7UZbsoJrUw%3D%3D"

        device = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&cursor={cursor}&count={count}&item_type=0&insert_ids=&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1200&browser_language=zh&browser_platform=Win32&browser_name=Edge&browser_version=120.0.2276.80&browser_online=true&engine_name=Blink&engine_version=122.0.6285.217&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7356175988425049638&msToken={msToken}'
        res = await self.call('window.build_x_b(' + f"\"{device}\"" + ');')
        print(res)

    # 初始化部件
    def initUI(self):
        self.browser = QWebEngineView()
        self.browser.setPage(MWebPage(self.browser))
                                                    
    # 启动app
    def startApp(self):
        self.browser.setHtml(str(self._JavaScript))
        sys.exit(self._app.exec())
    
    # 退出程序
    def quitApp(self):
        self._app.quit()

if __name__ == '__main__':
    appjava = AppJavaScriptLoader()
    print(appjava)
    js = JSDemo(appjava)
    url = os.getcwd() + '/app.html'
    js.startApp()
