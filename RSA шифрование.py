from rsa import *
from tkinter import *
(pubkey_a, privkey_a) = newkeys(512)
(pubkey_b, privkey_b) = newkeys(512)


def send_m_a():
    a=textentry_a.get()
    message=a.encode('utf8')
    global crypto_a
    crypto_a = encrypt(message, pubkey_a)
    textentry_a.delete(0,END)

def receive_m_a():
    b=decrypt(crypto_a, privkey_a)
    output_a.insert(END, '\n')
    output_a.insert(END, b)

def delete():
    output_a.delete('1.0',END)

def send_m_b():
    b=textentry_b.get()
    message=b.encode('utf8')
    global crypto_b
    crypto_b = encrypt(message, pubkey_b)
    textentry_b.delete(0,END)

def receive_m_b():
    b=decrypt(crypto_b, privkey_b)
    output_b.insert(END, '\n')
    output_b.insert(END, b)

def delete_b():
    output_b.delete('1.0',END)

root = Tk()
root.title('cryptation')

Label (root, text="Your Message", bg="black", fg="white", font="bold") .grid (row=0, column=0, pady=10)
Label (root, text="Received Message", bg="black", fg="white", font="bold") .grid (row=0, column=1)


textentry_a = Entry (root, width=40, bg="white")
textentry_a.grid(row=1, column=0, padx=10)

output_a = Text(root, width=40, height=3, background="white")
output_a.grid(row=1, column=1, padx=10, pady=10)

Button(root, text="Send Message",width=15,command=send_m_a).grid(row=2,column=0)
Button(root, text="Receive Message",width=15,command=receive_m_a).grid(row=2,column=1)
Button(root, text="Delete",width=15,command=delete).grid(row=3,column=1)

#reverse
Label (root, text="Your Message", bg="black", fg="white", font="bold") .grid (row=4, column=1)
Label (root, text="Received Message", bg="black", fg="white", font="bold") .grid (row=4, column=0)

textentry_b = Entry (root, width=40, bg="white")
textentry_b.grid(row=5, column=1, padx=10)

output_b = Text(root, width=40, height=3, background="white")
output_b.grid(row=5, column=0, padx=10, pady=10)

Button(root, text="Send Message",width=15,command=send_m_b).grid(row=6,column=1)
Button(root, text="Receive Message",width=15,command=receive_m_b).grid(row=6,column=0)
Button(root, text="Delete",width=15,command=delete_b).grid(row=7,column=0)

root.mainloop()
