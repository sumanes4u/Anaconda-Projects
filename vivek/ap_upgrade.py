import time
import sys
import paramiko
import json
import os
import re
import ftplib
import time
import sys
import os
import timeit
import threading
import operator
from operator import itemgetter
from ftplib import FTP
from tkinter import *
#import iap_image_upgrade
'''
if len(sys.argv)<2:
        print ('Usage:ftp.py <IMAGE FTP SRV> <Branch_BuildNO>')
        sys.exit()
else:
        ftp_srv = sys.argv[1]
        build = sys.argv[2]
        print ('Usage is Correct:')
        pass
'''
#for i in sys.argv[1:]:
#       print ('Arguments passed are:',i)

#os.system('ls -l ArubaInstant*'+build+'*')
#os.system('rm -rf ArubaInstant*'+build+'*')
def perform_ftp():
    def threadcall():
            srv = e1.get()
            build = e4.get()
            vcips = e5.get()
            username = e6.get()
            password = e7.get()
            tftp_srv = e8.get()
            first = operator.itemgetter(0)
            build_tmp = build.split('_')
            branch_tmp = first(build_tmp).split('.')
            branch = '.'.join(branch_tmp[0:2])
            print ('Downloading all images from branch:{one}'.format(one=branch))

            print ('BUILD:',build)
            print ('BRANCH',branch)
            ftp = FTP(srv)
            ftp.login()
            if branch == "6.5":
                ftp.retrbinary('RETR ArubaInstant_Pegasus_'+build,open('ArubaInstant_Pegasus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Centaurus_'+build,open('ArubaInstant_Centaurus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Taurus_'+build,open('ArubaInstant_Taurus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Hercules_'+build,open('ArubaInstant_Hercules_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Lupus_'+build,open('ArubaInstant_Lupus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Ursa_'+build,open('ArubaInstant_Ursa_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Vela_'+build,open('ArubaInstant_Vela_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Aries_'+build,open('ArubaInstant_Aries_'+build,'wb').write)
                time.sleep(.200)
                ftp.quit()
            elif branch == "8.3":
                ftp.retrbinary('RETR ArubaInstant_Centaurus_'+build,open('ArubaInstant_Centaurus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Draco_'+build,open('ArubaInstant_Draco_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Hercules_'+build,open('ArubaInstant_Hercules_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Lupus_'+build,open('ArubaInstant_Lupus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Ursa_'+build,open('ArubaInstant_Ursa_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Vela_'+build,open('ArubaInstant_Vela_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Aries_'+build,open('ArubaInstant_Aries_'+build,'wb').write)
                time.sleep(.200)
                ftp.quit()
            elif branch == "8.4":
                print ("Image is 8.4")
                ftp.retrbinary('RETR ArubaInstant_Centaurus_'+build,open('ArubaInstant_Centaurus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Draco_'+build,open('ArubaInstant_Draco_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Hercules_'+build,open('ArubaInstant_Hercules_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Lupus_'+build,open('ArubaInstant_Lupus_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Ursa_'+build,open('ArubaInstant_Ursa_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Vela_'+build,open('ArubaInstant_Vela_'+build,'wb').write)
                time.sleep(.200)
                ftp.retrbinary('RETR ArubaInstant_Aries_'+build,open('ArubaInstant_Aries_'+build,'wb').write)
                time.sleep(.200)
                ftp.quit()     
            else:
                pass

            buildnumber = e4.get()
            print ('buildnumber:',buildnumber)
            build,version = buildnumber.split('_',1)
            print ('build:',build)
            print ('version:',version)
            build = build.split('.')
            build = '.'.join(build[0:2])
            vcips = e5.get().split(',')
            username = e6.get()
            password = e7.get()
            tftp_srv = e8.get()
            print ('Upgrade is going to be performed on VCIP\'s:',vcips,'Using Build:',buildnumber)
            print (buildnumber)
            print(build)
            pass


            if build == '6.5':
                Aries = 'Aries@tftp://'+tftp_srv+'/ArubaInstant_Aries_'+buildnumber
                Centaurus = 'Centaurus@tftp://'+tftp_srv+'/ArubaInstant_Centaurus_'+buildnumber
                Hercules = 'Hercules@tftp://'+tftp_srv+'/ArubaInstant_Hercules_'+buildnumber
                Lupus = 'Lupus@tftp://'+tftp_srv+'/ArubaInstant_Lupus_'+buildnumber
                Pegasus = 'Pegasus@tftp://'+tftp_srv+'/ArubaInstant_Pegasus_'+buildnumber
                Taurus = 'Taurus@tftp://'+tftp_srv+'/ArubaInstant_Taurus_'+buildnumber
                Ursa = 'Ursa@tftp://'+tftp_srv+'/ArubaInstant_Ursa_'+buildnumber
                Vela = 'Vela@tftp://'+tftp_srv+'/ArubaInstant_Vela_'+buildnumber
                imageupgrade = 'upgrade-image2 '+Aries+';'+Centaurus+';'+Hercules+';'+Lupus+';'+Pegasus+';'+Ursa+';'+Vela+';'+Taurus
                print (imageupgrade)       #Prints the upgrade complete command for refference
            elif build == '8.3':
                Aries = 'Aries@tftp://'+tftp_srv+'/ArubaInstant_Aries_'+buildnumber
                Centaurus = 'Centaurus@tftp://'+tftp_srv+'/ArubaInstant_Centaurus_'+buildnumber
                Hercules = 'Hercules@tftp://'+tftp_srv+'/ArubaInstant_Hercules_'+buildnumber
                Lupus = 'Draco@tftp://'+tftp_srv+'/ArubaInstant_Draco_'+buildnumber
                Draco = 'Lupus@tftp://'+tftp_srv+'/ArubaInstant_Lupus_'+buildnumber
                Ursa = 'Ursa@tftp://'+tftp_srv+'/ArubaInstant_Ursa_'+buildnumber
                Vela = 'Vela@tftp://'+tftp_srv+'/ArubaInstant_Vela_'+buildnumber
                imageupgrade = 'upgrade-image2 '+Aries+';'+Centaurus+';'+Hercules+';'+Lupus+';'+Ursa+';'+Vela+';'+Draco
                print (imageupgrade)
            elif build == '8.4':
                Aries = 'Aries@tftp://'+tftp_srv+'/ArubaInstant_Aries_'+buildnumber
                Centaurus = 'Centaurus@tftp://'+tftp_srv+'/ArubaInstant_Centaurus_'+buildnumber
                Hercules = 'Hercules@tftp://'+tftp_srv+'/ArubaInstant_Hercules_'+buildnumber
                Lupus = 'Draco@tftp://'+tftp_srv+'/ArubaInstant_Draco_'+buildnumber
                Draco = 'Lupus@tftp://'+tftp_srv+'/ArubaInstant_Lupus_'+buildnumber
                Ursa = 'Ursa@tftp://'+tftp_srv+'/ArubaInstant_Ursa_'+buildnumber
                Vela = 'Vela@tftp://'+tftp_srv+'/ArubaInstant_Vela_'+buildnumber
                imageupgrade = 'upgrade-image2 '+Aries+';'+Centaurus+';'+Hercules+';'+Lupus+';'+Ursa+';'+Vela+';'+Draco
                print (imageupgrade)           #Prints the upgrade complete command for refference
            else: 
                pass



            class ssh:
                def __init__(self,host,user,passwd):
                    self.host = host
                    self.user = user
                    self.passwd = passwd
                    self.conn = ''
                def connecthost(self):
                    '''SSH Connection to Given Host using Paramiko Module'''
                    print('Connecting to host',self.host)
                    remote_conn_pre = paramiko.SSHClient()
                    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    remote_conn_pre.connect(self.host,username = self.user,password = self.passwd,look_for_keys=False, allow_agent=False)
                    print ('SSH Connection is Established')
                    self.conn = remote_conn_pre.invoke_shell()
                    print('Interactive Shell Established with:%s'%self.host)
                    output = self.conn.recv(1000)
                    print (output)
            #        time.sleep(.500)i
            #        self.conn.send('\n')
            #        self.conn.send('show version\n')
            #        self.conn.send('show aps\n')
            #        time.sleep(5)
            #        output = self.conn.recv(65000)
            #        print(output)
                    return self.conn

                def ispingable(self):
                    '''Checks weather the host is Reachable or Not'''
                    print ('PINGING HOST %s'%self.host)
                    presult = os.popen('ping %s -c 5\r'%self.host).read()
                    ttlfind = re.findall('TTL',presult)
                    print (ttlfind)
                    if len(ttlfind) >= 2:
                        print ('PING SUCCESS!!!!!!!!!')
                        return True
                    else:
                        print ('PING FAILURE!!!!!!!!!')
            #            sys.exit()
                        return False    
               
            handle = {}        
            for srv in vcips:
                srv = srv.strip()
                print ('The Server is %s'%srv)
                handle[srv] = ssh(srv,username,password)
                result = handle[srv].ispingable()
                if result == True:
                    conn = handle[srv].connecthost()
                else:
                    continue
                conn.send('show aps\n')
                time.sleep(3)
                output = conn.recv(65000)
                print (output)
                output = str(output)
                pattern = r'\w+:\w+:\w+:\w+:\w+:\w+'
                macaddrs_before_upgrade = re.findall(pattern,output)
                print (macaddrs_before_upgrade[:len(macaddrs_before_upgrade)-1:])
                match = re.search(r'([\d]+) Access Points',output)
                no_of_aps = int(match.group(1))
                print('IAP\'s in SWARM:',no_of_aps)
                no_of_macs_beforeupgrade = int(len(macaddrs_before_upgrade) - 1)
                print ("The no of APS:{one} and No fo MACs:{two}".format(one= no_of_aps,two=no_of_macs_beforeupgrade))

                if no_of_aps == no_of_macs_beforeupgrade:
            #        conn.send('reload all\n')
                    conn.send(imageupgrade)
            #        conn.send('y\n')
                    conn.send('\n'*2)   
                    print ("No of AP Macs and No of APS are Equal")
                else:
                    break
                    print("The number of APS and MACS are not matching")
                time.sleep(3)
                output1 = conn.recv(65000)
                print(output1)
                output1 = str(output1)
                match = re.search(r'Upgrade is triggered',output1)
            #    match = re.search(r'reloading',output,re.I)
                if match.group():
                    print (output1)
                    print ('Confirming::'+match.group())
                    time.sleep(5)
                    conn.send('show upgrade\n')
                    time.sleep(2)
                    upgrd_status = conn.recv(65500)
                    print(upgrd_status)
                    time.sleep(600)
                else:
                    print ('Some Issue with the Upgrade::')
                    sys.exit()

                handle[srv].ispingable()
                conn = handle[srv].connecthost()
                conn.send('show aps\n')
                time.sleep(3)
                output2 = conn.recv(65000)
                print (output2)
                output2 = str(output2)
                pattern = r'\w+:\w+:\w+:\w+:\w+:\w+'
                macaddrs_after_upgrade = re.findall(pattern,output2)
                print (macaddrs_after_upgrade[:len(macaddrs_after_upgrade)-1:])
                match = re.search(r'([\d]+) Access Points',output2)
                no_of_aps_afterugrade =int(match.group(1))
                print('IAP\'s in SWARM:',no_of_aps_afterugrade)
                no_of_macs_afterugrade = int(len(macaddrs_after_upgrade) - 1)
                print ("The no of APS:{one} and No fo MACs:{two}".format(one= no_of_aps_afterugrade,two=no_of_macs_afterugrade))
                if no_of_macs_beforeupgrade == no_of_macs_afterugrade:
                    print ("No of AP Macs and No of APS are Equal After Upgrade")
                                                                                                            
                else:
                    Lost_Macaddr = [x for x in macaddrs_before_upgrade if x not in macaddrs_after_upgrade]
                    print ("The LOST MAC ADDRESS during Upgrade IS {one}".format(one=Lost_Macaddr))    
                    print("The number of APS and MACS are not matching")    
                    break 
                conn.send('show version\n')
                time.sleep(3)
                output3 = conn.recv(65500)
                print(output3)
                output3 = str(output3)
                match_ver = re.search(version,output3)
                version_after_upgrade = match_ver.group()
                print("IMAGE VERSION AFTER UPGRADE: "+version_after_upgrade)
                if version_after_upgrade == version:
                    print ('Upgrade Sucessfull!!!!!!!!!as upgraded to :{one}'.format(one=version_after_upgrade))
                else:
                    print ('Upgrade Failure!!!!!!!!!!!!as upgraded to :{one}'.format(one=version_after_upgrade))
                    
        #    print ("HIIIIII: "+ build + " " + vcips + " " + username + " " + password)    
        #    os.popen("python iap_image_upgrade_withcheck.py build vcips username password tftp_srv")        
    def threadcall1():
            srv = e1.get()
            build = e4.get()
            vcips = e5.get()
            username = e6.get()
            password = e7.get()
            tftp_srv = e8.get()
            print ('11111111')
            print (build)
            os.popen("python iap_image_upgrade_withcheck.py build vcips username password tftp_srv")
            print ('2222222')

            #os.popen("python iap_image_upgrade_withcheck.py $buildnumber $vcips $username $password")
    t = threading.Thread(target=threadcall)
    t.start()
    

master = Tk()
Label(master, text="FTP_SRV address").grid(row=0)
Label(master, text="FTP username").grid(row=1)
Label(master, text="FTP password").grid(row=2)
Label(master, text="Build Number").grid(row=3)
Label(master, text="VC IP").grid(row=4)
Label(master, text="VC username").grid(row=5)
Label(master, text="VC password").grid(row=6)
Label(master, text="TFTP SRV IP").grid(row=7)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)


#Button(master, text='Quit', command=quit).grid(row=3, column=0, sticky=W, pady=4)
try:
#        prf_ftp = lambda x,y:perform_ftp(x,y)
#        prf_ftp(ftp_srv,build)
    Button(master, text='Submit', command=perform_ftp).grid(row=8, column=1, sticky=W, pady=4)
    
except Exception as e:
        print ('Exception Occured',e,sys.exc_info()[0])
        exit()
finally:
    print ('FTP DOWNLOADING JOB INITIATED!!!!!!!')

mainloop()
