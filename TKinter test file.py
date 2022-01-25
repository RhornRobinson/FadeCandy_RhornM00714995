import tkinter as tk

window = tk.Tk()     # object that is root window
window.title('TKInter RHORNS  CAR  SHOWROOM')

text = tk.Label(text = 'WELCOME TO RHORNS AUTOMOTIVE SHOWROOM', width = 100, height = 10, bg = 'green')
text2 = tk.Label(text = 'Available Cars', width = 10, height = 3, bg = 'green')
text3 = tk.Label(text = ' 1. Mercedes ')
text4 = tk.Label(text = '2. Lexus ')
text5 = tk.Label(text = '3. Chevrolet')

text.pack()
text2.pack()
text3.pack()
text4.pack()
text5.pack()

entry =tk.Entry(width = 30)
entry.pack()

def save_and_print():
    name = entry.get()  #name which you type 'string'
    entry.delete (0,tk.END)  #number of values of your above text
    print (name)

button = tk.Button (text = 'Submit' , width = 30, height = 5, command = save_and_print)
button.pack(padx =5,pady = 5)

window.bind('<Return>', save_and_print)

#print(text.configure().keys())
window.mainloop ()   # this starts the event loop on topp of window option
