def getConf(config_file_path):
    with open(config_file_path,'rt',encoding='utf-8') as f:#'conf.ini'
        for line in f:
            if (line.find("user =") != -1):
                username = line[6:-1].strip()
                #print(username)
            if (line.find("password =") != -1):
                password = line[10:-1].strip()
                #print(password)
            if (line.find("to =") != -1):
                to = line[4:-1].strip()#.strip('"')
                #print(to)
        return username, password, to


