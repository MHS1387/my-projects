from tkinter import * 
from time import * 
from setings import *
from random import *    


tk = Tk() 
canvas = Canvas(tk, width=800, height=400) 
canvas.pack()

list_of_sentences = list(sentences.split('.'))
hight = 30
num_of_shapes = 0

def main(hight):
    sentence = (choice(list_of_sentences))
    
    for x in range(len(sentence)): 
        text = canvas.create_text(400, hight, text=sentence[0:x])
        tk.update() 
        canvas.delete(text)
        sleep(0.05)

    canvas.create_text(400, hight, text=sentence)
    hight += 30
    
    main(hight)

main(hight)


mainloop()