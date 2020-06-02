import os
import sched
import time
import argparse

parser = argparse.ArgumentParser(description='custom exabgp')
parser.add_argument("-d", dest="dest", help="destination packet")
parser.add_argument("-s", dest="source", help="source packet")
parser.add_argument("-dp", dest="dest_port", help="destination port")
parser.add_argument("-p", dest="protocols", help="protocols")
args = parser.parse_args()

scheduler = sched.scheduler(time.time, time.sleep)

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
# insert2file()

cmd = '''echo "announce flow route {match { destination %s; source %s; destination-port =%s; protocol %s; } then { discard;}}" >> ./test1.txt''' % (args.dest,args.source,args.dest_port,args.protocols)
cmd_withdraw = '''echo "withdraw flow route {match { destination %s; source %s; destination-port =%s; protocol %s; } then { discard;}}" >> ./test1.txt''' % (args.dest,args.source,args.dest_port,args.protocols)
os.system(cmd) 
# os.system(cmd_withdraw)
print ('START:', now)
scheduler.enterabs(now+30, 1, os.system, (cmd_withdraw,))

scheduler.run()




