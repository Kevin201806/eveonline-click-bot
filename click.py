import codecs
import os
import time
import playsound
import pyautogui


# pyautogui样例
# https://blog.csdn.net/weixin_43430036/article/details/84650938
def write_and_click(x1, y1, write):
    # 点击两次 绝对坐标
    pyautogui.click(x1, y1)
    pyautogui.click(x1, y1)
    # 输入"write"的内容 花费时间0.7s
    pyautogui.typewrite(message=str(write), interval=0.7)
    # 按下/抬起enter键
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

# 判断字符串是否包含中文
# def check_contain_chinese(check_str):
#     for ch in check_str.decode('utf-8'):
#         if u'\u4e00' <= ch <= u'\u9fff':
#             return True
#     return False

# 从读取日志并匹配最后一行
def take_log(Chatname, spec_word_list, logpath, Mask_list):
    # 本地时间
    # today = str(datetime.date.today()).split("-")
    # 格林威治时间
    gmtimes = time.strftime("%Y-%m-%d/%H:%M:%S", time.gmtime(time.time())).split('/')[0].split('-')
    specword = str(Chatname + "_" + str(gmtimes[0] + gmtimes[1] + gmtimes[2]))
    with codecs.open(logpath + getname(logpath, specword), mode='r', encoding="utf_16_le") as f:  # 打开文件
        last_line = f.readlines()[-1]  # 取最后一行
        # print('最后一行为：' + last_line)
    talk_th = last_line.split(' > ')[1][0:-2].split(" ")
    # if check_contain_chinese(talk_th) == False:
    for word in spec_word_list:
        if word in talk_th:
            typeA = True
            for word2 in Mask_list:
                for word3 in talk_th:
                    if word2 in word3:
                        typeA = False
            if typeA == True:
                print(talk_th)
                return "click"

if __name__ == '__main__':

    # 需要匹配的关键词
    # spec_word_list = ["6/10", "10/10", "6-10", "10-10", "1010"]
    spec_word_list = ["10/10", "10-10","1010"]
    # EVE频道日志的绝对位置
    logpath = "c://users//18201//Documents//EVE//logs//Chatlogs//"
    # 如果存在列表内的词则忽略
    mask_list = ["置顶","野生","预定","测试","维纳尔","自己","工具","签约","找个","test","有人","出吗","脚本","出么"]
    # 频道名称
    chatname = "Escalation 静寂谷"
    while True:
        AAA = take_log(chatname, spec_word_list, logpath, mask_list)
        if AAA == "click":
            # 在屏幕的绝对坐标输入1
            write_and_click(390, 593, "1")
            break
        # time.sleep(0.2)
    # 检测到则播放音频 可以选择wav/mp3格式的
    playsound.playsound('hp.wav')

# 测试专用行 用来切换回IDE
# pyautogui.click(2840,476)
