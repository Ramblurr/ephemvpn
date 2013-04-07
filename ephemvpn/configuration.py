AWS_API_KEY = None
AWS_SECRET_KEY = None
AWS_KEY_FILE = None
LOCAL_AWS_KEY_FILE = None
#AMI SETTINGS
# AMI IDs are available on http://cloud.ubuntu.com/ami/

# Ubuntu 12.04 EBS Backed Instances
AMI_ID_BY_REGION = {
    'ap-northeast-1' : 'ami-d71a9ad6',
    'ap-southeast-1' : 'ami-6686ca34',
    'ap-southeast-2' : 'ami-4a38a970',
    'eu-west-1'      : 'ami-1ef5ff6a',
    'sa-east-1'      : 'ami-c371aade',
    'us-east-1'      : 'ami-1ebb2077',
    'us-west-1'      : 'ami-b0c3eef5',
    'us-west-2'      : 'ami-3a891d0a',
}

# Ubuntu 12.04 instance-store Backed Instances
AMI_ID_BY_REGION_INSTANCE = {
    'ap-northeast-1' :  'ami-bd1797bc',
    'ap-southeast-1' :  'ami-ae85c9fc',
    'ap-southeast-2' :  'ami-5238a968',
    'eu-west-1'      :  'ami-02f4fe76',
    'sa-east-1'      :  'ami-a771aaba',
    'us-east-1'      :  'ami-e2861d8b',
    'us-west-1'      :  'ami-f6c3eeb3',
    'us-west-2'      :  'ami-8c881cbc',
}

AMI_SECURITY_GROUP = 'vpn'
AMI_TYPES = ('vpnipsec',)
AWS_USER_NAME = 'ubuntu'

AT_RUNNING_MINUTES = "60"
