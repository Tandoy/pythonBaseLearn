# This is a export pic  Python script.
import time as time1
import mysql.connector
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os
from PIL import Image
from pdf2image import convert_from_path


# 模拟点击导出图片动作
def get_pic(exType):
    # exType image&extype=BMP/JPG/PNG/GIF    pdf
    FR_LOGIN_ADDR = 'http://47.100.72.147:37799/webroot/decision/login'
    FR_USER = 'WeHotel_Admin'
    FR_PASSWORD = 'ceV2_y'

    ## 总指标数
    CPT_NAME = 'card_dim'
    metric_name = 'member_spu_point:spu积分数'
    api_url = 'https://wdapig.bestwehotel.net/20221017180509'
    time_col = 'week:year_wh_week'
    group_by = 'year_wh_week'
    filters = 'year_wh_week_2:202303;year_wh_week_3:202310'
    page_size = '999'
    page_no = '0'
    order_by = 'year_wh_week asc '
    company = 'wh'
    output = 'year_wh_week as time,wh_week_001 as time_cn,platform as gp1,member_spu_point as target,hb_member_spu_point as hb'
    target_name = 'yzzb0001'

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
        # 连接到MySQL数据库
        cnx = mysql.connector.connect(user='shunan', password='S82-#1KHg',
                                      host='172.25.62.63', database='member_bi')

        # 执行SQL查询
        query = '''
        select  distinct
SUBSTRING_INDEX(file_name,'.',1) as CPT_NAME 
,CONCAT(t3.english_name ,":",t3.name) as metric_name
,mai.url as url
,case when t1.dim_group is not null then concat(t1.dim_group,",",'full_date') else 'full_date' end as group_by
,case when t5.`type` = 'static' then concat(CONCAT(t5.param_name,":",t5.param_value),";","full_date_2:20230509",";","full_date_3:20230509") else concat("full_date_2:20230509",";","full_date_3:20230509") end as filters
,'full_date asc' as order_by
,case when t1.dim_group is not null then concat('full_date as time,year_month_date as time_cn,',concat(t1.dim_group,' as gp1,'),concat(t3.english_name,' as target'))
else concat('full_date as time,year_month_date as time_cn,',concat(t3.english_name,' as target')) end as output
,t1.cpt_id as CPT_NAME
from cpt t1
left join metric_cpt t2
on t1.cpt_id = t2.cpt_id 
left join meta_business_metric t3
on t3.metric_id = t2.metric_id 
left join meta_tech_metric mtm 
on mtm.metric_id = t3.metric_id
and time_type = 'DATE'
left join meta_relation_tech_metric_api t4
on t4.tech_id = mtm.tech_id 
left join meta_api_info mai 
on mai.id = t4.api_id
left join cpt_param t5
on t5.cpt_id = t1.cpt_id
where mai.url is not null order by t1.cpt_id;
        '''
        cursor = cnx.cursor()
        cursor.execute(query)

        index = 1
        for row in cursor:
            driver.get(
                f'http://47.100.72.147:37799/webroot/decision/view/report?ref_c=79156ee5-2918-4a7c-a85e-e112a35c7517&viewlet=Wehotel_PC%252Ftz%252Fprod-new%252F'
                f'{CPT_NAME}.cpt' # cpt --> file_name
                f'&ref_t=design'
                f'&metric_name={metric_name}' # meta_business_metric --> name
                f'&api_url={api_url}'
                f'&time_col={time_col}'
                f'&group_by={group_by}'
                f'&filters={filters}'
                f'&page_size={page_size}'
                f'&page_no={page_no}'
                f'&order_by={order_by}'
                f'&company={company}'
                f'&output={output}'
                f'&format=image&extype=JPG'
                f'&__filename__={CPT_NAME}+{target_name}')
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
    # resize_image_all(r'E:\1', r'E:\2', 500, 300)
