#!/usr/bin/python

from rq import get_current_job
import subprocess

##will take screenshot and save it
def take_save_ss(url):
    job = get_current_job()
    args = ['/usr/local/bin/wkhtmltoimage',
            url,
            "ss/"+job.id+".png"]
    try:
        child = subprocess.Popen(args, stdout=subprocess.PIPE)
        streamdata = child.communicate()[0]
        rc = child.returncode
        return rc
    except:
        return -1
