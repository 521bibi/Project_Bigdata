import data_reader
# import numpy as np
from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties

# font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)

# 数据获取
reader = data_reader.XLSReader()
datas = reader.read()
df = datas.iloc[:525,:3]
# print(df.tail())

class KMeans_current(object):
    def __init__(self):
        # 聚类器
        estimator = KMeans(n_clusters=2,init='k-means++',n_jobs=1)
        #fit方法对数据做training并得到模型
        self.kmeans = estimator.fit(df)
        # 聚类簇label
        self.y_pred = estimator.fit_predict(df)

    #     """
    # def current_kmplt(self):
    #     plt.scatter(df.iloc[:,0], df.iloc[:,1], c=self.y_pred)
    #     plt.title('A-B聚类可视化',fontproperties=font_set)
    #     plt.savefig("cache_data/out/A-B聚类可视化.png")
    #     # plt.show()
    #     plt.scatter(df.iloc[:,0], df.iloc[:,2], c=self.y_pred)
    #     plt.title('A-C聚类可视化',fontproperties=font_set)
    #     plt.savefig("cache_data/out/A-C聚类可视化.png")
    #     # plt.show()
    #     plt.scatter(df.iloc[:,1], df.iloc[:,2], c=self.y_pred)
    #     plt.title('B-C聚类可视化',fontproperties=font_set)
    #     plt.savefig("cache_data/out/B-C聚类可视化.png")
    #     # plt.show()

    #下面是KMeans三个属性
    def current_kmjson(self):
        # '''把聚类的样本打标签'''
        labelPred = self.kmeans.labels_
        # '''显示聚类的质心'''
        centroids =self.kmeans.cluster_centers_
        # '''这个也可以看成损失，就是样本距其最近样本的平方总和'''
        inertia = self.kmeans.inertia_

        jsontext = {'kmeans': []}
        jsontext['kmeans'].append({'centroids': "%s"%centroids, 'inertia': "%s"%inertia})
        import json
        jsondata = json.dumps(jsontext)
        f = open("cache_data/interface/interfaceout_1.json", 'w')
        f.write(jsondata)
        f.close()

        # print(jsontext)
        # print(centroids)
        # print(inertia)

    def current_kmresult(self):
        df_result = df.iloc[:,:3]
        df_result['label'] = self.y_pred

        return df_result
        # df_result.loc[df_result['y_pred'] == 1] = [np.nan,np.nan,np.nan,1]
        # return df_result
        # print(df_result.loc[df_result['y_pred'] == 1])

if __name__ == '__main__':
    KM = KMeans_current()
    # KM.current_kmplt()
    KM.current_kmjson()
    df_result = KM.current_kmresult()
    # print(df_result)
    df_result.to_excel("cache_data/out/data.xlsx")