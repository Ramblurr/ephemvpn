import os
import random
import ConfigParser
from pipes import quote as q
from ephemvpn.vpntypes import VPNConfig, names, human_readble_pass


class IPSecVPN(VPNConfig):
    _type = 'ipsec'

    def __init__(self, config, running_minutes):

        defaults = {
                'user'     : random.choice(names),
                'password' : human_readble_pass(),
                'psk'      : human_readble_pass()
        }

        try:
            defaults['user']     = config.get(self._type, 'user')
            defaults['password'] = config.get(self._type, 'password')
            defaults['psk']      = config.get(self._type, 'psk')
        except ConfigParser.NoSectionError:
            pass

        VPNConfig.__init__(self, defaults, running_minutes)



    def config_script(self):
        fname  = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data/ipsec-config.sh")
        f      = open(fname, 'r')
        script = f.read()
        f.close()

        psk      = q(self.config['psk'])
        user     = q(self.config['user'])
        password = q(self.config['password'])

        return script.format(psk, user, password, self.running_minutes)

    def _data(self):
        return self.config

    def human_readable_data(self):
        return {
                "VPN type"             : "IPSEC/L2TP PSK",
                "Pre-shared key (PSK)" : self.config['psk'],
                "Username"             : self.config['user'],
                "Password"             : self.config['password']
               }

