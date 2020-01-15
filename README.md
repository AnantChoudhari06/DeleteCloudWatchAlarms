# DeleteCloudWatchAlarms
This script checks if the CloudWatch alarm exists or not and provides the response


While deleting the CloudWatch alarm via the Boto3 or the AWS CLI, there is no output which shows if the Alarm was successfully deleted or was there any error.



If you provide an Alarm Name that does not even exist or has already been deleted, the command does not give any sort of error messgae.



For example, Alarm 'Testing' does not exist in my account but the following Boto3 script goes through without any errors:


cloudwatch.delete_alarms(
  AlarmNames=['Testing'],
)


As a workaround, this Python script does the following:

--Make a describe alarms API call and get the List of existing alarms
--Get the alarm name from the user that has to be deleted
--Check if that Alarm exsists in the List of Alarms
  --If yes: Delete the Alarm
  --Else: Provide an error message
