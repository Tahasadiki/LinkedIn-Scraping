import requests
from bs4 import BeautifulSoup
from itertools import cycle

def get_page_links(url,proxy):
    params = {}

    headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    params["headers"]=headers

    if proxy:
        proxies={"http":proxy,"https":proxy}
        params["proxies"]=proxies

    linkedin_urls=[]
    try:
        search_result = requests.get(url,**params)
        if search_result.status_code!=200:
            raise(Exception(search_result.status_code))

        soup = BeautifulSoup(search_result.content,features="lxml")
        child_divs = soup.find_all("div",{"class":"TbwUpd"})
        linkedin_urls = [child_div.find_parent("a").get("href") for child_div in child_divs]
    except Exception as e:
        raise(e)

    return linkedin_urls

def get_proxy_pool(proxies):
    if proxies:
        return cycle(proxies)
    else:
        return None

def get_profiles_links(query,proxies):
    start=0
    linkedin_urls = []
    proxy_pool=get_proxy_pool(proxies)

    proxy=None
    try:
        proxy= next(proxy_pool)
    except Exception:
        print("[-] Proxy list is empty")

    arguments=""
    for key,value in query.arguments:
            arguments+=f"&{key}={value}"

    while True:
        url = f"https://www.google.com/search?q={query.q}&num={query.num}&start={start}{arguments}"
        retries=1 
        if proxy_pool:
            retries=98

        while retries>0:
            try:
                print(proxy)
                page_links = get_page_links(url,proxy)
                break
            except Exception:
                print(f"[-] proxy {proxy} FAILED")
                proxy=next(proxy_pool)
                retries-=1
            

        if page_links:
            linkedin_urls.extend(page_links)
            print(f"[+] #profiles: {len(linkedin_urls)}")
            start+=query.num
        else:
            break
    return linkedin_urls