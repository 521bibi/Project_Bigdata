import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line
from flask import Flask,render_template

app = Flask(__name__)

"""line_loss读取数据"""
file = 'cache_data/out/%s' % ('loss.xlsx')
loss_read = pd.read_excel(file, header=None, parse_dates=[0])
# parse_data = loss_read.iloc[1:,1:].values
# data = parse_data.tolist()
loss_xaxis = loss_read.iloc[1:,0].values
yaxis_loss = loss_read.iloc[1:,1].values
yaxis_valloss = loss_read.iloc[1:,2].values

"""line_LSTM读取数据"""
file = 'cache_data/out/%s' % ('rebuilt.xlsx')
rebuilt_read = pd.read_excel(file, header=None, parse_dates=[0])
# parse_data = rebuilt_read.iloc[1:,1:].values
# data = parse_data.tolist()
lstm_xaxis = rebuilt_read.iloc[1:,0].values
yaxis_A = rebuilt_read.iloc[1:,1].values
yaxis_Ahat = rebuilt_read.iloc[1:,2].values

class myLSTM(object):
    def __init__(self):
        pass

    def Line_loss() -> Line:
        c = (
            Line()
            .set_global_opts(
                tooltip_opts=opts.TooltipOpts(is_show=False),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                ),
            )
            .add_xaxis(xaxis_data=loss_xaxis)
            .add_yaxis(
                series_name="loss",
                y_axis=yaxis_loss,
                symbol="emptyCircle",
                is_symbol_show=True,
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
            )
            .add_yaxis(
                series_name="valloss",
                y_axis=yaxis_valloss,
                symbol="emptyCircle",
                is_symbol_show=True,
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
            )
            # .render("smoothed_line_chart.html")
        )
        return c

    def Line_lstm() -> Line:
        c = (
            Line()
            .set_global_opts(
                tooltip_opts=opts.TooltipOpts(is_show=False),
                xaxis_opts=opts.AxisOpts(type_="category"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                ),
            )
            .add_xaxis(xaxis_data=lstm_xaxis)
            .add_yaxis(
                series_name="A",
                y_axis=yaxis_A,
                symbol="emptyCircle",
                is_symbol_show=True,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(color="blue"),
                label_opts=opts.LabelOpts(is_show=False),
            )
            .add_yaxis(
                series_name="Ahat",
                y_axis=yaxis_Ahat,
                symbol="emptyCircle",
                is_symbol_show=True,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(color="red"),
                label_opts=opts.LabelOpts(is_show=False),
            )
            # .render("smoothed_line_chart.html")
        )
        return c

# c = myLSTM.Line_lstm()
# c.render("linelstm.html")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/')
def test():
    return render_template("LSTMboard.html")


@app.route('/test/lineChart')
def get_Line_loss_chart():
    c = myLSTM.Line_loss()
    return c.dump_options_with_quotes()

@app.route('/test/barChart')
def get_Line_lstm_chart():
    c = myLSTM.Line_lstm()
    return c.dump_options_with_quotes()

if __name__ == '__main__':
    app.run(debug= True)