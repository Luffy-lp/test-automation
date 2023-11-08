import multiprocessing


def init():
    multiprocessing.freeze_support()
    manager = multiprocessing.Manager()
    # pool = multiprocessing.Pool(processes=5)
    shared_queue = manager.Queue()
    shared_dict = manager.dict()
    shared_list = manager.list()
    shared_queue.put('111')
    shared_queue.put('222')
    shared_queue.put('333')
    shared_queue.put('444')
    shared_queue.put('555')
    shared_queue.put('666')
    shared_queue.put('777')
    return shared_queue, shared_dict, shared_list

def chapters_reading():
    pass