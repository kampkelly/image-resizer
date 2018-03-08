from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import back


global selected_tuple #make this a global varirable to be accessible outside this function

def picker():
	window.update()
	file_path = askopenfilename()
	print(file_path)
	list1.delete(0,END)
	list1.insert(END,file_path)
#	split = file_path.split("/")
#	print(split[-1])
#	list1.insert(END,split)



def showdimensions():
	index=list1.curselection()[0] 
	selected_tuple=list1.get(index) 
	img = selected_tuple
	shape = back.ResizeClass.showdimensions(img)
	list2.delete(0,END)
	list2.insert(END,shape)
	#f = asksaveasfile(mode='w', defaultextension=".txt")
	#print(f.name)

def half():
	index=list1.curselection()[0] #get the index of selected item
	selected_tuple=list1.get(index) #get the tuple (contents) of selected item
	img = selected_tuple
	newname = back.ResizeClass.half(img)
	list1.insert(END,newname)

def low():
	index=list1.curselection()[0] #get the index of selected item
	img = selected_tuple = list1.get(index) #get the tuple (contents) of selected item
	newname = back.ResizeClass.low(img)
	list1.insert(END,newname)

def medium():
	index=list1.curselection()[0] #get the index of selected item
	img = selected_tuple=list1.get(index) #get the tuple (contents) of selected item
	newname = back.ResizeClass.medium(img)
	list1.insert(END,newname)

def high():
	index=list1.curselection()[0] #get the index of selected item
	img = selected_tuple=list1.get(index) #get the tuple (contents) of selected item
	newname = back.ResizeClass.high(img)
	list1.insert(END,newname)

window=Tk()

window.wm_title("Resize Images")
window.configure(background='darkgreen')

#window.withdraw(). #to hide the gui window

#l1=Label(window,text="Choose Image")
style = ttk.Style()
style.configure("BW.TLabel", foreground="darkgreen", background="black")

#l1=ttk.Label(text="Choose Images", style="BW.TLabel")
#l1.grid(row=0,column=0)

l2=Label(window,text="File Path")
l2.grid(row=1,column=0)

l3=Label(window,text="Image Dimensions")
l3.grid(row=0,column=2)

l4=Label(window,text="Resize Methods")
l4.grid(row=3,column=2)

list1=Listbox(window,height=6,width=25) #for listbox
list1.configure(background='grey')
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list2=Listbox(window,height=2,width=20) #for listbox
list2.configure(background='grey')
list2.grid(row=1,column=2,rowspan=1,columnspan=1)

b1=Button(window,text="Choose image",width=12,command=picker)
b1.grid(row=0,column=0)

b2=Button(window,text="Show Dimension",width=12,command=showdimensions)
b2.grid(row=1,column=3)

b3=Button(window,text="Half",width=6,command=half)
b3.grid(row=4,column=2)

b4=Button(window,text="Low",width=6,command=low)
b4.grid(row=4,column=3)

b5=Button(window,text="Medium",width=6,command=medium)
b5.grid(row=5,column=2)

b6=Button(window,text="High",width=6,command=high)
b6.grid(row=5,column=3)

b7=Button(window,text="Close",width=20,command=window.destroy)
b7.grid(row=6,column=2)

window.mainloop()