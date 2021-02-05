import PySimpleGUI as sg
import requests
import pandas as pd
import numpy as np
import json
layout = [
[sg.Text('Welcome to Quantum Lunch Decider v0.0.1', font=("Helvetica", 14))],
[sg.Text('The mathematically guaranteed way to have a random lunch')],
[sg.Text("Randomness generated by measuring the zero-point energy of vaccum fluctuations at Australlian National University")],
[sg.Text('Please choose a txt file containing your choices of lunch')],
[sg.Input(), sg.FileBrowse()],
[sg.Button('Generate my Lunch!>')],
[sg.Text('By Patrick Wang 2020, Creative commons')]
]


window = sg.Window("Title", layout)
event, values = window.read()
window.close()

listofchoices = pd.read_fwf(values[0])
lengthofchoices = len(listofchoices)
gen_layout=[
[sg.Text('Quantum mechanics say you will have:')],
[sg.Text('for lunch')]
] 
def decider(randomnumber, lengthofchoices):
    
    decision = int(np.floor(randomnumber / np.floor(65535/lengthofchoices)))-1

    return decision
r=requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint16&size=1')
array = r.json(encoding=str)
randomnumber_convert = array["data"]
randomnumber = randomnumber_convert[0]
decision = decider(randomnumber, lengthofchoices)
gen_layout=[
[sg.Text('Quantum mechanics say you will have:')],
[sg.Text(listofchoices.iat[decision,0]+' for lunch')]
] 
window = sg.Window('Quantum Lunch Decider', gen_layout)

event, values = window.read()
window.close()

