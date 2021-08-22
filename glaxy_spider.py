import codecs
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

def get_glaxy_list(star_field_url, proxies=None, timeout=None, headers=headers):
    # get htmlhandls
    # https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len
    htmlhandls = requests.get(star_field_url, proxies=proxies, timeout=timeout, headers=headers).text
    soup = BeautifulSoup(htmlhandls, "html.parser")
    # codecs.open("html.html", 'w', 'utf-8').write(str(soup))
    div_comicdetail = soup.find(name="svg").find(name="g",attrs={"id":"map"}).find(name="defs").find_all("symbol")
    codecs.open("html.html", 'w', 'utf-8').write(str(div_comicdetail))
    glaxy_dict = {"ss":[],"es":[]}
    for glaxy in div_comicdetail:
        # soup = BeautifulSoup(glaxy, "html.parser")
        if glaxy.find(name="a"):
            a = glaxy.find(name="a")
            # print(a)
            if a.find(name="text",attrs={"class":"ss"}):
                ss = a.find(name="text",attrs={"class":"ss"}).string
                glaxy_dict["ss"].append(ss)
                # print(ss)

            elif a.find(name="text",attrs={"class":"es"}):
                es = a.find(name="text",attrs={"class":"es"}).string
                glaxy_dict["es"].append(es)
                # print(es)
    return glaxy_dict

def creat_star_field_dic(url):
    htmlhandls = requests.get(url, proxies=None, timeout=None, headers=headers).content
    soup = BeautifulSoup(htmlhandls, "html.parser")
    # print(soup)
    # codecs.open("html.html", 'w', 'utf-8').write(str(soup))
    div_comicdetail = soup.find("body").find(name='div', attrs={"id": "outer"}).find(name='div', attrs={"id": "body"}). \
        find(name="div", attrs={"class": "clearfix"}).find(name="div", attrs={"id": "col_main"}). \
        find(name="div", attrs={"id": "inner"}).find(name="div", attrs={"class": "listmaps"}). \
        find(name="ul", attrs={"class": "clearbox"}).find_all(name="li")
    url_dict = {}
    # num = 0
    for star_field in div_comicdetail:
        # add_url = star_field.find(name="a").attrs["href"]
        star_field_name = star_field.find(name="a").string
        # url_dict[star_field_name] = {"url":url + add_url}
        url_dict[star_field_name] = {"url": url + "/svg/" + star_field_name + ".svg"}
    return url_dict


if __name__ == '__main__':
    # 获取星域网址字典
    map_basic_url = "https://evemaps.dotlan.net"
    url_dict = creat_star_field_dic(map_basic_url)

    # 为节省时间,直接将字典写于此

    # 创建星系列表
    for name in url_dict:
        url = url_dict[name]["url"]
        print(name + ": " + url)
        glaxy_dict = get_glaxy_list(url)
        url_dict[name]["glaxy_dict"] = glaxy_dict
    print(glaxy_dict)

