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

    def awakeFromNib(self):
        u"""
        Must inform the window that we want mouse moves after all object are
        created and linked.

        Let our internal routine make the API call so that everything stays in
        synch. Change the calue in the init routine to change the default
        behavior.
        """
        self.setCaptureMouseMoves_(self.mCaptureMouseMoves)

    def mouseDown_(self, theEvent):
        self.handleMouseEvent_(theEvent)

        # Save the loc the mouse down occurred at. This will be used by the
        # Drawing code during a Drag event to follow.
        self.mLastLoc = self.convertPoint_fromView_(theEvent.locationInWindow(), None)

    def mouseDragged_(self, theEvent):
        u"""
        Updating the text display of the stats can take up a lot of time.  This
        can lead to less smooth curves being drawn. Toggle the Update Stats
        During Drag menu option to see the difference.
        """
        keepOn = True

        if (self.mUpdateStatsDuringDrag):
            self.drawCurrentDataFromEvent_(theEvent)
            self.handleMouseEvent_(theEvent)
        else:
            while(keepOn):
                theEvent = self.window().nextEventMatchingMask_(NSLeftMouseUpMask | NSLeftMouseDraggedMask)

                t = theEvent.type()
                if t == NSLeftMouseDragged:
                    self.drawCurrentDataFromEvent_(theEvent)
                    break
                elif t == NSLeftMouseUp:
                    keepOn = False
                    break
                else:
                    break

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

    def setCaptureMouseMoves_(self, value):
        self.mCaptureMouseMoves = value
        self.window().setAcceptsMouseMovedEvents_(self.mCaptureMouseMoves)

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
