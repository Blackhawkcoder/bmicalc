#!/usr/bin/env python3
""" Runs the BMI-calculator """

#import bmiwindow
import bmiwindowbasic
import tkinter as tk

class unitwindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.metunit = tk.Button(
            self.frame,
            text = 'Metric',
            width = 25,
            command = self.metric
            )
        
        self.impunit = tk.Button(
            self.frame,
            text = 'Imperial',
            width = 25,
            command = self.imperial
            )
        
        self.metunit.grid(row = 1, column = 1, sticky = tk.E, 
                                   padx = 20)
        self.impunit.grid(row = 1, column = 2, sticky = tk.W,
                               padx = 20)
        self.frame.pack()

    def metric(self):
        bmiwindowbasic.BmiWindow()
            
    def imperial(self):
            bmiwindowbasic.BmiWindow2()
        
        

        
    
def main(): 
    root = tk.Tk()
    app = unitwindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()






