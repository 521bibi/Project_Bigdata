import json
import data_reader
import json_reader

class unit_json(object):
    def __init__(self):
        pass

    def Xlsx2json():
        reader = data_reader.XLSReader()
        datas = reader.read()
        # print(datas)
        df = datas.iloc[:525, :]
        df = df.reset_index()
        df.columns=['Time', 'value',  'value', 'value']
        df2 = df.iloc[:, :2]
        aa = df2.to_json(orient='records')

        return aa

    def json_write(aa):
        TempData = aa
        with open("cache_data/interface/TempData.json", "w") as f:
            json.dump(TempData, f)
        print("写入完成")

class mydata2json(object):
    def __init__(self):
        pass

    def CThome_json():
        filename = 'cache_data/interface/alarm_home.json'
        with open(filename, 'r', encoding='UTF-8') as f:
            aa = json.load(f)
        return aa

    def CTrm_json():
        filename = 'cache_data/interface/alarm_mes.json'
        with open(filename, 'r', encoding='UTF-8') as f:
            aa = json.load(f)
        pltdata = json_reader.pltdata()

        alarmitems = aa['alarm_mes_%s'%pltdata]
        return alarmitems

    def DA_original_data():
        # aa = unit_json.Xlsx2json()
        # unit_json.json_write(aa)
        filename = 'cache_data/interface/DA_original_data.json'
        with open(filename, 'r', encoding='UTF-8') as f:
            aa = json.load(f)
        return aa

# aa = mydata2json.DA_original_data()
# print(aa)
