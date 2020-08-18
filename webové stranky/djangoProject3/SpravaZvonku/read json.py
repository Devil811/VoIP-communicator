import json
from builtins import print

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['placed']:
        print('From: ' + p['remoteParty'])
        print('To:' + 'zvonek1@sip2sip.info')
        print('Start time:' + p['startTime'])
        print('Stop Time:' + p['stopTime'])
        print('')