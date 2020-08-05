import tkinter
#初始化主視窗，包括其標題與尺寸
top = tkinter.Tk()
top.title("Hello GUI")
top.minsize(200,40)
#標籤小精靈
helloLabel = tkinter.Label(top ,text = "Hello World!")
helloLabel.pack()
#啟動並開啟視窗
top.mainloop()
