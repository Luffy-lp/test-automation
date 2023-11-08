import importlib
import json
import socket
import zipfile

from models.pathsData import *
import yaml
from base64 import b64encode, b64decode
from Crypto.Cipher import ChaCha20
from PIL import Image
from functools import wraps
from time import perf_counter, sleep
import datetime
from airtest.core.api import *
import os
import time

spendtime = None
def get_fileList(path):
    """获取文件夹里面的文件"""
    fileList = os.listdir(path)
    return fileList

def get_IMGSize(path):
    """获取图片的分辨率"""
    img = Image.open(path)
    width, heigt= img.size
    return width, heigt

def clock(type=None):  # 计时器
    """stop结束返回时间"""
    global start_time
    if type == "stop":
        spendtime = '%.9f' % (perf_counter() - start_time)
        print("花费时间{}秒:".format(spendtime))
        return spendtime
    else:
        start_time = perf_counter()

def timing_decorator(func):
    "计算函数所花费的时间"
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} 执行时间: {execution_time} 秒")
        return result
    return wrapper

def log_funcName(func):
    """打印函数名"""
    @wraps(func)
    def with_logging(*args, **kwargs):
        start_time = datetime.now()
        end_time = datetime.now()
        haoshi = (end_time - start_time).total_seconds()
        # timeSpent = end_time - start_time
        # print(timeSpent)
        print("{0}函数运行耗时{1}".format(func.__name__, haoshi))
        re = func(*args, **kwargs)
        if re is False:
            print(func.__name__ + "->was called return False")
        return func(*args, **kwargs)

    return with_logging

def try_func(func):
    @wraps(func)
    def with_try(t=3,*args, **kwargs):
        while t > 0:
            t -= 1
            try:
                func(*args, **kwargs)
                break
            except Exception as e:
                resource_result_utils(False, func.__name__,des=e)
        return func(*args, **kwargs)
    return with_try


def fileCheck(filepath):
    """文件正确性验证"""
    filebool = os.path.exists(filepath)
    return filebool


# def report( result, type, chapter, des, roleID=None, chat=None):
#     if not result:
#         if type == 0:
#             content = "{0}-->【{1}异常】-【角色{2}】-【id:{3}】：{4}".format(chapter, type, roleID, chat, des)
#             mylog.error(content)
#         if chat:
#             content = "{0}-->【{1}异常】-【角色{2}】-【id:{3}】：{4}".format(chapter, type, roleID, chat, des)
#             mylog.error(content)
#         else:
#             content = "{0}-->【{1}异常】-【角色{2}】:{3}".format(chapter, type, roleID, des)
#             mylog.error(content)


def read_yaml(path):
    with open(path, encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data


def write_yaml(path, data):
    with open(path, 'w+', encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)


def read_file(path):
    with open(path, "r", encoding='utf-8') as f:
        data = f.read()
    return data


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print("创建->", path)
        return True

def PosTurn(pos, device):  # 坐标转化
    width = device.display_info['width']
    height = device.display_info['height']
    POS = [pos[0] * width, pos[1] * height]
    return POS

import requests



def mytrans(str):
    data = {
        'doctype': 'json',
        'type': 'AUTO',
        'i': str
    }
    url = "http://fanyi.youdao.com/translate"
    r = requests.get(url, params=data)
    # print(r.text)
    result = r.json()
    # return result
    return result["translateResult"][0][0]["tgt"]

# def mysnapshot(loc_desc,IMG_parameter,quality=None,max_size=None):
#     # 0, 160, 1067, 551
#     filename = loc_desc + ".png"
#     file_path = os.path.join(path_RESOURCE_IMAGE, filename)
#     if not ST.LOG_DIR or not ST.SAVE_IMAGE:
#         return
#     if not quality:
#         quality = ST.SNAPSHOT_QUALITY
#     if not max_size:
#         max_size = ST.IMAGE_MAXSIZE
#     screen = G.DEVICE.snapshot()
#     screen = aircv.crop_image(screen, IMG_parameter)
#     aircv.imwrite(file_path, screen, quality, max_size=max_size)
#
#     try_log_screen(screen)

def myscreenshot(file_path, loc_desc):
    # date_decs = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = str(loc_desc) + ".png"
    file_path = os.path.join(file_path, filename)
    try:
        snapshot(filename=file_path, msg=loc_desc)
    except Exception as e:
        print(e)

    # tempalte = Template(
    #     r"C:\Users\admin\AppData\Local\Temp\AirtestIDE\scripts\e54a0377105932d86d3b89f24ad95d13\1616493784313.jpg")
    # print(tempalte)
    # pos = tempalte.match_in(screen)


def time_difference(time_start):
    """计算时间差"""
    time_end = time.time()  # 结束计时
    time_c = time_end - time_start  # 运行所花时间
    return time_c


def set_offset(screens, ADBdevice):
    """计算点击偏移量"""
    # GData.compatibility["screen"][ADBdevice]=screen
    mystr: str = screens[ADBdevice]
    mystr = mystr.replace("(", "")
    mystr = mystr.replace(")", "")
    NFlist = mystr.split(",")
    offset = 1 - (int(NFlist[3]) - int(NFlist[1])) / int(NFlist[3])
    return offset

    # def addReportPhoto(self, content):
    #     content = content + '.png'
    #     oss_file = os.path.join(str(date), content)
    #     http_url = self.url + oss_file
    #     update_local_file = os.path.join(path_BOOKREAD_ERROR_IMAGE, content)
    #     time = path_BOOKREAD_ERROR_IMAGE.split('\\')[2]
    #     oss_files = self.baseUploadPath + time + '\\' + content
    #     oss_files = oss_files.replace('\\', '/')
    #     print(update_local_file)
    #     self.bucket.put_object_from_file(oss_files, update_local_file)
    #     return http_url

def resource_result_utils(result, type, des, book_id, chapter_id=None, screen=True):
    """检测结果"""
    if result is False:
        dec = "{0}【{1}】-{2}".format(chapter_id, type, des)
        log(Exception(dec), snapshot=True)
        myscreenshot(path_BOOKREAD_ERROR_IMAGE, dec)
        # http_url = addReportPhoto(dec)
        # addReportData(self.chapter_info['book_id'], self.chapter_info['chapter_id'], http_url, dec, type, role_id,
        #               self.chat_info["chat_conf"]['id'])

    # def resource_result(self, result, type, des, screen=True, role_id=None):
    #     """检测结果"""
    #     if result is False:
    #         if role_id == None:
    #             try:
    #                 role_id = str(self.chat_info["chat_conf"]["role_id"])
    #             except Exception as e:
    #                 role_id = None
    #         dec = "{0}【{1}】[{2}]{3}".format(self.chapter_info["chapter_id"], type, role_id, des)
    #         # desc = "{0}【{1}】[{2}]{3}".format(self.chapter_info["chapter_id"], type, role_id, des)
    #         log(Exception(dec))
    #         if dec not in self.resultPicture_record:
    #             if "hair未渲染" in dec and "face1未渲染" in dec:
    #                 w_yaml_nonHuman([role_id])
    #                 myscreenshot(path_NonHuman_File, dec)
    #             self.resultPicture_record.append(dec)
    #             if screen:
    #                 myscreenshot(path_BOOKREAD_ERROR_IMAGE, dec)

class ChaptersChaCha20:
    # chapters 客户端加密key:
    # KEY_ = bytes.fromhex(str(config.data["chapters"]["story"]["key"]))
    # NONCE_ = bytes.fromhex(str(config.data["chapters"]["story"]["nonce"]))
    KEY_ = bytes.fromhex("fca6dc62ccadaeab20191109feacdba038485868788898a8dba038485ca13de6")
    NONCE_ = bytes.fromhex("07000000404142434445464748494a4b0000000009112019")

    @staticmethod
    def encryto(plaintext):
        print(ChaptersChaCha20.KEY_.decode())
        print(ChaptersChaCha20.NONCE_.decode())
        cipher = ChaCha20.new(key=ChaptersChaCha20.KEY_, nonce=ChaptersChaCha20.NONCE_)
        ciphertext = cipher.encrypt(plaintext)
        print(ciphertext.decode('ISO-8859-1'))
        nonce = b64encode(cipher.nonce).decode('utf-8')
        ct = b64encode(ciphertext).decode('utf-8')
        return ct
        # result = json.dumps({'nonce': nonce, 'ciphertext': ct})
        # return result

    @staticmethod
    def decryto(encode_content):
        try:
            # b64 = json.loads(json_input)
            cipher = ChaCha20.new(key=ChaptersChaCha20.KEY_, nonce=ChaptersChaCha20.NONCE_)
            nonce = b64encode(cipher.nonce).decode('utf-8')
            # nonce = b64decode(b64['nonce'])
            # ciphertext = b64decode(b64['ciphertext'])
            ciphertext = b64decode(encode_content)
            plaintext = cipher.decrypt(ciphertext)
            return plaintext
        except (ValueError, KeyError):
            # print("Incorrect decryption")
            return False

    @staticmethod
    def decryto_chapter_info(chapter_info):
        for id,info in chapter_info.items():
            if "content" in info:
                info["content"] = ChaptersChaCha20.decryto(info["content"]).decode('UTF-8')
            # print(info["content"])
        return chapter_info

def api_requests(times=20,timeOut=10):
    def decorator(func):
        def wrapper(*args,**kwargs):
            header,url,body,type = func(*args,**kwargs)
            myTimes = times
            while myTimes >= 0:
                myTimes = myTimes -1
                try:
                    print("拉取{0}接口".format(func.__name__))  # 补充正则截取
                    if type == 'get':
                        response = requests.get(url=url, headers=header, data=body, timeout=timeOut)
                    else:
                        response = requests.post(url=url, headers=header, data=body, timeout=timeOut)
                    dir_json = json.loads(response.text)
                    dir = eval(str(dir_json))['data']
                except Exception as e:
                    # traceback.print_exc()
                    print("拉取{0}接口失败{1}，重试".format(func.__name__, e))
                    sleep(1)
                else:
                    print("拉取{0}接口成功".format(func.__name__))
                    return dir
            return dir
        return wrapper
    return decorator

def unzip_file(fz_name, path):
    """
    解压缩文件
    :param fz_name: zip文件
    :param path: 解压缩路径
    :return:
    """
    flag = False

    if zipfile.is_zipfile(fz_name):  # 检查是否为zip文件
        with zipfile.ZipFile(fz_name, 'r') as zipf:
            zipf.extractall(path)
            # for p in zipf.namelist():
            #     # 使用cp437对文件名进行解码还原， win下一般使用的是gbk编码
            #     p = p.encode('cp437').decode('gbk')  # 解决中文乱码
            #     print(fz_name, p,path)
            flag = True

    return {'file_name': fz_name, 'flag': flag}

def downloardurl(address):
    # zp = None
    # source_dir = os.getcwd()
    path = "/resource"
    try:
        r = requests.get(address, stream=True)
        print("下载成功")
    except:
        print("下载失败")
    zip_file = zipfile.ZipFile('gamecfg_0805test_20201217_Q5yEz1.zip')
    zip_list = zip_file.namelist()
    folder_abs = path
    for f in zip_list:
        zip_file.extract(f, folder_abs)
    zip_file.close()

def local_address():
    '''获取本机地址'''
    local_address = None
    try:
        myname = socket.getfqdn(socket.gethostname())
    # 获取本机ip
        local_address = socket.gethostbyname(myname)
    except:
        print("获取ip异常")
    return local_address

def import_module(myClass,module_path):
    """

    动态导入模块

    """
    module_name = myClass.lower()

    module = importlib.import_module(module_name, package=module_path)

    class_obj = getattr(module, myClass)

    return class_obj