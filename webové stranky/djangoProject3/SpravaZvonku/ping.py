import os

hostname = "192.168.0.1"
response = os.system("ping " + hostname + " /n 1")


if response == 0:
  print ('Zvonke je dostupny')
else:
  print ('Zvonke je nedostupny!')