from ephemvpn import xkcd_password
my_wordlist = xkcd_password.generate_wordlist(wordfile=xkcd_password.wordfile,
                                min_length=5,
                                max_length=9,
                                valid_chars='.')



def human_readble_pass():
    return xkcd_password.generate_xkcdpassword(my_wordlist,
                                interactive=False,
                                n_words=4,
                                acrostic=False)

names = [ 'bob', 'yoda', 'mcfly', 'eminem', 'ghandi', 'jeff', 'joan', 'hillary', 'robin' ]

class VPNConfig(object):

    def __init__(self, config, running_minutes):
        self.config = config
        self.running_minutes = running_minutes

    def config_script(self):
        '''
        Retrieve the script to be passed to the instance during creation
        via the user data field
        '''
        return ""

    def needs_post_configure(self):
        '''
        Do we need to call post configure?"
        '''
        return False

    def post_configure(self):
        '''
        Run after the instance has been started.
        '''
        pass

    def data(self):
        '''
        The data required by the user to connect to the VPN
        '''

    def human_readable_data(self):
        '''
        Message to display to the user after setup
        '''

# import vpn types
# TODO do this all dynamically?

from ipsec import IPSecVPN

TYPES = { 'ipsec' : IPSecVPN }

def _vpn(vpn_type):
    if vpn_type not in TYPES.keys():
        raise ValueError('Unknown VPN Type {0}'.format(vpn_type))

    return TYPES[vpn_type]

def VPN(vpn_type, config_parser, running_minutes):
    return _vpn(vpn_type)(config_parser, running_minutes)

