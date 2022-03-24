import csv
import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

import PySimpleGUI as sg

import environment as env


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "9", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


def show_csv():
    # root = tkinter.Tk()
    #
    # root.geometry("1010x710")
    # root.pack_propagate(True)
    #
    # # Frame for TreeView
    # frame1 = tkinter.LabelFrame(root, text="Excel Data", background='black')
    # frame1.place(height=700, width=1000)
    #
    # ## Treeview Widget
    # tv1 = ttk.Treeview(frame1)
    # tv1.place(relheight=1, relwidth=1)
    #
    # treescrolly = tkinter.Scrollbar(frame1, orient="vertical", command=tv1.yview)
    # treescrollx = tkinter.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
    # tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    # treescrollx.pack(side="bottom", fill="x")
    # treescrolly.pack(side="right", fill="y")
    #
    # file_path = "files/output.csv"
    #
    # df = pd.read_csv(file_path)
    #
    # tv1["column"] = list(df.columns)
    # tv1["show"] = "headings"
    # for column in tv1["columns"]:
    #     tv1.heading(column, text=column)  # let the column heading = column name
    # df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
    # for row in df_rows:
    #     tv1.insert("", "end", values=row)
    #
    # root.mainloop()

    filename = 'files/output.csv'
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        header_list = next(reader)
        data = list(reader)
    sg.SetOptions(element_padding=(0, 10),
                  background_color='black')

    layout = [
        [sg.Table(
            key='table1',
            values=data,
            headings=header_list,
            max_col_width=25,
            auto_size_columns=False,
            justification='left',
            background_color='#444444',
            alternating_row_color='black',
            num_rows=25,
            enable_events=True)],
    ]

    window = sg.Window(
        title='CSV File',
        return_keyboard_events=True,
        grab_anywhere=False).Layout(layout)

    while True:
        event, values = window.Read()

        if event is None or event == 'Exit':
            window.close()
            break

        if event == 'Escape:27':  # Exit on ESC
            window.close()
            break
    env.s.theme_use("alt")
    return mainloop()


b_filename = ""


def browse_files():
    global b_filename
    b_filename = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Video",
                                                        "*.mp4*"),
                                                       ("csv file",
                                                        "*.csv")))
    if b_filename == "":
        env.label_information.configure(text="File could not be opened !!! " + b_filename)
    else:
        env.label_information.configure(text="File Opened: " + b_filename)


def minimize_window():
    env.window.wm_state('iconic')
    env.window.iconify()


def restart_program():
    os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)

    python = sys.executable
    os.execl(python, python, *sys.argv)


def change_label():
    env.label_information['text'] = "kjhkhk"


def center(win, pyqt=False):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
