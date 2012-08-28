#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Tue Aug 28 10:43:12 2012

import wx

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.bild = wx.BitmapButton(self, -1, wx.Bitmap("noname.png", wx.BITMAP_TYPE_ANY))
        self.stodbild = wx.BitmapButton(self, -1, wx.Bitmap("nonameB.png", wx.BITMAP_TYPE_ANY))
        self.namnruta = wx.TextCtrl(self, -1, "")
        self.OK = wx.Button(self, -1, "OK")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.genamn, self.bild)
        self.Bind(wx.EVT_BUTTON, self.gestod, self.stodbild)
        self.Bind(wx.EVT_TEXT_ENTER, self.nameok, self.namnruta)
        self.Bind(wx.EVT_BUTTON, self.namnok, self.OK)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.bild.SetSize(self.bild.GetBestSize())
        self.stodbild.SetSize(self.stodbild.GetBestSize())
        self.namnruta.SetMinSize((400, 20))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        topram = wx.BoxSizer(wx.VERTICAL)
        ram2 = wx.BoxSizer(wx.VERTICAL)
        delarenere = wx.BoxSizer(wx.HORIZONTAL)
        delareuppe = wx.BoxSizer(wx.HORIZONTAL)
        delareuppe.Add(self.bild, 0, 0, 0)
        delareuppe.Add(self.stodbild, 0, 0, 0)
        ram2.Add(delareuppe, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        delarenere.Add(self.namnruta, 0, 0, 0)
        delarenere.Add(self.OK, 0, 0, 0)
        ram2.Add(delarenere, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        topram.Add(ram2, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(topram)
        topram.Fit(self)
        self.Layout()
        # end wxGlade

    def genamn(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `genamn' not implemented!"
        event.Skip()

    def gestod(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `gestod' not implemented!"
        event.Skip()

    def nameok(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `nameok' not implemented!"
        event.Skip()

    def namnok(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `namnok' not implemented!"
        event.Skip()

# end of class MyFrame
class traning(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MyFrame(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class traning

if __name__ == "__main__":
    namn = traning(0)
    namn.MainLoop()
