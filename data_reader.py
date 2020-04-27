import pandas as pd
import json_reader
# from flask import g
#
# def json_record():
#     json_in = g.file_name
#     print('test:%s'%json_in)

file_name = json_reader.demoin_json[0]

class XLSReader(object):
    def __init__(self):
        file = 'cache_data/input/%s'%(file_name)
        self.xls_read = pd.read_excel(file, header=None, parse_dates=[0])

    def read(self):
        xls_data = self.xls_read
        parse_data = self.parse_xls(xls_data)
        return parse_data

    def parse_xls(self, content):
        parse_data = content.iloc[3:, 1:5]
        parse_data[1] = pd.to_datetime(parse_data[1], format="%Y/%m/%d %H:%M:%S")
        parse_data.set_index(1, inplace=True)
        return parse_data

class outReader(object):
    def __init__(self):
        file  = 'cache_data/out/data.xlsx'
        self.xls_read = pd.read_excel(file,header=None,parse_dates=[0])

    def read(self):
        xls_data = self.xls_read
        parse_data = self.parse_xls(xls_data)
        return parse_data

    def parse_xls(self,content):
        parse_data = content.iloc[1:,:]
        # parse_data[0] = pd.to_datetime(parse_data[0], format="%Y/%m/%d %H:%M:%S")
        parse_data.set_index(0, inplace=True)
        return parse_data

if __name__ == '__main__':
    # reader = XLSReader()
    # datas = reader.read()
    # # print(datas)
    # datas.to_excel('cache_data/out/dataread.xlsx')
    reader = outReader()
    datas = reader.read()
    print(datas)