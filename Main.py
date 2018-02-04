# -*- coding: utf-8 -*-
import time
from getScore import *
from sendEmail import *
from parseParameter import *

if __name__ == '__main__':
    username, password, to = getConf("conf.ini")
    ans = {}
    while True:
        try:
            ans = getScore(username, password)
            break
        except Exception:
            print("Error, 请检查是否正确填写了conf.ini中的统一认证用户名、密码和代接收的邮箱")
            exit(0)

    print(ans)
    send_email("zhaoyi1031@gmail.com", "zy12345678", [to], "A mail start to score notification.", "目前已知的成绩汇总:\n"+str(ans))

    tot = 0
    while True:
        while True:
            try:
                ansNew = getScore(username, password)
                if (len(ansNew) != len(ans)):
                    print("NEW!!!")
                    print("第Query",tot,"次查询: ",ansNew)
                    for  i in ansNew:
                        if not i in ans:
                            newCourse = i
                            newScore = ansNew[i]
                    nowTime = time.strftime("%m-%d %H:%M:%S", time.localtime())
                    send_email("zhaoyi1031@gmail.com", "zy12345678", [to], "New Score Appears!", newCourse + " 出分了！\n"+"当前时间: "+nowTime+"\n"+"新出的课程: "+newCourse+"   成绩: "+newScore+"\n"+"已知的成绩汇总: "+str(ansNew))
                tot = tot+1
#                print('Query',tot,': ',ansNew)
                break
            except Exception:
                print("error")
        ans = ansNew
        time.sleep(5)
