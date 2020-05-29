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
    fin = open("test1.txt", "rt")
#read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace(content, '')
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("test1.txt", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()

now = time.time()
insert2file()
print ('START:', now)
scheduler.enterabs(now+30, 1, delete2file, (args.content,))

scheduler.run()


# a= "announce flow route {match { destination 8.8.8.8/32; source 101.96.88.0/24; destination-port =53; protocol udp; } then { discard;}}"
# print (a[80])



