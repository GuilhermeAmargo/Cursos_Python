import datetime
import os
import tkinter as tk
import time
import winsound  # Importa o módulo winsound

def alarm():
    set_alarm_time = f'{hour.get()}:{minute.get()}:{second.get()}'
    alarm_path = os.path.abspath('Alarm.wav')

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            winsound.PlaySound(alarm_path, winsound.SND_FILENAME)
            break

root = tk.Tk()
root.geometry("400x200")
root.title('Alarme Python')

tk.Label(root, text="Alarme Python", font=('Helvetica 20 bold')).pack(pady=10)
tk.Label(root, text="Definir alarme").pack(pady=5)

frame = tk.Frame(root)
frame.pack()

def option(value):
    opt = tk.StringVar(root)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hour = option(24)
minute = option(60)
second = option(60)

tk.Button(root, text="Definir", font=('Helvetica 15'), command=alarm).pack(pady=20)
root.mainloop()
