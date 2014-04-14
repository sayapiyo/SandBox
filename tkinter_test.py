#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

from Tkinter import (
    Frame, Label, Button,
    TOP, LEFT, RIGHT,
    StringVar
)
import time

class App(Frame):
    TIME = 10 * 1
    TIME_FORMAT = "%02d:%02d"

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.time = 0
        self.master.title("Test Timer")
        self.timestr = StringVar()
        self.timestr.set("03:00")
        title = Label(self,textvariable=self.timestr,
                      font=('Helvetica', '48', 'bold'))
        start_btn = Button(self,text="Start", command=self.countdown)
        quit_btn = Button(self,text="Quit", command=self.master.destroy)
        for obj, sideparam in ((title,TOP),(start_btn,LEFT),(quit_btn,RIGHT)):
            obj.pack(side=sideparam)
        self.pack()

    def countdown(self):
        if self.time == 0:
            self.time = time.time()
        timeleft = self.TIME - (time.time() - self.time)
        timeleft = max(timeleft, 0)
        min, sec = ((timeleft) / 60, timeleft % 60)
        self.timestr.set(self.TIME_FORMAT % (min, sec))
        if 1 > timeleft:
            return
        if __debug__:
            print 'timeleft: %d' % timeleft
        self.after(1 * 1000, self.countdown) #１秒後にメソッドを呼ぶ

if __name__ == "__main__":
    app = App()
    app.mainloop()
