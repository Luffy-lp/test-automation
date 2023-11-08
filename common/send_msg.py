import oss2
import os
import json
import requests
import time
ding_list = []
urls_list = []
errors_list = []
def create_html(htmlpath):
    show_model = """<div style="width:300px;display:inline-block;vertical-align:top">
          <img style="width:300px;height:600px" src="{{url}}">
      <span >{{error}}</span>
      </div>"""
    show_list = "<html>"
    for i in range(0, len(urls_list)):
        # print(len(errors_list[i]))
        # if len(errors_list[i]) > 30:
        #     str1=errors_list[i][:30]
        #     str2=errors_list[i][30:]
        #     errors=str1+"<br/>"+str2
        # else:
        errors=errors_list[i]
        show_list = show_list + show_model.replace("{{url}}", urls_list[i]).replace("{{error}}",errors)
    show_list += "</html>"
    # print(show_list)
    # 打开文件，准备写入
    f = open(htmlpath, 'w')
    f.write(show_list)
    f.close()

# def create_html(htmlpath):
#     show_model = """<div style="display:inline-block">
#         <div>
#           <img style="width:300px;height:600px" src="{{url}}">
#         </div>
#         <span style="">{{error}}</span>
#       </div>"""
#     show_list = "<html>"
#     for i in range(0, len(urls_list)):
#         if len(errors_list[i]) > 30:
#             str1=errors_list[i][:30]
#             str2=errors_list[i][30:]
#             errors=str1+"<br/>"+str2
#         else:
#             errors=errors_list[i]
#         show_list = show_list + show_model.replace("{{url}}", urls_list[i]).replace("{{error}}", errors)
#     show_list += "</html>"
#     # 打开文件，准备写入
#     f = open(htmlpath, 'w')
#     f.write(show_list)
#     f.close()

#



def localhost2oss(local_file,endpoint,accesskey_id,accesskey_secret,bucket_name,baseUploadPath,url):
    auth = oss2.Auth(accesskey_id, accesskey_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    mytime=str(int(time.time()))
    for root, dirs, files in os.walk(local_file):
        oss_files = local_file.split('\\')[2]
        for file in files:
            if "html" in file:
                continue
            errors_list.append(file.replace(".png",""))
            update_local_file = os.path.join(root, file)
            # oss_files = local_file.split('\\')[2]
            oss_file = update_local_file.replace(local_file, '')
            oss_file = oss_file.replace('\\', '/')
            oss_file = baseUploadPath + oss_files + oss_file
            http_url = url + '/' + oss_file
            urls_list.append(http_url)
            bucket.put_object_from_file(oss_file, update_local_file)
        html_name = oss_files+"-"+mytime+ ".html"
        html_path = os.path.join(local_file, html_name)
        create_html(htmlpath=html_path)
        update_local_file = os.path.join(root, html_name)
        oss_files = local_file.split('\\')[2]
        oss_file = update_local_file.replace(local_file, '')
        oss_file = oss_file.replace('\\', '/')
        oss_file = baseUploadPath + oss_files + oss_file
        http_url = url + '/' + oss_file
        bucket.put_object_from_file(oss_file, update_local_file)
        ding_list.append(http_url)
        return oss_files, http_url


def send_msg(time,times,num, error,adbl,channel_id,des,strerror,dingrobot,data):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data_dict = {
        "msgtype": "markdown",
        "markdown": {
            "title": "自动化阅读",
            "text": "### "+str(time)+des+"\n\n"
                    "> **渠道号:** "+channel_id+"\n\n"
                    "> **设备号:** "+adbl+"\n\n"
                    "> **主版本号:** "+"10020.0.0"+"\n\n"
                    "> **完成阅读章节:** "+str(num)+"\n\n"
                    "> **阅读失败章节:** "+str(error)+"\n\n"
                    "> **失败章节列表:** "+strerror+"\n\n"
                    "> **总时长:** "+str(times)+"minute"+"\n\n"
                    "> **结果列表:** "+str(data)+"\n\n"                     
                    '> **<font color = red size=6 face="微软雅黑">访问http://172.16.20.60:8899/ChaptersAutoRead/ReadReport</font>**\n\n'
                    # '[![screenshot](http://product-editor-back.oss-cn-shenzhen.aliyuncs.com/test-Tripp%2F2021-08-17%2Fcharpters.png)]'+"("+http_url+")"
        }
    }
    r = requests.post(dingrobot, data=json.dumps(data_dict), headers=headers)
    return r.text

# if __name__ == '__main__':
#     time, times, num, error, http_url, chapterlist, channel_id, ADBdevice, des, dingrobot, data=0,60,10,
#     send_msg(time,times,num, error, http_url,chapterlist,channel_id,ADBdevice,des,dingrobot,data)
#     local_file = "D:\\Read_Result\\2021-08-17"
#     error = 20
#     chapterlist=["10001","10002"]
#     data = localhost2oss(local_file)
#     print(data)
#     aa=send_msg(num=28,error=error,data=data[0],http_url=data[1],chapterlist=chapterlist)
#     print(aa)