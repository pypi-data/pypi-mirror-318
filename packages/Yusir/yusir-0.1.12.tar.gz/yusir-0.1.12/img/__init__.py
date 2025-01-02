import calendar
import datetime
import os
import subprocess
import sys
import time
import pyautogui as pa
import pyperclip


def get_first_and_last_day():
    """return返回【当天、本月第一天和本月最后一天】的日期列表"""
    today = datetime.date.today()
    year = today.year
    month = today.month
    first_day = today.replace(day=1)
    last_day = today.replace(day=calendar.monthrange(year, month)[1])
    return [today, first_day, last_day]


def get_file_modified_date(file_path):
    """
    :param file_path: 文件完整路径
    :return: 文件修改日期
    """
    timestamp = os.stat(file_path)
    modified_time = datetime.datetime.fromtimestamp(timestamp.st_mtime)
    return modified_time


def flag(f1, f2):
    """
    :param f1: 文件1的路径
    :param f2: 文件2的路径
    :return:若文件修改时间等于当前时间则返回flag
    """
    erp = get_file_modified_date(f1).strftime('%Y%m%d%H')
    hd = get_file_modified_date(f2).strftime('%Y%m%d%H')
    th = datetime.datetime.now().strftime('%Y%m%d%H')
    if erp == th and hd == th:
        return 'flag'


def locate_pic(path, match=0.85, repeat_count=77):
    """
    :param repeat_count: 重试次数，默认77次
    :param match: 匹配度，默认0.85
    :param path: 图片路径locate_pic(r'x.png')
    :return: 返回当前图片的坐标(x,y)
    """
    for cnt in range(repeat_count):
        try:
            time.sleep(1.5)
            return pa.locateOnScreen(path, confidence=match)
        except Exception as e:
            print(f"{path.split('\\')[-1]} try again...{e}")
            time.sleep(1.5)
            continue
    sys.exit()


def wx_search_user(username, img_path):
    """
    搜索用户,并点击搜索到的用户，以便切换到用户界面
    :param img_path: 图片文件目录
    :param username: 微信用户名
    :return:
    """
    for i in ['C:\\Program Files', 'D:\\Program Files', 'C:\\Program Files (x86)']:
        try:
            subprocess.Popen(fr'{i}\Tencent\WeChat\WeChat.exe')
            break
        except WindowsError:
            print(f'程序不在{i}\\Tencent\\WeChat\\WeChat.exe中')
    loc_user = locate_pic(fr'{img_path}\user.png')
    pa.click(loc_user.left + 77, loc_user.top + 12)
    pyperclip.copy(username)
    time.sleep(1)
    pa.hotkey('ctrl', 'v')
    time.sleep(1.5)
    pa.click(loc_user.left + 77, loc_user.top + 98)


def send_msg_text(ps):
    """param ps: {'user': '微信用户名', 'msg': '要发送的文本内容','img_path':'图片所在目录'}"""
    wx_search_user(ps['user'], fr'{ps["img_path"]}')  # 搜索用户并切换到用户界面
    # 点击文本输入框，并输入需要发送的文本内容和点击发送按钮
    loc_msg = locate_pic(fr'{ps["img_path"]}\msg.png')
    pa.click(loc_msg.left + 100, loc_msg.top + 77)
    pyperclip.copy(ps['msg'])
    pa.hotkey('ctrl', 'v')
    time.sleep(1.5)
    pa.press('enter')
    # 点击【关闭】按钮
    loc_close = locate_pic(fr'{ps["img_path"]}\close.png')
    pa.click(loc_close.left + 12, loc_close.top + 12)


def send_msg_file(ps):
    """param ps: {'user': '微信用户名', 'filename': r'待发送文件完整路径','img_path':'图片所在目录'}"""
    wx_search_user(ps['user'], fr'{ps["img_path"]}')  # 搜索用户并切换到用户界面
    # 点击发送文件【图片按钮】
    loc_file = locate_pic(fr'{ps["img_path"]}/filebtn.png')
    pa.click(loc_file.left + 10, loc_file.top + 10)
    time.sleep(2)
    pyperclip.copy(ps['filename'])
    pa.hotkey('ctrl', 'v')
    time.sleep(1)
    pa.press('enter')
    # 点击【发送】按钮
    loc_send = locate_pic(fr'{ps["img_path"]}/sendbtn.png')
    pa.click(loc_send.left + 35, loc_send.top + 15)
    # 点击【关闭】按钮
    loc_close = locate_pic(fr'{ps["img_path"]}/close.png')
    pa.click(loc_close.left + 12, loc_close.top + 12)


def wait_for_appear(img_path, times=20, match=0.8):  # 等待元素出现，默认等待20秒
    for i in range(times):
        time.sleep(1)
        try:
            pa.locateOnScreen(fr'{img_path}', confidence=match)
            break
        except Exception as e:
            print(f"已经等待了{i + 1}秒，元素未出现，继续等待...{e}")
            continue


def wait_for_disappear(img_path, times=20, match=0.8):  # 等待元素消失，默认等待20秒
    time.sleep(2)
    for i in range(times):
        time.sleep(1)
        try:
            pa.locateOnScreen(img_path, confidence=match)
            continue
        except Exception as e:
            print(e)
            break


def wait_appear_or_disappear(option, img_path, times=20, match=0.8):
    """
    :param option: 0表示等待元素出现，1表示等待元素消失
    :param img_path: 图片完整路径
    :param times: 重试次数，每次等1秒,默认20次
    :param match: 匹配度
    """
    if option == 0:
        wait_for_appear(img_path, times, match)
    elif option == 1:
        wait_for_disappear(img_path, times, match)
    else:
        raise Exception('option参数错误')


if __name__ == '__main__':
    # send_msg_text({'user': '糊涂虫', 'msg': '风华正茂', 'img_path': r'D:\pythonProject\selenium\Yusir\img'})
    # send_msg_file({'user': '糊涂虫', 'filename': r'D:\2024\001.png', 'img_path': r'D:\pythonProject\selenium\Yusir\img'})
    print(get_first_and_last_day())
    print(flag(r'D:\2024\read_from_erp.xlsm', r'D:\2024\read_from_hd.xlsm'))
    print(get_file_modified_date(r'D:\2024\read_from_erp.xlsm'))
    wait_appear_or_disappear(0, r'D:\pythonProject\selenium\Yusir\img\user.png')
    pass
