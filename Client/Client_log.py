# -*- coding: utf-8 -*-


from datetime import datetime
import sqlite3
import time
sqlite_file = 'example.db'


class Log():
    #Var globales
    logLocation = "log.txt"
    parent=None
    organisation=""
    user=""
    clientip=None
    dbip=None
    
#    def __init__(self,organisation="Organisation",user="User",action="Action",ip = "8.8.8.8",db="1.1.1.1"):
    def __init__(self,ip):
        self.clientip=ip
        
        #=======================================================================
        # logLocation='Logs.sqlite'
        # logdb = sqlite3.connect(logLocation)
        # curseur = logdb.cursor()
        # curseur.execute('''CREATE TABLE logs (date text, organisation text, user text, ip text, db text, module text, action text)''')
        #=======================================================================
        
        #=======================================================================
        # 
        # conn.commit()
        # conn.close()
        # 
        # #Ecrit le log localement
        # self.log  = open(self.logLocation, "w")
        # self.log.write(time.strftime("%c")+" - "+organisation+" - "+user+" - "+ip+" - "+db+" - "+module+" - "+action)
        # self.log.close()
        #=======================================================================
    pass

    def setLog(self,organisation="Organisation",user="User",db="1.1.1.1"):
        #Assigner les valeurs qui ne changeront pas directement dans la classe
        self.organisation=organisation
        self.user=user
        self.dbip=db
        pass

    def setLogParent(self,parent):
        self.parent=parent
           
    def writeLog(self,action="Actionman",module="Client"):
        print(self.getTime() + " "+self.organisation + " "+self.user + " "+self.clientip + " "+self.dbip + " "+module + " "+action)
        self.parent.serveur.writeLog(self.getTime(),self.organisation,self.user,self.clientip,self.dbip,module,action)
        pass
    
    #===========================================================================
    # def logWrite2(self,module="a.py",action="Action"):
    #     #log in txt file
    #     self.log = open(self.logLocation, "a")
    #     self.log.write("\n"+time.strftime("%c")+" - "+organisation+" - "+user+" - "+ip+" - "+db+" - "+module+" - "+action)
    #     self.log.close()
    #===========================================================================
        
    #===========================================================================
    # def logRead(self):
    #     with open(self.logLocation) as f:
    #         for line in f:
    #             print (line,end="")         
    #     f.closed
    #===========================================================================
    
    def getTime(self):
        return (datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
