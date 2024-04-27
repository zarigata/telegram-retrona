from time import sleep, ctime, localtime, gmtime
import os


def get_current_date():
    return str(ctime())
print("Current date is : " + get_current_date() )
