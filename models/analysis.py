import re
# from common.utils import *
from models.pathsData import *

class Analysis():
    """解析用例"""
    function_regexp = re.compile(r"^\$\{(\w+)\(([\$\w =,]*)\)\}$")
    stepdata_list = []
    index = 0
    Case_dir = {}
    popup_list = []
    cases = []
    path = None
    case_info = {}

    def file_name(self):
        """解析当前路径的目录"""
        path = os.path.join(path_config_DIR, "yamlCase")
        for root, dirs, files in os.walk(path):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录
            # print(files) #当前路径下所有非目录子文件
            filesName = files[0].split(".yml")[0]
            self.case_info["casename"] = filesName
            self.path = os.path.join(path, files[0])

    # def is_functon(self, content):
    #     matched = self.function_regexp.match(content)
    #     return True if matched else False

    def parse_function(self, content):
        """解析字符串"""
        function_meta = {
            "args": [],
            "kwargs": {}
        }
        matched = self.function_regexp.match(content)
        function_meta["func_name"] = matched.group(1)

        args_str = matched.group(2).replace(" ", "")
        if args_str == "":
            return function_meta

        args_list = args_str.split(',')
        for arg in args_list:
            if '=' in arg:
                key, value = arg.split('=')
                function_meta["kwargs"][key] = value
            else:
                function_meta["args"].append(arg)

        return function_meta

    # def is_function(self, tup):
    #     """ Takes (name, object) tuple, returns True if it is a function.
    #     """
    #     name, item = tup
    #     if isinstance(item, types.FunctionType):
    #         aa = eval(str(item.__name__))
    #     return

    # def import_module_functions(self, modules):
    #     """ import modules and bind all functions within the context
    #     """
    #     for module_name in modules:
    #         imported = importlib.import_module(module_name)
    #         imported_functions_dict = dict(filter(self.is_function, vars(imported).items()))
    #     return imported_functions_dict

    def yaml_case(self):
        """解析yamlcase数据"""
        function_meta = {
            "func_name": None,
            "args": [],
            "kwargs": {}
        }
        yamldata_dir = read_yaml(self.path)
        for i, val in yamldata_dir.items():
            dir = {}
            dir.update({"casename": val["casename"]})
            dir.update({"casedec": val["casedec"]})
            dir.update({"reportname": val["reportname"]})
            dir.update({"caseauthor": val["caseauthor"]})
            dir.update({"repeattime": int(val["repeattime"])})
            self.case_info[i] = dir
            caselist = yamldata_dir[i]["step"]
            for k in range(0, len(caselist)):
                function_meta = self.parse_function(caselist[k])
                function_meta["func_name"] = function_meta['func_name']
                function_meta["args"] = function_meta['args']
                function_meta["kwargs"] = function_meta['kwargs']
                self.stepdata_list.append(function_meta)
            self.Case_dir[i] = self.stepdata_list
            self.stepdata_list = []
        return self.case_info

    def yaml_data_popup(self):
        """解析弹框数据"""
        popup_list=[]
        popup_dir={}
        function_meta = {
            "popup_name": None,
            "element": [],
            "kwargs": {}
        }
        yamldatalist = read_yaml(os.path.join(path_config_DIR, "yamlGame/popup.yml"))
        for i in range(0, len(yamldatalist)):
            # self.index = i
            caselist = yamldatalist[i][i]["step"]
            for k in range(0, len(caselist)):
                thefunction_meta = self.parse_function(caselist[k])
                function_meta["Popupname"] = thefunction_meta['func_name']
                function_meta["element"] = thefunction_meta['args']
                function_meta["kwargs"] = thefunction_meta['kwargs']
                popup_list.append(thefunction_meta)
                popup_dir[i] = popup_list
            popup_list = []
        return popup_dir

    def getrunlist(self):
        Runlist_dir={}
        for k, var in self.Case_dir.items():
            for i in range(0, len(var)):
                args = var[i]["args"]
                func_name = var[i]["func_name"]
                item = {"args": args, "func_name": func_name}
                self.cases.append(item)
                Runlist_dir[k] = self.cases
            self.cases = []
        return  Runlist_dir

# MyAnalysis1=Analysis()
# MyAnalysis1.yaml_case()
