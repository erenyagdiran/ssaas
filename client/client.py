#!/usr/bin/python

import time
import requests

url = "http://188.166.81.55:8081"

def addTask(domain):
  task = requests.post(url+"/addTask",data = {"domain":domain})
  return task.json()['jobId']

def getStatus(jobId):
  job = requests.get(url+"/status/"+jobId)
  return job.content

def getScreenShot(jobId):
  return "SS can be seen at " + (url+"/getSS/"+jobId)

jobid = addTask("http://www.google.se")

content = getStatus(jobid)
print "Polling Starts"
while content == "None":
  print "Job in progress"
  time.sleep(1)
  content = getStatus(jobid)
print "Polling ends"

if content.isdigit() == True and int(content) == 0:
  print "Success !"
  print getScreenShot(jobid)
else:
  print "Problem with something internal"
 
