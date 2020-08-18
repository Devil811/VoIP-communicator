import os

hostname = "192.168.0.1"
response = os.system("ping " + hostname + " /n 1")

#and then check the response...
if response == 0:
  test = True
  print (hostname, 'is up!')
else:
  test = False
  print (hostname, 'is down!')