import requests
from django.shortcuts import render
import sys
import os
import json
from subprocess import run, PIPE
from requests.auth import HTTPDigestAuth

def button(request):
    return render(request,'home.html')

def ping(request):
    hostname = "192.168.0.5"
    response = os.system("ping " + hostname + " /n 1" " /w 5")

    if response == 0:
        print('Zvonke je dostupny')
        data="Zvonek je dostupny"
        return render(request, 'home.html', {'data': data})

    else:
        print('Zvonke je nedostupny!')
        data = "Zvonek je nedostupny"
        return render(request, 'home.html', {'data': data})




def data(request):
    out = run([sys.executable, 'C:\\Users\\tomas\\PycharmProjects\\djangoProject3\\SpravaZvonku\\data.py', ],shell=False,stdout=PIPE)
    print(out)
    return render(request, 'home.html', {'out2': out.stdout})

def data2(request):
    response = requests.get("https://enrollment.sipthor.net/settings.phtml?action=get_history&realm=sip2sip.info",
                            auth=HTTPDigestAuth('zvonek1', 'Silent5Killer'))
    data = response.json()
    data = json.dumps(data)

    with open("data.json", "w") as f:
        f.write(data)

    with open('data.json') as json_file:
        data = json.load(json_file)

        for p in data['placed']:
            text = 'From: ' + 'zvonek1@sip2sip.info' + ' To: ' + p['remoteParty'] + ' Start time: ' + p['startTime'] + ' Stop Time: ' + p['stopTime'] + ' ' +'/n'

    return render(request, 'home.html', {'out1': text})