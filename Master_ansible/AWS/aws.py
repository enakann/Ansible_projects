import boto3
from boto import ec2
#connection=ec2.connect_to_region('us-east-2',aws_access_key_id='AKIAIGGSS2746BMNPW2A',aws_secret_access_key='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')

connection=ec2.connect_to_region('us-east-2',aws_access_key_id='AKIAJWZLQW4YZJXGKNDA',aws_secret_access_key='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')
reservations=connection.get_all_instances();
for reservation in reservations:
 for instances in reservation.instances:
     print(instances.tags['Name'], instances.ip_address)
#http://www.tothenew.com/blog/getting-started-with-boto-python-interface-for-aws/

