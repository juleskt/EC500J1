import subprocess
import time
import gspread
from random import randint
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

SECONDS_IN_A_MINUTE = 60

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Lab2-GSheet').sheet1

def hasBeenThirtySeconds(lastPrintTime):
    if (time.time() - lastPrintTime >= 30):
        return True

    return False

rowCount = 1
lastPrint = time.time()
duration = time.time() + (SECONDS_IN_A_MINUTE*3)

while time.time() < duration:
	if (randint(0,10000) is randint(0,5000) or hasBeenThirtySeconds(lastPrint)):
		fortuneCall = subprocess.Popen(['fortune'], stdout=subprocess.PIPE)
		fortuneMsg = fortuneCall.stdout.readlines()
		timeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
		
		print (timeStamp, fortuneMsg)
		wks.update_cell(rowCount, 1, timeStamp)
		wks.update_cell(rowCount, 2, fortuneMsg)
		
		rowCount = rowCount + 1
		lastPrint = time.time()

