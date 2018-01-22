from libs import prepare_env;
from libs.source import baidu;
from libs.util import file;

import urllib.request as request;
from PIL import Image
import io;
import base64;
import time;


pn = 0;
rn = 30;

TEMP = 'temp'

prepare_env.prepare(TEMP);

provider = baidu.Provider();


def image_scale(url):
    provider.img(url,show_imag);

def show_imag(data):
    f = file.open_file(TEMP+'/'+str(time.time())+'.jpg',mode='w+b');
    f.write(data);
    # img = Image.open(f);
    # img.show();
    f.close();



def success(result):
    global pn;
    pn = pn + result['num'];
    for img in result['imgs']:
        image_scale(img['url']);


def serach(word,width=None,height=None):
    provider.search(word,pn,rn,callback=success,width=width,height=height);

serach('明星',width=1080,height=1920);