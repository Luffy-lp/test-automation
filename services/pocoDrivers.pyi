from poco.drivers.unity3d import UnityPoco

__all__ = ['find_Object','click_object']

poco:UnityPoco = None
def test(poco:UnityPoco):...
def find_Object(*objectName,**ObjectSet):...
def UnityPoco_find(*objectName,**ObjectSet):...
def click_object(*objectName, **objectSet):...
def UnityPoco_click(*objectName, **objectSet):...
def AndroidPoco_click(*objectName, **objectSet):...