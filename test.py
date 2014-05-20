#!/usr/bin/python
import sys #Modul um Kommandozeilenparameter auszuwerten
import os
#import zbar
#import subprocess
#for eachArg in sys.argv:
#	print(eachArg)
print "end"
#zbarcam -Sdisable -Sqrcode.enable --raw /dev/video0

#process = subprocess.Popen(["/usr/bin/zbarcam -Sdisable -Sqrcode.enable --raw /dev/video0"], stdout=subprocess.PIPE)
#result = process.communicate()[0]
#print result
#output = subprocess.check_output('/usr/bin/zbarcam -Sdisable -Sqrcode.enable --raw /dev/video0', stderr=subprocess.STDOUT)
#print output
project_folder = '/home/eisflo/QR-TuxLuX/'
p=os.popen('/usr/bin/zbarcam -Sdisable -Sqrcode.enable --nodisplay --raw /dev/video0','r')
code = p.readline()
print 'Got barcode:', code
print 'Yay'
p=os.popen('killall zbarcam','r')
p=os.popen('aplay ' + project_folder + 'JetztGehtsLos.wav','r')
