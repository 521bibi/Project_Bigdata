# import random
from pyecharts.charts import Scatter3D
from pyecharts import options as opts



# 配置 config
config_xAxis3D = "A"
config_yAxis3D = "B"
config_zAxis3D = "C"
config_color = "fiber"

# 构造数据
# data = [
#     [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
#     for _ in range(80)
# ]
# print(data)
# print(type(data))

import pandas as pd

file = 'cache_data/out/%s' % ('data.xlsx')
xls_read = pd.read_excel(file, header=None, parse_dates=[0])
parse_data = xls_read.iloc[1:, 1:4].values
data = parse_data.tolist()


class AA(object):
    def __init__(self):
        pass

    def bar_base() -> Scatter3D:
        c = (
            Scatter3D(
                init_opts=opts.InitOpts(width="1440px", height="720px")
            )  # bg_color="black"
            .add(
            series_name="",
            data=data,
            xaxis3d_opts=opts.Axis3DOpts(
                name=config_xAxis3D,
                type_="value",
                # textstyle_opts=opts.TextStyleOpts(color="#fff"),
                ),
            yaxis3d_opts=opts.Axis3DOpts(
                name=config_yAxis3D,
                type_="value",
                # textstyle_opts=opts.TextStyleOpts(color="#fff"),
                ),
            zaxis3d_opts=opts.Axis3DOpts(
                name=config_zAxis3D,
                type_="value",
                # textstyle_opts=opts.TextStyleOpts(color="#fff"),
                ),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
            )
                # .render("scatter3d.html")
        )
        return c

# AA.bar_base()

# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/scatter3d/')
# def scatter3d():
#     return render_template("scatter3d.html")
#
#
# @app.route('/scatter3d/barChart')
# def get_bar_chart():
#     c = AA.bar_base()
#     return c.dump_options_with_quotes()

