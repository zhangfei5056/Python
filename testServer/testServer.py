__author__ = 'caoyuan'
import bottle
@bottle.get("/")
def getfuc():
    print "nice----------------"
    return "hello world ddd."

@bottle.post("/")
def postFunc():
    print "-----here post come-----"
    # data = bottle.request._get_body_string()#this is get body's string
    data = bottle.request.body.readlines()#this is return a list, which set some string in it
    print data
    return data
bottle.run(host="127.0.0.1",port=8089,reloader=True,debug=True)