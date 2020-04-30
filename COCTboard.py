import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.globals import ChartType
from pyecharts.charts import Line,Pie,Map3D
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
        data2.append(opts.MarkPointItem(name="局部放电",type_="max", value='warning'))

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

    def Map_CT() -> Map3D:

        example_data = [
            ("黑龙江", [127.9688, 45.368, 100]),
            ("内蒙古", [110.3467, 41.4899, 100]),
            ("吉林", [125.8154, 44.2584, 100]),
            ("辽宁", [123.1238, 42.1216, 100]),
            ("河北", [114.4995, 38.1006, 100]),
            ("天津", [117.4219, 39.4189, 100]),
            ("山西", [112.3352, 37.9413, 100]),
            ("陕西", [109.1162, 34.2004, 100]),
            ("甘肃", [103.5901, 36.3043, 100]),
            ("宁夏", [106.3586, 38.1775, 100]),
            ("青海", [101.4038, 36.8207, 100]),
            ("新疆", [87.9236, 43.5883, 100]),
            ("西藏", [91.11, 29.97, 100]),
            ("四川", [103.9526, 30.7617, 100]),
            ("重庆", [108.384366, 30.439702, 100]),
            ("山东", [117.1582, 36.8701, 100]),
            ("河南", [113.4668, 34.6234, 100]),
            ("江苏", [118.8062, 31.9208, 100]),
            ("安徽", [117.29, 32.0581, 100]),
            ("湖北", [114.3896, 30.6628, 100]),
            ("浙江", [119.5313, 29.8773, 100]),
            ("福建", [119.4543, 25.9222, 100]),
            ("江西", [116.0046, 28.6633, 100]),
            ("湖南", [113.0823, 28.2568, 100]),
            ("贵州", [106.6992, 26.7682, 100]),
            ("广西", [108.479, 23.1152, 100]),
            ("海南", [110.3893, 19.8516, 100]),
            ("上海", [121.4648, 31.2891, 100]),
        ]

        c = (
            Map3D()
                .add_schema(
                itemstyle_opts=opts.ItemStyleOpts(
                    color="rgb(5,101,123)",
                    opacity=1,
                    border_width=0.8,
                    border_color="rgb(62,215,213)",
                ),
                map3d_label=opts.Map3DLabelOpts(
                    is_show=False,
                    formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
                ),
                emphasis_label_opts=opts.LabelOpts(
                    is_show=False,
                    color="#fff",
                    font_size=10,
                    background_color="rgba(0,23,11,0)",
                ),
                light_opts=opts.Map3DLightOpts(
                    main_color="#fff",
                    main_intensity=1.2,
                    main_shadow_quality="high",
                    is_main_shadow=False,
                    main_beta=10,
                    ambient_intensity=0.3,
                ),
            )
                .add(
                series_name="XX换流站",
                data_pair=example_data,
                type_=ChartType.SCATTER3D,
                bar_size=1,
                shading="lambert",
                label_opts=opts.LabelOpts(
                    is_show=False,
                    formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
                ),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Scatter3D"))
                # .render("map3d_with_scatter3d.html")
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

        x_data = ["局部放电","数据异常"]
        y_data = [1,15]
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

# c = myCOCT.Map_CT()
# c.render("map3d_with_scatter3d.html")