import socket
import MergeSort
import Procedure

#HOST = '192.168.1.242'
HOST = '192.168.1.253'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


#Receives arraystring in chunks
arraystring = ''
print 'Receiving data...'
# while 1:
#
#     data = s.recv(4096)	#Receives data in chunks
# #    print data
#     arraystring += data	#Adds data to array string
#     if ']' in data:	 #When end of data is received
#
#         break
# #print arraystring
# array = eval(arraystring)
# print 'Data received, sorting array... '
#
#
# #Sorts the array which it is allocated
# array = MergeSort.mergesort(array)
# print 'Array sorted, sending data...'

strDefFuncEntry, strDefFunc, strDefArg = Procedure.recvFuncParam(s)

# evaluate function
exec(strDefFunc)

print "--------"
print strDefFunc
print "--------"
print strDefArg
print ";;:::::"
arr =  eval(strDefArg)
print arr
arrRes = MergeSort.mergesort(arr)
arr2 = [2, 1, 4, 0]
arrRes2 = MergeSort.mergesort(arr2)
print strDefFuncEntry
print repr(arrRes)
print repr(arrRes2)


# execute
array = eval( strDefFuncEntry + "(" + strDefArg + ")" )
print array
#Converts array into string to be sent back to server
# arraystring = repr(array)
arraystring = array
s.sendall(arraystring)	#Sends array string
print 'Data sent.'

s.close()
