#!/usr/bin/env python3
import easyquotation
import requests
from json import loads
code='131810'
quotation = easyquotation.use('sina')
quote = quotation.stocks(code)
buy = quote[code]['buy']
payload = {'app': 'c1433827-a6ab-902e-d3af-f169eb7a2c22','eventId': '12345','eventType': 'trigger','alarmName':code+' rush'}
if buy>7.5:
  print(code + " rush!")
  res = requests.post('http://api.110monitor.com/alert/api/event', data = payload)
  print(res.content)
