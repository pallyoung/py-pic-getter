from libs.spider import HttpClient;
import urllib
import json;
import time;

HOST = "http://image.baidu.com/";
HEADERS = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
PATH = {
    "search":r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&ie=utf-8&oe=utf-8&lm=-1",
    'items':'http://image.baidu.com/channel/listjson?ie=utf8'
}


class Provider():

    def __search_success(self,body,callback):
        body = json.loads(body.decode('utf-8'));
        data = body['data'];
        result = {}
        imgs = [];
        for img in data:
            if 'replaceUrl' in img:
                imgs.append({
                    'url': img['replaceUrl'][0]['ObjURL']
                });
            elif 'largeTnImageUrl' in img and img['largeTnImageUrl']:
                imgs.append({
                    'url': img['largeTnImageUrl']
                });
            elif 'middleURL' in img:
                imgs.append({
                    'url':img['middleURL']
                });
        result['imgs']=imgs;
        result['num']=len(imgs);

        if callback:
            callback(result)

    def img(self,url,callback):
        http_client = HttpClient.HttpClient(url);
        http_client.headers = HEADERS;
        http_client.on_success(callback);
        http_client.send();

    def search(self,word,pn=0,rn=30,callback=None,width=None,height=None):

        word = urllib.parse.quote(word);
        url = r"%s&queryWord=%s&word=%s&pn=%i&rn=%i" % (PATH['search'],word,word, pn, rn);
        if width:
            url = r"%s&width=%i"%(url,width);
        if height:
            url = r"%s&height=%i"%(url,height);

        http_client = HttpClient.HttpClient(url);
        http_client.headers = HEADERS;
        http_client.on_success(lambda body:self.__search_success(body,callback));
        http_client.send();

    def items(self,pn=0,rn=30,**kwargs):
        tag_string = "";
        tags = kwargs['tags'];
        for index in range(len(tags)):
            tag_string="%s&tag%i=%s"%(tag_string,index+1,urllib.parse.quote(tags[index]) );
        url = "%s&pn=%i&rn=%i%s" % (PATH['items'],pn,rn,tag_string);
        http_client = HttpClient.HttpClient(url);
        http_client.headers = HEADERS;
        http_client.on_success( lambda body: print(body));
        http_client.send();
