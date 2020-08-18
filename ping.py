import os

hostname = "192.168.0.1"
response = os.system("ping " + hostname + " /n 1")


if response == 0:
  test = True
  print ('Zvonke je dostupny')
else:
  test = False
  print ('Zvonek je nedostupny!')