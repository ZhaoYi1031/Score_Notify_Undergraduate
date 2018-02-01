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
    send_email("zhaoyi1031@gmail.com", "zy12345678", [to], "This is a mail to start to score notify by ohazyi.", "First:\n"+str(ans))
    
    tot = 0
    while True:
        while True:
            try:
                ansNew = getScore(username, password)
                if (len(ansNew) != len(ans)):
                    print("NEW!!!")
                    send_email("zhaoyi1031@gmail.com", "zy12345678", [to], "New Score Appears!", "Now:\n"+str(ans))
                tot = tot+1
                print('Query',tot,': ',ansNew)
                break
            except Exception:
                print("error")
        ans = ansNew
        time.sleep(5)
        


