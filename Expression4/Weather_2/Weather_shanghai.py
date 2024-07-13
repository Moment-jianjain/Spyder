# �C coding: gbk �C
import requests
from bs4 import BeautifulSoup
import pandas
import pandas as pd
from matplotlib import pyplot as plt


# def get_data(weather_url):
#     rseponse = requests.get(weather_url)
#
#     html = rseponse.content.decode('gbk')
#     soup = BeautifulSoup(html, 'html.parser')
#
#     tr_lsit = soup.find_all('tr')
#     # Ѱ��tr��ǩ�µ���������
#
#     print(tr_lsit)
#     dates, conditions, temp, fengxiang = [], [], [], []
#     for data in tr_lsit[1:]:
#         sub_data = data.text.split()
#         # ['2024��06��30��', '������', '/������', '27��', '/', '32��', '����', '1-2��', '/����', '1-2��']
#
#         dates.append(sub_data[0])
#         conditions.append(''.join(sub_data[1:3]))
#         temp.append(''.join(sub_data[3:6]))
#         fengxiang.append(''.join(sub_data[6:9]))
#         # join���������ַ���
#
#     # ���ݱ���
#     _data = pandas.DataFrame()
#     _data['����'] = dates
#     _data['�������'] = conditions
#     _data['����'] = temp
#     _data['����'] = fengxiang
#
#     return _data
#     # print(_data)
#     # _data.to_csv('anqing.csv',index=False,encoding='gbk')
#     # ��ȡ���ݲ�����csv��ʽ��������������ݷ���
#
#
# # ����ɺ�����ʽ���з�װ
# data_month_1 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202405.html')
# data_month_2 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202406.html')
# data_month_3 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202407.html')
#
# # ʹ��drop���������⽫���������Ϊ�У�
# data = pandas.concat([data_month_1, data_month_2, data_month_3]).reset_index(drop=True)
# # ����csv���
# data.to_csv('shanghai.csv', index=False, encoding='utf-8')
# ����
data1 = pd.read_csv('shanghai.csv')

# ��ͼ
# ��������
plt.rcParams['font.sans-serif'] = ['SimHei']
# ������ŵ���������
plt.rcParams['axes.unicode_minus'] = False
# ����
datalsit = pandas.read_csv('shanghai.csv', encoding='utf-8')

# ���ݴ���
# ����split�����ַ�����/��ȡ������������
datalsit['�������'] = datalsit['����'].str.split('/', expand=True)[0]
datalsit['�������'] = datalsit['����'].str.split('/', expand=True)[1]
# ȡ���¶��еġ����
datalsit['�������'] = datalsit['�������'].map(lambda x: int(x.replace('��', '')))
datalsit['�������'] = datalsit['�������'].map(lambda x: int(x.replace('��', '')))

dates = datalsit['����']
highs = datalsit['�������']
lows = datalsit['�������']

# ��ͼ
# ���ÿ��ӻ�ͼ�ι��
fig = plt.figure(dpi=128, figsize=(10, 6))
# ����ͼ��������ɫ��ϸ����
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# �����·�����Ϊ��ɫ
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# ͼ���ʽ
# ����ͼ���ͼ�θ�ʽ
plt.title('2024�Ϻ���5-7���������', fontsize=24)
plt.xlabel('����', fontsize=12)
# x���ǩ��б  Ĭ��30�� ��ͨ��rotation=30�ı�
fig.autofmt_xdate()
plt.ylabel('����', fontsize=12)
# �̶�����ʽ����
plt.tick_params(axis='both', which='major', labelsize=10)
# �޸Ŀ̶� ����ÿ10����ʾ1��
plt.xticks(dates[::10])
# ����ͼ�εĴ���...
# ����ͼ�ε�����
plt.savefig('2024�Ϻ���5-7���������.png')


# ���Ʒ�������ͼ
# ��ȡ������ĸ�����ռ��  ������ϴ
fengxiang = data1['����'].value_counts()
fengxiang = fengxiang[fengxiang.values > 3]
plt.figure(figsize=(15, 5))
# ��ס��ͼ��Բ ����Ĭ����Բ
plt.axes(aspect='equal')
plt.pie(x=fengxiang.values,
        labels=fengxiang.index,
        autopct="%.2f%%",
        radius=1
        )
plt.title('����ռ��')
plt.savefig('2024�Ϻ���5-7�·���ռ��.png')

# ֱ����ʾ
# plt.show()