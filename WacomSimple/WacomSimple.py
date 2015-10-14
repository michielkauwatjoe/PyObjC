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

    txtEventType = IBOutlet()
    txtMouseX = IBOutlet()
    txtMouseY = IBOutlet()
    txtPressure = IBOutlet()
    clrForeColor = IBOutlet()
    wtvTabletDraw = IBOutlet()
    mnuLineSize = IBOutlet()
    mnuOpacity = IBOutlet()
    mnuCaptureMouseMoves = IBOutlet()
    mnuUpdateStatsDuringDrag = IBOutlet()

    def awakeFromNib(self):
        pass


    @IBAction
    def opacityMenuAction_(self, sender):
        pass

    @IBAction
    def lineSizeMenuAction_(self, sender):
        pass

    @IBAction
    def captureMouseMovesAction_(self, sender):
        pass

    @IBAction
    def updateStatsDuringDragAction_(self, sender):
        pass

    @IBAction
    def openColorPanel_(self, sender):
        pass

    def changeColor_(self, sender):
        pass

    def wtvUpdatedStats_(self, theNotification):
        pass
