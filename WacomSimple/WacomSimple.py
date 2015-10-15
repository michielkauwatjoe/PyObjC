from AppKit import *

WTViewUpdatedNotification = "WTViewStatsUpdatedNotification"
maxBrushSize = 50.0

class WTView(NSView):
    u"""
    """

    mEventType = objc.ivar.int()
    mMouseX = objc.ivar.float()
    mMouseY = objc.ivar.float()
    mSubX = objc.ivar.float()
    mSubY = objc.ivar.float()
    mPressure = objc.ivar.float()
    mForeColor = objc.ivar()
    mAdjustOpacity = objc.ivar.bool()
    mAdjustSize = objc.ivar.bool()
    mCaptureMouseMoves = objc.ivar.bool()
    mUpdateStatsDuringDrag = objc.ivar.bool()

    def initWithFrame_(cls, frame):
        self = super(WTView, cls).initWithFrame_(frame)
        print self, 'init with frame'

        if not self is None:
            # Initialization code here.
            mAdjustOpacity = True
            mAdjustSize = False
            mCaptureMouseMoves = True
            mUpdateStatsDuringDrag = True

        return self

    def mouseMoved_(self, theEvent):
        self.handleMouseEvent_(theEvent)

    def mouseUp_(self, theEvent):
        self.handleMouseEvent_(theEvent)

    def handleMouseEvent_(self, theEvent):
        self.mEventType = theEvent.type()
        loc = theEvent.locationInWindow()
        self.mMouseX = loc.x
        self.mMouseY = loc.y
        self.mSubX = 0.0
        self.mSubY = 0.0

        if not self.mEventType == NSMouseMoved:
            self.mPressure = theEvent.pressure()
        else:
            self.mPressure = 0.0

        NSNotificationCenter.defaultCenter().postNotificationName_object_(WTViewUpdatedNotification, self)

    def setForeColor_(self, newColor):
        pass

    def setAdjustOpacity_(self, adjust):
        pass

    def setAdjustSize_(self, adjust):
        pass

    def setCaptureMouseMove_(self, value):
        pass

    def setUpdateStatsDuringDrag_(self, value):
        pass

    def drawCurrentDataFromEvent_(self, theEvent):
        pass

    def acceptsFirstResponder(self):
        return True

    def drawRect_(self, rect):
        pass

class PressureWinController(NSObject):
    u"""
    """

    txtEventType = objc.IBOutlet()
    txtMouseX = objc.IBOutlet()
    txtMouseY = objc.IBOutlet()
    txtPressure = objc.IBOutlet()
    clrForeColor = objc.IBOutlet()
    wtvTabletDraw = objc.IBOutlet()
    mnuLineSize = objc.IBOutlet()
    mnuOpacity = objc.IBOutlet()
    mnuCaptureMouseMoves = objc.IBOutlet()
    mnuUpdateStatsDuringDrag = objc.IBOutlet()

    def init(cls):
        u"""
        """
        self = super(PressureWinController, cls).init()
        print self, 'init PressureWinController'

        if self is None:
            return None

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(self, "wtvUpdatedStats:", WTViewUpdatedNotification, self.wtvTabletDraw)
        return self


    def awakeFromNib(self):
        print 'awakeFromNib'
        self.wtvTabletDraw.setForeColor_(NSColor.orangeColor())

        # Set check marks of Pressure Menu Items.
        if(self.wtvTabletDraw.mAdjustOpacity is True):
           self.mnuOpacity.setState_(NSOnStates)
        else:
           self.mnuOpacity.setState_(NSOffState)

        if(self.wtvTabletDraw.mAdjustSize is True):
           self.mnuOpacity.setState_(NSOnState)
        else:
            self.mnuLineSize.setState_(NSOffState)
        # Set check marks for Events menu
        if(self.wtvTabletDraw.mCaptureMouseMoves is True):
           self.mnuCaptureMouseMoves.setState_(NSOnState)
        else:
           self.mnuCaptureMouseMoves.setState_(NSOffState)

        if(self.wtvTabletDraw.mUpdateStatsDuringDrag is True):
           self.mnuUpdateStatsDuringDrag.setState_(NSOnState)
        else:
           self.mnuUpdateStatsDuringDrag.setState_(NSOffState)

    @objc.IBAction
    def opacityMenuAction_(self, sender):
        pass

    @objc.IBAction
    def lineSizeMenuAction_(self, sender):
        pass

    @objc.IBAction
    def captureMouseMovesAction_(self, sender):
        pass

    @objc.IBAction
    def updateStatsDuringDragAction_(self, sender):
        pass

    @objc.IBAction
    def openColorPanel_(self, sender):
        pass

    def changeColor_(self, sender):
        pass

    def wtvUpdatedStats_(self, theNotification):
        pass
