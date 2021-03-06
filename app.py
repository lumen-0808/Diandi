from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': '冉婷媛',
    'address' : '湖北师范大学',
    # 'job': 'Student',
    'tel': '15549864073',
    'email': 'ing0909@outlook.com',
    'capsname':'冉婷媛',
    'description' : '我认为我自己认真并有耐心，能承受工作压力 ,乐于并善于学习。有良好的学习能力、团队协作能力和沟通能力,善于思考，能独立分析和解决问题。在大学我花了大量的时间学习充实自己，在此期间我通过了英语四六级考试，同时也考取了高级信息技术教师资格证，对自己所学的专业也有了一定的了解和掌握。 ',
    'qq': '1373932',
    'wechat': 'huuubb',
    'github': 'https://github.com/lumen-0808',

	'languages' : ['HTNL','CSS (Stylus)', 'JavaScript'],

	'education' : ['C程序设计','面向对象程序设计(JAVA)',  '软件过程与管理','数据分析'],

    'experiences' : [
        {
            'NO' : '商城项目的简单实现',
            'light': '2020/9-2020/12',
            'justified' : '项目主要实现，用户管理模块,商品浏览模块,商品管理模块,购物车模块,订单模块，管理员模块。系统是B/S模式实现,WEB层使用jsp技术,控制转发层使用自定义的Servlet来控制整个系统的业务逻辑流程,业务逻辑层使用轻量级的Java Bean,通过JDBC操作数据库'
        },
        {
        	'NO' : ' 微信记账本小程序',
        	'light': '2021/3-2021/5',
        	'justified' : '该项目是使用微信开发平台开发的一个记账本类小程序主要功能模块有：记一笔模块，消费一览模块，消费明细模块。消费报表模块，个人模块。使用云开发技术，实现用户信息的存储，读取等，还可以实现用户账单的分类查看，和使用图表等方式全方位展示用户的消费习惯'
        }
    ]

}


@app.route('/')
def cv(person=person):
	return render_template('index3.html',person=person)

@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))

@app.route('/callback1', methods=['POST', 'GET'])
def cb1():
    return gm1(request.args.get('data'))

@app.route('/callback10', methods=['POST', 'GET'])
def cb10():
    return gm10(request.args.get('data'))



@app.route('/chart')
def index():
    return render_template('chartsajax.html', graphJSON=gm(),graphJSON1=gm1(),
        graphJSON6=gm6(),graphJSON7=gm7(),graphJSON8=gm8(),graphJSON9=gm9(),graphJSON10=gm10())

@app.route('/chart2')
def index2():
    return render_template('chartsajax2.html', graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5(),graphJSON11=gm11())



def gm(country='Switzerland'):
    df=pd.DataFrame(px.data.gapminder())
    # fig=px.line(df[df['country']==country], x='year', y="pop") 
    fig=px.bar(df[df['country']==country], x="year",  # 横坐标
       y="pop",  # 纵坐标
       color="pop")  # 颜色取值
    graphJSON=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def gm1(continent='Africa'):
    df=pd.DataFrame(px.data.gapminder())
    fig=px.scatter(df[df['continent']==continent],   # 传入的数据集
           x="year",  # 横坐标是人均GDP
           y="lifeExp",  # 纵坐标是平均寿命
           color="country"  # 颜色取值：根据洲的值来取
          )
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

def gm2():
    iris= pd.DataFrame(px.data.iris())
    fig=px.scatter_matrix(iris,  # 传入绘图数据
                  dimensions=["sepal_width","sepal_length","petal_width","petal_length"],  # 维度设置
                  color="species")  # 颜色取值
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2



def gm3():
    iris= pd.DataFrame(px.data.iris())
    fig=px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_x="histogram",
    marginal_y="rug")
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3


def gm4():
    iris= pd.DataFrame(px.data.iris())

    fig=px.box(iris,  # 数据集
       x="petal_width",  # 横轴数据
       y="petal_length",  # 纵轴数据
       color="species",  # 颜色
       notched=True)  # 连接处的锥形部分显示出来
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON4
    
def gm5():
    iris= pd.DataFrame(px.data.iris())
    fig=px.density_contour(iris,  # 数据集
                   x="petal_width",  # xy轴
                   y="petal_length",
                   color="species"  # 颜色取值
                  )  
    graphJSON5= json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5

def gm6(year=2002):
    df=pd.DataFrame(px.data.gapminder())
    fig=px.line_geo(
    df[df['year']==year],
    locations="iso_alpha",
    color="continent",
    projection="orthographic")
    graphJSON6 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON6
    
def gm7():
    df=pd.DataFrame(px.data.gapminder())
    fig=px.scatter_3d(
    df,  # 传入数据集
    x="lifeExp",  # 指定XYZ坐标轴的数据
    y="pop",  
    z="gdpPercap",  
    color="continent",  # 颜色取值
     )  # 改变默认颜色


    graphJSON7 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON7

def gm8(year=2002):
    df=pd.DataFrame(px.data.gapminder())
    fig=px.scatter(df[df['year']==year]
        ,x="gdpPercap"  # 横坐标
        ,y="pop"  # 纵坐标
        ,color="continent"  # 区分颜色
        ,size="pop"   # 区分圆的大小
        ,size_max=60  # 散点大小
        )
    graphJSON8 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON8


def gm9():
    df=pd.DataFrame(px.data.gapminder())
    fig=px.area(df,   # 绘图的数据集
        x="year",   # 横轴数据
        y="pop",  # 纵轴数据
        color="continent",  # 颜色取值
        line_group="country")  # 线型分组
    graphJSON9 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON9


def gm10(country='Switzerland'):
    df=pd.DataFrame(px.data.gapminder())
    fig=px.line(df[df['country']==country], x='year', y="pop") 
    graphJSON10=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON10

def gm11():
    iris= pd.DataFrame(px.data.iris())
    fig=px.density_heatmap(   # 密度热力图
    iris,  
    x="sepal_width",
    y="sepal_length",
    marginal_y="rug",
    marginal_x="histogram"   
    )  # 连接处的锥形部分显示出来
    graphJSON11=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON11


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
