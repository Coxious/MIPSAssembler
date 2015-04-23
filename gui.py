#!/usr/bin/env python
#Life is short, use python!

import sys
import os
import wx
import asm
import deasm


class MainFrame(wx.Frame):
	
	ID_OPENASM = 100
	ID_OPENCOE = 101
	ID_SAVECOE = 102
	ID_SAVEASM = 103
	ID_ASM	   = 104
	ID_DISASM  = 105
	Input = ""
	Output = ""
	IsAssemble = True
	textAsm = None
	textCoe= None

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
		scoemi= wx.MenuItem(fileMenu, self.ID_SAVEASM ,'&Save ASM file')
		sasmmi= wx.MenuItem(fileMenu, self.ID_SAVECOE ,'&Save COE file')
		assemble= wx.MenuItem(fileMenu, self.ID_ASM,'&Assemble')
		deassemble= wx.MenuItem(fileMenu, self.ID_DISASM,'&Disassemble')

		fileMenu.AppendItem(asmmi)
		fileMenu.AppendItem(coemi)

		fileMenu.AppendSeparator()

		fileMenu.AppendItem(sasmmi)
		fileMenu.AppendItem(scoemi)

		fileMenu.AppendSeparator()

		fileMenu.AppendItem(assemble)
		fileMenu.AppendItem(deassemble)

		fileMenu.AppendSeparator()
		fileMenu.AppendItem(qmi)

		self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
		self.Bind(wx.EVT_MENU, self.OnOpenASM, asmmi)
		self.Bind(wx.EVT_MENU, self.OnOpenCOE, coemi)
		self.Bind(wx.EVT_MENU, self.OnSaveAsm, scoemi)
		self.Bind(wx.EVT_MENU, self.OnSaveCoe, sasmmi)
		self.Bind(wx.EVT_MENU, self.OnAssemble, assemble)
		self.Bind(wx.EVT_MENU, self.OnDisassemble, deassemble)

		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)

		self.SetSize((805,400))
		self.SetTitle('Assembler & Deassembler')
		self.Centre()
		self.textAsm = wx.TextCtrl(panel, pos=(3, 3), size=(400,800),style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP))	
		self.textCoe = wx.TextCtrl(panel, pos=(403, 3), size=(400,800),style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP))	
		self.SetMaxSize((805,805))
		self.SetMinSize((805,805))
		self.Show(True)

		
	def OnAssemble(self,event):
		try:
			textIn = self.textAsm.GetString(0,-1)
			textOut = asm.compileText(textIn)
			self.textCoe.Clear()
			self.textCoe.AppendText(textOut)
		except:
			error = sys.exc_info()[0]
			wx.MessageBox(str(error),'Error',wx.OK|wx.ICON_ERROR)

	def OnDisassemble(self,event):
		try:
			textIn = self.textCoe.GetString(0,-1)
			textOut = deasm.compileCoeText(textIn)
			self.textAsm.Clear()
			self.textAsm.AppendText(textOut)
		except:
			error = sys.exc_info()[0]
			wx.MessageBox(str(error),'Error',wx.OK|wx.ICON_ERROR)


	def OnQuit(self, e):
		self.Close()
		
	def OnOpenASM(self, event):
		try:
			file_wildcard = "ASM files(*.asm)|*.asm|All files(*.*)|*.*" 
			dlg = wx.FileDialog(self, "Open asm file...",
								os.getcwd(), 
								style = wx.OPEN,
								wildcard = file_wildcard)
			if dlg.ShowModal() == wx.ID_OK:
				self.Input= dlg.GetPath()
				self.IsAssemble = True
				with open(self.Input, "r") as fin:
					data=fin.read()
					self.textAsm.Clear()
					self.textCoe.Clear()
					self.textAsm.AppendText(data)
			dlg.Destroy()
		except:
			error = sys.exc_info()[0]
			wx.MessageBox(str(error),'Error',wx.OK|wx.ICON_ERROR)


	def OnOpenCOE(self, event):
		try:
			file_wildcard = "COE files(*.coe)|*.coe|All files(*.*)|*.*" 
			dlg = wx.FileDialog(self, "Open coe file...",
								os.getcwd(), 
								style = wx.OPEN,
								wildcard = file_wildcard)
			if dlg.ShowModal() == wx.ID_OK:
				self.Input= dlg.GetPath()
				self.IsAssemble = False
				with open(self.Input, "r") as fin:
					data=fin.read()
					self.textCoe.Clear()
					self.textAsm.Clear()
					self.textCoe.AppendText(data)
			dlg.Destroy()
		except:
			error = sys.exc_info()[0]
			wx.MessageBox(str(error),'Error',wx.OK|wx.ICON_ERROR)


	def OnSaveAsm(self, event):
		try:
			file_wildcard = "All files(*.*)|*.*" 
			dlg = wx.FileDialog(self, "Save ASM file...",
								os.getcwd(), 
								style = wx.SAVE,
								wildcard = file_wildcard)
			if dlg.ShowModal() == wx.ID_OK:
				self.Output = dlg.GetPath()
			dlg.Destroy()
	
			data = self.textCoe.GetString(0,-1)
			with open(self.Output,"w") as fout:
				fout.write(data)
			wx.MessageBox("Save finished!",'Information',wx.OK|wx.ICON_INFORMATION)
		except:
			error = sys.exc_info()[0]
			wx.MessageBox(str(error),'Error',wx.OK|wx.ICON_ERROR)
		
	def OnSaveCoe(self, event):
		try:
			file_wildcard = "All files(*.*)|*.*" 
			dlg = wx.FileDialog(self, "Save COE file...",
								os.getcwd(), 
								style = wx.SAVE,
								wildcard = file_wildcard)
			if dlg.ShowModal() == wx.ID_OK:
				self.Output = dlg.GetPath()
			dlg.Destroy()
	
			data = self.textCoe.GetString(0,-1)
			with open(self.Output,"w") as fout:
				fout.write(data)
			wx.MessageBox("Save finished!",'Information',wx.OK|wx.ICON_INFORMATION)
		except:
			error = sys.exc_info()[0]
			wx.MessageBox(str(error),'Error',wx.OK|wx.ICON_ERROR)
		
def main():
	
	ex = wx.App()
	MainFrame(None)
	ex.MainLoop()	

if __name__ == '__main__':
	main()

