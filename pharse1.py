import os
import sched
import time
import argparse

parser = argparse.ArgumentParser(description='Check Edge Image')
parser.add_argument("-c", dest="content", help="content what you want add to file")
args = parser.parse_args()

scheduler = sched.scheduler(time.time, time.sleep)

def insert2file():
    f = open('test1.txt', 'a')
    f.write("\n" + args.content)
    f.close()

def delete2file(content):
    cmd1 = " sed -i 's/%s//' ./test1.txt " % content
    os.system(cmd1)

now = time.time()
insert2file()
print ('START:', now)
scheduler.enterabs(now+30, 1, delete2file, (args.content,))

scheduler.run()


