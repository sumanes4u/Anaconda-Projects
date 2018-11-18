from tkinter import *
import webbrowser
import threading
import paramiko
import time
import csv
import sys
import re
import os

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
        output = self.handle.recv(100000000)
        print("output is ", output)
        #print("type of output is ", type(output))
        output = output.decode('utf-8')
        #print("output decode is ", output)
        #print("type of output decode is ", type(output))
        return output

    def closessh(self):
        self.prehandle.close()

def sendcmd_all(aps, cmds):
    out = {}
    for ap in aps:
        global roww
        global ssidfilename
        roww = 7
        outlist = []
        apcon = Connect(ap, iapuser, iappaswd)
        try:
            apcon.ssh()
        except:
            print("Could not connect to " + ap + ". Please check the connectivity for this AP!!")
            out[ap] = ["AP " + ap + " is unreachable"] * len(cmds)
        else:
            for cmd in cmds:
                print(cmd)
                newrow = incr_row()
                sendmsg(message = "                                                                          " , row  = newrow, column = 1, columnspan = 3, sticky = 'W')
                sendmsg(message = "Sending command " + cmd + " to AP " + ap , row  = newrow, column = 1, columnspan = 3, sticky = 'W')
                outap = str(apcon.sendcmd(cmd))
            
                #print("outap is ", outap)
                #print("type of outap is ", type(outap))
                #with open(ssidfilename, 'a') as fp:
                #    fp.write(outap)
                #print(out)
                outlist.append(outap)
            out[ap] = outlist
            apcon.prehandle.close()    
    return out

def sendmsg(**geometry):
    if geometry['message']:
        msg = geometry['message']
    if geometry['row']:
        r = geometry['row']
    if geometry['column']:
        c = geometry['column']
    if geometry['columnspan']:
        cs = geometry['columnspan']
    if geometry['sticky']:
        s = geometry['sticky']

    Label(master, text=msg).grid(row=r, column=c, columnspan=cs, sticky=s)
    master.update()

#def quit():
#    def threadcall():
#        sys.exit()
#    t = threading.Thread(target=threadcall)
#    t.start()

def incr_row():
    global roww
    roww = roww + 1
    return roww

roww = 4
timestamp = '_'.join('_'.join(time.ctime().split()).split(':'))
        #timestamp = '0'
        
ssidfilename = 'SSID_' + timestamp + '.txt'
def exec_program():
    def threadcall():  
        sendmsg(message = "Starting...", row  = incr_row(), column = 1, columnspan = 3, sticky = 'W')
        global iapuser
        global iappaswd
        global ssidfilename
        iapip = e1.get()
        iapuser = e2.get()
        iappaswd = e3.get()
        commands = e4.get()
#        waittime = int(e4.get())

        sendmsg(message = "Connecting to " + iapip + "...", row  = incr_row(), column = 1, columnspan = 3, sticky = 'W')
        
        iap = Connect(iapip, iapuser, iappaswd)
        try:
            iap.ssh()
        except:
            print("Could not connect to " + iapip + ". Please check the connectivity and try again!!")
        else:
            out = iap.sendcmd('show version')
            print(out)
            out = iap.sendcmd('show aps')
            print(out)
            aps = re.findall('\d+\.\d+\.\d+\.\d+', str(out)) 
        
            #aps = [] #apip
            apname = []
            aptype = []
            apuptime = []
            for line in out.split('\n'):
                print("LINE is ", line)
                if re.compile(r'\d+\.\d+\.\d+\.\d+').search(line):    #check if the line contains mac address
                    linesplit = line.split()
                    print("linesplit is ", linesplit)
                    apname.append(linesplit[0])
                    #aps.append(re.compile('\d+\.\d+\.\d+\.\d+').search(linesplit[1]).group())
                    aptype.append(linesplit[5])
                    apuptime.append(re.compile('(\d+d:)?(\d+h:)?(\d+m:)?\d+s').search(line).group())
            apzip = zip(aps, apname, aptype, apuptime)
            apzipdict = {}
            for item in apzip:
                apzipdict[item[0]] = item
            print ("apzipdict is ", apzipdict)
            #commandlist = ('show cpu', 'show memory')
            out = {}
        
                
            flag = True
            num_iter = 0
        
            global roww
            roww = 6 
            num_iter += 1
            sendmsg(message = "Iteration number " + str(num_iter), row  = incr_row(), column = 1, columnspan = 3, sticky = 'W')
            commandlist = [x.strip() for x in commands.split(',')]
            out = sendcmd_all(aps, commandlist)
            print(out)

            with open(ssidfilename, 'a') as fp:
                apcount = 0
                for ap in aps:
                    commandlen = 0
                    apcount = apcount + 1
                    fp.write("\n***************************" + "AP" + str(apcount) + "********************************\n")
                    fp.write("   ".join(item for item in apzipdict[ap]) + "\n")
                    while commandlen < len(commandlist):
                        fp.write(re.sub('\n.*?#', "", ">>>" + out[ap][commandlen]) + "\n\n")
                        commandlen = commandlen + 1

              
#           waittime = e4.get()
            #sendmsg(message = "SSID report created at " + os.getcwd() + '\\' + ssidfilename, row  = incr_row(), column = 1, columnspan = 3, sticky = 'W')
            filepath = os.getcwd() + '\\' + ssidfilename
            message = "SSID report created at " + filepath
            link = Label(master, text=message, fg="blue", cursor="hand2")
            link.grid(row  = incr_row(), column = 1, columnspan = 3, sticky = 'W')
            def openreportfile(event):
                webbrowser.open_new(filepath)
                #webbrowser.open_new("file:\\" + filepath)
            link.bind("<Button-1>", openreportfile)
            iap.prehandle.close()
    
    t = threading.Thread(target=threadcall)
    t.start()
###########UI part############

master = Tk()
Label(master, text="IAP ip address").grid(row=0)
Label(master, text="IAP username").grid(row=1)
Label(master, text="IAP password").grid(row=2)
Label(master, text="Commands(comma separated)").grid(row=3)
Label(master, text="Logs:").grid(row=5, sticky=W)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


#Button(master, text='Quit', command=quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=exec_program).grid(row=4, column=1, sticky=W, pady=4)

mainloop()

#########UI part end###############