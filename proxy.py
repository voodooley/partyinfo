# name
# pass
# antwort: 560c30be28c2e9e17fb82dc98bb39b01

# name=voodoobet@yandex.ru
# pass=5/Nigfbu
# antwort=0691e4720280a8990ad058987108405e

# https://partyinfo.ru/auth
import requests


def loginsite(login, password):
    s = requests.Session()
    s.get('https://partyinfo.ru/tabs?info=contacts&ess=event&essid=10392&cat=10392', verify=False)
    data = {
        'name': login,
        'pass': password,
        'antwort': '0691e4720280a8990ad058987108405e'
    }

    r = s.post('https://partyinfo.ru/auth', data=data)

    some = requests.get('https://partyinfo.ru/tabs?info=contacts&ess=event&essid=10392&cat=10392', verify=False, cookies=r.cookies)

    return some.text


r = loginsite('voodoobet@yandex.ru', '5/Nigfbu')


print(r)
