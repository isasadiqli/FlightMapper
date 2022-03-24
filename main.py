import threading
import tkinter as tk

import PIL.Image
from PIL import ImageTk

import tools
from gui_tools import *
from ocr import get_text

import sys


# import psutil


def start_process():
    # vid = tools.files(env.image_frames)
    # process(vid)
    if not env.is_high_FPS:
        get_text()


def thread_handling():
    t = threading.Thread(target=start_process)
    if not t.is_alive():
        t.daemon = True
        t.start()
    else:
        t.join()
        t = threading.Thread(target=start_process)
        t.daemon = True
        t.start()


def thread_handling_for_cvs():
    t = threading.Thread(target=show_csv)
    if not t.is_alive():
        t.daemon = True
        t.start()
    else:
        t.join()
        t = threading.Thread(target=show_csv)
        t.daemon = True
        t.start()


def fun():
    print(threading.active_count())


env.thread_map[env.t_m] = threading.Thread(target=tools.create_kml)
env.t_m = 0


def thread_handling_for_map():
    print('t_m', env.t_m)
    print('len', env.thread_map.__len__())
    print('act thre', threading.active_count())
    if not env.thread_map[0].daemon:
        # print('inside')
        env.thread_map[env.t_m].daemon = True
        env.thread_map[env.t_m].start()

        env.t_m += 1


    else:
        env.thread_map[env.t_m - 1].join()
        thread_map = (threading.Thread(target=tools.create_kml))
        thread_map.daemon = True
        thread_map.start()



    # t = threading.Thread(target=tools.create_kml)
    # if not env.thread_map.is_alive():
    #     print('49')
    #     # env.thread_map.daemon = True
    #     env.thread_map.start()
    #     # env.thread_map.join()
    # else:
    #     # env.thread_map.join()
    #     print(threading.active_count())
    #     env.thread_map = threading.current_thread()
    #     # print(env.thread_map.daemon)
    #     # env.thread_map.join()
    #     # env.thread_map.
    #     # env.thread_map.daemon = False
    #
    #     # print(env.thread_map.daemon)
    #     # env.thread_map = threading.Thread(target=tools.create_kml)
    #     # env.thread_map = threading.Thread(target=tools.create_kml)
    #     # tools.create_kml()
    #     # print(env.thread_map.daemon)
    #     # env.thread_map.daemon = True
    #
    #     # print(env.thread_map.daemon)
    #     # env.thread_map.start()
    #
    #     # print(env.thread_map.daemon)


env.init()
env.window.title('Aircraft Data Scanning and Processing Program')
env.window.geometry("1280x720")
# env.window.overrideredirect(True)
env.window.resizable(False, False)

filename = PhotoImage(file="res/background_img.png")
background_label = Label(env.window, image=filename)

exit_icon = PIL.Image.open("res/exit_icon.png")
exit_icon = exit_icon.resize((35, 35))
exit_icon = ImageTk.PhotoImage(exit_icon)

minimize_icon = PIL.Image.open("res/minimize_icon.png")
minimize_icon = minimize_icon.resize((35, 35))
minimize_icon = ImageTk.PhotoImage(minimize_icon)

browse_folder_icon = PIL.Image.open("res/browse_video.png")
browse_folder_icon = browse_folder_icon.resize((60, 60))
browse_folder_icon = ImageTk.PhotoImage(browse_folder_icon)

fps_icon = PIL.Image.open("res/fps_icon.png")
fps_icon = fps_icon.resize((55, 55))
fps_icon = ImageTk.PhotoImage(fps_icon)

start_icon = PIL.Image.open("res/start_icon.png")
start_icon = start_icon.resize((60, 60))
start_icon = ImageTk.PhotoImage(start_icon)

create_kml_icon = PIL.Image.open("res/kml_icon.png")
create_kml_icon = create_kml_icon.resize((60, 60))
create_kml_icon = ImageTk.PhotoImage(create_kml_icon)

show_csv_icon = PIL.Image.open("res/show_csv_icon.png")
show_csv_icon = show_csv_icon.resize((60, 60))
show_csv_icon = ImageTk.PhotoImage(show_csv_icon)

browse_csv_icon = PIL.Image.open("res/browse_csv_icon.png")
browse_csv_icon = browse_csv_icon.resize((60, 60))
browse_csv_icon = ImageTk.PhotoImage(browse_csv_icon)

reset_icon = PIL.Image.open("res/reset_icon.png")
reset_icon = reset_icon.resize((60, 60))
reset_icon = ImageTk.PhotoImage(reset_icon)

# Create a File Explorer label
label_window = tk.Label(env.window,
                        text="Aircraft Data Scanning and Processing Program",
                        fg="white", background='black')

label_window.config(font=("Verdana", 20))
env.label_information = tk.Label(env.window,
                                 text="",
                                 fg="red", background='black')

env.label_information.config(font=("Verdana", 15))

env.label_information2 = tk.Label(env.window,
                                  text="WELCOME",
                                  fg="gray", background='black', font=("Verdana", 18))

label_window.after(3000, env.label_information2.destroy)

label_buttons = tk.Label(env.window, background='black')

button_explore = tk.Button(env.window, command=browse_files, background='black', image=browse_folder_icon, relief=FLAT,
                           borderwidth=0)
# button_explore.config(font=("Verdana", 9))
env.fps_variable = DoubleVar(env.window)
env.fps_variable.set("0.15")
select_fps = tk.OptionMenu(env.window, env.fps_variable, "0.1", "0.15", "0.2", "1", "5", "10", "20", "30", "60")

select_fps.config(image=fps_icon, background='black', borderwidth=0, highlightthickness=0, activebackground="black")
# text_FPS = Label(env.window, text="Please Select FPS:")

button_start_process = tk.Button(env.window, image=start_icon, command=thread_handling, relief=FLAT, borderwidth=0)
button_start_process.config(bg="black")

# button_start_process.config(font=("Verdana", 9))
button_loadCSV = tk.Button(env.window, image=browse_csv_icon, command=browse_files, background='black',
                           activebackground="#ff73c8", relief=FLAT, borderwidth=0)
button_loadCSV.config(font=("Verdana", 9))
button_exit = tk.Button(env.window, command=exit, width=35, height=35, background='black', image=exit_icon)
button_create_kml = tk.Button(env.window, image=create_kml_icon, command=thread_handling_for_map, background='black',
                              relief=FLAT,
                              borderwidth=0)
button_create_kml.config(font=("Verdana", 9))
button_showCSV = tk.Button(env.window, image=show_csv_icon, command=show_csv, background='black', relief=FLAT,
                           borderwidth=0)
# button_showCSV.config(font=("Verdana", 9))
button_reset = tk.Button(env.window, image=reset_icon, background='black', relief=FLAT, borderwidth=0,
                         command=restart_program)
button_reset.config(font=("Verdana", 9))
button_minimize = tk.Button(env.window, width=35, height=35, command=minimize_window,
                            background='black', image=minimize_icon)

CreateToolTip(button_explore, text='Browse video file')
CreateToolTip(button_loadCSV, text='Browse CSV File\nfor load manually CSV file')
CreateToolTip(button_showCSV, text='Show CSV File')
CreateToolTip(button_reset, text='Reset')
CreateToolTip(button_create_kml, text='Create KML file')
CreateToolTip(button_start_process, text='Start to process')
CreateToolTip(select_fps, text='Select FPS')

background_label.place(x=0, y=0, relwidth=1, relheight=1)
label_window.place(x=0, y=0, width=1280, height=60)
env.label_information2.place(x=127, y=525, width=1000, height=50)
env.label_information.place(x=127, y=525, width=1000, height=50)
# button_exit.place(x=900, y=900, relwidth=0.06, relheight=0.05)
label_buttons.place(x=0, y=0, width=100, height=1000)
button_explore.place(x=8, y=100)
select_fps.place(x=10, y=175)
# text_FPS.place(x=100, y=175, relwidth=0.07, relheight=0.015)
button_create_kml.place(x=8, y=475)
button_showCSV.place(x=9, y=400)
button_loadCSV.place(x=13, y=325)
button_start_process.place(x=8, y=250)
button_reset.place(x=8, y=550)
button_exit.place(x=1230, y=10)
button_minimize.place(x=1175, y=10)

env.s.theme_use("alt")
env.s.configure("TProgressbar", thickness=5, background='yellow', troughcolor='black')

env.read_progress_bar = Progressbar(env.window, orient=HORIZONTAL,
                                    length=500, mode='determinate', style="TProgressbar")

env.process_progress_bar = Progressbar(env.window, orient=HORIZONTAL,
                                       length=500, mode='determinate', style="TProgressbar")

center(env.window)
env.window.mainloop()
