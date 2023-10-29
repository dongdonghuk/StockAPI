import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(verbose=True)

this_path = os.path.dirname(os.path.abspath(__file__))
root_path = Path(this_path).parent #현재경로의 부모 -> 프로젝트 경로
output_path = os.path.join(root_path, 'output')

# 프로젝트 경로
def get_root_path():
    return root_path

# output 경로
def get_output_path():
    return output_path

def get_file_logger_handler():
    # 파일 logger 포맷
    # output/log 폴더에 날짜별로
    log_file = os.path.join(output_path, 'log', '{}.log'.format(datetime.now().date()))
    file_handler = logging.FileHandler(log_file)  # 로그파일 저장할 경로
    file_formatter = logging.Formatter('[%(asctime)s|%(name)s][%(levelname)-7s] : %(message)s')
    file_handler.setFormatter(file_formatter)

    # 로그파일로 남길 레벨 설정
    file_handler.level = logging.INFO
    return file_handler

def get_console_logger_handler():
    # 콘솔 logger 포맷
    console_formatter = logging.Formatter('[%(asctime)s | %(name)s:%(lineno)s][%(levelname)s] > %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    # 콘솔 로그로 남길 레벨
    console_handler.level = logging.DEBUG
    return console_handler