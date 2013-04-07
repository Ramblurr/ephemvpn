from time import sleep
from fabric.api import settings
from ephemvpn import configuration as config
from ephemvpn import vpntypes
from ephemvpn import awshelpers as aws
import logging as log

__version_info__ = (0,1)
__version__ = '.'.join(map(str, __version_info__))


def launch(vpn, aws_region):
    '''Launch a single instance of the provided ami

    Parameters:
        vpn   -- the VPN object
    '''

    root_device = '/dev/sda1'
    root_device_size = '10'

    ec2_connection= aws._get_ec2_connection(aws_region)
    log.info('preparing cloud conjuring ritual')
    aws._create_security_group(ec2_connection)
    ami_id = config.AMI_ID_BY_REGION[ec2_connection.region.name]
    mapping = aws._get_block_device_mapping(root_device, root_device_size, delete_on_terminate=True)
    reservation = ec2_connection.run_instances(
            ami_id,
            key_name=config.AWS_KEY_FILE,
            security_group_ids=[config.AMI_SECURITY_GROUP],
            block_device_map=mapping,
            instance_initiated_shutdown_behavior='terminate',
            instance_type='t1.micro',
            user_data = vpn.config_script()
    )

    # TODO good idea to assume it's the first one?
    instance = reservation.instances[0]
    log.info('summoning a vpn from the cloud . . .')
    sleep(10)

    instance.update()

    while instance.state != 'running':
        sleep(3)
        log.info(' . . .')
        instance.update()

    if instance.state == 'running':
        log.debug('new instance "' + instance.id + '" accessible at ' + instance.public_dns_name)
    else:
        log.error('starting failed. instance status: ' + instance.state)
        return None

    instance.add_tag('vpn_type', vpn._type)
    return instance.public_dns_name


def configure(hostname, vpn):
    log.debug('configuring instance')
    with settings(host_string=hostname, key_filename=config.LOCAL_AWS_KEY_FILE,
        user=config.AWS_USER_NAME,connection_attempts=10):
        vpn.post_configure()



