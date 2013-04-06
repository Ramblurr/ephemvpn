from boto.ec2.blockdevicemapping import BlockDeviceType
from boto.ec2 import connect_to_region
from boto.ec2.blockdevicemapping import BlockDeviceMapping

import configuration as config

def _create_security_group(conn):

    groups = conn.get_all_security_groups()
    for g in groups:
        if config.AMI_SECURITY_GROUP == g.name:
            return

    sec = conn.create_security_group(config.AMI_SECURITY_GROUP, 'VPN Security Group')
    # TODO only allow us to ssh
    sec.authorize('tcp', 22, 22, '0.0.0.0/0')

    sec.authorize('tcp', 500, 500, '0.0.0.0/0')
    sec.authorize('udp', 500, 4500, '0.0.0.0/0')


def _get_ec2_connection(aws_region):
    """ Creates an EC2 Connection for the specified region.

    parameters:
    aws_region -- the aws region code (us-east-1, us-west-1, etc)
    """
    return connect_to_region(aws_region, aws_access_key_id=config.AWS_API_KEY, aws_secret_access_key=config.AWS_SECRET_KEY)


def _get_block_device_mapping(device_name, size, delete_on_terminate = False):
    """ Returns a block device mapping object for the specified device and size.

    Block Device Mapping is used to associate a device on the VM with an EBS Volume.

    parameters:
    device_name -- The name of the device in the VM, such as /dev/sda1, /dev/sdb1. etc
    size -- The amount of space to allocate for the EBS drive.
    delete_on_terminate -- Whether the volume should be deleted when the instance is terminated

    """
    block_device = BlockDeviceType(delete_on_termination=delete_on_terminate)
    block_device.size = size
    bdm = BlockDeviceMapping()
    bdm[device_name] = block_device

    return bdm


