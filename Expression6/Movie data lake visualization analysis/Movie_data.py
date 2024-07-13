# �C coding: gbk �C
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 21:13
# @Author  : jianjian
# @File    : Movie_data.py
# @Software: PyCharm
import requests,csv  #�����ͱ����
import pandas as pd  #��ȡcsv�ļ��Լ���������
from lxml import etree #����html��
from pyecharts.charts import *  #���ӻ���

# �������ַ
url = 'https://ssr1.scrape.center/page/1'

# ����ͷ
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# �������󣬻�ȡ�ı�����
reponse = requests.get(url, url, headers=headers)
print(reponse)

# ����csv�ļ�
with open('��Ӱ����.csv', mode='w', encoding='utf-8', newline='') as f:
    # ����csv����
    csv_save = csv.writer(f)

    # ��������
    csv_save.writerow(['��Ӱ��', '��Ӱ��ӳ��', '��Ӱʱ��', '��ӳʱ��', '��Ӱ����'])

    for page in range(1, 11):  # �����ؼ�1��10ҳ��ҳ��

        # �������ַ
        url = 'https://ssr1.scrape.center/page/{}'.format(page)
        print('��ǰ����ҳ����', page)

        # ����ͷ
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        response = requests.get(url, url, headers=headers, verify=False)
        print(response)

        html_data = etree.HTML(response.text)

        # ��ȡ��Ӱ��
        title = html_data.xpath(
            '//div[@class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]/a/h2/text()')

        # ��ȡ��Ӱ������
        gbs = html_data.xpath(
            '//div[@class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]/div[2]/span[1]/text()')

        # ��ȡ��Ӱʱ��
        time = html_data.xpath('//div[@class="m-v-sm info"]/span[3]/text()')

        # ��ȡ��Ӱ��ӳʱ��
        move_time = html_data.xpath(
            '//div[@class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]/div[3]/span/text()')

        # ��Ӱ����
        numder = html_data.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()')

        for name, move_gbs, times, move_times, numders in zip(title, gbs, time, move_time, numder):
            print('��Ӱ����', name, '  ��Ӱ��ӳ��ַ��', move_gbs, '   ��Ӱʱ����', times, '   ��Ӱ��ӳʱ�䣺', move_times,
                  '   ��Ӱ����:', numders)
            # name,move_gbs,times,move_times,numders

            # д��csv�ļ�
            csv_save.writerow([name, move_gbs, times, move_times, numders])