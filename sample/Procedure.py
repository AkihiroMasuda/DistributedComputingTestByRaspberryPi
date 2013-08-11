import socket

def sendFuncParam(conn, addr, defFunc, defParam, defFuncEntry):
    # send a function and parameter
    # conn.sendto("<FUNCENTRY>" + defFuncEntry + "</FUNCENTRY>" + "<FUNCTION>" + defFunc + "</FUNCTION>" + "<DATA>" + repr(defParam) + "</DATA>", addr )	#Sends function string
    conn.sendto("<FUNCENTRY>" + defFuncEntry + "</FUNCENTRY>" + "<FUNCTION>" + defFunc + "</FUNCTION>" + "<DATA>" + defParam + "</DATA>", addr )	#Sends function string
    return

# split string by tag1 and tag2, and get content
def getStrBetweenTags(str, tag1, tag2):
    head, body = str.split(tag1)
    content, tail = body.split(tag2)
    return content

def recvFuncParam(soc):
    """

    :rtype : object
    :param socket:
    :return: [strDefFuncEntry, strDefFunc, strDefArg]
    """
    strPacket = ''
    # receive data
    while 1:
        data = soc.recv(4096)	#Receives data in
        strPacket += data	#Adds data to array string
        if strPacket.find("</DATA>") >= 0:
            break

    # parse function
    strDefFuncEntry = getStrBetweenTags(strPacket, "<FUNCENTRY>", "</FUNCENTRY>")

    # parse function
    strDefFunc = getStrBetweenTags(strPacket, "<FUNCTION>", "</FUNCTION>")

    # parse data
    strDefArg = getStrBetweenTags(strPacket, "<DATA>", "</DATA>")

    return [strDefFuncEntry, strDefFunc, strDefArg]
