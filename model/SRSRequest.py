
class SRSRequest(SRSObject):    
    __requestState = 0
    assert(type(__requestState)==object)
    __requestName = 0
    assert(type(__requestName)==object)
    __requestOwner = 0
    assert(type(__requestOwner)==object)
    __requestReport = 0
    assert(type(__requestReport)==object)
    __sampleRequest = 0
    assert(type(__sampleRequest)==SRSRequestSample)
    __requestOwner = 0
    assert(type(__requestOwner)==SRSRequestState)
    publicrequests = 0
    assert(type(publicrequests)==SRSApplication)


    def publicrenameRequest (self):        
        # implementation
    def publicrequestOwner (self):        
        # implementation
    def publiccancelRequest (self):        
        # implementation
    def publicexecuteRequest (self):        
        # implementation
    def publicfinalizeRequest (self):        
        # implementation
    def publiccancelRequest (self):        
        # implementation
    def publicpauseRequest (self):        
        # implementation
    def publicreport (self):        
        # implementation
    def publicsamples (self):        
        # implementation
    def publicisReported (self):        
        # implementation
    def publicisFinished (self):        
        # implementation
    def publicisCanceled (self):        
        # implementation
    def publicisInvalid (self):        
        # implementation
    def publicisRunning (self):        
        # implementation
    def publicisPaid (self):        
        # implementation
    def publicvalidStates (self):        
        # implementation

