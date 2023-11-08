from common.my_logger import mylog
from common.utils import timing_decorator

# from poco.exceptions import PocoNoSuchNodeException
# from common.comerror import ResourceError

__all__ = ['find_Object','click_object']

def default_find(*objectName, **ObjectSet): ...

def get_attr(prefab, attrType):
    texture = prefab.attr(attrType)
    return texture

@timing_decorator
def find_Object(*objectName, **objectSet):
    if objectSet.get("poco") is None:
        raise TypeError("缺少poco参数")
    if objectSet.get('type') is not None:
        type = objectSet['type']
    else:
        type = "UnityPoco"
    if objectSet.get("des") is not None:
        des = objectSet["des"]
        mylog.info("【find_Object】:{}".format(des))
    switch_dict = {
        "UnityPoco": UnityPoco_find,
        "AndroidPoco": AndroidPoco_find,
        "default": default_find
    }
    result = switch_dict.get(type, switch_dict["default"])(*objectName, **objectSet)
    return result

def UnityPoco_find(*objectName, **objectSet):
    poco = objectSet['poco']
    result =poco(objectName[0]).exists() if len(objectName) == 1 else poco(objectName[1]).offspring(
        objectName[0]).exists()
    return result

def click_object(*objectName, **objectSet):
    if objectSet.get("poco") is None:
        raise TypeError("缺少poco参数")
    if objectSet.get('type') is not None:
        type = objectSet['type']
    else:
        type = "UnityPoco"
    if objectSet.get("des") is not None:
        des = objectSet["des"]
        mylog.info("【click_object】:{}".format(des))
    switch_dict = {
        "UnityPoco": UnityPoco_click,
        "AndroidPoco": AndroidPoco_click,
        "default": default_find
    }
    result = switch_dict.get(type, switch_dict["default"])(*objectName, **objectSet)
    return result

def UnityPoco_click(*objectName, **objectSet):
    poco = objectSet['poco']
    if len(objectName) == 1:
        if poco(objectName[0]).exists():
            poco(objectName[0]).click()
        else:
            mylog.info("未找到{}".format(objectName[0]))
    else:
        poco(objectName[1]).offspring(objectName[0]).click()

def AndroidPoco_click(*objectName, **objectSet): ...
def AndroidPoco_find(*objectName, **ObjectSet): ...