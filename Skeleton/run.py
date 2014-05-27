# -*- coding: UTF-8 -*- # -----------------------------------------------------------------------------
#     BuroFont Editor
#     (c) 2014+  Font Bureau
#
#     No distribution without permission.
#
# -----------------------------------------------------------------------------
#
#   run.py
#
import os
from PyObjCTools import AppHelper
from AppKit import NSApplication, NSApp, NSBundle, NSLog # @UnresolvedImport
import objc
objc.setVerbose(True) # @UndefinedVariable

import AppDelegate
import MyWindowController

app = NSApplication.sharedApplication()
nibPath = os.path.join(os.path.dirname(__file__), "dist", "Skeleton.app", "Contents", "Resources", "English.lproj", "MainMenu.nib")
NSBundle.loadNibFile_externalNameTable_withZone_(nibPath, {}, None) # @UndefinedVariable
nibPath = os.path.join(os.path.dirname(__file__), "dist", "Skeleton.app", "Contents", "Resources", "English.lproj", "TestWindow.nib")
NSBundle.loadNibFile_externalNameTable_withZone_(nibPath, {}, None) # @UndefinedVariable
delegate = AppDelegate.AppDelegate.alloc().init() # @UndefinedVariable
app.setDelegate_(delegate)

# Bring app to top
NSApp.activateIgnoringOtherApps_(True)

AppHelper.runEventLoop()
