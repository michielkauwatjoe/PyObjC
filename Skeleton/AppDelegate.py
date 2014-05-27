from Cocoa import *
from MyWindowController import *

class AppDelegate(NSObject):
    u"""
    Delegate is the main logic component, which sets the controllers.
    """
    myWindowController = objc.ivar()

    def applicationDidFinishLaunching_(self, notification):
        u"""
        Open a new document after application launch.
        """
        if self.myWindowController is None:
            self.myWindowController = MyWindowController.alloc().initWithWindowNibName_("TestWindow")

        self.myWindowController.showWindow_(self)

