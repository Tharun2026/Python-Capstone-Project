from tkinter import * 
import random , string
import pyperclip 

web = Tk() 
web.geometry("400x300")
web.resizable(0,0)
web.title("PYTHON PROJECT  -  CAPTACHA GENERATOR")

Label(web,text = "Captacha Generator", font = 'arial 20 bold').pack()
Label(web, text = "________",  font = 'arial 20 bold').pack(side = BOTTOM)

pass_label = Label(web,text = "CAPTACHA LENGTH", font = 'arial 20 bold').pack()
pass_len = IntVar()
length = Spinbox(web, from_ = 6, to_ = 30, textvariable = pass_len, width = 15).pack()
pass_str = StringVar()

def Generator():
    captacha = []

     # Ensuring at least one character from each type (Uppercase, Lowercase, Digits, Punctuation)
    if pass_len.get() >=4:
        captacha.append(random.choice(string.ascii_uppercase))
        captacha.append(random.choice(string.digits))
        captacha.append(random.choice(string.punctuation))
        captacha.append(random.choice(string.ascii_lowercase))


        for _ in range(pass_len.get()-4):
            captacha.append(random.choice(string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase))

            #shuffle to ensure randomness
        random.shuffle(captacha)
    else:
        # If length is less than 4, just fill the required length with random choices
        for _ in range(pass_len.get()):
            captacha.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
    
    # Convert list to string and set it to the variable
    pass_str.set(''.join(captacha))


def Copy_captacha():
    pyperclip.copy(pass_str.get())

Button(web, text = "GENERATE CAPTACHA", command = Generator).pack(pady=5)
Entry(web, textvariable = pass_str).pack()
Button(web, text = 'COPY TO CLIPBORD', command = Copy_captacha).pack(pady = 5)

web.mainloop()

