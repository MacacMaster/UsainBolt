# -*- coding: UTF-8 -*-


import time
import sqlite3
sqlite_file = 'example.db'


class Log():
    logLocation = "log.txt"
    def __init__(self,organisation="Organisation",user="User",action="Action",ip = "8.8.8.8",db="1.1.1.1"):
        #Assigner les valeurs qui ne changeront pas directement dans la classe
        self.organisation=organisation
        self.user=user
        self.clientip=ip
        
        #testing only
        conn = sqlite3.connect(sqlite_file)
        c=conn.cursor()
        self.table = "logs"
        #c.execute('''CREATE TABLE ' (date text, organisation text, user text, ip text, db text, module text, action text)''')
        
        c.execute('INSERT INTO {tn} ({nf} {ft})'\
                  .format(tn="table_name1", nf="new_field", ft="field_type"))
        
        conn.commit()
        conn.close()
        
        #Ecrit le log localement
        self.log  = open(self.logLocation, "w")
        self.log.write(time.strftime("%c")+" - "+organisation+" - "+user+" - "+ip+" - "+db+" - "+module+" - "+action)
        self.log.close()
    pass

    def logWrite(self,module="a.py",action="Action"):
        self.log = open(self.logLocation, "a")
        self.log.write("\n"+time.strftime("%c")+" - "+organisation+" - "+user+" - "+ip+" - "+db+" - "+module+" - "+action)
        self.log.close()
        
    def logRead(self):
        with open(self.logLocation) as f:
            for line in f:
                print (line,end="")         
        f.closed
    
    def sendLog(self):
        
        pass

if __name__ == '__main__':
    logclass=Log()
    logclass.logWrite("Org","USR")
    logclass.logRead()
    pass