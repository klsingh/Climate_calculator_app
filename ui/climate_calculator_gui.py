import tkinter as tk
from tkinter import ttk
from src.user_interface import App
from src.carbon_footprint_calculator import CarbonFootprintCalculator
from src.carbon_credit_system import CarbonCreditSystem


class ClimateCalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x300')
        self.master.title('Climate Calculator')
        self.master.resizable(False, False)

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')

        self.home_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.home_frame, text='Home')
        self.calculator_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.calculator_frame, text='Calculator')

        self.app = App(self.home_frame)
        self.carbon_calculator = CarbonFootprintCalculator(self.calculator_frame)
        self.credit_system = CarbonCreditSystem()

if __name__ == '__main__':
    root = tk.Tk()
    app = ClimateCalculatorGUI(root)
    root.mainloop()
