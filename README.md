Ephemeral VPN
============

VPNs that last a short time.

**Example:**

    # ephemvpn -t 5m
    ephemvpn v0.1
    summoning one ipsec vpn
    the vpn will be released into the ether 5 minutes after boot
    (probably around Sun Apr 07 16:54 2013)
    proceed? [n]|y: y
    preparing cloud conjuring ritual
    summoning a vpn from the cloud . . .
     . . .
     . . .
     . . .

    ephemeral vpn summoned

                VPN type: IPSEC/L2TP PSK
    Pre-shared key (PSK): unknown impish shorten downtown
                Username: mcfly
                Password: baton loony paycheck obituary
                Hostname: ec2-54-246-64-31.eu-west-1.compute.amazonaws.com

## Setup

### 1. Python

Requires Python 2.7 and virtualenv

Create your virtualenv then:

    $ source your/virtenv/bin/activate
    $ git clone https://github.com/Ramblurr/ephemvpn.git
    $ cd ephemvpn
    $ pip install -e .

(TODO: submit to pypi?)

### 2. EC2

1. A valid AWS account with API and Secret Keys is required.
2. Create a SSH Key Pair for each region(s) which will be used to store AMIs and run instances.
3. Copy the private key to your local machine's "ssh" directory (~/.ssh on Linux), don't forget to chmod 600 it

### 3. Config

Create `~/.ephemvpnrc` with your credentials, unless you want to specify them on
the command line every time

Finally, `$ ephemvpn` to summon a vpn.

## TODO & Known Issues

* Audit ipsec config
* Add Openvpn
* Generate keypair for user ([ctrl+f create_keypair here](http://boto.s3.amazonaws.com/ref/ec2.html))

## License and Credits

ephemvpn is licensed under the BSD 3-clause license. Various components retain
their own licenses:

**EC2 and boto snippets**

* [dixonwh/aws-provisioning](https://github.com/dixonwh/aws-provisioning) for some EC2+boto snippets

**ipsec config**

The IPSEC config script is Copyright Thomas Sarlandie 2012 It is licensed under
the Creative Commons Attribution-ShareAlike 3.0 Unported License:
http://creativecommons.org/licenses/by-sa/3.0/

Project: [sarfata/voodooprivacy](https://github.com/sarfata/voodooprivacy)

