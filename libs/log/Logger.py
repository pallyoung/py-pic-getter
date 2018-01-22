import types;
import time;
from enum import Enum;

from libs.util import file as fileUtil;


def generator_storageFunc(path):
    print()
    def func(level):
        return path;
    return func;


class LOGGER_LEVEL(Enum):
    E='E';
    W='W';
    D='D';
    I='I';

class Logger:

    def __init__(self,storageFunc=''):
        self.tag = '';
        self.setStorage(storageFunc);

    def debug(self,message):
        level = LOGGER_LEVEL.D.value;

        self.__print(level,message);
    def waring(self,message):
        level = LOGGER_LEVEL.W.value;

        self.__print(level, message);

    def info(self, message):
        level = LOGGER_LEVEL.I.value;

        self.__print(level, message);

    def error(self, message):
        level = LOGGER_LEVEL.E.value;

        self.__print(level, message);

    def setStorage(self,storageFunc):
        arg_type = type(storageFunc);

        if(arg_type is types.FunctionType):
            self.__storageFunc = storageFunc;
        elif(arg_type==type('')):
            self.__storageFunc = generator_storageFunc(storageFunc);
    def __mk_message(self,level,message):
        time_str =  time.strftime("%Y-%m-%d-%H-%M-%S" ,time.localtime(time.time()));
        return r'%s %s %s:%s'%(level,self.tag,time_str, message);

    def __print(self,level,message):
        message = self.__mk_message(level, message);
        print(message);
        self.__storage(level,message);

    def __storage(self,level,message):
        if(self.__storageFunc):
            storagePath = self.__storageFunc(level);
            if(storagePath):
                file = fileUtil.open_file(storagePath,'a+',newline='\r');
                file.write(message+'\r\n');
                file.close();





