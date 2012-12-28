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
commandlist=['trimlines','trimlinesleading','trimlinestrailing','win2dos','dos2win','rememptylines','replacestring']


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
        linelist_lineendingsremoved.append(rstrip(line,'\n\r'))                

    processestext='\n'.join(linelist_lineendingsremoved)
    
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



def dos2win(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_lineendingsremoved=[]
    for line in linelist:
        linelist_lineendingsremoved.append(rstrip(line,'\n\r'))

    processestext='\r\n'.join(linelist_lineendingsremoved)
    
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


def rememptylines(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_rememptylines=[]
    for line in linelist:
        strippedline=strip(line,'\n\r\t ')
        if strippedline:
            linelist_rememptylines.append(strippedline)

    processestext='\n'.join(linelist_rememptylines)
    
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
    
    


def replacestring(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    if len(arglist)<2:
        print "Subcommand error. Please specify original string and replacement string"
        return None
    origstring=   str(arglist[0])
    replstring=   str(arglist[1])
        
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_stringreplaced=[]
    for line in linelist:
        linelist_stringreplaced.append(rstrip(line,'\n\r').replace(origstring,replstring))

    processestext='\r\n'.join(linelist_stringreplaced)
    
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
