import RPi.GPIO as G
import time
import MySQLdb

G.setwarnings(False)
G.setmode(G.BCM)
G.setup(17,G.OUT)
G.setup(27,G.OUT)
G.setup(22,G.OUT)
G.setup(5,G.OUT)
G.setup(6,G.OUT)
G.setup(13,G.OUT)

                                                                          
conn = MySQLdb.connect( 
        host='localhost', 
        user='techno',  
        password = "admin", 
        db='TECHNOFRAM', 
        )
while True:        
#############################################

    cur = conn.cursor() 
    cur.execute("SELECT ALELAY1 FROM ALELAY WHERE id = 1;") 
    conn.commit()
    for row in cur.fetchall():
        l1 = row[0]
        G.output(17,int(l1))
#############################################   
    cur = conn.cursor() 
    cur.execute("SELECT ALELAY1 FROM ALELAY WHERE id = 2;") 
    conn.commit()
    for row in cur.fetchall():
        l2 = row[0]
        G.output(27,int(l2))
#############################################   
    cur = conn.cursor() 
    cur.execute("SELECT ALELAY1 FROM ALELAY WHERE id = 3;") 
    conn.commit()
    for row in cur.fetchall():
        l3 = row[0]
        G.output(22,int(l3))
#############################################   
    cur = conn.cursor() 
    cur.execute("SELECT ALELAY1 FROM ALELAY WHERE id = 4;") 
    conn.commit()
    for row in cur.fetchall():
        l4 = row[0]
        G.output(5,int(l4))
#############################################   
    cur = conn.cursor() 
    cur.execute("SELECT ALELAY1 FROM ALELAY WHERE id = 5;") 
    conn.commit()
    for row in cur.fetchall():
        l5 = row[0]
        G.output(6,int(l5))
#############################################   
    cur = conn.cursor() 
    cur.execute("SELECT ALELAY1 FROM ALELAY WHERE id = 6;") 
    conn.commit()
    for row in cur.fetchall():
        l6 = row[0]
        G.output(13,int(l6))


    


      



           




