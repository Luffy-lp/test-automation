import threading
import colorlog

LOGGING = dict(
    level='DEBUG',
    fh_level="DEBUG",
    sh_level="ERROR",
    ih_level="INFO",
    log_name="logging.log",
)
import os
from models.pathsData import path_myLOG_DIR
import logging
from logging.handlers import TimedRotatingFileHandler
from models.data import SysData


#  日志相关的配置

class MyLogger():
    _instance_lock = threading.Lock()

    def __init__(self):
        self.mylog: logging.Logger = None
        self.file_path = os.path.join(path_myLOG_DIR, LOGGING.get('log_name'))
        self.create_logger()

    def __new__(cls, *args, **kwargs):
        if not hasattr(MyLogger, "_instance"):
            with MyLogger._instance_lock:
                if not hasattr(MyLogger, "_instance"):
                    MyLogger._instance = object.__new__(cls)
        return MyLogger._instance

    def create_logger(self):
        """创建日志收集器"""
        self.mylog = logging.getLogger("automation")
        self.mylog.setLevel(LOGGING.get('level'))
        fh = TimedRotatingFileHandler(self.file_path, when='d',
                                      interval=1, backupCount=1,
                                      encoding="utf-8")
        fh.setLevel(LOGGING.get(SysData.loglevel))
        self.mylog.addHandler(fh)
        sh = logging.StreamHandler()
        sh.setLevel(LOGGING.get(SysData.loglevel))
        self.mylog.addHandler(sh)
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(levelname)s%(reset)s %(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red'
            }
        )
        # mate = logging.Formatter(formatter)
        # fh.setFormatter(mate)
        # sh.setFormatter(mate)
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        return self.mylog


logger = MyLogger().mylog
