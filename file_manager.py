# coding:utf-8
import os


class FileManager(object):
    def __init__(self):
        pass

    def genPath(self, model, set, basePath):
        path = basePath+model+"/"+set+"/"
        path = path.strip()

        isExists = os.path.exists(path)

        if not isExists:
            os.makedirs(path)
            print path + " 目录创建成功\n"
            return path
        else:
            print path + ' 目录已存在\n'
            return False