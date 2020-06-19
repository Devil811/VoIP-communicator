import sys
import pjsua as pj
import argparse
import RPi.GPIO as GPIO

BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN)

class ParseArgumennts():
    def parse(self,args=sys.argv[1:]):
        parser= argparse.ArgumentParser()


        parser.add_argument("--id")
        parser.add_argument("--registrar")
        parser.add_argument("--realm")
        parser.add_argument("--username")
        parser.add_argument("--password")
        parser.add_argument("--contact")
        parser.add_argument("--outbound")
        parser.add_argument("--thread-cnt")
        parser.add_argument("--nameserver", action="append")
        parser.add_argument("--publish", action="store_true")
        parser.add_argument("--clock-rate")
        parser.add_argument("--add-codec")
        parser.add_argument("--dis-codec", action="append")
        parser.add_argument("--clienta")
        parser.add_argument("--clientb")
        options = parser.parse_args(args)
        return options


LOG_LEVEL=3
current_call = None

# Logging callback
def log_cb(level, str, len):
    print str,


# Callback to receive events from account
class MyAccountCallback(pj.AccountCallback):

    def __init__(self, account=None):
        pj.AccountCallback.__init__(self, account)

    # Notification on incoming call
    def on_incoming_call(self, call):
        global current_call 
        if current_call:
            call.answer(486, "Busy")
            return
            
        print "Incoming call from ", call.info().remote_uri
        print "Press 'a' to answer"

        client1=args.clienta
        client2=args.clientb
        if call.info().remote_uri == client1:
            current_call = call
            call_cb = MyCallCallback(current_call)
            current_call.set_callback(call_cb)
            current_call.answer(100)
        else call.info().remote_uri == client2:
            current_call = call
            call_cb = MyCallCallback(current_call)
            current_call.set_callback(call_cb)
            current_call.answer(100)

        
# Callback to receive events from Call
class MyCallCallback(pj.CallCallback):

    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    # Notification when call state has changed
    def on_state(self):
        global current_call
        print "Call with", self.call.info().remote_uri,
        print "is", self.call.info().state_text,
        print "last code =", self.call.info().last_code, 
        print "(" + self.call.info().last_reason + ")"
        
        if self.call.info().state == pj.CallState.DISCONNECTED:
            current_call = None
            print 'Current call is', current_call

    # Notification when call's media state has changed.
    def on_media_state(self):
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            # Connect the call to sound device
            call_slot = self.call.info().conf_slot
            pj.Lib.instance().conf_connect(call_slot, 0)
            pj.Lib.instance().conf_connect(0, call_slot)
            print "Media is now active"
        else:
            print "Media is inactive"

    def on_dtmf_digit(self,digits):
        print(digits)

# Function to make call
def make_call(uri):
    try:
        print "Making call to", uri
        return acc.make_call(uri, cb=MyCallCallback())
    except pj.Error, e:
        print "Exception: " + str(e)
        return None


parser = ParseArgumennts()
args = parser.parse()
# Create library instance
lib = pj.Lib()

try:
    # Init library with default config and some customized
    # logging config.
    lib.init(log_cfg = pj.LogConfig(level=LOG_LEVEL, callback=log_cb))

    # Create UDP transport which listens to any available port
    transport = lib.create_transport(pj.TransportType.UDP, 
                                     pj.TransportConfig(0))
    print "\nListening on", transport.info().host, 
    print "port", transport.info().port, "\n"
    
    # Start the library
    lib.start()

    # Create local account
    #acc = lib.create_account_for_transport(transport, cb=MyAccountCallback())
    acc = lib.create_account(pj.AccountConfig(username=args.username, password=args.password, domain=args.realm, proxy=args.outbound))

    # If argument is specified then make call to the URI
    if len(sys.argv) > 1:
        lck = lib.auto_lock()
        current_call = make_call(sys.argv[1])
        print 'Current call is', current_call
        del lck

    my_sip_uri = "sip:" + transport.info().host + \
                 ":" + str(transport.info().port)

    # Menu loop
    while True:
        print "My SIP URI is", my_sip_uri
        input = GPIO.input(BUTTON)
#        input = sys.stdin.readline().rstrip("\r\n")
        if input :

            lck = lib.auto_lock()
            current_call = make_call(address = args.client)
            del lck


    # Shutdown the library
    transport = None
    acc.delete()
    acc = None
    lib.destroy()
    lib = None

except pj.Error, e:
    print "Exception: " + str(e)
    lib.destroy()
    lib = None

