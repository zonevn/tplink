import base64
import hashlib
import re
import urllib

import requests


class WR841Nv11:
    LOGIN_URL = "http://{0}/userRpm/LoginRpm.htm?Save=Save"
    LOGOUT_URL = "http://{0}/{1}/userRpm/LogoutRpm.htm"
    REBOOT_URL = "http://{0}/{1}/userRpm/SysRebootRpm.htm"
    PPPOE_URL = "http://{0}/{1}/userRpm/PPPoECfgRpm.htm"
    VLAN_URL = "http://{0}/{1}/userRpm/LanBrModeRpm.htm"
    AUTH_KEY_RE = r"http\://[0-9A-Za-z.]+/([A-Z]{16})/userRpm/Index.htm"

    def __init__(self, host='192.168.0.1', user='admin', password='admin'):
        self.host = host

        md5 = hashlib.md5(password.encode())
        password = md5.hexdigest()

        auth = urllib.parse.quote(
            "Basic {0}".format(
                base64.b64encode(
                    "{0}:{1}".format(user, password).encode('ascii')
                ).decode('ascii')
            )
        )
        self.auth_cookie = {'Authorization': auth}
        self.key = WR841Nv11.__login__(self)

    def __login__(self):
        res = requests.get("http://{0}".format(self.host))
        print(res.status_code)
        if res.status_code != 200:
            raise Exception("Response from {0} not OK".format(self.host))

        res = requests.get(self.LOGIN_URL.format(self.host), cookies=self.auth_cookie)
        auth_key_match = re.search(self.AUTH_KEY_RE, res.text)

        if auth_key_match:
            return auth_key_match.group(1)
        else:
            raise Exception("Login error. No authentication key found in response.")

    def __logout__(self):
        requests.get(self.LOGOUT_URL.format(self.host, self.key),
                     cookies=self.auth_cookie)

    def reboot(self):
        res = requests.get(self.REBOOT_URL.format(self.host, self.key),
                           cookies=self.auth_cookie,
                           headers={'referer': self.REBOOT_URL.format(self.host, self.key)},
                           params={'Reboot': 'Reboot'})
        print("Reboot error" if res.status_code != 200 else "Router rebooting")

    def set_auth(self, account, password):
        query_params = {
            'wan': '0',
            'wantype': '2',
            'acc': account,
            'psw': password,
            'confirm': password,
            'SecType': '0',
            'sta_ip': '0.0.0.0',
            'sta_mask': '0.0.0.0',
            'linktype': '2',
            'Save': 'Save'
        }

        res = requests.get(self.PPPOE_URL.format(self.host, self.key),
                           cookies=self.auth_cookie,
                           headers={
                               'referer': self.PPPOE_URL.format(self.host, self.key)
                           },
                           params=query_params)
        print("PPPoE error" if res.status_code != 200 else "Assigned {0} to PPPoE".format(account))

    def tag_vlan(self, enable=False):
        query_params = {
            'mode_sel': '2',
            'nat_vid': '35',
            'vlanInetEnb': '1',
            'nat_pri': '0',
            'iptv_vid': '36',
            'iptv_pri': '4',
            'ip_phone_vid': '37',
            'ip_phone_pri': '5',
            'Lan': '0',
            'Lan': '0',
            'Lan': '0',
            'lan_brmask': '15',
            'lan_iptv_mask': '0',
            'lan_ipPhone_mask': '0',
            'Save': 'Save'
        } if enable else {
            'mode_sel': '0',
            'lan_brmask': '15',
            'lan_iptv_mask': '0',
            'lan_ipPhone_mask': '0',
            'Save': 'Save'
        }

        res = requests.get(self.VLAN_URL.format(self.host, self.key),
                           cookies=self.auth_cookie,
                           headers={
                               'referer': self.VLAN_URL.format(self.host, self.key)
                           },
                           params=query_params)
        print("Modification of VLAN error" if res.status_code != 200 else "VLAN modified. Router rebooting")


class WR841Nv8:
    STATUS_URL = "http://{0}/userRpm/StatusRpm.htm"
    VLAN_URL = "http://{0}/userRpm/VlanTagCfgRpm.htm"
    PPPOE_URL = "http://{0}/userRpm/PPPoECfgRpm.htm"
    REBOOT_URL = "http://{0}/userRpm/SysRebootRpm.htm"

    def __init__(self, host, user='admin', password='admin'):
        self.host = host
        self.auth = 'Basic {}'.format(base64.b64encode('{0}:{1}'.format(user, password).encode()).decode('ascii'))

    def tag_vlan(self, enable=False):
        res = requests.get(self.VLAN_URL.format(self.host), headers={
            'Authorization': self.auth,
            'Referer': self.VLAN_URL.format(self.host)
        }, params={
            'vlan_enb': 1,
            'nat_vid': 35,
            'nat_pri': 0,
            'iptv_vid': 36,
            'iptv_pri': 4,
            'Lan': 0,
            'Lan': 0,
            'Lan': 0,
            'lan_brmask': 15,
            'Save': 'Save'
        } if enable else {
            'vlan_enb': 0,
            'lan_brmask': 15,
            'Save': 'Save'
        })
        print("Modification of VLAN error" if res.status_code != 200 else "VLAN modified. Router rebooting")

    def set_auth(self, account, password):
        res = requests.get(self.PPPOE_URL.format(self.host), headers={
            'Authorization': self.auth,
            'Referer': self.PPPOE_URL.format(self.host)
        }, params={
            'wan': 0,
            'wantype': 2,
            'acc': account,
            'psw': password,
            'confirm': password,
            'SecType': 0,
            'sta_ip': '0.0.0.0',
            'sta_mask': '0.0.0.0',
            'linktype': '2',
            'Connect': 'Connect'
        })
        print("PPPoE error" if res.status_code != 200 else "Assigned {0} to PPPoE".format(account))

    def reboot(self):
        res = requests.get(self.REBOOT_URL.format(self.host), headers={
            'Authorization': self.auth,
            'Referer': self.REBOOT_URL.format(self.host)
        }, params={
            'Reboot': 'Reboot'
        })
        print("Reboot error" if res.status_code != 200 else "Router rebooting")
