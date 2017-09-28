#!/bin/bash
ACCOUNT_NUMBER=$1
ROLE=$2
FILENAME=/var/lib/jenkins/.aws/config
REGION=us-east-1
rm ${FILENAME}
cat >> ${FILENAME} << EOF
[profile jenkins_role]
[profile ${ACCOUNT_NUMBER}]
role_arn = arn:aws:iam::${ACCOUNT_NUMBER}:role/${ROLE}
source_profile = jenkins_role
region = ${REGION}
EOF
cat ${FILENAME}
