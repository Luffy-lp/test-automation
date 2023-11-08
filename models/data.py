from models.pathsData import *
from common.utils import *
class DeviceData():
    """

    获取设备配置以及定义数据结构

    """
    deviceData = None
    if deviceData is None:
        deviceData = read_yaml(os.path.join(path_config_DIR, "deviceConf.yml"))

class SysData():
    """

    获取系统配置以及定义数据结构

    """
    sysData = None
    if sysData is None:
        sysData = read_yaml(os.path.join(path_config_DIR, "sysConf.yml"))
    connectData = sysData['connectConf']
    reportData = sysData['reportConf']
    loglevel = sysData['loglevel']
    platformUrl = sysData['platformUrl']
    local_address = sysData['local_address']

class TaskData():
    """

    获取任务配置以及定义数据结构

    """
    taskDatas = None
    if taskDatas is None:
        taskDatas = read_yaml(os.path.join(path_config_DIR, "taskConf.yml"))