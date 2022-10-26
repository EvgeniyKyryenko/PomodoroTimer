import time
from tkinter import *
from tkinter import messagebox
from winotify import Notification,audio

root = Tk()

class PomodoroTimer():
    def __init__(self,root):
        self.root = root
        self.root.title("Time Counter")
        self.root.geometry('362x268')
        self.root.resizable(0, 0)
        self.root.config(bg="#01002a")
        self.total_second = 5#3600
        self.default_total_second = 3600
        self.time_for_short_brake = 600
        self.time_for_long_brake = 1200
        self.timer_is_on = False
        self.job = None
        self.notifycation = Notification(
            app_id='Pomodoro Timer',
            title="Timer",
            msg='Nice, you done this session.Take a break!',
            duration="long",
        )

        # create label for timer
        self.label = Label(self.root, text="60:00", font=('Agency FB', 82), fg="#2e75b6", bg="#01002a")
        self.label.grid(row=1, columnspan=3)

        # create images for buttons
        self.image_for_start_btn = PhotoImage(file="Buttons/play_64.png")
        self.image_label_start_btn = Label(image=self.image_for_start_btn)

        self.image_for_pause_btn = PhotoImage(file="Buttons/pause_64.png")
        self.image_label_pause_btn = Label(image=self.image_for_pause_btn)

        self.image_for_restart_btn = PhotoImage(file="Buttons/restart_64.png")
        self.image_label_restart_btn = Label(image=self.image_for_restart_btn, borderwidth=0)

        # create image for upper buttons
        self.image_for_work_time = PhotoImage(file="Buttons/work_time.png")
        self.image_label_work_time = Label(image=self.image_for_work_time)
        self.image_for_short_brake = PhotoImage(file="Buttons/short_brake.png")
        self.image_label_short_brake = Label(image=self.image_for_short_brake)
        self.image_for_long_brake = PhotoImage(file="Buttons/long_brake.png")
        self.image_label_long_brake = Label(image=self.image_for_long_brake)

        # create start,stop,restart buttons
        self.start_btn = Button(self.root, image=self.image_for_start_btn, command=self.start_timer, borderwidth=0, background="#01002a",
                           activebackground="#01002a", highlightbackground="#01002a", activeforeground="#01002a")
        self.start_btn.grid(row=2, column=0)

        self.stop_btn = Button(self.root, image=self.image_for_pause_btn, borderwidth=0, command=self.stop_timer, background="#01002a",
                          activebackground="#01002a", highlightbackground="#01002a", activeforeground="#01002a")
        self.stop_btn.grid(row=2, column=1)

        self.restart_btn = Button(self.root, image=self.image_for_restart_btn, command=self.restart_timer, borderwidth=0,
                             background="#01002a", activebackground="#01002a", highlightbackground="#01002a",
                             activeforeground="#01002a")
        self.restart_btn.grid(row=2, column=2)

        # create a work and rest time button
        self.work_time_btn = Button(self.root, text="work time", command=self.work_time, image=self.image_for_work_time, borderwidth=0,
                               bg="#01002a", activebackground="#01002a", highlightbackground="#01002a",
                               activeforeground="#01002a")
        self.work_time_btn.grid(row=0, column=0)

        self.short_break_btn = Button(self.root, text="short break", command=self.short_break, image=self.image_for_short_brake,
                                 borderwidth=0, bg="#01002a", activebackground="#01002a", highlightbackground="#01002a",
                                 activeforeground="#01002a")
        self.short_break_btn.grid(row=0, column=1)

        self.long_break_btn = Button(self.root, text="long break", command=self.long_break, image=self.image_for_long_brake, borderwidth=0,
                                bg="#01002a", activebackground="#01002a", highlightbackground="#01002a",
                                activeforeground="#01002a")
        self.long_break_btn.grid(row=0, column=2)



    def cansel_job(self):
        if self.job is not None:
            self.root.after_cancel(self.job)
            self.job = None


    def set_time(self,second):
        minutes = str(second // 60)
        seconds = str(second % 60)
        if len(minutes) == 1:
            minutes = '0' + minutes
        if len(seconds) == 1:
            seconds = '0' + seconds
        self.label.config(text=f"{minutes}:{seconds}")


    def timer(self):
        if self.timer_is_on:
            if self.total_second > 0:
                self.total_second -= 1
                self.set_time(self.total_second)
                self.job = self.label.master.after(1000, self.timer)
            else:
                self.notifycation.set_audio(audio.LoopingAlarm4, loop=True)
                self.notifycation.show()
        else:
            return

    def start_timer(self):
        self.timer_is_on = True
        self.timer()
        self.start_btn.config(state=DISABLED)
        self.stop_btn.config(state=NORMAL)

    def stop_timer(self):
        self.timer_is_on = False
        self.cansel_job()
        self.start_btn.config(state=NORMAL)
        self.stop_btn.config(state=DISABLED)

    def restart_timer(self):
        self.start_btn.config(state=NORMAL)
        self.stop_btn.config(state=NORMAL)
        self.cansel_job()
        self.stop_timer()
        self.total_second = self.default_total_second
        self.set_time(self.default_total_second)

    def work_time(self):
        self.stop_timer()
        self.cansel_job()
        self.total_second = self.default_total_second
        self.set_time(self.total_second)

    def short_break(self):
        self.stop_timer()
        self.cansel_job()
        self.total_second = self.time_for_short_brake
        self.set_time(self.total_second)

    def long_break(self):
        self.stop_timer()
        self.cansel_job()
        self.total_second = self.time_for_long_brake
        self.set_time(self.total_second)

PomodoroTimer(root)
root.mainloop()


