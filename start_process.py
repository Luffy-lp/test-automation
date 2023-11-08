import multiprocessing
from models.data import *
from common.utils import *
import sys
from common.my_logger import logger

class Run(multiprocessing.Process):
    def __init__(self, myClass, taskDate,args):
        super().__init__()
        self.myClass = myClass
        self.taskDate = taskDate
        self.name = taskDate[1]['taskDes']
        self.args = args
        logger.info(f'完成创建【{self.name}】')

    def run(self):
        logger.info(f'开始执行【{self.name}】->进程ID【{self.pid}】')
        self.myClass(self.taskDate,self.args,self.pid)

def run_tasks(taskDate,args):
    task_path = os.path.join(path_BASE_DIR,taskDate[1]['task_path'])
    sys.path.append(task_path)
    myClass = import_module('Start', task_path)
    my_process = Run(myClass, taskDate,args)
    return my_process
