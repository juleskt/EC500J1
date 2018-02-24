import subprocess
import os
import serial
import time
import signal
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Lab2-GSheet').sheet1

for r in range (1,5):
	print (' '*40)
	print ('Row: %d' % r)
	for c in range (1,5):
		fortuneCall = subprocess.Popen(['fortune'], stdout=subprocess.PIPE)
		wks.update_cell(r,c, fortuneCall.stdout.readlines())
		print ("[",r,",",c,"]: ",wks.cell(r,c).value)
