import logging
from logging import *
from base.env import get_file_logger_handler, get_console_logger_handler

class MyLogger:

    # 생성자 - 기본 레벨 DEBUG
    def __init__(self, name=None, level=DEBUG):
        '''로거명이 정의되어 있지 않으면 현재 클래스명을 사용'''
        if not name:
            name = self.__class__.__name__

        # logger 설정
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        '''
        콘솔 logger 설정
        '''
        self.logger.addHandler(get_console_logger_handler())
        '''
        파일 logger 설정
        '''
        self.logger.addHandler(get_file_logger_handler())


    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warn(msg, extra=extra)

    def critical(self, msg, extra=None):
        self.logger.critical(msg, extra=extra)