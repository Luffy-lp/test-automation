from models.pathsData import *
from models.data import SysData, DeviceData
from common.my_logger import logger


class AdbConnect():
    """
    adb连接设备

    """
    method = SysData.connectData['method']
    simulator = SysData.connectData['simulator']
    adbPath = SysData.connectData['adbPath']
    deviceDatas = DeviceData.deviceData

    def __init__(self, devicesId):
        self.devicesId = devicesId
        self.deviceData = self.deviceDatas[devicesId]
        self.connect_device()

    def connect_device(self):
        time = 5
        while time > 0:
            time -= 1
            try:
                conf = "android" + "://" + self.deviceData['ip'] + "/" + self.devicesId
                logdir = os.path.join(path_airtestLOG_DIR, self.devicesId)
                auto_setup(__file__, logdir=logdir, devices=[conf + self.method, ], project_root=path_BASE_DIR)
                logger.info(f'成功连接设备-->【{self.devicesId}】')
                return True
            except:
                logger.error(f'连接设备失败重试-->【{self.devicesId}】')
        raise

    def adb_dispose(self, adbPath):
        """初始化"""
        i = 10
        devlist = None
        while i >= 0:
            i = i - 1
            try:
                # print(os.open(adbPath + " services"))
                connectfile = os.popen(adbPath + ' services')
                devlist = connectfile.readlines()
                # print("devlist",devlist)
                for i in range(1, len(devlist)):
                    if "device" in devlist[i]:
                        list = devlist[i].split("	device")
                        ADBdevice = list[0]
                        return ADBdevice
                raise
            except:
                sleep(8)
                print("查询设备信息异常")

    def getdevlist(self):
        devlist = []
        connectfile = os.popen('adb services')
        list = connectfile.readlines()
        # for i in range(len(list)):
        #     if list[i].find('\tdevice') != -1:
        #         temp = list[i].split('\t')
        #         devlist.append(temp[0])
        # return devlist

    def checkAdbConnectability(self, flag=0):
        '''
        flag =0时，当连接正常时返回True(default)
        flag!=0时，直接打印出结果
        '''
        connectstring = '''ADB连接失败, 请check以下项:
        1. 是否有连接上手机？请连接上手机选并重新check连接性!
        2. 是否有开启"开发者选项\\USB调试模式"?\n'''
        connectinfolist = self.getdevlist()
        if len(connectinfolist) == 0:
            return False
        if len(connectinfolist) == 1:
            if flag != 0:
                print('连接正常')
                print(f'设备SN: {connectinfolist[0]}')
            else:
                return True
        if len(connectinfolist) >= 2:
            print('连接正常，当前有连接多台设备. ')
            for i in range(len(connectinfolist)):
                print(f'设备{i + 1} SN: {connectinfolist[i]}')
            return True
