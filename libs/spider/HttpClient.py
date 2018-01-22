import urllib;
import urllib.request as request;
import socket;
import ssl;
import traceback
import json;
import threading;
import time;
import urllib.response as Response;

ssl._create_default_https_context = ssl._create_unverified_context


class HttpHeaders:
    def __init__(self):
        self.__headers = {}

    def append(self, key, value):
        self.__headers[key] = value;

    def get(self, key):
        return self.__headers[key];

    def value(self):
        return self.__headers;


class HttpClient:
    def __init__(self, url):
        self.__success = None;
        self.__error = None;
        self.__timeout = None;

        '''
        默认一分钟超时
        '''
        self.timeout = 60;
        '''
        默认get
        '''
        self.method = 'GET';

        self.url = url;
        self.headers = {};
        self.response = None;

    def on_success(self, success_callback):
        self.__success = success_callback;
        return self;

    def onerror(self, error_callback):
        self.__error = error_callback;

    def on_timeout(self, timeout_callback):
        self.__timeout = timeout_callback;

    def send(self, data=None):
        c_request = request.Request(self.url,data=data,headers=self.headers,method=self.method);
        try:
            self.response = request.urlopen(c_request,timeout=self.timeout);

            result = self.response.read();

            if self.__success:
                self.__success(result);
        except urllib.error.URLError as err:
            traceback.print_exc()

            if isinstance(err.reason,socket.timeout):
                if self.__timeout:
                    self.__timeout();
                else:
                    traceback.print_exc();
        except BaseException as err:
            traceback.print_exc();
            if isinstance(err,socket.timeout):
                if self.__timeout:
                    self.__timeout();
                elif self.__error:
                    self.__error(err);
                else:
                    traceback.print_exc();

