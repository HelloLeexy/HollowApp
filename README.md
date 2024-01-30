# HollowApp
This is a campus forum Web APP based on Vue+Django

配置环境：
Django:
按照老师给的教程即可
额外依赖包：
请安装：pip install django-cors-headers

Vue:
首先安装：https://nodejs.org/en
然后再安装：WebStorm 编译器


测试方法：
使用anconda开启后端：
首先切换到Django环境里：例如：conda activate rango
将anconda的目录切换到：~\HollowApp\hollow_backend
在anconda终端输入 python manage.py runserver
这个时候后端服务已启动：端口号为8000

然后开启Vue前端：
打开终端：
把终端的根目录切换到：HollowApp\hollow_frontend>
然后在终端输入命令：npm run serve
这个时候前端服务已开启 端口号为8080

打开浏览器 输入http://localhost:8080
即可获得从后端传入到前端的数据 Demo完成