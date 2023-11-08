from models.pathsData import *
from models.data import SysData

class TaskAPI():
    """

    测试平台API常规配置

    """
    platformUrl = SysData.platformUrl
    local_address = SysData.local_address
    @api_requests(times=5, timeOut=15)
    def addMachineTask(task_info, task_state=0):
        """
        添加任务信息接口API请求配置

        """
        url = f'{TaskAPI.platformUrl}/api/chaptersRead/addMachineTask'
        body = {"host": TaskAPI.local_address,
                "task_info": task_info,
                "task_state": task_state}
        return body, url, 'post'

    @api_requests(times=5, timeOut=15)
    def updateMachineTask(task_id, task_info, task_state=0):
        """

        获取更新任务信息接口API请求配置

        """
        url = f'{TaskAPI.platformUrl}/api/chaptersRead/updateMachineTask'
        body = {
            "host": TaskAPI.local_address,
            "task_id": task_id,
            "task_info": task_info,
            "task_state": task_state
        }
        return body, url, 'post'

    @api_requests(times=5, timeOut=15)
    def updateMachine(state):
        """
        获取更新任务信息接口API请求配置

        """
        url = f'{TaskAPI.platformUrl}/api/chaptersRead/updateMachine'
        body = {"host": TaskAPI.local_address,
                "state": state
                }
        return body, url, 'post'

    @api_requests(times=5, timeOut=15)
    def addReportData(book_id, chapter_id, p_url, des, type, role_id, chat_id):
        """
        获取单个报告记录接口API请求配置

        """
        url = f'{TaskAPI.platformUrl}/api/chaptersRead/addReportData'
        body = {"book_id": book_id,
                "chapter_id": chapter_id,
                "url": p_url,
                "desc": des,
                "type": type,
                "role_id": role_id,
                "chat_id": chat_id,
                }
        return body, url, 'post'