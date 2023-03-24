# This is a export pic  Python script.
import time as time1
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os
from PIL import Image
from pdf2image import convert_from_path


# 拿到某个目录下所有指标名称以及中文名称
def get_listDir_cptName():
    data = {}
    file = open('cpt.txt', 'r', encoding='utf-8')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        data[row.split(",")[0]] = row.split(",")[1].replace("\n", "")
    return data


# 模拟点击导出图片动作
def get_pic(exType):
    # exType image&extype=BMP/JPG/PNG/GIF    pdf
    FR_LOGIN_ADDR = 'http://47.100.72.147:37799/webroot/decision/login'
    FR_USER = 'WeHotel_Admin'
    FR_PASSWORD = 'ceV2_y'

    targets = get_listDir_cptName()

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
        for key in targets:
            target = key
            target_name = targets[key]
            driver.get(
                f'http://47.100.72.147:37799/webroot/decision/view/report?viewlet=Wehotel_PC%252Ftz%252Fmember_spu_commodities-chart_line-date.cpt&ref_t=design&ref_c=f9676866-840d-4192-a623-94547d558484&full_date_2=20230321&full_date_3=20230310&url=https://wdapig.bestwehotel.net/20221017175934&orderby=full_date asc&output=full_date as time,year_month_date as time_cn,{target} as target&dim_group=full_date&seriesname={target_name}&format={exType}&__filename__=member_spu_commodities-chart_line-date-+{target}')
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


def resize_image_all(input_dir, output_dir, width=None, height=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历所有 jpg、jpeg、png 格式的文件
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)
        try:
            # 只处理 jpg, jpeg ,bmp 和 png 格式的图片
            if input_path.endswith(('jpg', 'jpeg', 'png', 'bmp')):
                resize_image(input_path, output_path, width, height)
        except OSError:
            print(f"Cannot process {file_name}")

        print("图片大小调整完成！")


def resize_image(input_image_path, output_image_path, width, height):
    original_image = Image.open(input_image_path)
    w, h = original_image.size

    # 如果指定了宽度和高度，则以这些为准；否则，保持原始宽高比缩放
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, int(height * (w / h)))
    elif height:
        max_size = (int(width * (h / w)), height)
    else:
        # 未指定缩放大小，则输出原图
        max_size = (w, h)

    # crop = original_image.crop((0, 0, width, height))
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)


# pdf --> jpg
def pdf_to_jpg(pdf_dir, output_dir):
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            # 获取PDF文件的绝对路径
            pdf_path = os.path.join(pdf_dir, filename)

            # 将PDF转换为图像
            images = convert_from_path(pdf_path, poppler_path=r'E:\poppler\poppler-0.68.0\bin')

            # 将每个图像保存到输出目录
            for i, image in enumerate(images):
                image.save(os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.jpg"), "JPEG")


if __name__ == '__main__':
    # 导出cpt为pdf
    get_pic(exType='image&extype=JPG')
    # 调整图片尺寸
    resize_image_all(r'E:\1', r'E:\2', 500, 300)
