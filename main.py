#/usr/bin/env python3
#
# $Id:$

# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello Big Blue Bad World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()

# End of app
