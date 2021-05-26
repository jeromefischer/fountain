import json

import requests


r =requests.get('http://tasmota_brunnen/cm?cmnd=status%2010')
# print(r.content)

# res = r.content.decode("utf-8")
res = json.loads(r.content)
print(res)

print(res['StatusSNS']['ENERGY']['Voltage'])
# res = res['StatusSNS']['ENERGY']

with open('meas.json', 'w') as outfile:
    json.dump(res, outfile, indent=4)


