import time
from datetime import datetime, timedelta
import threading
import MySQLdb
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

conn = MySQLdb.connect( 
        host='localhost', 
        user='moihour',  
        password = "admin", 
        db='moisensor', 
        )
        
# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.


# Main program loop.
    # Read all the ADC channel values in a list.
values = [0]*8
for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
        ib0 = values[0]
        ib1 = values[1]
        ib2 = values[2]
        ib3 = values[3]
        ib4 = values[4]
        ib5 = values[5]
        ib6 = values[6]

def wait_an_event_thread(trigger):
            while not trigger.wait(3600):
                print ("1 hour has passed")
                now = datetime.now()
                print("now =", now)
                global ib0,ib1,ib2

                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                
                print("date and time =", dt_string)
                print(ib0)
                print(ib1)
                print(ib2)
                a = dt_string
                cur = conn.cursor() 
                cur.execute("update dtmoisensor10 set datet = (%s)",(dt_string, ))
                cur.execute("update dtmoisensor20 set datet = (%s)",(dt_string, ))
                cur.execute("update dtmoisensor30 set datet = (%s)",(dt_string, ))
                cur.execute("update hour1data set data = (%s)",(ib0, ))
                cur.execute("update hour1datab set data = (%s)",(ib1, ))
                cur.execute("update hour1datac set data = (%s)",(ib2, ))

                conn.commit()

            



trigger = threading.Event()
the_thread = threading.Thread(name='wait_an_event_thread', 
                              target=wait_an_event_thread,
                              args=(trigger,))

    
the_thread.start()                              



    


    
