from PyObjCTools import NibClassBuilder

'''
FIXME: merge nib files or load differently.

from https://pythonhosted.org/pyobjc/api/module-PyObjCTools.NibClassBuilder.html:

Deprecated since version 2.4: Use of this module is deprecated because it
cannot be used with modern versions of Xcode (starting at Xcode 4.0), and
because recent versions of Xcode can extract class information from Python
sources.

Introduction

The module is used to avoid repeating class inheritance and outlet definitions
in both python sources and Interface Builder NIB files.

The module reads this information from NIB files and provides a magic meta
class that inserts the right superclass and outlet definitions.

Do not use this module for new developement, it will likely disappear in a
future version of PyObjC because it can no longer work with modern versions of
Xcode, and in particular not with XIB files and compiled NIB files.
'''

NibClassBuilder.extractClasses("MainMenu")
NibClassBuilder.extractClasses("TLayerDemo")

from PyObjCTools import AppHelper

import AppDelegate
import Circle
import Extras
import ShadowOffsetView
import TLayerDemo
import TLayerView

import objc; objc.setVerbose(True)

AppHelper.runEventLoop()
