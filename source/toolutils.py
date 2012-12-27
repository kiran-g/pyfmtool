#!/usr/bin/env python
"""
    Tools utility definitions
"""

"""
    Function Definitions Start
"""

from string import *
from shutil import *
commandlist=['trimlines','trimlinesleadin','trimlinestrailing']


def containsotherthan(str, set):
    """Check whether 'str' contains ANY of the chars in 'set'"""
    for c in str:
        if c not in set:
            return  True
    return   False  

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
   

def trimfile(f,type):
    linelist=f.readlines()
    processedlist=[]
    for line in linelist:
        if (type=='both') or (type=='l'):
            line=lstrip(line,'\n\r\t ')
        if (type=='both') or (type=='r'):
            line=rstrip(line,'\n\r\t ')
        if (type !='both') and (type!='r') and  (type!='l'):
            print "Illegeal option"
            return None
        if line != '' and line != '\n':
            #print "|"+line+"|"
            if containsotherthan(line,'\n\r\t '):
                processedlist.append(line)
    return '\n'.join(processedlist)    