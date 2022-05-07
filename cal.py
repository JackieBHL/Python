import tkinter as tk
    

def number(givenvalue):
    print(givenvalue)

root = tk.Tk()
root.geometry("800x1200")
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.RIGHT)

for i in range(10):
    Number1 = tk.Button(frame,text= i,width=15,command=number(i))
    Number1.pack(side=tk.LEFT)



root.mainloop()