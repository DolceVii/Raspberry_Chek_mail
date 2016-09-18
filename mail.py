!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time
import os

DEBUG = 1

USERNAME = "User"       # just the part before the @ sign, add yours here
PASSWORD = "Pass"       # Your pass

NEWMAIL_OFFSET = 1      # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 180   # check mail every 3 minutes

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

try:
    while True:

        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

        if DEBUG:
                os.system("clear")
                print "You have", newmails, "new emails!"

        if newmails > NEWMAIL_OFFSET:
                GPIO.output(GREEN_LED, True)
                GPIO.output(RED_LED, False)
        else:
                GPIO.output(GREEN_LED, False)
                GPIO.output(RED_LED, True)

        time.sleep(MAIL_CHECK_FREQ)
    
except KeyboardInterrupt:
      GPIO.cleanup()
