#!/usr/bin/python

import time
from redis import Redis
from rq import Queue
import web
import json

q = Queue(connection=Redis())
from screenshot_worker import take_save_ss

urls = (
    '/addTask', 'add_task',
    '/status/(.*)', 'get_status',
    '/getSS/(.*)', 'get_ss'
)

app = web.application(urls, globals())

class add_task:
    def POST(self):
        domain = web.input(domain="no domain")
        job = q.enqueue(take_save_ss, domain.domain)
        web.header('Content-Type', 'application/json')
        return json.dumps({"jobId" : job.id})

class get_status:
    def GET(self,id):
        jobStatus = 1
        job = q.fetch_job(id)
        return job.result

class get_ss:
    def GET(self,id):
        try:
            f = open('ss/'+id+".png", 'r')
            web.header('Content-Type', 'image/png')
            return f.read()
        except:
            return "Error probably disk IO" 

if __name__ == "__main__":
    app.run()    
