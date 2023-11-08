from poco.utils.simplerpc.utils import sync_wrapper

@sync_wrapper
def get_UserID(rpcClient):
    return rpcClient.call("GetUserID")

@sync_wrapper
def get_ReadProgress(rpcClient):
    return rpcClient.call("GetReadProgress")

@sync_wrapper
def get_ReadChapterID(rpcClient):
    return rpcClient.call("GetReadChapterId")

@sync_wrapper
def get_Music(rpcClient):
    return rpcClient.call("GetMusic")