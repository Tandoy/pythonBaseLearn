# This is a export pic  Python script.

import time as time1
from selenium import webdriver
from PIL import Image
import os
from selenium.common.exceptions import TimeoutException


# 拿到某个目录下所有cpt名称
def get_listDir_CptName():
    data = []
    file = open('cpt.txt', 'r')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        data.append(row.replace('\n', ''))  # 将每行数据插入data中
    return data


# 根据图标类型调整像素
def get_adjust_image(filePath, savePath):
    raw_files = os.walk(filePath)
    width, height = 224, 224
    # 如果没有这个文件夹，就新建
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    for root, dirs, files in raw_files:
        for file in files:  # 展现各文件
            picture_path = os.path.join(root, file)  # 得到图像的绝对路径
            pic_org = Image.open(picture_path)  # 打开图像
            pic_new = pic_org.resize((width, height), Image.ANTIALIAS)  # 图像尺寸修改
            _, sub_folder = os.path.split(root)  # 得到子文件夹名字
            pic_new_path = os.path.join(savePath, sub_folder)
            if not os.path.exists(pic_new_path):
                os.makedirs(pic_new_path)  # 建立子文件夹
            pic_new_path = os.path.join(pic_new_path, file)  # 新图像存储绝对路径
            pic_new.save(pic_new_path)  # 存储文件
            print("%s have been resized!" % pic_new_path)


# 模拟点击导出图片动作
def get_pic():
    FR_LOGIN_ADDR = 'http://47.100.72.147:37799/webroot/decision/login'
    FR_USER = 'WeHotel_Admin'
    FR_PASSWORD = 'ceV2_y'

    cpt_names = get_listDir_CptName()

    webdriver_options = webdriver.ChromeOptions()

    # webdriver_options.add_argument('--headless')
    webdriver_options.add_argument('--disable-gpu')
    webdriver_options.add_argument('--no-sandbox')
    webdriver_options.add_argument('--disable-dev-shm-usage')
    webdriver_options.add_argument('window-size=1024x768')
    driver = webdriver.Chrome(options=webdriver_options)

    SELENIUM_HEADSTART = 5

    driver.get(FR_LOGIN_ADDR)
    try:
        # 循环导出图片
        index = 1
        for CPT_NAME in cpt_names:
            driver.get(
                f'http://47.100.72.147:37799/webroot/decision/view/report?viewlet=Wehotel_PC%252Ftz%252F{CPT_NAME}.cpt&format=image&extype=JPG')
            # 除了第一次之外 其它故意填错用户名和密码以免登录成功后重定向
            if index == 1:
                driver.find_elements_by_css_selector('input[type=text]')[0].send_keys(FR_USER)
                driver.find_elements_by_css_selector('input[type=password]')[0].send_keys(FR_PASSWORD)
                driver.find_elements_by_class_name('bi-basic-button')[3].click()
            else:
                continue
            index = + index

            time1.sleep(SELENIUM_HEADSTART)

    except TimeoutException as e:
        print('timeout--------------')

    finally:
        driver.quit()


if __name__ == '__main__':
    get_adjust_image('E:\\1', 'E:\\2')
