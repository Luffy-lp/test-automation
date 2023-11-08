from init_process import *
from start_process import *


if __name__ == '__main__':
    shared_queue, shared_dict, shared_list = init()
    processes = []
    for taskDate in TaskData.taskDatas.items():
        my_process = run_tasks(taskDate, args=(shared_queue, shared_dict, shared_list))  # 创建多进程任务
        my_process.start()
        processes.append(my_process)
    for p in processes:
        p.join()
        # my_processte # 关闭进程任务.termina
    print("All workers have finished")