# Django 项目部署

###### date: 2022/1/20

##### 题外话

```
ssh 连接 ssh root@xxx.xxx.xxx.xxx 

useradd -m -s /bin/bash xxxx		//新建用户
usermod -a -G sudo xxxx				//用户添加到超级权限组 
passwd xxxx							//设置密码
su - xxxx 							//切换到用户
修改python3的优先级，例如：
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5.2
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6.2
修改python的默认值
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3 150

记得配置安全组
```

1. 更新系统

   ```
   sudo apt-get update
   sudo apt-get upgrade
   ```

2. 安装一些包

   ```
   sudo apt-get install nginx	
   sudo apt-get install git python3 python3-pip
   sudo pip3 install virtualenv	//之后的操作将在虚拟环境下进行
   sudo pip3 install uwsgi
   安装mysql
   sudo apt-get install mysql-server
   sudo apt-get install mysql-client
   sudo apt-get install libmysqlclient-dev
   mysql -u root -p
   初始情况下root是没有密码的
   可以通过 set password="xxxxx"
   create database web_bill;
   创建一个web_bill数据库
   ```

3. 启动nginx服务

   ```
   sudo service nginx start
   或者sudo /etc/init.d/nginx start //可替换reload,stop,restart
   sudo nginx -s quit
   ```

   输入公网ip（成功

   ![image-20220120180201067](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120180201067.png)

4. 新建一个虚拟环境导入django项目

   ```
   例如我是在/var/www目录下
   cd /var/www
   virtualenv bill 
   source bill/bin/activate
   上传项目文件到bill中
   可以采用FTP工具（filezilla）也可以用git clone http://xxxxx
   在虚拟环境中安装项目所需的包
   pip3 install django 
   pip3 install mysqlclient
   ......
   运行下
   python manage.py makemigrations
   pyhton manage.py migrate
   初始化一下数据库
   ```

5. 设置setting.py

   ![image-20220120183303274](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120183303274.png)

![image-20220120183336750](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120183336750.png)

![image-20220120183402583](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120183402583.png)

6. 配置nginx

   ```
   同样还是在虚拟环境下
   cd /etc/nginx
   gedit nginx.conf
   在http下加入以下代码
   在该目录下新建一个uwsgi_params文件
   我用touch uwsgi_params后打开的该文件自身就具有了配置内容（有点奇怪）
   ```

   ![image-20220120183644056](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120183644056.png)

7. 配置uwsgi

   在/etc/nginx目录下新建一个bill.ini文件加入以下内容

   ![image-20220120184014206](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120184014206.png)

```
uwsgi --ini bill.ini
运行
```

8. 静态文件的处理

   ![image-20220120184320021](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120184320021.png)

   在manage.py那个目录下运行python manage.py collectstatic 将会下bill目录下新增一个static文件夹

   在nginx.conf和bill.ini文件中加入以下即可

   

   ![image-20220120184349405](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120184349405.png)

![image-20220120184409256](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120184409256.png)

![image-20220120184756396](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120184756396.png)

![image-20220120184818750](C:\Users\知行合一\AppData\Roaming\Typora\typora-user-images\image-20220120184818750.png)

