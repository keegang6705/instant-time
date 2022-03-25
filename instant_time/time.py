import time
from datetime import datetime
import pytz
def timestamp(timezone: pytz.timezone,integer: bool =False):
    tme = datetime.now(pytz.timezone(f"{timezone}"))
    tmstamp = datetime.timestamp(tme)
    if integer == True:
        return int(tmstamp)
    elif integer == False:
        return tmstamp
    else:
        return tmstamp
def date(timezone: pytz.timezone):
    tme = datetime.now(pytz.timezone(f"{timezone}"))
    tmf = tme.strftime(f"%A %d %B(%m) %G | %H:%M:%S")
    return tmf