import json
# f = open("cache_data/interface/record.json",'r')
# f_pltdata = open("cache_data/interface/pltdata.json",'r')
# ln = 0
# for line in f.readlines():
#     ln += 1
#     dic = json.loads(line)
#     t = dic['file_name'],dic['MODEL_name']
#     f = open("out/data.txt",'a',encoding='utf-8')
#     f.writelines(str(t));f.write("\n")
# f.close()
def json_in():
    f = open("cache_data/interface/record.json", 'r')
    for line in f.readlines():
        dic = json.loads(line)
        demoin_json = dic['file_name'],dic['Model_name']
    return demoin_json

def pltdata():
    f_pltdata = open("cache_data/interface/pltdata.json", 'r')
    for line in f_pltdata.readlines():
        dic = json.loads(line)
        pltdata = dic['pltdata']
    return pltdata

demoin_json = json_in()
# print(demoin_json)