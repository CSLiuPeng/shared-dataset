import re

import pandas

filter_datas = []


def handle_yinwen(title):
    return title

for records in pandas.read_excel("原始数据表.xlsx",dtype=str).to_dict(orient='records'):

    if len(records.get("标题")) >= 30 and  len(re.sub('[^\u4e00-\u9fa5]+', '', handle_yinwen(records.get("标题")))) >= 12:
        filter_datas.append(records)

df = pandas.DataFrame(filter_datas)
df.drop_duplicates(['标题','描述'],inplace=True)
df.to_excel("处理数据表.xlsx",index=False)