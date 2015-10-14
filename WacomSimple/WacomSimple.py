from AppKit import *

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

    def handleMouseEvent(self, theEvent):
        pass

    def drawCurrentDataFromEvent_(self, theEvent):
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

    def init(self):
        self = super(NSObject, self).init()

    def awakeFromNib(self):
        pass

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
