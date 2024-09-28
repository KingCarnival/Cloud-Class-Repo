# Dependency Imports
import boto3
from operator import itemgetter

#get region and snapshots
ec2_client = boto3.client('ec2', region_name = "eu-west-3")

snapshots =  ec2_client.describe_snapshots(
    OwnerIds =['self']
)

# sort snapshots in descending order
sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)


for snap in sorted_by_date[2:]:
    # delete snapshot here
    response = ec2_client.delete_snapshot(
        SnapshotId = snap['SnapshotId']
    )
    print(response)