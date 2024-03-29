#!/usr/bin/env python
"""
    Multipurpose file manipulation tool
"""
import sys
import toolfunctions
import os

"""
    main
"""

usage=getattr(toolfunctions,'usage')
totalargcount=len(sys.argv)
if totalargcount<3:
    print "Unsufficient Arguments"
    usage(sys.argv[0])
    sys.exit(1)
#toolutils.usage(sys.argv[0])
    
if sys.argv[1] not in toolfunctions.commandlist:
    print "Unknown Command"
    usage(sys.argv[0])
    sys.exit(1)    
command=sys.argv[1]
filename=sys.argv[2]
if totalargcount>3:
    extraargs=sys.argv[3:]
    #print extraargs   
else:
    extraargs=[]

if not os.path.exists(filename):
    print "File does not exist"
    usage(sys.argv[0])
    sys.exit(1)     
        



try:
    getattr(toolfunctions,command)(filename,extraargs)
except Exception,e:
    print "Error:"+str(e)
    usage(sys.argv[0])
    sys.exit(1)   

