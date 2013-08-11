import socket
# import MergeSort
import Procedure

#HOST = '192.168.1.242'
HOST = '192.168.1.253'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Receives arraystring in chunks
arraystring = ''
print 'Receiving data...'

strDefFuncEntry, strDefFunc, strDefArg = Procedure.recvFuncParam(s)

# evaluate function
exec(strDefFunc)

# for debug
# print "--------"
# print strDefFunc
# print "--------"
# print strDefArg
# print strDefFuncEntry

# execute
array = eval( strDefFuncEntry + "(" + strDefArg + ")" )

#Converts array into string to be sent back to server
arraystring = repr(array)

s.sendall(arraystring)	#Sends array string
print 'Data sent.'

s.close()
