import json_reader
import myKM
import os
from multiprocessing import Process

t= json_reader.demoin_json[1]

def myLSTM(f):
    os.system(f)

def KMeans():
    KM = myKM.KMeans_current()
    # KM.current_kmplt()
    KM.current_kmjson()
    df_result = KM.current_kmresult()
    df_result.to_excel("cache_data/out/data.xlsx")

def main():
    if t == 'KMeans':
        KMeans()
        print("完成KMeans")
    elif t == 'LSTM':
        p1 = Process(target=myLSTM,args=('python myKM.py',))
        p2 = Process(target=myLSTM,args=('python myLSTM.py',))
        p1.start()
        p2.start()
        print("完成LSTM")
    else:
        print("error")


if __name__ == '__main__':
    main()
