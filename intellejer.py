from tkinter import *

class OutputText:
    def __init__(self):
        self.inc = 0
        
    def get_number(self, edits):
        self.array = []
        self.x = 0
        self.y = 0
        canvas.delete("all")
        text.delete(1.0, END)
        self.inc = int(edits)
        self.Len = 400/self.inc
        for i in range(self.inc):
            self.array.append([])
            for j in range(self.inc):
                self.array[i].append(0)
                canvas.create_rectangle(self.x, self.y, self.x + self.Len, self.y + self.Len, tag = "rec" + str(j) + str(i))
                self.x += self.Len
            self.x = 0
            self.y += self.Len
            
    def mouse_event(self, event):
        self.xx = event.x
        self.yy = event.y
        self.x_inc = 0
        self.y_inc = 0
        while(self.xx > 0):
            if(self.xx > 0):
                self.x_inc += 1
                self.xx -= self.Len
        while(self.yy > 0):
            if(self.yy > 0):
                self.y_inc += 1
                self.yy -= self.Len
        if(self.array[self.y_inc - 1][self.x_inc - 1] == 0):
            self.array[self.y_inc - 1][self.x_inc - 1] = 1
            self.rect_color("rec" + str(self.x_inc - 1) + str(self.y_inc - 1))
        else:
            self.array[self.y_inc - 1][self.x_inc - 1] = 0
            self.re_color("rec" + str(self.x_inc - 1) + str(self.y_inc - 1))
            
    def rect_color(self, rectangle):
        canvas.itemconfigure(rectangle, fill = 'Black')
    
    def re_color(self, rectangle):
        canvas.itemconfigure(rectangle, fill = 'white')

    def outs(self):
        text.delete(1.0, END)
        for i in range(self.inc):
            for j in range(self.inc):
                text.insert(END, self.array[i][j])

           
root = Tk()

outText = OutputText()
root.geometry("1000x520+50+50")

label = Label(root, text = "Enter number: ", font = "Arial 12 bold")
label.place(x = 300, y = 10)


edit = Entry(root, width = 20)
edit.insert(0,9)
edit.place(x = 430, y = 13)

button = Button(root, text = "Enter", font = "Arial 10 bold", width = 10,
                command = lambda: outText.get_number(edit.get()))
button.place(x = 560, y = 10)

out = Button(root, text = "Output", font = "Arial 10 bold", width = 10,
               command = lambda: outText.outs())
out.place(x = 660, y = 10)

text = Text(root, height = 2, width = 120, font = "Arial 10 bold", wrap = WORD)
text.place(x = 75, y = 50)

canvas = Canvas(root, width = 400, height = 400, bg = 'white')
canvas.place(x = 300, y = 100)

canvas.bind('<Button-1>', outText.mouse_event)

root.mainloop()
