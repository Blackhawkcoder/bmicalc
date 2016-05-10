import tkinter
import tkinter.messagebox
from tkinter import END
import bmiutils


class BmiWindow(): 
    def __init__(self):
        self.app = tkinter.Tk()

        self.app.title("BMI Calculator")

        self.setup_ui()

        # Confirm quitting the application
        self.app.wm_protocol("WM_DELETE_WINDOW", self.confirm_quit)

        # Bind Enter to calculate
        self.app.bind('<Return>', self.calculate)

        self.app.mainloop()


    def setup_ui(self):
        """ Sets up the UI itself. Placing the buttons and entry
        fields """

        # Todo: Clean up to make shorter
        self.length_label = tkinter.Label(
            self.app,
            text = "Length (cm)",
            justify = tkinter.LEFT
        )

        self.length_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT,
        )

        self.weight_label = tkinter.Label(
            self.app,
            text = "Weight (kg)",
            justify = tkinter.LEFT
        )

        self.weight_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT,
        )

        self.calculate_button = tkinter.Button(
            self.app,
            text = "Calculate",
            command = self.calculate,
            justify = tkinter.RIGHT
        )

        self.clear_button = tkinter.Button(
            self.app,
            text = "Clear All",
            command = self.clear,
            justify = tkinter.LEFT
        )

        self.bmi_label = tkinter.Label(
            self.app,
            text = "BMI",
            justify = tkinter.LEFT
        )
        
        self.status_label = tkinter.Label(
            self.app,
            text = "Status",
            justify = tkinter.LEFT
        )

        self.bmi_result = tkinter.Label(
            self.app,
            text = "0",
            justify = tkinter.RIGHT,
        )

        self.bmi_verdict = tkinter.Label(
            self.app,
            text = "Undefined",
            justify = tkinter.RIGHT,
            )

        self.length_label.grid(row = 0, column = 0)
        self.length_entry.grid(row = 0, column = 1)
        self.weight_label.grid(row = 1, column = 0)
        self.weight_entry.grid(row = 1, column = 1)
        self.calculate_button.grid(row = 2, column = 1, sticky = tkinter.E, 
                                   padx = 20)
        self.clear_button.grid(row = 2, column = 0, sticky = tkinter.W,
                               padx = 20)
        self.bmi_label.grid(row = 4, column = 0)
        self.status_label.grid(row = 5, column = 0)
        self.bmi_result.grid(row = 4, column = 1, sticky = tkinter.E, 
                             padx = 20)
        self.bmi_verdict.grid(row = 5, column = 1, sticky = tkinter.E,
                              padx = 20)


    def calculate(self, event = None):
        """ Calculates and updates the BMI result """
        bmires = bmiutils.bmi(self.length_entry.get(),self.weight_entry.get())
        self.bmi_result.config(text = "{0:.1f}".format(bmires))
        self.bmi_verdict.config(text = "{0:s}".format(bmiutils.bmi_verdict(
            bmires)))
        #determines color of verdict/status
        print("bim_verdict %s" % self.bmi_verdict.cget("text"))
        print("bim_verdict %s" % self.bmi_verdict)
        
        if self.bmi_verdict.cget("text") == "You are underweight":
            self.bmi_verdict.config(fg = "blue")
            
        elif self.bmi_verdict.cget("text") == "You are of normal weight":
            self.bmi_verdict.config(fg = "green")
            
        elif self.bmi_verdict.cget("text") == "You are overweight":
            self.bmi_verdict.config(fg = "orange")
            
        elif self.bmi_verdict.cget("text") == "You are obese":
            self.bmi_verdict.config(fg = "red")
        else:
            self.bmi_verdict.config(fg = "purple")

    def clear(self):
            """clears all Inputs"""
            self.length_entry.delete(0, END)
            self.weight_entry.delete(0, END)
            self.bmi_verdict.config(text = "Undefined", fg = "black")
            self.bmi_result.config(text = "0")
        


    def confirm_quit(self):
        """ Ask the user for confirmation they want to close the
        program """
        if(tkinter.messagebox.askokcancel("Quit",
                                          "Do you really want to quit?")):
            self.app.destroy()

class BmiWindow2(): 
    def __init__(self):
        self.app = tkinter.Tk()

        self.app.title("BMI Calculator")

        self.setup_ui2()

        # Confirm quitting the application
        self.app.wm_protocol("WM_DELETE_WINDOW", self.confirm_quit2)

        # Bind Enter to calculate
        self.app.bind('<Return>', self.calculate2)

        self.app.mainloop()


    def setup_ui2(self):
        """ Sets up the UI itself. Placing the buttons and entry
        fields """

        # Todo: Clean up to make shorter
        self.lengthft_label = tkinter.Label(
            self.app,
            text = "Length (ft)",
            justify = tkinter.LEFT
        )

        self.lengthft_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT,
        )
        self.lengthinch_label = tkinter.Label(
            self.app,
            text = "Length (inch)",
            justify = tkinter.LEFT
        )

        self.lengthinch_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT,
        )

        self.weightlb_label = tkinter.Label(
            self.app,
            text = "Weight (lb)",
            justify = tkinter.LEFT
        )

        self.weightlb_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT,
        )

        self.calculate_button = tkinter.Button(
            self.app,
            text = "Calculate",
            command = self.calculate2,
            justify = tkinter.RIGHT
        )

        self.clear_button = tkinter.Button(
            self.app,
            text = "Clear All",
            command = self.clear2,
            justify = tkinter.LEFT
        )

        self.bmi_label = tkinter.Label(
            self.app,
            text = "BMI",
            justify = tkinter.LEFT
        )
        
        self.bmi_verdict_label = tkinter.Label(
            self.app,
            text = "Status",
            justify = tkinter.LEFT
        )

        self.bmi_result = tkinter.Label(
            self.app,
            text = "0",
            justify = tkinter.RIGHT,
        )

        self.bmi_verdict = tkinter.Label(
            self.app,
            text = "Undefined",
            justify = tkinter.RIGHT,
            )

        self.lengthft_label.grid(row = 0, column = 0)
        self.lengthft_entry.grid(row = 0, column = 1)
        self.lengthinch_label.grid(row = 1, column = 0)
        self.lengthinch_entry.grid(row = 1, column = 1)
        self.weightlb_label.grid(row = 2, column = 0)
        self.weightlb_entry.grid(row = 2, column = 1)
        self.calculate_button.grid(row = 3, column = 1, sticky = tkinter.E, 
                                   padx = 20)
        self.clear_button.grid(row = 3, column = 0, sticky = tkinter.W,
                               padx = 20)
        self.bmi_label.grid(row = 4, column = 0)
        self.bmi_verdict_label.grid(row = 5, column = 0)
        self.bmi_result.grid(row = 4, column = 1, sticky = tkinter.E, 
                             padx = 20)
        self.bmi_verdict.grid(row = 5, column = 1, sticky = tkinter.E,
                              padx = 20)


    def calculate2(self, event = None):
        """ Calculates and updates the BMI result """
        bmires = bmiutils.bmi2(self.lengthft_entry.get(), self.lengthinch_entry.get(), self.weightlb_entry.get())
        self.bmi_result.config(text = "{0:.1f}".format(bmires))
        self.bmi_verdict.config(text = "{0:s}".format(bmiutils.bmi_verdict(
            bmires)))
        #determines color of verdict/status
        print("bim_verdict %s" % self.bmi_verdict.cget("text"))
        print("bim_verdict %s" % self.bmi_verdict)
        
        if self.bmi_verdict.cget("text") == "You are underweight":
            self.bmi_verdict.config(fg = "blue")
            
        elif self.bmi_verdict.cget("text") == "You are of normal weight":
            self.bmi_verdict.config(fg = "green")
            
        elif self.bmi_verdict.cget("text") == "You are overweight":
            self.bmi_verdict.config(fg = "orange")
            
        elif self.bmi_verdict.cget("text") == "You are obese":
            self.bmi_verdict.config(fg = "red")
        else:
            self.bmi_verdict.config(fg = "purple")

    def clear2(self):
            """clears all Inputs"""
            self.lengthft_entry.delete(0, END)
            self.lengthinch_entry.delete(0, END)
            self.weightlb_entry.delete(0, END)
            self.bmi_verdict.config(text = "Undefined", fg = "black")
            self.bmi_result.config(text = "0")
        


    def confirm_quit2(self):
        """ Ask the user for confirmation they want to close the
        program """
        if(tkinter.messagebox.askokcancel("Quit",
                                          "Do you really want to quit?")):
            self.app.destroy()
