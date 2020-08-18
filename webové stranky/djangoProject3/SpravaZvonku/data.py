import requests
from requests.auth import HTTPDigestAuth
import json
from builtins import print

response = requests.get("https://enrollment.sipthor.net/settings.phtml?action=get_history&realm=sip2sip.info",
                        auth=HTTPDigestAuth('zvonek1', 'Silent5Killer'))
data = response.json()
data = json.dumps(data)
with open("data.json", "w") as f:
    f.write(data)

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['placed']:
        print('From: ' + 'zvonek1@sip2sip.info' + ' To: ' + p['remoteParty'] + ' Start time: ' + p['startTime'] + '¨Stop Time: ' + p['stopTime'] + '')