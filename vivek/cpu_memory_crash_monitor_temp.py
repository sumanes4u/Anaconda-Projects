import paramiko
import time
import csv
import sys
import re

class Connect:
    def __init__(self, ipaddress, username, password):
        self.ip = ipaddress
        self.username = username
        self.password = password
        self.prehandle = ''
        self.handle = ''
        
    def ssh(self):
        self.prehandle = paramiko.SSHClient()
        self.prehandle.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.prehandle.connect(self.ip, username = self.username, password = self.password, look_for_keys = False, allow_agent = False)
        self.handle = self.prehandle.invoke_shell()
        self.handle.recv(1000)

    
    def sendcmd(self, cmd):
        cmd += '\n'
        self.handle.send(cmd)
        time.sleep(2)
        output = self.handle.recv(10000)
        return output

    def closessh(self):
        self.prehandle.close()

if len(sys.argv) == 4:
    vcip = sys.argv[1]
    vcusername = sys.argv[2]
    vcpassword = sys.argv[3]
else:
    print("Wrong number or arguments. Usage --> <scriptname> <VCIP> <username> <password>")
    sys.exit()

#vcip = '192.168.74.10'
#vcusername = 'admin'
#vcpassword = 'admin'
iap = Connect(vcip, vcusername, vcpassword)
iap.ssh()
out = iap.sendcmd('show version')
print(out)
out = iap.sendcmd('show aps')
print(out)
aps = re.findall('\d+\.\d+\.\d+\.\d+', str(out))
aptype = re.findall('(\d{3}[A-Z]?)\((?:in|out)door\)', str(out), re.I)
apmac = re.findall('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}',str(out))
aptuples = zip(aptype, apmac)
aptuples = list(aptuples)
apdict = {}
for i in list(range(len(aps))):
    apdict[aps[i]] = aptuples[i]
print('apdic is -->', apdict)

def sendcmd_all(aps, *cmds):
    out = {}
    for ap in aps:
        outlist = []
        apcon = Connect(ap, 'admin', 'arura@123')
        apcon.ssh()
        for cmd in cmds:
            print(cmd)
            outap = str(apcon.sendcmd(cmd))
            #print(out)
            outlist.append(outap)
        out[ap] = outlist
        apcon.prehandle.close()    
    return out
  
def crash_find(aplist, show_version_out):
    for oneap in aplist:
        match = re.search('reboot.*[\n]?.*(reset|kernel|panic|hung|lockup|fatal|exception|core)', show_version_out.lower())
        if match:
            print("****Crash seen in ap ",  oneap, " ", apdict[oneap][0], " ", apdict[oneap][1], "--->", match.group(0))
        elif re.search('cmd at uptime', show_version_out.lower()):
            print("----No crash in ap ", oneap, ' ', apdict[oneap][0], ' ', apdict[oneap][1])
        else:
            print("!!!!AP ", oneap, ' ', apdict[oneap][0], ' ', apdict[oneap][1], " is in unknown state. Please login to the ap and check")

#commandlist = ('show cpu', 'show memory')
out = {}


timestamp = '_'.join('_'.join(time.ctime().split()).split(':'))
#timestamp = '0'

cpufilename = 'cpu_' + vcip + '_'  + timestamp + '.csv'
memoryfilename = 'memory_' + vcip + '_' + timestamp + '.csv'

flag = True
while True:
    out = sendcmd_all(aps, 'show cpu', 'show memory', 'show version')
    crash_find(aps, out[ap][2])
    with open(cpufilename, 'a', newline='') as fp:
        writer = csv.writer(fp)
    
        if flag:
            writer.writerow(['APIP', 'AP Type', 'MAC address', 'user', 'nice', 'system', 'idle', 'io', 'irq', 'softirq'])
        
        for ap in aps:
            cpu = re.findall('\d+\%', out[ap][0])
            cpu.insert(0, ap)
            cpu.insert(1, apdict[ap][0])
            cpu.insert(2, apdict[ap][1])
            writer.writerow(cpu)


    with open(memoryfilename, 'a', newline='') as fp1:
        writer = csv.writer(fp1)
    
        for ap in aps:
            if flag:
                out[ap][1] = re.sub('.{2}:.{2}:.{2}:.{2}:.{2}:.{2}','', out[ap][1])
                memhead = re.findall('[a-zA-Z_\(\)]+:', out[ap][1])
                memhead.insert(0, 'APIP')
                memhead.insert(1, 'AP Type')
                memhead.insert(2, 'MAC address')
                writer.writerow(memhead)
                flag = False
    
            memory = re.findall('\d+\s[a-zA-Z]{2}', out[ap][1])
            memory.insert(0, ap)
            memory.insert(1, apdict[ap][0])
            memory.insert(2, apdict[ap][1])
            writer.writerow(memory)
    waittime = 60
    print("Waiting for ", waittime, " seconds...")
    time.sleep(waittime)
iap.prehandle.close()
