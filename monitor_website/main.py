import requests
import smtplib
import os
import paramiko
import boto3
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def restart_server_and_container():
    # restart linode server
    print('Rebooting the server...')
    ec2_resource = boto3.resource('ec2', region_name='us-east-2')
    ec2_client = boto3.client('ec2', region_name="us-east-2")
    ec2_client.reboot_instances(InstanceIds=['i-0e5d938204a8cce42'])

    # restart the application
    while True:
        instance = ec2_resource.Instance('i-0e5d938204a8cce42')
        print(instance.state['Name'])
        if instance.state['Name'] == 'running':
            print('Server is up and running! Restarting the container in 15 seconds...')
            time.sleep(15)
            restart_container()
            break


def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

def restart_container():
    print('Restarting the application...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='3.142.252.102', username='ec2-user', key_filename='/Users/tonyrudny/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl start docker')
    stdin, stdout, stderr = ssh.exec_command('docker start nginx')
    print(stdout.readlines())
    ssh.close()

# testing
# send_notification('Test message')
# restart_server_and_container()
# restart_container()


def monitor_application():
    try:
        response = requests.get('http://ec2-3-142-252-102.us-east-2.compute.amazonaws.com:8080/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f'Application returned {response.status_code}'
            send_notification(msg)
            restart_container()
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible at all'
        send_notification(msg)
        restart_server_and_container()


schedule.every(10).seconds.do(monitor_application)

while True:
    schedule.run_pending()
