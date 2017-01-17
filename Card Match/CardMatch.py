from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.back = PhotoImage(file="cards/b.gif")
        self.solved = PhotoImage(file="cards/iu.gif")
        self.spades = PhotoImage(file="cards/ac.gif")
        self.hearts = PhotoImage(file="cards/ah.gif")

        self.cards = [self.spades, self.hearts, self.hearts, self.spades]
        random.shuffle(self.cards)  	# best way to randomize order
        
        self.reveal = [False, False, False, False]
        
        self.button0 = Button(self, image=self.back, command=self.change_image0)
        self.button0.grid(row = 0, column = 0)
        self.button1 = Button(self, image=self.back, command=self.change_image1)
        self.button1.grid(row = 0, column = 1)
        self.button2 = Button(self, image=self.back, command=self.change_image2)
        self.button2.grid(row = 0, column = 2)
        self.button3 = Button(self, image=self.back, command=self.change_image3)
        self.button3.grid(row = 0, column = 3)

        self.output = Label(self, text = "Match the Aces!")
        self.output.grid(row = 1, column = 0, columnspan = 4)

    def change_image0(self):
        self.button0["image"] = self.cards[0]
        self.reveal[0] = True
        self.after(1000, self.check_match)

    def change_image1(self):
        self.button1["image"] = self.cards[1]
        self.reveal[1] = True
        self.after(1000, self.check_match)

    def change_image2(self):
        self.button2["image"] = self.cards[2]
        self.reveal[2] = True
        self.after(1000, self.check_match)

    def change_image3(self):
        self.button3["image"] = self.cards[3]
        self.reveal[3] = True
        self.after(1000, self.check_match)

    def check_match(self):	# random, so check each possible combination!
        if self.reveal[0] and self.reveal[1] and self.cards[0] == self.cards[1]:
            self.button0["image"] = self.solved
            self.button1["image"] = self.solved
        if self.reveal[0] and self.reveal[2] and self.cards[0] == self.cards[2]:
            self.button0["image"] = self.solved
            self.button2["image"] = self.solved
        if self.reveal[0] and self.reveal[3] and self.cards[0] == self.cards[3]:
            self.button0["image"] = self.solved
            self.button3["image"] = self.solved
        if self.reveal[1] and self.reveal[2] and self.cards[1] == self.cards[2]:
            self.button1["image"] = self.solved
            self.button2["image"] = self.solved
        if self.reveal[1] and self.reveal[3] and self.cards[1] == self.cards[3]:
            self.button1["image"] = self.solved
            self.button3["image"] = self.solved
        if self.reveal[2] and self.reveal[3] and self.cards[2] == self.cards[3]:
            self.button2["image"] = self.solved
            self.button3["image"] = self.solved

        if False not in self.reveal:
            self.output["text"] = "YOU WIN!" 

# main
root = Tk()
root.title("Card Match!")
root.geometry("320x130")
app = Application(root)
root.mainloop()
