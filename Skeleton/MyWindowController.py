from Cocoa import *

class MyWindowController(NSWindowController):

    def initWithPath_(self, newPath):
        return super(MyWindowController, self).init()

    def awakeFromNib(self):
        # make sure our angle text input keep the right format
        pass
