import json

with open('sample-data.json') as pars_json:
    jsonData = json.load(pars_json)

data=jsonData["imdata"]
print('Interface Status\n' + 85*'=' + '\nDN' + 49*' ' +'Description          Speed   MTU\n' + 50*'-' + ' ' + 20*'-' + ' ' + 6*'-' + ' ' + 6*'-')

for i in data:
    status = ""
    item = i["l1PhysIf"]
    at = item["attributes"]
    Dn = at["dn"]
    Speed = at["speed"]
    MTU = at["mtu"]
    
    if(len(Dn)==42):
        status += Dn + 30*' '  +Speed+'  '+ MTU
    else:
        status += Dn + 31*' ' + Speed + '  ' + MTU
    print(status)
