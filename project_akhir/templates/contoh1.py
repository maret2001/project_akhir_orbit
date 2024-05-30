from tkinter import *

class GraphicalInterface:
##Initialisation of the GUI class.
    def __init__(self, height, width):
        self.blockColor = 'DarkSeaGreen3'
        self.block_size=75
        self.padding=1
        self.frame_height = height*self.block_size
        self.frame_width = width*self.block_size
        self.root = Tk()
        self.root.resizable(width=0, height=0)
        self.height = height
        self.width = width
        
        self.frm = Frame(self.root, height=self.frame_height+8+self.padding*(height*2),
                         width=self.frame_width+8+self.padding*(width*2), background='lightgray',
                         cursor='circle', relief='sunken', borderwidth=4)
        self.frm.grid_propagate(0)
        self.frm.grid(column=0, row=0, padx=20, pady=20)
        for i in range(0,width):
            for j in range(0,height):
                cur_frame = Frame(self.frm, background=self.blockColor, height=self.block_size, width=self.block_size)
                cur_frame.grid(column=i,row=j, padx=self.padding, pady=self.padding)

    def create_circle(self, x, y, r, canvasName, color):  # center coordinates, radius       https://stackoverflow.com/questions/17985216/simpler-way-to-draw-a-circle-with-tkinter
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=color)

    def setObstacle(self, x, y):
        cv = Canvas(self.frm, height=self.block_size-15, width=self.block_size-15, background= self.blockColor, highlightthickness=0)
        self.create_circle(x = cv.winfo_reqheight()/2, y=cv.winfo_reqwidth()/2, r=30, canvasName=cv, color='black')
        cv.grid(column=x, row=y, padx=0, pady=0)

    def setAgent(self, x, y):
        cv = Canvas(self.frm, height=self.block_size-15, width=self.block_size-15, background=self.blockColor, highlightthickness=0)
        self.create_circle(x=cv.winfo_reqheight()/2, y=cv.winfo_reqwidth()/2, r=25, canvasName=cv, color='firebrick4')
        cv.grid(column=x, row=y)

    def set_all(self):
        for i in range(self.width):
            for j in range(self.height):
                self.setObstacle(i, j)
                self.root.update()
                self.root.after(250)  # like time.sleep()
                
    def run(self):
        #self.root.after(100, self.setObstacle, 0, 0)
        self.root.after(100, self.set_all)
        self.root.mainloop()
        
GraphicalInterface(5, 5).run()   