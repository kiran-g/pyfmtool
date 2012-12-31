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
commandlist=['trimlines','trimlinesleading','trimlinestrailing','win2unix','unix2win','rememptylines','replacestring','remnthline','remlinerange','remnlinesfrom','translate']


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



def win2unix(filename,arglist):
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



def unix2win(filename,arglist):
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

    processestext='\n'.join(linelist_stringreplaced)
    
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


def remnthline(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    if len(arglist)<1:
        print "Subcommand error. Please specify the line number to remove"
        return None
    try:
        linenum= int(arglist[0])
    except:
        print "Error: Expected number"
        return None

        
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_lineremoved=[]
    linecount=0
    for line in linelist:
        linecount=linecount+1
        if(linecount != linenum):
            linelist_lineremoved.append(rstrip(line,'\n\r'))

    processestext='\n'.join(linelist_lineremoved)
    
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




def remlinerange(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    if len(arglist)<2:
        print "Subcommand error. Please specify the start line number and   stop line number  of line range to remove"
        return None
    try:
        linenum_start= int(arglist[0])
        linenum_end= int(arglist[1])
    except:
        print "Error: Expected number"
        return None
    if (linenum_start >  linenum_end):  
        print "start line number should be less than stop line number"
        return None        
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_linerangeremoved=[]
    linecount=0
    for line in linelist:
        linecount=linecount+1
        if ((linecount < linenum_start) or (linecount > linenum_end)) :
            linelist_linerangeremoved.append(rstrip(line,'\n\r'))

    processestext='\n'.join(linelist_linerangeremoved)
    
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
#','remnlinesfrom


def remnlinesfrom(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    if len(arglist)<2:
        print "Subcommand error. Please specify the start line number and   stop line number  of line range to remove"
        return None
    try:
        linenum_start= int(arglist[0])
        numliestoremove= int(arglist[1])
    except:
        print "line number argument is not an number"
        return None
    if (numliestoremove<=0):  
        print "Error: Expected number"
        return None        
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_linerangeremoved=[]
    linecount=0
    for line in linelist:
        linecount=linecount+1
        if ((linecount < linenum_start) or (linecount > linenum_start+numliestoremove-1)) :
            linelist_linerangeremoved.append(rstrip(line,'\n\r'))

    processestext='\n'.join(linelist_linerangeremoved)
    
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



def translate(filename,arglist):
    #print "trimlines function with args"+str(arglist)
    if len(arglist)<1:
        print "Subcommand error. Please specify the string to be truncated"
        return None
    trun_string=arglist[0].strip("\n")

    
    try:
        f=open(filename,'r+w')
    except IOError as e:
        print 'Unable to open file'
        return None
    linelist=f.readlines()
    linelist_linetruncated=[]
    linecount=0
    for line in linelist:
        if trun_string in line:    
            linelist_linetruncated.append(tr(trun_string,line.strip('\n')))
        else:
            linelist_linetruncated.append(line.strip('\n'))
    processestext='\n'.join(linelist_linetruncated)
    
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
