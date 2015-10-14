from AppKit import *

WTViewUpdatedNotification = "WTViewStatsUpdatedNotification"
maxBrushSize = 50.0

class WTView(NSView):
    u"""
    """

    mEventType = None
    mMouseX = None
    mMouseY = None
    mSubX = None
    mSubY = None
    mPressure = None
    mForeColor = None
    mAdjustOpacity = None
    mAdjustSize = None
    mCaptureMouseMoves = None
    mUpdateStatsDuringDrag = None

    def initWithFrame_(cls, frame):
        print 'WTView init with frame'
        self = super(WTView, cls).initWithFrame_(frame)
        print self

        if not self is None:
            # Initialization code here.
            mAdjustOpacity = True
            mAdjustSize = False
            mCaptureMouseMoves = True
            mUpdateStatsDuringDrag = True
        return self

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

    def handleMouseEvent_(self, theEvent):
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
        print 'init PressureWinController'
        self = super(PressureWinController, cls).init()
        print self

        if self is None:
            return None

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(self, "wtvUpdatedStats:", WTViewUpdatedNotification, self.wtvTabletDraw)

        #.addObserver_selector_name_object_(self, "textDidChange:", NSTextStorageDidProcessEditingNotification, view.textStorage())
        #self.nc.addObserver_selector_name_object_(self, selector, WTViewUpdatedNotification, self.wtvTabetDraw)
        #[[NSNotificationCenter defaultCenter] addObserver:self
        #       selector:@selector(wtvUpdatedStats:)
        #       name:WTViewUpdatedNotification
        #       object:wtvTabletDraw];
        return self


    def awakeFromNib(self):
        print 'awake'
        #clrForeColor
        #self.wtvTabletDraw.setForeColor_(color)

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
