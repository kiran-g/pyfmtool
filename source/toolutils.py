from string import *

def containsotherthan(str, set):
    """Check whether 'str' contains ANY of the chars in 'set'"""
    for c in str:
        if c not in set:
            return  True
    return   False  



def trimfile(f,type):
    linelist=f.readlines()
    processedlist=[]
    for line in linelist:
        if (type=='both') or (type=='l'):
            line=lstrip(line,'\n\r\t ')
            line=rstrip(line,'\n')  #Removing newline for now. Will be added during file write
        if (type=='both') or (type=='r'):
            line=rstrip(line,'\n\r\t ')
        if (type !='both') and (type!='r') and  (type!='l'):
            print "Illegeal option"
            return None
        if line != '' and line != '\n':
            #print "|"+line+"|"
            if containsotherthan(line,'\n\r\t '):
                processedlist.append(line)
        print "trimfile <<"+line+">>"        
    return '\n'.join(processedlist)    

    

def tr(trstr,strng):
    if len(trstr)>len(strng):
        return strng
    if not trstr in strng:
        return strng
    if count(strng,trstr) == 1:
        return strng
    while count(strng,trstr) > 1:
        oldstr=strng
        strng=strng.replace(trstr+trstr,trstr)
        if strng==oldstr:
            break
    return    strng 