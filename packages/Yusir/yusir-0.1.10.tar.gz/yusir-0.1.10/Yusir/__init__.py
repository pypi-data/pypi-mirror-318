import calendar
import datetime
import os
import subprocess
import sys
import time
import pyautogui as pa
import pyperclip


def get_first_and_last_day():
    today = datetime.date.today()
    year = today.year
    month = today.month
    first_day = today.replace(day=1)
    last_day = today.replace(day=calendar.monthrange(year, month)[1])
    return [today, first_day, last_day]


def get_file_modified_date(file_path):
    timestamp = os.stat(file_path)
    modified_time = datetime.datetime.fromtimestamp(timestamp.st_mtime)
    return modified_time


def flag(f1, f2):
    erp = get_file_modified_date(f1).strftime('%Y%m%d%H')
    hd = get_file_modified_date(f2).strftime('%Y%m%d%H')
    th = datetime.datetime.now().strftime('%Y%m%d%H')
    if erp == th and hd == th:
        return 'flag'


def locate_pic(path, match=0.85, repeat_count=77):
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
    wx_search_user(ps['user'], fr'{ps["img_path"]}')
    loc_msg = locate_pic(fr'{ps["img_path"]}\msg.png')
    pa.click(loc_msg.left + 100, loc_msg.top + 77)
    pyperclip.copy(ps['msg'])
    pa.hotkey('ctrl', 'v')
    time.sleep(1.5)
    pa.press('enter')
    loc_close = locate_pic(fr'{ps["img_path"]}\close.png')
    pa.click(loc_close.left + 12, loc_close.top + 12)


def send_msg_file(ps):

    wx_search_user(ps['user'], fr'{ps["img_path"]}')
    loc_file = locate_pic(fr'{ps["img_path"]}/filebtn.png')
    pa.click(loc_file.left + 10, loc_file.top + 10)
    time.sleep(2)
    pyperclip.copy(ps['filename'])
    pa.hotkey('ctrl', 'v')
    time.sleep(1)
    pa.press('enter')
    loc_send = locate_pic(fr'{ps["img_path"]}/sendbtn.png')
    pa.click(loc_send.left + 35, loc_send.top + 15)
    loc_close = locate_pic(fr'{ps["img_path"]}/close.png')
    pa.click(loc_close.left + 12, loc_close.top + 12)


def wait_for_appear(img_path, times=20, match=0.8):
    for i in range(times):
        time.sleep(1)
        try:
            pa.locateOnScreen(fr'{img_path}', confidence=match)
            break
        except Exception as e:
            print(f"已经等待了{i + 1}秒，元素未出现，继续等待...{e}")
            continue


def wait_for_disappear(img_path, times=20, match=0.8):
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
    if option == 0:
        wait_for_appear(img_path, times, match)
    elif option == 1:
        wait_for_disappear(img_path, times, match)
    else:
        raise Exception('option参数错误')

