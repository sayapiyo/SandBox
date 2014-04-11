#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

from Tkinter import *
import time

class App(Frame):
	TIME = 60 * 3
	def __init__(self, master = None):
		Frame.__init__(self,master)
		self.time = 0
		self.master.title("Test Timer")
		self.timestr = StringVar()
		self.timestr.set("03:00")
		l = Label(self,textvariable=self.timestr,
				font=('Helvetica', '48', 'bold'))
		b1 = Button(self,text="Start", command=self.countdown)
		b2 = Button(self,text="Quit",
					command=self.master.destroy)
		for obj,sideparam in ((l,TOP),(b1,LEFT),(b2,RIGHT)):
				obj.pack(side=sideparam)
		self.pack()

	def countdown(self):
		if self.time == 0:
			self.time = time.time()
		timeleft = max(self.TIME-(time.time()-self.time), 0)
		min,sec = (timeleft) / 60, timeleft % 60
		self.timestr.set("%02d:%02d" % (min, sec))
		self.after(1000,self.countdown) #１秒後にメソッドを呼ぶ

if __name__ == "__main__":
		app = App()
		app.mainloop()
