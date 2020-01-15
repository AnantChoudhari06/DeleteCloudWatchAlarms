#!/usr/bin/python3
import boto3
import json
import re


print("\n")
# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

#List Alarms
response = cloudwatch.describe_alarms()

#Response is of type 'Dict'. Get the values for the key 'MetricAlarms'
alarmDetails=response.get("MetricAlarms")
Alarms=[]

for i in range(0,len(alarmDetails), 1):
        Alarms.append(alarmDetails[i]['AlarmName'])    #from the key 'AlarmName' get the values which will be the names of Alarms read into the Alarm[]

print("List of existing Alarms")
print(Alarms)
print("\n")
print("Enter the name of the alarm to be deleted ")
name=input()

if name in  Alarms: 
        cloudwatch.delete_alarms(
                AlarmNames=[name],
        )
	print("Alarm with the name" + " " + name + " " + "deleted")

else:
     	print("Alarm with the Name " + "  " + name+ " " + "is not found")
