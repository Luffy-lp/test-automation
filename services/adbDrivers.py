from models.pathsData import *
from pathlib import Path

def installGame(dev,package,mypath):  # 安装应用
    my_file = Path(mypath)
    if my_file.is_file():
        list =dev.list_app(third_only=True)
        for i in list:
            if i == package:
                print("{0}包已经安装".format(package))
                return True
        print("正在安装apk这时间可能有点长", package)  # 需要解决安装很慢。。。。。。。。。。。。。。
        dev.install_app(mypath)
        return True
    else:
        print("未找到对应的安装包")
        return False

def uninstallGame(dev,package,mypath):  # 卸载应用
    my_file = Path(mypath)
    if my_file.is_file():
        list =dev.list_app(third_only=True)
        for i in list:
            if i == package:
                dev.uninstall_app(package)
                return True

def starGame(dev,package):  # 启动游戏
   dev.start_app(package)
   print("启动游戏",package)
   sleep(20)

def mwake(dev):
    dev.wake()

def stopGame(dev,package):
    dev.stop_app(package)
    # GData.DeviceData_dir["poco"] = None  待处理
    # GData.RpcClient= None
    # GData.DeviceData_dir["androidpoco"] = None
    print("停止游戏{}".format(package))
    return True

def clearGame(dev,package):
    dev.clear_app(package)
    print("清理设备上的游戏数据")
