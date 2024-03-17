# HollowApp
This is a campus forum Web APP based on Vue+Django
现已部署到阿里服务器：http://8.208.87.180/#/Login

配置环境：
Django 2.1.5 以上:
额外依赖包：
请安装：pip install django-cors-headers (解决跨域问题)

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
先安装vue依赖
npm install

把终端的根目录切换到：HollowApp\
然后在终端输入命令：npm run dev
这个时候前端服务已开启 端口号为8080

打开浏览器 输入http://localhost:8080
即可获得从后端传入到前端的数据 Demo完成

演示图片
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/83e20eaf-483e-4ab0-802a-df4a43bf4b90)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/90e42c87-dcb1-44ab-86c8-7070a7c66ef7)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/a1026e71-bddd-435e-9507-234738dd8355)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/ad60d9fd-9364-4824-8e1f-fc3032eb53f0)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/e598becd-d821-41c2-856a-3b41ab761990)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/31c35b28-1afd-400c-8a7f-3ba105131af7)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/7c497492-4962-4dc3-a681-61d3818c0a8f)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/d4acb69f-0158-41ae-b76c-68414f1654fe)
![image](https://github.com/HelloLeexy/HollowApp/assets/76617194/39c7e95e-7784-409c-8267-af3b73a9227e)


