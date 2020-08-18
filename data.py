from builtins import print

import requests
from requests.auth import HTTPBasicAuth


response = requests.get("https://enrollment.sipthor.net/settings.phtml?action=get_history&realm=sip2sip.info",
                        auth=HTTPBasicAuth('zvonek1','Silent5Killer'))
data=response.json()
print(type(data))
print(data)