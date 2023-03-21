import time
from datetime import datetime
import threading
import MySQLdb
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


               
conn = MySQLdb.connect( 
        host='localhost', 
        user='moisensor',  
        password = "password", 
        db='moisensor', 
        )



# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)


# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
        
    # Print the ADC values.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    datasend0 = values[0]
    cur = conn.cursor() 
    cur.execute("insert into moidata values(%s)",(datasend0, ))
    cur.execute("update moirecent10 set data = (%s)",(datasend0, ))
    cur.execute("update recenttime1 set datet = (%s)",(dt_string, ))
    conn.commit()
    
    datasend1 = values[1]
    cur = conn.cursor() 
    cur.execute("insert into moidata2 values(%s)",(datasend1, ))
    cur.execute("update moirecent20 set data = (%s)",(datasend1, ))
    conn.commit()
    
    
    datasend2 = values[2]
    cur = conn.cursor() 
    cur.execute("insert into moidata3 values(%s)",(datasend2, ))
    cur.execute("update moirecent30 set data = (%s)",(datasend2, ))
    conn.commit()
    

    
    datasend3 = values[3]
    cur = conn.cursor() 
    cur.execute("insert into moidata4 values(%s)",(datasend3, ))
    cur.execute("update moirecent40 set data = (%s)",(datasend3, ))
    conn.commit()

    
    datasend4 = values[4]
    cur = conn.cursor() 
    cur.execute("insert into moidata5 values(%s)",(datasend4, ))
    cur.execute("update moirecent50 set data = (%s)",(datasend4, ))
    conn.commit()
    

    datasend5 = values[5]
    cur = conn.cursor() 
    cur.execute("insert into moidata6 values(%s)",(datasend5, ))
    cur.execute("update moirecent60 set data = (%s)",(datasend5, ))
    conn.commit()

    
    datasend6 = values[6]
    cur = conn.cursor() 
    cur.execute("insert into moidata7 values(%s)",(datasend6, ))
    cur.execute("update moirecent70 set data = (%s)",(datasend6, ))
    conn.commit()

    
    datasend7 = values[7]
    cur = conn.cursor() 
    cur.execute("insert into moidata8 values(%s)",(datasend7, ))
    cur.execute("update moirecent80 set data = (%s)",(datasend7, ))
    conn.commit()


    

        # Pause for half a second.
    time.sleep(0.5)




   
    
 
    



    
    



