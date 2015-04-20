
#
class SRSRequestState(SRSObject):    
    __requestOwner = 0
    assert(type(__requestOwner)==object)
    __reason = 0
    assert(type(__reason)==str)
    __requestState = 0
    assert(type(__requestState)==SRSRequest)


    def publicrun (self):        
        # implementation
    #Answer a Report object
    def publicreport (self):        
        # implementation
    def publicstatusUserText (self):        
        # implementation
    def publicfinalize (self):        
        # implementation
    #
    def publicreason (self, reasonString):        
        # implementation
    def publiccancel (self):        
        # implementation
    def publicpreviousState (self):        
        # implementation
    def publicnextState (self):        
        # implementation

