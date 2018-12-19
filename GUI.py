# Codes by Jiabao Qiu
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
from tkinter import *
import pet_detection as det

#def all_children (root) :
#    _list = root.winfo_children()
#    for item in _list :
#        if item.winfo_children() :
#            _list.extend(item.winfo_children())
#    return _list
#
#def loadFile():
#    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#    return root.filename
#
#def openFile():
##    print(root.filename)
#    widget_list = all_children(root)
#    for item in widget_list:
#        item.pack_forget()
#    root.configure(bg=white)
#    figure = det.pet_predict(root.filename)
#    canvas = FigureCanvasTkAgg(figure, master=root)
#    canvas.get_tk_widget().grid(row=3,column=0)
#    canvas.draw()
#    ex = Button(root,highlightbackground=white,fg=black,text='Go Back',font='Helvetica',
#                   command = lambda: reopen())
#    ex.place(relx=.5, rely=.9, anchor="center")
#
#def helper(event):
#    loadFile()
#
#def helper2(event):
#    openFile()

# Rests are the widgets

black = '#191414'
white = '#FCFAF2'
yellow = '#DAC9A6'

def start():
    def all_children (root) :
        _list = root.winfo_children()
        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())
        return _list

    def loadFile():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        return root.filename

    def openFile():
    #    print(root.filename)
        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()
        root.configure(bg=white)
        figure = det.pet_predict(root.filename)
        canvas = FigureCanvasTkAgg(figure, master=root)
        canvas.get_tk_widget().grid(row=0,column=0,sticky='NW')
#        hbar = Scrollbar(root)
#        hbar.grid(column=0, row=1, sticky='EW')
#        vbar = Scrollbar(root)
#        vbar.grid(column=1, row=0, sticky='NS')
#        canvas.get_tk_widget().config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
#        canvas.config(width=600,height=400)
#        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.draw()
        ex = Button(root,highlightbackground=white,fg=black,text='Go Back',font='Helvetica',
                command = lambda: reopen(root))
        ex.place(relx=.5, rely=.9, anchor="center")

    def helper(event):
        loadFile()

    def helper2(event):
        openFile()

    root = Tk()
    root.winfo_toplevel().title("Shiba or Marshmallow")
    root.geometry("900x600")
#    root.resizable(False,False)
    root.configure(bg=yellow)

    l1 = Label(root,text="Load your own images!",bg=yellow,fg=white,font='Helvetica',cursor="hand2")
#hint.grid(row=0,columnspan=2)
    l1.bind("<Button-1>",helper)
    l1.place(relx=.5, rely=.4, anchor="center")
    l2 = Label(root,text="And run a test?",bg=yellow,fg=white,font='Helvetica',cursor="hand2")
#hint.grid(row=0,columnspan=2)
    l2.bind("<Button-1>",helper2)
    l2.place(relx=.5, rely=.6, anchor="center")

    label = Label(root,text="Shiba Or Marshmallow",bg='#DAC9A6',fg=white,font=('Helvetica','36'))
#label.grid(row=2,columnspan=2)
    label.place(relx=.5, rely=.5, anchor="center")

    root.bind("<Escape>", lambda e: root.destroy())

#load = Button(root,highlightbackground=white,fg=black,text='Open File',font='Helvetica',
#               command = lambda: loadFile())
#load.grid(row=1,column=0)
#ex = Button(root,highlightbackground=white,fg=black,text='Run!',font='Helvetica',
#               command = lambda: openFile())
#ex.grid(row=1,column=1)

    mainloop()

def reopen(root):
    root.destroy()
    start()

#root = Tk()
#root.winfo_toplevel().title("Shiba or Marshmallow")
#root.geometry("600x500")
#root.resizable(False,False)
#root.configure(bg=yellow)
start()
