import codecs
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}


# def creat_xlsx_file(dict,filename):
#     wb = Workbook()
#     ws = wb.active
#     ws1 = wb.create_sheet('star_field', 0)
#

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
    # map_basic_url = "https://evemaps.dotlan.net"
    # url_dict = creat_star_field_dic(map_basic_url)

    # 为节省时间,直接将字典写于此
    url_dict = {'Aridia': {'url': 'https://evemaps.dotlan.net/svg/Aridia.svg'},
                'Black_Rise': {'url': 'https://evemaps.dotlan.net/svg/Black_Rise.svg'},
                'The_Bleak_Lands': {'url': 'https://evemaps.dotlan.net/svg/The_Bleak_Lands.svg'},
                'Branch': {'url': 'https://evemaps.dotlan.net/svg/Branch.svg'},
                'Cache': {'url': 'https://evemaps.dotlan.net/svg/Cache.svg'},
                'Catch': {'url': 'https://evemaps.dotlan.net/svg/Catch.svg'},
                'The_Citadel': {'url': 'https://evemaps.dotlan.net/svg/The_Citadel.svg'},
                'Cloud_Ring': {'url': 'https://evemaps.dotlan.net/svg/Cloud_Ring.svg'},
                'Cobalt_Edge': {'url': 'https://evemaps.dotlan.net/svg/Cobalt_Edge.svg'},
                'Curse': {'url': 'https://evemaps.dotlan.net/svg/Curse.svg'},
                'Deklein': {'url': 'https://evemaps.dotlan.net/svg/Deklein.svg'},
                'Delve': {'url': 'https://evemaps.dotlan.net/svg/Delve.svg'},
                'Derelik': {'url': 'https://evemaps.dotlan.net/svg/Derelik.svg'},
                'Detorid': {'url': 'https://evemaps.dotlan.net/svg/Detorid.svg'},
                'Devoid': {'url': 'https://evemaps.dotlan.net/svg/Devoid.svg'},
                'Domain': {'url': 'https://evemaps.dotlan.net/svg/Domain.svg'},
                'Esoteria': {'url': 'https://evemaps.dotlan.net/svg/Esoteria.svg'},
                'Essence': {'url': 'https://evemaps.dotlan.net/svg/Essence.svg'},
                'Etherium_Reach': {'url': 'https://evemaps.dotlan.net/svg/Etherium_Reach.svg'},
                'Everyshore': {'url': 'https://evemaps.dotlan.net/svg/Everyshore.svg'},
                'Fade': {'url': 'https://evemaps.dotlan.net/svg/Fade.svg'},
                'Feythabolis': {'url': 'https://evemaps.dotlan.net/svg/Feythabolis.svg'},
                'The_Forge': {'url': 'https://evemaps.dotlan.net/svg/The_Forge.svg'},
                'Fountain': {'url': 'https://evemaps.dotlan.net/svg/Fountain.svg'},
                'Geminate': {'url': 'https://evemaps.dotlan.net/svg/Geminate.svg'},
                'Genesis': {'url': 'https://evemaps.dotlan.net/svg/Genesis.svg'},
                'Great_Wildlands': {'url': 'https://evemaps.dotlan.net/svg/Great_Wildlands.svg'},
                'Heimatar': {'url': 'https://evemaps.dotlan.net/svg/Heimatar.svg'},
                'Immensea': {'url': 'https://evemaps.dotlan.net/svg/Immensea.svg'},
                'Impass': {'url': 'https://evemaps.dotlan.net/svg/Impass.svg'},
                'Insmother': {'url': 'https://evemaps.dotlan.net/svg/Insmother.svg'},
                'Kador': {'url': 'https://evemaps.dotlan.net/svg/Kador.svg'},
                'The_Kalevala_Expanse': {'url': 'https://evemaps.dotlan.net/svg/The_Kalevala_Expanse.svg'},
                'Khanid': {'url': 'https://evemaps.dotlan.net/svg/Khanid.svg'},
                'Kor-Azor': {'url': 'https://evemaps.dotlan.net/svg/Kor-Azor.svg'},
                'Lonetrek': {'url': 'https://evemaps.dotlan.net/svg/Lonetrek.svg'},
                'Malpais': {'url': 'https://evemaps.dotlan.net/svg/Malpais.svg'},
                'Metropolis': {'url': 'https://evemaps.dotlan.net/svg/Metropolis.svg'},
                'Molden_Heath': {'url': 'https://evemaps.dotlan.net/svg/Molden_Heath.svg'},
                'Oasa': {'url': 'https://evemaps.dotlan.net/svg/Oasa.svg'},
                'Omist': {'url': 'https://evemaps.dotlan.net/svg/Omist.svg'},
                'Outer_Passage': {'url': 'https://evemaps.dotlan.net/svg/Outer_Passage.svg'},
                'Outer_Ring': {'url': 'https://evemaps.dotlan.net/svg/Outer_Ring.svg'},
                'Paragon_Soul': {'url': 'https://evemaps.dotlan.net/svg/Paragon_Soul.svg'},
                'Period_Basis': {'url': 'https://evemaps.dotlan.net/svg/Period_Basis.svg'},
                'Perrigen_Falls': {'url': 'https://evemaps.dotlan.net/svg/Perrigen_Falls.svg'},
                'Placid': {'url': 'https://evemaps.dotlan.net/svg/Placid.svg'},
                'Pochven': {'url': 'https://evemaps.dotlan.net/svg/Pochven.svg'},
                'Providence': {'url': 'https://evemaps.dotlan.net/svg/Providence.svg'},
                'Pure_Blind': {'url': 'https://evemaps.dotlan.net/svg/Pure_Blind.svg'},
                'Querious': {'url': 'https://evemaps.dotlan.net/svg/Querious.svg'},
                'Scalding_Pass': {'url': 'https://evemaps.dotlan.net/svg/Scalding_Pass.svg'},
                'Sinq_Laison': {'url': 'https://evemaps.dotlan.net/svg/Sinq_Laison.svg'},
                'Solitude': {'url': 'https://evemaps.dotlan.net/svg/Solitude.svg'},
                'The_Spire': {'url': 'https://evemaps.dotlan.net/svg/The_Spire.svg'},
                'Stain': {'url': 'https://evemaps.dotlan.net/svg/Stain.svg'},
                'Syndicate': {'url': 'https://evemaps.dotlan.net/svg/Syndicate.svg'},
                'Tash-Murkon': {'url': 'https://evemaps.dotlan.net/svg/Tash-Murkon.svg'},
                'Tenal': {'url': 'https://evemaps.dotlan.net/svg/Tenal.svg'},
                'Tenerifis': {'url': 'https://evemaps.dotlan.net/svg/Tenerifis.svg'},
                'Tribute': {'url': 'https://evemaps.dotlan.net/svg/Tribute.svg'},
                'Vale_of_the_Silent': {'url': 'https://evemaps.dotlan.net/svg/Vale_of_the_Silent.svg'},
                'Venal': {'url': 'https://evemaps.dotlan.net/svg/Venal.svg'},
                'Verge_Vendor': {'url': 'https://evemaps.dotlan.net/svg/Verge_Vendor.svg'},
                'Wicked_Creek': {'url': 'https://evemaps.dotlan.net/svg/Wicked_Creek.svg'}}
    for name in url_dict:
        url = url_dict[name]["url"]
        print(name + ": " + url)
        glaxy_dict = get_glaxy_list(url)
        url_dict[name]["glaxy_dict"] = glaxy_dict
        # break
    print(url_dict)