from airtest.core.api import touch
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.unity3d import UnityPoco
from common.my_logger import mylog


class POCO():
    poco = None
    rpcClient = None
    def __init__(self,screens,ADBdevice,device=None):
        self.screens=screens
        self.ADBdevice = ADBdevice
        self.apoco = AndroidUiautomationPoco(device=device)
        self.poco = UnityPoco(device=device)
        self.rpcClient = self.poco.myClient
        if ADBdevice in screens:
            self.poco.use_render_resolution(True, screens[ADBdevice])

    def __new__(cls, *args, **kwargs):
        if not hasattr(POCO, "_instance"):
            if not hasattr(POCO, "_instance"):
                POCO._instance = object.__new__(cls)
        return POCO._instance

    # def google_tryfind(self):
    #     """尝试寻找，不一定存在"""
        # if self.ADBdevice == "SKSVB20515004696":
        #     touch([500, 500])
        # try:
        #     mylog.debug("尝试寻找{0}".format("谷歌框架提醒"))
        #     if self.apoco("android:id/button1").exists():
        #         # self.apoco("android:id/button1").click()
        #         touch[500,500]
        #         mylog.debug("发现{0}".format("谷歌框架提醒"))
        # except Exception as e:
        #     mylog.debug(e)