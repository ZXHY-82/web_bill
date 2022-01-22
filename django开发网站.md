# django开发网站

#### 1. 新建django项目

##### 命令行新建（pycharm专业版的可以直接通过pycharm新建）

###### 举个例子

```
进入放项目的目录
django-admin startproject xxxx  //新建项目xxxx
cd xxxx  						//进入项目目录
python manage.py startapp yyyy	//在项目中创建一个应用yyyy
```

![image-20220122172837008](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122172837008.png)

##### 打开django项目

![image-20220122173041861](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122173041861.png)

![image-20220122173051295](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122173051295.png)

###### 创建的app记得在settings.py的INSSTALLED_APPS中进行注册

![image-20220122180349364](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122180349364.png)

###### 解释说明：

migrations记录对models中的操作日志

models.py（对数据库进行）

views.py（视图函数）

settings（配置设置）

urls.py（url路径，与视图函数进行关联）

##### 静态文件、html文件

新建两个文件夹（名字不能改，必须得是这样！）

![image-20220122190401325](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122190401325.png)

#### 2. 定义数据模型

###### 在models.py中创建

![image-20220122180249987](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122180249987.png)

###### mysql新建一个数据库

```
mysql -u root -p
输入密码
create database xxx；
use xxx
```

###### 在settings.py中修改数据库的参数

![image-20220122180908558](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122180908558.png)

###### 数据库迁移

```
在该项目下执行 
python manage.py makemigrations
python manage.py migrate
```

![image-20220122181129008](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122181129008.png)

###### 如果要修改数据模型，需要修改完之后再重新执行以上两条语句

但是可能会遇上bug就是无法在数据库中完成相应修改

建议删除全部内容重新对所有表进行创建

1. 删除数据表

2. 删除django_migrations表中app = 你创建的app的元组

   ![image-20220122181810047](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122181810047.png)

3. 删除migration中除__init__以外的全部.py

![image-20220122181902639](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122181902639.png)

#### 3. 登录界面设计(含cookie，session)

urls.py中加入以下

![image-20220122182241308](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122182241308.png)

###### Form介绍：

HTML页面中利用form表单向后端提交数据时，都会写一些获取用户输入的标签并且用form标签把它们包起来。

与此同时我们在好多场景下都需要对用户的输入做校验，比如校验用户是否输入，输入的长度和格式等正不正确。如果用户输入的内容有错误就需要在页面上相应的位置显示对应的错误信息.。

Django form组件就实现了上面所述的功能。

form组件的主要功能如下:

生成页面可用的HTML标签；对用户提交的数据进行校验；保留上次输入内容

![image-20220122183042927](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122183042927.png)

###### 如果需要额外接受参数，需要重写构造函数，如上图红框中的内容

![image-20220122184627289](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122184627289.png)

1. 如果是GET方法，返回登录界面
2. 判断用户输入的数据是否合法
3. 添加session记录（添加内容为用户名，设定时间为一小时 60*60）

![image-20220122185331386](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122185331386.png)

![image-20220122185358937](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122185358937.png)

4. 用户输入信息不合法，此时的form会自动携带一些错误信息

   在html中可以像下面这样写用来显示错误信息

![image-20220122185642927](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122185642927.png)

![image-20220122190043809](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122190043809.png)

5. 用户信息无法在数据库中找到对应的

   此时我是在password下添加了错误信息

   ![image-20220122185926701](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122185926701.png)

![image-20220122190015600](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122190015600.png)

#### 4. 中间件

![image-20220122190511847](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122190511847.png)

发送一个请求要穿过所有的中间件才能到达视图函数再返回（黑色路径），如果没能通过其中一个中间件（红色路径）

###### 中间件写法

![image-20220122190703176](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122190703176.png)

这里设置一个中间件，只允许登录的用户才能访问其余页面。

###### settings.py中的相应设置

![image-20220122190920875](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122190920875.png)

#### 5. 注册页面

###### ModelForm

通常在Django项目中，我们编写的大部分都是与Django 的模型紧密映射的表单。 举个例子，你也许会有个Book 模型，并且你还想创建一个form表单用来添加和编辑书籍信息到这个模型中。 在这种情况下，在form表单中定义字段将是冗余的，因为我们已经在模型中定义了那些字段。

基于这个原因，Django 提供一个辅助类来让我们可以从Django 的模型创建Form，这就是ModelForm。

![image-20220122191114456](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122191114456.png)

1. 新增一个确认密码字段
2. Meta类
3. 钩子函数用于密码校验
4. post返回的值

![image-20220122192600125](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122192600125.png)

![image-20220122192816504](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122192816504.png)

#### 6. 支出、收入账单页面

![image-20220122193248772](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122193248772.png)

###### 新增url

![image-20220122193844232](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122193844232.png)

1. ###### 新增功能（与注册功能实现类似）

   ![image-20220122193709958](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122193709958.png)

2. ###### 编辑功能

   ![image-20220122193937289](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122193937289.png)

   编辑栏初始原有数据

   ![image-20220122194159965](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122194159965.png)

3. ###### 删除功能

   ![image-20220122194235054](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122194235054.png)

4. 时间控件

   ![image-20220122194433261](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122194433261.png)

   ![image-20220122194542982](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122194542982.png)

5. 分页功能

   源码见[web_bill/page.py at master · ZXHY-82/web_bill (github.com)](https://github.com/ZXHY-82/web_bill/blob/master/bill/utils/page.py)

   ![image-20220122194739812](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122194739812.png)

#### 7. 数据统计与分析（echarts）

按照月份进行统计

![image-20220122195036232](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122195036232.png)

```python
def analysis(request):
    search_data = request.GET.get("year_month")
    if search_data:
        year = search_data[0:4]
        month = search_data[5:7]
        if month[0] == '0':
            month = month[1]
        if month == '2':
            day_num = 29
        elif (month == '4')|(month == '6')|(month == '9')|(month == '11'):
            day_num = 30
        else:
            day_num = 31
        x = []                     # x轴参数
        for i in range(day_num):
            x.append(str(i+1)+"日")
        legend = ["支出", "收入"]
        info_dict = request.session.get("info")
        name = info_dict.get('name')
        queryset_in = models.BillIncome.objects.filter(belong_in=name).order_by("time_in")
        queryset_out = models.BillOutcome.objects.filter(belong_out=name).order_by("time_out")
        m_in = []
        m_out = []
        t_out = []
        t_in = []
        income = 0
        outcome = 0
        for j in range(day_num):
            m_in.append(0)
            m_out.append(0)
        for k in range(9):
            t_out.append(0)
        for m in range(10):
            t_in.append(0)
        for r_1 in queryset_in:
            if (str(r_1.time_in.year) == year) & (str(r_1.time_in.month) == month):
                m_in[r_1.time_in.day] = m_in[r_1.time_in.day] + float(r_1.money_in)
                t_in[int(r_1.classify_type_in)-1] += float(r_1.money_in)
                income += float(r_1.money_in)
        for r_2 in queryset_out:
            if (str(r_2.time_out.year) == year) & (str(r_2.time_out.month) == month):
                m_out[r_2.time_out.day] = m_out[r_2.time_out.day] + float(r_2.money_out)
                t_out[int(r_2.classify_type_out)-1] += float(r_2.money_out)
                outcome += float(r_2.money_out)
        surplus = income - outcome
        series_list = [
            {
                "name": '支出',
                "type": 'bar',
                "data": m_out
            },
            {
                "name": '收入',
                "type": 'bar',
                "data": m_in
            }
        ]
        data_list = [
            {"value": t_out[0], "name": '餐饮'},
            {"value": t_out[1], "name": '交通'},
            {"value": t_out[2], "name": '购物'},
            {"value": t_out[3], "name": '居家'},
            {"value": t_out[4], "name": '娱乐'},
            {"value": t_out[5], "name": '人情'},
            {"value": t_out[6], "name": '医疗'},
            {"value": t_out[7], "name": '金融'},
            {"value": t_out[8], "name": '其他'},
        ]
        data_list_2 = [
            {"value": t_in[0], "name": '工资'},
            {"value": t_in[1], "name": '兼职'},
            {"value": t_in[2], "name": '经营'},
            {"value": t_in[3], "name": '利息'},
            {"value": t_in[4], "name": '奖金'},
            {"value": t_in[5], "name": '加班'},
            {"value": t_in[6], "name": '基金'},
            {"value": t_in[7], "name": '股票'},
            {"value": t_in[8], "name": '债券'},
            {"value": t_in[9], "name": '其他'},
        ]

        context_dict = {
            "name": name,
            "search_data": search_data,
            'legend': legend,
            'series_list': series_list,
            'x_axis': x,
            "data": data_list,
            "data_2": data_list_2,
            "income": income,
            "outcome": outcome,
            "surplus": surplus,
        }
        print(context_dict)
        return render(request, 'analysis.html', context_dict)
    else:
        info_dict = request.session.get("info")
        name = info_dict.get('name')
        context_dict = {
            "name": name,
            "search_data": search_data,
        }
        return render(request, 'analysis.html', context_dict)
```

![image-20220122195525792](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220122195525792.png)

```html
    <script type="text/javascript">
        $(function() {
            init_chart_1();
            init_chart_2();
            init_chart_3();
        })
        function init_chart_1(){
            var myChart = echarts.init(document.getElementById('chart_1'));

            var option = {
                title: {
                    text: '月收入支出',
                    textAlign: "auto",
                    left: "center",
                },
                tooltip: {},
                legend: {
                    data: {{ legend | safe }},  // 后台获取
                    bottom: 0
                },
                xAxis: {
                    data: {{ x_axis | safe }},  // 后台获取
                },
                yAxis: {},
                series: {{ series_list | safe }},  // 后台获取
            };
            myChart.setOption(option);
<!--            $.ajax({-->
<!--                url: "/bill/zzbill/analysis/bar",-->
<!--                type: "get",-->
<!--                dataType: "JSON",-->
<!--                success: function (res) {-->
<!--                    // 将后台返回的数据，更新到option中。-->
<!--                    if (res.status) {-->
<!--                        option.legend.data = res.data.legend;-->
<!--                        option.xAxis.data = res.data.x_axis;-->
<!--                        option.series = res.data.series_list;-->

<!--                        // 使用刚指定的配置项和数据显示图表。-->
<!--                        myChart.setOption(option);-->
<!--                    }-->
<!--                }-->
<!--            })-->
        }
        function init_chart_2() {
            var myChart = echarts.init(document.getElementById('chart_2'));
            var option = {
            title: {
                text: '各类型支出占比',
                left: 'center'
            },
                tooltip: {
                    trigger: 'item'
                },
                legend: {

                    bottom: 0
                },
                series: [
                    {
                        name: '预算',
                        type: 'pie',
                        radius: '50%',
                        data: {{ data | safe }},
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };
            myChart.setOption(option);
<!--            $.ajax({-->
<!--                url: "/bill/zzbill/analysis/pie",-->
<!--                type: "get",-->
<!--                dataType: "JSON",-->
<!--                success: function (res) {-->
<!--                    if (res.status) {-->
<!--                        option.series[0].data = res.data;-->
<!--                        myChart.setOption(option);-->
<!--                    }-->
<!--                }-->
<!--            })-->
        }
        function init_chart_3() {
            var myChart = echarts.init(document.getElementById('chart_3'));
            var option = {
            title: {
                text: '各类型收入占比',
                left: 'center'
            },
                tooltip: {
                    trigger: 'item'
                },
                legend: {

                    bottom: 0
                },
                series: [
                    {
                        name: '预算',
                        type: 'pie',
                        radius: '50%',
                        data: {{ data_2 | safe }},
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };
            myChart.setOption(option);
        }
    </script>
```

#### 8. Ajax动态请求

运用ajax在后台偷偷请求进行页面更新

例如：

```html
        $(function() {
            init_chart_1();
        })
        function init_chart_1(){
            var myChart = echarts.init(document.getElementById('chart_1'));

            var option = {
                title: {
                    text: '月收入支出',
                    textAlign: "auto",
                    left: "center",
                },
                tooltip: {},
                legend: {
                    data:[],  // 后台获取
                    bottom: 0
                },
                xAxis: {
                    data:[],  // 后台获取
                },
                yAxis: {},
                series: [],  // 后台获取
            };
            $.ajax({
                url: "/bill/zzbill/analysis/bar",
				type: "get",
                dataType: "JSON",
                success: function (res) {
                    // 将后台返回的数据，更新到option中。
                    if (res.status) {
                        option.legend.data = res.data.legend;
                        option.xAxis.data = res.data.x_axis;
                        option.series = res.data.series_list;
                        // 使用刚指定的配置项和数据显示图表。
                        myChart.setOption(option);
                    }
                }
            })
        }
```

```python
def bar(request):
    legend = ["xxx", "yyy"]
    series_list = [
        {
            "name": 'xxx',
            "type": 'bar',
            "data": [xx, xx, xxx, xx, xx, xx]
        },
        {
            "name": 'yyy',
            "type": 'bar',
            "data": [xx, xx, xx, xx, xx, xx]
        }
    ]
    x_axis = ['xx', 'xx', 'x', 'xx', 'xx', 'xx']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)
```

