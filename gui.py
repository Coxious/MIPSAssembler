#!/usr/bin/env python
#Life is short, use python!

import sys
import os

import asmpattern	 as pattern
import asmclosure	 as closure
import asminstruction as inst
import asmlabel	   as lbl
import hextobin

import wx


class MainFrame(wx.Frame):
	
	ID_OPENASM = 100
	ID_OPENCOE = 101

	def __init__(self, *args, **kwargs):
		super(MainFrame, self).__init__(*args, **kwargs) 
			
		self.InitUI()
	def InitUI(self):
		
		menubar = wx.MenuBar()
		panel = wx.Panel(self, -1)
		
		fileMenu = wx.Menu()

		qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
		asmmi = wx.MenuItem(fileMenu, self.ID_OPENASM, '&Open ASM File')
		coemi = wx.MenuItem(fileMenu, self.ID_OPENCOE, '&Open COE File')
		smi= wx.MenuItem(fileMenu, wx.ID_SAVE ,'&Save')
		fileMenu.AppendItem(smi)
		fileMenu.AppendItem(asmmi)
		fileMenu.AppendItem(coemi)
		fileMenu.AppendSeparator()
		fileMenu.AppendItem(qmi)

		self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
		self.Bind(wx.EVT_MENU, self.OnOpenASM, asmmi)
		self.Bind(wx.EVT_MENU, self.OnOpenCOE, coemi)
		self.Bind(wx.EVT_MENU, self.OnSave, smi)

		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)

		self.SetSize((350, 250))
		self.SetTitle('Submenu')
		self.Centre()
		wx.TextCtrl(panel, pos=(3, 3), size=(250, 150))	
		self.Show(True)
		
	def OnQuit(self, e):
		self.Close()
		
	def OnOpenASM(self, event):
		file_wildcard = "ASM files(*.asm)|*.asm|All files(*.*)|*.*" 
		dlg = wx.FileDialog(self, "Open asm file...",
							os.getcwd(), 
							style = wx.OPEN,
							wildcard = file_wildcard)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetPath()
			self.ReadFile()
			self.SetTitle(self.title + '--' + self.filename)
		dlg.Destroy()
	

	def OnOpenCOE(self, event):
		file_wildcard = "COE files(*.coe)|*.coe|All files(*.*)|*.*" 
		dlg = wx.FileDialog(self, "Open coe file...",
							os.getcwd(), 
							style = wx.OPEN,
							wildcard = file_wildcard)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetPath()
		dlg.Destroy()
	
	def OnSave(self, event):
		file_wildcard = "All files(*.*)|*.*" 
		dlg = wx.FileDialog(self, "Open file...",
							os.getcwd(), 
							style = wx.OPEN,
							wildcard = file_wildcard)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetPath()
		dlg.Destroy()


def main():
	
	ex = wx.App()
	MainFrame(None)
	ex.MainLoop()	

if __name__ == '__main__':
	main()

