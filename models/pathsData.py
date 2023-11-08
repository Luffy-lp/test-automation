import os
import winreg
import datetime
import shutil
from common.utils import *

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )
Desktop = winreg.QueryValueEx(key, "Desktop")[0]

date = datetime.date.today()
# file = os.getcwd()

# 公共配置
path_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目的根路径
path_res_DIR = os.path.join(path_BASE_DIR, "resource")  # 资源路径
path_IMAGE_DIR = os.path.join(path_res_DIR, "IMAGE")  # 资源图片路径 im
path_config_DIR = os.path.join(path_BASE_DIR, "config")  # yamlfiles路径
path_result_DIR = os.path.join(Desktop, "result")  # 测试结果的目录路径
path_report_DIR = os.path.join(path_result_DIR, "report")  # 测试报告的目录路径
path_RES_DIR = os.path.join(path_result_DIR, "res")  # 测试报告录屏的目录路径
path_airtestLOG_DIR = os.path.join(path_result_DIR, "log")  # airtest日志目录的项目路径
path_myLOG_DIR = os.path.join(path_result_DIR, "report/mylog")  # 自定义日志目录的项目路径


# chapters配置
path_readRecord_YML = os.path.join(path_config_DIR, "yamlBookRead")
path_CASE_DIR = os.path.join(path_BASE_DIR, "step/testcases")  # 测试用例的目录路径
path_DATA_DIR = os.path.join(path_BASE_DIR, "casedatas")  # 用例数据的项目路径
path_BOOKREAD_ERROR_IMAGE = os.path.join("D:\Read_Result", str(date))
path_bookcheck_result_yml = os.path.join(path_BASE_DIR, "bookread_result.yml")


def clearFolder():
    print("清空文件夹")
    pathBookRead = os.path.join(path_config_DIR, "yamlBookRead")
    fileNamelist = [path_result_DIR, pathBookRead, path_res_DIR]
    for fileName in fileNamelist:
        if not os.path.isdir(fileName):
            break
        filelist = os.listdir(fileName)
        for f in filelist:
            filepath = os.path.join(fileName, f)
            if os.path.isfile(filepath):
                os.remove(filepath)
            else:
                shutil.rmtree(filepath)


def createFolder():
    print("创建文件夹")
    folder_list = [path_result_DIR, path_report_DIR, path_myLOG_DIR, path_airtestLOG_DIR, path_res_DIR, path_IMAGE_DIR,
                   path_RES_DIR, path_BOOKREAD_ERROR_IMAGE, path_bookcheck_result_yml]
    for folder in folder_list:
        if not os.path.exists(folder):
            os.makedirs(folder)

    log_path = os.path.join(path_myLOG_DIR, "logging.log")
    with open(log_path, 'w') as f:
        f.seek(0)
        f.truncate()
# def createFolder():
#     print("创建文件夹")
#     mkdir(path_Result_DIR)  # 测试结果
#     mkdir(path_REPORT_DIR)  # 测试报告
#     mkdir(path_LOG_MY)  # mylog日志
#     mkdir(path_LOG_DIR)  # log日志
#     mkdir(path_resource)  # 资源路径
#     mkdir(path_RESOURCE_IMAGE)  # 图片资源路径
#     mkdir(path_RES_DIR)  # 测试报告录屏的目录路径
#     mkdir(path_BOOKREAD_ERROR_IMAGE)
#     mkdir(path_bookcheck_result_yml)
#     mkdir(path_Result_DIR)  # 测试结果
#     mkdir(path_REPORT_DIR)  # 测试报告
#     mkdir(path_LOG_MY)  # mylog日志
#     mkdir(path_LOG_DIR)  # log日志
#     mkdir(path_resource)  # 资源路径
#     mkdir(path_RESOURCE_IMAGE)  # 图片资源路径
#     mkdir(path_RES_DIR)  # 测试报告录屏的目录路径
#     mkdir(path_BOOKREAD_ERROR_IMAGE)
#     mkdir(path_bookcheck_result_yml)
#     path = os.path.join(path_LOG_MY, "logging.log")
#     with open(path, 'w') as f1:
#         f1.seek(0)
#         f1.truncate()
