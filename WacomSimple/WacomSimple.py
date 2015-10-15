from AppKit import *

WTViewUpdatedNotification = "WTViewStatsUpdatedNotification"
maxBrushSize = 50.0

class WTView(NSView):
    u"""
    View class for Wacom Simple example.
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

        if not self is None:
            # Initialization code here.
            self.mAdjustOpacity = True
            self.mAdjustSize = False
            self.mCaptureMouseMoves = True
            self.mUpdateStatsDuringDrag = True
            self.mForeColor = NSColor.orangeColor()

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

        if self.mUpdateStatsDuringDrag is True:
            self.drawCurrentDataFromEvent_(theEvent)
            self.handleMouseEvent_(theEvent)
        else:
            while keepOn:
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
        u"""
        All of the Mouse Events are funneled through this function so that we
        do not have to duplicate this code. If you do something like this,
        you must be careful because certain fields are only valid for particular
        events. For example, [NSEvent pressure] is not valid for Mouse Moves!
        """
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
        self.mForeColor = newColor

    def setAdjustOpacity_(self, adjust):
        self.mAdjustOpacity = adjust

    def setAdjustSize_(self, adjust):
        self.mAdjustSize = adjust

    def setCaptureMouseMoves_(self, value):
        self.mCaptureMouseMoves = value
        self.window().setAcceptsMouseMovedEvents_(self.mCaptureMouseMoves)

    def setUpdateStatsDuringDrag_(self, value):
        self.mUpdateStatsDuringDrag = value

    def drawCurrentDataFromEvent_(self, theEvent):
        u"""
        This is where the pretty colors are drawn to the screen!
        A 'Real' app would probably keep track of this information so that the
        -(void) drawRect; function can properly re-draw it.
        """
        path = NSBezierPath.alloc().init()
        currentLoc = self.convertPoint_fromView_(theEvent.locationInWindow(), None)
        pressure = theEvent.pressure()

        if self.mAdjustSize is True:
            brushSize = pressure * maxBrushSize
        else:
            brushSize = 0.5 * maxBrushSize

        if self.mAdjustOpacity is True:
            opacity = pressure
        else:
            opacity = 1.0

        # Don't forget to lockFocus when drawing to view without
        # being inside -(void) drawRect;
        self.lockFocus()
        self.mForeColor.colorWithAlphaComponent_(opacity).set()
        path.setLineWidth_(brushSize)
        path.setLineCapStyle_(NSRoundLineCapStyle)
        path.moveToPoint_(self.mLastLoc)
        path.lineToPoint_(currentLoc)
        path.stroke()
        self.unlockFocus()

        '''
        If we are not updating the stats during a drag, then the
        window will not recieve an update message during the drag.
        So I explicitly force the window to flush it's contents after
        drawing each line segment. A 'Real' app would probably want to
        be smarter about this.
        '''

        self.window().flushWindow()
        self.mLastLoc = currentLoc

    def acceptsFirstResponder(self):
        return True

    def drawRect_(self, rect):
        NSColor.whiteColor().set()
        NSRectFill(self.bounds())

class PressureWinController(NSObject):
    u"""
    Controller class for Wacom Simple example.
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

        if self is None:
            return None

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(self, "wtvUpdatedStats:", WTViewUpdatedNotification, self.wtvTabletDraw)
        return self

    def awakeFromNib(self):
        self.wtvTabletDraw.setForeColor_(NSColor.orangeColor())

        # Set check marks of Pressure Menu Items.
        if(self.wtvTabletDraw.mAdjustOpacity is True):
           self.mnuOpacity.setState_(NSOnState)
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
        if sender.state() == NSOnState:
            sender.setState_(NSOffState)
            self.wtvTabletDraw.setAdjustOpacity_(False)
        else:
            sender.setState_(NSOnState)
            self.wtvTabletDraw.setAdjustOpacity_(True)

    @objc.IBAction
    def lineSizeMenuAction_(self, sender):
        if sender.state() == NSOnState:
            sender.setState_(NSOffState)
            self.wtvTabletDraw.setAdjustSize_(False)
        else:
            sender.setState_(NSOnState)
            self.wtvTabletDraw.setAdjustSize_(True)

    @objc.IBAction
    def captureMouseMovesAction_(self, sender):
        if sender.state() == NSOnState:
            sender.setState_(NSOffState)
            self.wtvTabletDraw.setCaptureMouseMoves_(False)
        else:
            sender.setState_(NSOnState)
            self.wtvTabletDraw.setCaptureMouseMoves_(True)

    @objc.IBAction
    def updateStatsDuringDragAction_(self, sender):
        if sender.state() == NSOnState:
            sender.setState_(NSOffState)
            self.wtvTabletDraw.setUpdateStatsDuringDrag_(False)
        else:
            sender.setState_(NSOnState)
            self.wtvTabletDraw.setUpdateStatsDuringDrag_(True)

    @objc.IBAction
    def openColorPanel_(self, sender):
        sender.activate(False)

    def changeColor_(self, sender):
        self.wtvTabletDraw.setForeColor_(sender.color())

    def wtvUpdatedStats_(self, theNotification):
        t = self.wtvTabletDraw.mEventType

        if t == NSLeftMouseDown or t == NSRightMouseDown:
            self.txtEventType.setStringValue_('Mouse Down')
        elif t == NSLeftMouseUp or t == NSRightMouseUp:
            self.txtEventType.setStringValue_('Mouse Up')
        elif t == NSLeftMouseDragged or t == NSRightMouseDragged:
            self.txtEventType.setStringValue_('Mouse Drag')
        elif t == NSMouseMoved:
            self.txtEventType.setStringValue_('Mouse Move')

        self.txtMouseX.setFloatValue_(self.wtvTabletDraw.mMouseX)
        self.txtMouseY.setFloatValue_(self.wtvTabletDraw.mMouseY)
        self.txtPressure.setFloatValue_(self.wtvTabletDraw.mPressure)
