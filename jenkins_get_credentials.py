import sys
import os
import requests

region = 'us-east-1'
credentials_file = "/var/lib/jenkins/.aws/credentials"
dir = '/var/lib/jenkins/.aws'

current_role    = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
credentials     = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/%s' % (current_role))
obj 		= credentials.json()

access_key_id     = obj["AccessKeyId"]
token             = obj["Token"]
secret_access_key = obj["SecretAccessKey"]
expiration        = obj["Expiration"]

if not os.path.exists(dir):
	os.makedirs(dir)

with open(credentials_file, 'w') as f:
	f.write('[jenkins_role]\n')
	f.write('region = %s\n' % region)
	f.write('output = json\n')
	f.write('aws_session_token = %s\n' % token)
	f.write('aws_access_key_id = %s\n' % access_key_id)
	f.write('aws_secret_access_key = %s\n' % secret_access_key)
	f.write('aws_session_expires_utc = %s\n' % expiration)
