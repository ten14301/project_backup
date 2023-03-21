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
                while not trigger.wait(7200):
                    print ("2 hour has passed")
                    now = datetime.now()
                    print("now =", now)
                    dt_string2 = now.strftime("%d/%m/%Y %H:%M:%S")
                    print("date and time =", dt_string2)
                    cur = conn.cursor() 
                    cur.execute("update dtmoisensor10 set datet = (%s)",(dt_string2, ))
                    cur.execute("update dtmoisensor20 set datet = (%s)",(dt_string2, ))
                    cur.execute("update dtmoisensor30 set datet = (%s)",(dt_string2, ))
                    cur.execute("update hour1data set data = (%s)",(ib0, ))
                    cur.execute("update hour2data set data = (%s)",(ib1, ))
                    cur.execute("update hour3data set data = (%s)",(ib2, ))
                    conn.commit()
trigger = threading.Event()
the_thread = threading.Thread(name='wait_an_event_thread', 
                              target=wait_an_event_thread,
                              args=(trigger,))
the_thread.start()	
