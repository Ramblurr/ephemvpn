Ephemeral VPN
============

VPNs that last a short time.

**Example:**

    $ ephemvpn
    authenticating to EC2
    spinning up the instance
    new instance "i-a6c4eaec" accessible at ec2-54-247-59-196.eu-west-1.compute.amazonaws.com
    configuring instance ec2-54-247-59-196.eu-west-1.compute.amazonaws.com

    VPN Deployed

    VPN Type: IPSEC/L2TP
    Preshared Key (PSK): checked flapjack banality full-time
    Username: eminem
    Password: violet clasp refuge prevent
    Hostname: ec2-54-247-59-196.eu-west-1.compute.amazonaws.com


## Setup

### 1. Python

Requires Python 2.7 and virtualenv

Create your virtualenv then:

    pip install -e requirements.txt

### 2. EC2

1. A valid AWS account with API and Secret Keys is required.
2. Create a SSH Key Pair for each region(s) which will be used to store AMIs and run instances.
3. Copy the private key to your local machine's "ssh" directory (~/.ssh on Linux), don't forget to chmod 600 it

### 3. Config

Create ~/.ephemvpnrc with your credentials, unless you want to specify them on
the command line every time

Finally, `$ ./ephemvpnrc`

## TODO & Known Issues

* [ Turn the VPNS Off!!! ](http://stackoverflow.com/questions/10541363/self-terminating-aws-ec2-instance)
* Audit ipsec config
* Add Openvpn
* Generate keypair for user ([ctrl+f create_keypair here](http://boto.s3.amazonaws.com/ref/ec2.html))

## License and Credits

**EC2 and boto snippets**

* [dixonwh/aws-provisioning](https://github.com/dixonwh/aws-provisioning) for some EC2+boto snippets

**ipsec config**

The IPSEC config script is Copyright Thomas Sarlandie 2012 It is licensed under
the Creative Commons Attribution-ShareAlike 3.0 Unported License:
http://creativecommons.org/licenses/by-sa/3.0/

Project: [sarfata/voodooprivacy](https://github.com/sarfata/voodooprivacy)

