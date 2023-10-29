import sys
from PyQt5.QAxContainer import *
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QApplication
from base.logger import MyLogger
from base.decorator import singleton

# 싱글톤 패턴으로 사용
@singleton
class KiwoomCore(QAxWidget):

    def __init__(self):
        super().__init__()
        # Logger
        self.logger = MyLogger(self.__class__.__name__)

        # 윈도우 레지스트리에 저장된 키움 openAPI 모듈 불러오기
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        
        self.OnEventConnect.connect(self.__login_slot)
        self.login_event_loop = None
        self.login_info = {}

    def _login_connect(self):
        '''키움증권 API에 연결해 로그인 요청 '''
        self.logger.debug("키움증권 API 연결시도")
        self.dynamicCall("CommConnect()")

        # 로그인 요청에 callback이 올때까지 다른 함수를 호출하지 못하도록 BLock을 건다.'''
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def __login_slot(self, err_code):
        '''로그인 요청에 대한 응답을 받는다'''
        if err_code == 0:
            self.logger.info("키움증권 API 연결성공")
        else:
            self.logger.error("키움증권 API 연결실패 : (" + err_code + ")")
            
            if err_code == -100:
               self.logger.error("> 사용자 정보교환 실패(-100)")
            if err_code == -101:
                self.logger.error("> 서버접속 실패(-101)")
            if err_code == -102:
                self.logger.error("> 버전처리 실패(-102)")

        # 로그인 이벤트 루프를 종료시킴
        self.login_event_loop.exit()

    def get_login_state(self):
        '''로그인 상태 체크(1 : 연결 / 0 : 연결안됨)'''
        return self.dynamicCall("GetConnectState()")

    def connect(self):
        '''키움증권 로그인 상태를 체크하고 로그인 연결'''
        if self.get_login_state() == 0:
            self._login_connect()

# 테스트
if __name__ == '__main__':
    app = QApplication(sys.argv)

    kiwoom = KiwoomCore()

    print(kiwoom.get_login_state())
    kiwoom.connect()
    print(kiwoom.get_login_state())

    app.exec_()