import boto3
from operator import itemgetter
import schedule

ec2_client = boto3.client('ec2', region_name="us-east-2")

def remove_volume_snapshots():
  volumes = ec2_client.describe_volumes(
      Filters=[
          {
              'Name': 'tag:Name',
              'Values': ['prod']
          }
      ]
  )

  print(volumes['Volumes'])

  for volume in volumes['Volumes']:
      snapshots = ec2_client.describe_snapshots(
          OwnerIds=['self'],
          Filters=[
              {
                  'Name': 'volume-id',
                  'Values': [volume['VolumeId']]
              }
          ]
      )

      sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)
      print('Deleting snapshot:', snapshots)

      for snap in sorted_by_date[2:]:
          response = ec2_client.delete_snapshot(
              SnapshotId=snap['SnapshotId']
          )
          print(response)

# remove_volume_snapshots()

schedule.every().week.do(remove_volume_snapshots)

while True:
    schedule.run_pending()