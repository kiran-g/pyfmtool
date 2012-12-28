#!/usr/bin/env python
"""
    Tools utility definitions
"""

"""
    Function Definitions Start
"""

from string import *
from shutil import *
from toolutils import *
commandlist=['trimlines','trimlinesleading','trimlinestrailing','win2dos','dos2win']


def usage(execname):
    print "Usage:"
    print "\t\t"+execname+" command filename [subcommands . . ]"
    print "\t\t"+"commands are: \n"+'\n'.join(['\t\t\t"'+i+'"' for i in commandlist ])

def trimlines(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    processestext=trimfile(f,'both')
    origfilename=f.name
    f.close()
    try:
        tmpf=open("/tmp/file.txt","w")
    except:
        print "Unable to open temp file for writing"
        return None
    
    print "|\n"+processestext+"\n|"
    if processestext:
        try:
            tmpf.write(processestext)
        except Exception,e:
            print "Write Error:"+str(e)    
            return None
        move(tmpf.name,origfilename)
        tmpf.close()
        return 1 
    else:
        return None
   

def trimlinesleading(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    processestext=trimfile(f,'l')
    origfilename=f.name
    f.close()
    try:
        tmpf=open("/tmp/file.txt","w")
    except:
        print "Unable to open temp file for writing"
        return None
    
    print "|\n"+processestext+"\n|"
    if processestext:
        try:
            tmpf.write(processestext)
        except Exception,e:
            print "Write Error:"+str(e)    
            return None
        move(tmpf.name,origfilename)
        tmpf.close()
        return 1 
    else:
        return None



def trimlinestrailing(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    processestext=trimfile(f,'r')
    origfilename=f.name
    f.close()
    try:
        tmpf=open("/tmp/file.txt","w")
    except:
        print "Unable to open temp file for writing"
        return None
    
    print "|\n"+processestext+"\n|"
    if processestext:
        try:
            tmpf.write(processestext)
        except Exception,e:
            print "Write Error:"+str(e)    
            return None
        move(tmpf.name,origfilename)
        tmpf.close()
        return 1 
    else:
        return None



def win2dos(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_lineendingsremoved=[]
    for line in linelist:
        linelist_lineendingsremoved=rtrsip(line,'\n\t')                
    
    
    origfilename=f.name
    f.close()
    try:
        tmpf=open("/tmp/file.txt","w")
    except:
        print "Unable to open temp file for writing"
        return None
    
    print "|\n"+processestext+"\n|"
    if processestext:
        try:
            tmpf.write(processestext)
        except Exception,e:
            print "Write Error:"+str(e)    
            return None
        move(tmpf.name,origfilename)
        tmpf.close()
        return 1 
    else:
        return None
