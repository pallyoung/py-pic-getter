from libs.spider import HttpClient;

INDEX = 'https://cn.bing.com/images/trending'

headers = {
    'origin':'https://cn.bing.com',
    'referer':'https://cn.bing.com/',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
httpClient = HttpClient.HttpClient(INDEX,headers=headers);

print(httpClient.send().read().decode('utf-8'))
