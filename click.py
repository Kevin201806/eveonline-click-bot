import codecs
import os
import re
import string
import time
import pyautogui
import numpy as np
from some_dict import glaxy_dict


# pyautogui样例
# https://blog.csdn.net/weixin_43430036/article/details/84650938
def write_and_click(x1, y1, write, speed):
    # 点击两次 绝对坐标
    pyautogui.click(x1, y1)
    pyautogui.click(x1, y1)
    # 输入"write"的内容 花费时间speed秒
    pyautogui.typewrite(message=str(write), interval=speed)
    # 按下/抬起enter键
    time.sleep(0.2)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    # 打印成功信息
    print("Seccess write " + str(write) + " on " + str(x1) + " " + str(y1))


# 从日志文件夹内取出最新的日志文件
def getname(path, specword):
    namelist = []
    for filename in os.listdir(path):
        if specword in filename:
            namelist.append(filename)
    # print(namelist)
    if len(namelist) == 1:
        return namelist[0]
    else:
        return namelist[-1]


# 判断是否为英文 是True 否False
def is_english_char(check_str):
    # print(check_str)
    punc = string.punctuation
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    for ch in check_str:
        if ch not in punc:
            match = zhPattern.search(ch)
            if match:
                return False
            else:
                return True


# 从读取日志并匹配最后一行
def take_log(Chatname, logpath):
    # 本地时间
    # today = str(datetime.date.today()).split("-")
    # 格林威治时间
    gmtimes = time.strftime("%Y-%m-%d/%H:%M:%S", time.gmtime(time.time())).split('/')[0].split('-')
    specword = str(Chatname + "_" + str(gmtimes[0] + gmtimes[1] + gmtimes[2]))
    with codecs.open(logpath + getname(logpath, specword), mode='r', encoding="utf_16_le") as f:  # 打开文件
        last_line = f.readlines()[-1]  # 取最后一行
        # print('最后一行为：' + last_line)
    talk_th = last_line.split(' > ')[1][0:-2].split(" ")
    return talk_th


# 匹配
def check_spec_word(talk_th, spec_word_list, Mask_list):
    # print(talk_th)
    # if check_contain_chinese(talk_th) == False:
    AAlist = []
    for A in talk_th:
        if A != '' or A != ' ':
            AAlist.append(A)
    typeB = False
    for AAAA in AAlist:
        if AAAA in spec_word_list:
            typeB = True
            # print(talk_th)
            break
    if typeB == True:
        print("含有关键词, 开始匹配: " + str(talk_th))
        galaxy = ""
        typeYZ = ""
        much = ""
        hour = ""
        for thi in AAlist:
            if thi in spec_word_list:
                typeYZ = thi
            elif is_english_char(thi) == True:
                # print(thi)
                if thi[-1] in punc:
                    thi = thi[0:-1]
                if thi in final_list1:
                    galaxy = thi
                elif len(thi) == 3 and thi[-1] in ["h", "H"]:
                    hour = thi
                elif len(thi) == 4 and thi[-2] in ["h", "H"]:
                    hour = thi
                elif len(thi) == 4 and thi[-1] in ["M", "m"]:
                    much = thi
                elif len(thi) == 3 and thi in ["200", "130", "140", "150", "210"]:
                    much = thi
                elif len(thi) == 7 and thi[3] in ["m","M"]:
                    much = thi
                elif len(thi) == 6 and thi[2] in ["H","h"] and thi[5] in ["M","m"]:
                    thi = time
        final_list = [galaxy, hour, much, typeYZ]
        print("匹配结果: " + str(final_list))
        return final_list


if __name__ == '__main__':
    punc = string.punctuation
    # 需要匹配的关键词
    spec_word_list = ["6/10", "10/10", "6-10", "10-10", "1010", "10", "maze", "Maze"]
    # EVE频道日志的绝对位置
    logpath = "c://users//18201//Documents//EVE//logs//Chatlogs//"
    # 如果存在列表内的词则忽略
    Mask_list = ["置顶", "野生", "预定", "测试", "维纳尔", "自己", "工具", "签约", "找个", "test", "有人", "出吗", "脚本", "出么", "野生"]
    # 频道名称
    chatname = "Escalation 静寂谷"
    ## 星系列表
    # 特布特 Tribute
    Tribute_list_ss = glaxy_dict["Tribute"]["glaxy_dict"]["ss"]
    Tribute_list_es = glaxy_dict["Tribute"]["glaxy_dict"]["es"]
    # 维纳尔 Venal
    Venal_list_ss = glaxy_dict["Venal"]["glaxy_dict"]["ss"]
    Venal_list_es = glaxy_dict["Venal"]["glaxy_dict"]["es"]
    # 寂静谷 Vale_of_the_Silent
    Vale_of_the_Silent_list_ss = glaxy_dict["Vale_of_the_Silent"]["glaxy_dict"]["ss"]
    Vale_of_the_Silent_list_es = glaxy_dict["Vale_of_the_Silent"]["glaxy_dict"]["es"]
    # 对舞之域 Geminate
    Geminate_list_ss = glaxy_dict["Geminate"]["glaxy_dict"]["ss"]
    Geminate_list_es = glaxy_dict["Geminate"]["glaxy_dict"]["es"]
    # 拼接列表并去重 寂静谷+维纳尔+特布特+对舞
    final_list1 = list(set(Tribute_list_ss + Tribute_list_es +
                        Vale_of_the_Silent_list_ss + Vale_of_the_Silent_list_es + \
                        Venal_list_es + Venal_list_ss + \
                        Geminate_list_ss + Geminate_list_es))
    # 拼接列表并去重 寂静谷 + 特布特
    final_list2 = list(set(Tribute_list_ss + Tribute_list_es +
                           Vale_of_the_Silent_list_ss + Vale_of_the_Silent_list_es))
    while True:
        gmtimes = time.strftime("%Y-%m-%d/%H:%M:%S", time.gmtime(time.time()))
        talk_th = take_log(chatname, logpath)
        final_list = check_spec_word(talk_th, spec_word_list, Mask_list)
        if final_list != None:
            # print(final_list)
            galaxy, hour, much, typeYZ = final_list[0], final_list[1], final_list[2], final_list[3]
            default_choice = True
            if hour != "":
                if int(hour[0:2]) <= 12 or int(hour[0:2]) > 24:
                    default_choice = False
            if much != "":
                if int(much[0:3]) < 60 or int(much[0:3]) > 240:
                    # print(much[0:3])
                    default_choice = False
            # if galaxy not in final_list1:
            #     default_choice = False
            num0 = 0
            for sth in final_list:
                if sth != "":
                    num0 += 1
            # print(default_choice)
            rand_num = float(str(np.random.uniform(0.5,1))[0:3])
            if default_choice == True and num0 >= 2:
                print("条件成立，判定是否为指定远征: " + str(final_list))
                if typeYZ != "" and galaxy != "":
                    if "6" not in final_list[3]:
                        print("是10/10，开始点击")
                        write_and_click(2303, 611, "1", rand_num)
                        write_and_click(617, 612, "1", rand_num)
                        time.sleep(5)
                        os.system("hp.wav")
                    # else:
                    #     write_and_click(373, 609, "1", rand_num)
                    #     time.sleep(5)
                    #     os.system("hp.wav")
                # write_and_click(394, 609, "1", 0.8)
                with open("point_his.txt", "a") as point_his:
                    point_his.write(str(gmtimes) + "\n")
                    point_his.write(str(final_list) + "\n")
                    point_his.close()
                # print(final_list)
                # os.system("hp.wav")
                time.sleep(10)
                # break
            # break

# 测试专用行 用来切换回IDE
# pyautogui.click(2840,476)
