from task.taskAPI import TaskAPI


class TaskManage():
    """

    获取任务配置

    """

    def __init__(self, taskInfo, devices, taskType=0):
        self.taskType = taskType  # 阅读
        self.devices = devices
        self.taskId = self.add_task(taskInfo, taskType, task_state=0)  # TODO 任务需要增加（任务类型 任务状态，任务详情）返回任务ID

    def add_task(taskInfo, taskType, task_state=1):
        """
        添加任务

        """
        return TaskAPI.addMachineTask(taskInfo, task_state=task_state)

    def update_task(self, taskId, taskInfo, task_state):
        """

        更新任务

        """
        return TaskAPI.updateMachineTask(taskId, taskInfo, task_state=task_state)

    def execute_tasks(self): ...  # 执行任务

    def pause_tasks(self): ...  # 暂停任务
