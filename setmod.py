from os import system
from tkinter import Tk, messagebox
from time import sleep

def setdown():
    setmod_window = Tk()
    setmod_window.withdraw()

    tid = messagebox.askyesno('Confirm','Are you sure you want to shut down the computer?')
    if tid:
        system('shutdown -s -f -t 0')
    elif not tid:
        messagebox.showwarning('Cancel','You have canceled the plan!')
    setmod_window.destroy()

def timedown(time):
    setmod_window = Tk()
    setmod_window.withdraw()

    tid = messagebox.askyesno('Confirm', f'Are you sure you want to shut down the computer?\nYour computer will shut down after {time} seconds!')
    if tid:
        system(f'shutdown -s -f -t {time}')
    elif not tid:
        messagebox.showwarning('Cancel', 'You have canceled the plan!')
    setmod_window.destroy()

def unshutdown():
    system('shutdown -a')

if __name__ == '__main__':
    timedown(60)
    sleep(5)
    unshutdown()

def reboot():
    setmod_window = Tk()
    setmod_window.withdraw()

    tid = messagebox.askyesno('Confirm','Are you sure you want to reboot the computer?')
    if tid:
        system('shutdown / r / t 0')
    elif not tid:
        messagebox.showwarning('Cancel', 'You have canceled the plan!')
    setmod_window.destroy()

def timereboot(time):
    setmod_window = Tk()
    setmod_window.withdraw()

    tid = messagebox.askyesno('Confirm',f'Are you sure you want to reboot the computer?\nYour computer will reboot after {time} seconds!')
    if tid:
        system('shutdown / r / t {time}')
    elif not tid:
        messagebox.showwarning('Cancel', 'You have canceled the plan!')
    setmod_window.destroy()

if __name__ == '__main__':
    timereboot(60)
    sleep(5)
    unshutdown()
