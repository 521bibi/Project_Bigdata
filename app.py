from flask import Flask,render_template,request,redirect,url_for,g
import json
from scatter3d import AA
from LSTMboard import myLSTM
from COCTboard import myCOCT
from subprocess import Popen
import os
app = Flask(__name__)


@app.route('/')
def index():

    filename = 'cache_data/interface/alarm_mes_all.json'
    with open(filename, 'r', encoding='UTF-8') as f:
        aa = json.load(f)
    alarmitems = aa['alarm_mes_all']

    return render_template('alarm_CT_home.html',alarmitems=alarmitems)

@app.route('/Pie_alarmPosition/')
def get_pie_alarmPosition():
    c = myCOCT.Pie_alarmPosition()
    return c.dump_options_with_quotes()

@app.route('/model_manage/',methods=['GET','POST'])
def model_manage():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect(url_for('alarm_CT_home.html'))

@app.route('/COCTboard/',methods=['GET','POST'])
def COCTboard():
    if request.method == 'GET':

        pltdata = request.args.get('pltdata')
        pltdata_dict = {'pltdata': pltdata}
        with open("cache_data/interface/pltdata.json", "w") as f:
            json.dump(pltdata_dict, f)

        filename = 'cache_data/interface/alarm_mes_all.json'
        with open(filename, 'r', encoding='UTF-8') as f:
            aa = json.load(f)
        alarmitems = aa['alarm_mes_%s'%pltdata]

        title = '%s'%pltdata+'相'

        return render_template('COCTboard.html',title=title,alarmitems=alarmitems)
    else:
        return redirect(url_for('alarm_CT_home.html'))

@app.route('/COCTboard/lineChart/')
def get_Line_COCT_chart():
    c = myCOCT.Line_COCT()
    return c.dump_options_with_quotes()

@app.route('/COCTboard/Pie_alarmTitle/')
def get_pie_alarmTitle():
    c = myCOCT.Pie_alarmTitle()
    return c.dump_options_with_quotes()

@app.route('/time_series/',methods=['GET','POST'])
def time_series():
    if request.method == 'GET':
        return render_template('time_series.html')
    else:
        file_name = request.form.get('file_name')
        Model_name = request.form.get('mymodel')
        test_dict = {'file_name':file_name,'Model_name':Model_name}
        # 使用g对象传递变量
        # g.file_name = file_name
        # json_record()
        ''' post表单写入json文件'''
        print(test_dict)
        with open("cache_data/interface/record.json", "w") as f:
            json.dump(test_dict, f)
        print("加载入文件完成...")
        '''post请求启动数据分析模块'''
        # p = Popen(["python","main.py"],)  #子进程
        # p.communicate()
        os.system("python main.py")
        print("启动OK")
        if Model_name == 'KMeans':
            return redirect(url_for('KMeans'))
        elif Model_name == 'LSTM':
            return redirect(url_for('scatter3d'))
        else:
            return render_template('404.html')


@app.route('/scatter3d/',methods=['GET','POST'])
def scatter3d():
    if request.method == 'GET':
        return render_template('scatter3d.html')
    else:
        return redirect(url_for('LSTMboard'))


@app.route('/scatter3d/barChart')
def get_bar_chart():
    c = AA.bar_base()
    return c.dump_options_with_quotes()

@app.route('/KMeans/',methods=['GET','POST'])
def KMeans():
    if request.method == 'GET':
        return render_template('KMeans.html')
    else:
        return redirect(url_for('index'))

@app.route('/LSTMboard/',methods=['GET','POST'])
def LSTMboard():
    if request.method == 'GET':
        return render_template('LSTMboard.html')
    else:
        return redirect(url_for('index'))

@app.route('/LSTMboard/lineChart')
def get_Line_loss_chart():
    c = myLSTM.Line_loss()
    return c.dump_options_with_quotes()

@app.route('/LSTMboard/barChart')
def get_Line_lstm_chart():
    c = myLSTM.Line_lstm()
    return c.dump_options_with_quotes()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug= True)


