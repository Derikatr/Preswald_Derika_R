import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
import csv

filename = 'Air_Quality.csv'

def print_csv_file(filename):
   with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)

def plot():
     df = pd.read_csv(filename)

     df = df[df['Data Value'] < 9.18]

     
     
     df['Start_Date'] = pd.to_datetime(df['Start_Date'])
     df = df.sort_values('Start_Date')
     
     plt.figure(figsize=(10, 25))
     plt.plot(df['Start_Date'], df['Data Value'], marker='x')
     plt.title('Air Quality')
     plt.xlabel('Time Period')
     plt.ylabel('Data Value')
     plt.xticks()
     plt.tight_layout()
     plt.show()
        
window = Tk()
window.geometry("500x500")
window.title("UI")
window.config(background="blue")

button = Button(window, text= 'Air Quality Data', command = lambda: print_csv_file(filename))
button.pack()

button_plot = Button(window, text = 'Show Plot', command= plot)
button.pack()

window.mainloop()

