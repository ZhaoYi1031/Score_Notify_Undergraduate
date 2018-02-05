# BUAA-Score-Notification

考完了，等成绩，每次刷渣渣教务系统也是心累。所以写了一个成绩更新通知，每当成绩更新的时候，会发给自己指定的邮箱。在学长luckcul的研究生教务的代码的思路下写的。很多地方沿袭了学长的写法。以及爬虫的部分代码是在学弟的基础上改的。



## Requirements and Prerequisites:

对于依赖的python包，直接`pip install -r requirements.txt`

环境及依赖包如下

* Python 3.x
  * bs4 0.0.1（pip install即安装好beautifulsoup4）
  * lxml 4.1.1

## Tips

* 在`conf.ini`里面填入自己教务网站统一认证的账号、密码和收邮件通知的邮件地址。
* 在python3的idle或者命令行执行`python3 Main.py`即可
* 初始会发一次邮件，代码开始启动监控了。之后会每**5秒**获得一次成绩，如果有新成绩会发送新邮件。
* **在输出successfully sent the mail后，如果填写的邮箱没有收到，请检查是否在垃圾邮件里或者被拦截**

## Structure

* getScore.py： 模拟登陆，爬虫获得成绩
* parseParameter.py：从conf.ini中提取统一认证的用户名、密码和所需要发送到的邮箱
* sendEmail ： 发邮件
* Main.py ：run!

## Notes

当前脚本是在校园网环境下使用的，如果想要在外网环境下使用，应该要先连接vpn，或者是把url改成e.buaa.edu.cn等。

## 效果展示图

![IMG_3503_Fotor.jpg](https://i.loli.net/2018/02/06/5a7885b4830df.jpg)








