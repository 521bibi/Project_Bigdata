import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Line,Pie
from pyecharts.commons.utils import JsCode
# from flask import g,current_app
import json_reader


# x_data = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
# y_data = [393, 438, 485, 631, 689, 824, 987, 1000, 1100, 1200]

# def test():
#     pltdata_file = "current%s"%g.pltdata+"_hat.xlsx"
#     print(pltdata_file)
#     return pltdata_file


# pltdata_name = json_reader.pltdata()
# pltdata_file = "current%s"%pltdata_name+".xlsx"
# # """读取数据"""
# # file = 'cache_data/out/%s' % ('current8111Ba_hat.xlsx')
# file = 'cache_data/out/%s' % (pltdata_file)
# rebuilt_read = pd.read_excel(file, header=None, parse_dates=[0])
# # parse_data = rebuilt_read.iloc[1:,1:].values
# # data = parse_data.tolist()
# COCT_xaxis = rebuilt_read.iloc[1:,0].values
# yaxis_A = rebuilt_read.iloc[1:,1].values
# # yaxis_Ahat = rebuilt_read.iloc[1:,2].values

background_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], true)"
)
area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
)

class myCOCT(object):
    def __init__(self):
        pass

    def Line_COCT() -> Line:
        pltdata_name = json_reader.pltdata()
        pltdata_file = "current%s" % pltdata_name + ".xlsx"
        file = 'cache_data/out/%s' % (pltdata_file)
        rebuilt_read = pd.read_excel(file, header=None)
        COCT_xaxis = rebuilt_read.iloc[1:, 0].values
        yaxis_A = rebuilt_read.iloc[1:, 2].values

        df_warning = rebuilt_read.loc[rebuilt_read[1] == 1]
        warning_xaxis = df_warning[0].values
        warning_yaxis = df_warning[2].values

        data2 = []
        for i in range(15):
            data1 = opts.MarkPointItem(name="数据异常", coord=[warning_xaxis[i], warning_yaxis[i]], value='warning')
            data2.append(data1)


        # c = (
        #     Line()
        #         .set_global_opts(
        #         tooltip_opts=opts.TooltipOpts(is_show=False),
        #         xaxis_opts=opts.AxisOpts(type_="category"),
        #         yaxis_opts=opts.AxisOpts(
        #             type_="value",
        #             axistick_opts=opts.AxisTickOpts(is_show=True),
        #             splitline_opts=opts.SplitLineOpts(is_show=False),
        #         ),
        #     )
        #         .add_xaxis(xaxis_data=COCT_xaxis)
        #         .add_yaxis(
        #         series_name="loss",
        #         y_axis=yaxis_A,
        #         symbol="emptyCircle",
        #         is_symbol_show=True,
        #         is_smooth=True,
        #         label_opts=opts.LabelOpts(is_show=False),
        #     )
        #
        #     # .render("smoothed_line_chart.html")
        # )
        # return c

        c = (
            # Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
            Line()
            .add_xaxis(xaxis_data=COCT_xaxis)
            .add_yaxis(
                series_name="监测时间",
                y_axis=yaxis_A,
                markpoint_opts=opts.MarkPointOpts(
                    data=data2
                ),
                is_smooth=True,
                is_symbol_show=False,
                # symbol="circle",
                # symbol_size=6,
                linestyle_opts=opts.LineStyleOpts(color='#eb64fb'),
                # label_opts=opts.LabelOpts(is_show=False, position="top", color="white"),
                # itemstyle_opts=opts.ItemStyleOpts(
                #     color="red", border_color="#fff", border_width=3
                # ),
                # tooltip_opts=opts.TooltipOpts(is_show=False),
                # areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
            )

            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="%s"%pltdata_name+"相",
                    pos_bottom="5%",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(color="black", font_size=16),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=False,
                    axislabel_opts=opts.LabelOpts(margin=30, color="##3fbbff0d"),
                    axisline_opts=opts.AxisLineOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=25,
                        linestyle_opts=opts.LineStyleOpts(color="#3fbbff0d"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True,linestyle_opts=opts.LineStyleOpts(color="#3fbbff0d")
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    # min_="min",
                    # position="right",
                    axislabel_opts=opts.LabelOpts(margin=20, color="black"),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(width=2, color="black")
                    ),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=15,
                        linestyle_opts=opts.LineStyleOpts(color="black"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(color="black")
                    ),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
            # .render("line_color_with_js_func.html")
        )
        return c

    def Pie_alarmPosition() -> Pie:

        x_data = ["8111B-A相", "8111B-B相", "8112B-A相", "8112B-B相"]
        y_data = [2, 1, 5, 4]
        data_pair = [list(z) for z in zip(x_data, y_data)]
        data_pair.sort(key=lambda x: x[1])

        c = (
            Pie()
            .add(
            "",
            data_pair,
            center=["60%", "50%"],
            )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="告警部位统计"),
            legend_opts=opts.LegendOpts(pos_left="25%"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            # .render("pie_position.html")
        )
        return c

    def Pie_alarmTitle() -> Pie:

        x_data = ["局部放电"]
        y_data = [2]
        data_pair = [list(z) for z in zip(x_data, y_data)]
        data_pair.sort(key=lambda x: x[1])

        c = (
            Pie()
            .add(
            "",
            data_pair,
            center=["60%", "50%"],
            )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="告警原因统计"),
            legend_opts=opts.LegendOpts(pos_left="25%"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            # .render("pie_position.html")
        )
        return c

# c = myCOCT.Pie_alarmPosition()
# c.render("pie_position.html")