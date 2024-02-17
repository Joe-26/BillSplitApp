import tkinter
import customtkinter


class BillSplit:
    def __init__(self, name, total):
        self.name = name
        self.total = total


def priceCalculation(payload):
    payload['Price'] = float(payload['Price'])
    for taxItem in payload['Tax']:
        if taxItem != '0':
            break
    totalValue = payload['Price'] + (payload['Price'] * (float(taxItem)/100))

    numOfPeople = 0
    for item in payload['People']:
        if item == '1':
            numOfPeople += 1
    shareEach = totalValue / numOfPeople
    print(shareEach)
    # price allocation
    for i in range(len(payload['People'])):
        if i == 0 and payload['People'][i] == '1':
            harsh.total += shareEach
        elif i == 1 and payload['People'][i] == '1':
            joseph.total += shareEach
        elif i == 2 and payload['People'][i] == '1':
            shashank.total += shareEach
        elif i == 3 and payload['People'][i] == '1':
            akshar.total += shareEach

    print('Harsh Total= ', harsh.total)
    print('Joe Total= ', joseph.total)
    print('Shashank Total= ', shashank.total)
    print('Akshar Total= ', akshar.total)

    hTotal.configure(text=f'Harsh = {round(harsh.total, 2)}')
    jTotal.configure(text=f'Joseph = {round(joseph.total, 2)}')
    sTotal.configure(text=f'Shashank = {round(shashank.total, 2)}')
    aTotal.configure(text=f'Akshar = {round(akshar.total, 2)}')

def submit():
    payload = {'Price': priceEntry.get(),
               'People': [boxH.get(), boxJ.get(), boxS.get(), boxA.get()],
               'Tax': [box80.get(), box30.get(), box89.get(), box49.get(), customTax.get()]}
    print("Payload - ", payload)
    priceCalculation(payload)


def checkbox_event():
    pass

def clear():
    harsh.total = 0.0
    joseph.total = 0.0
    shashank.total = 0.0
    akshar.total = 0.0

    hTotal.configure(text=f'Harsh = {round(harsh.total, 2)}')
    jTotal.configure(text=f'Joseph = {round(joseph.total, 2)}')
    sTotal.configure(text=f'Shashank = {round(shashank.total, 2)}')
    aTotal.configure(text=f'Akshar = {round(akshar.total, 2)}')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.geometry("700x500")
app.title("Bill Split v2")
app.resizable(width=False, height=False)

label = customtkinter.CTkLabel(app, text='BILL SPLIT v2.0')
label.pack(pady=10)

priceEntry = customtkinter.CTkEntry(app, placeholder_text="Enter Price")
priceEntry.pack(pady=10)

# <<< ----- Class Initialization ----- >>> #
harsh = BillSplit('harsh', 0.0)
joseph = BillSplit('joseph', 0.0)
shashank = BillSplit('shashank', 0.0)
akshar = BillSplit('akshar', 0.0)

# Frame for people checkboxes
splitFrame = customtkinter.CTkFrame(app)
splitFrame.pack(pady=10)

boxH = customtkinter.StringVar(value="0")
boxJ = customtkinter.StringVar(value="0")
boxS = customtkinter.StringVar(value="0")
boxA = customtkinter.StringVar(value="0")
checkHarsh = customtkinter.CTkCheckBox(splitFrame, text="Harsh", command=checkbox_event,
                                     variable=boxH, onvalue=1, offvalue=0)
checkJoe = customtkinter.CTkCheckBox(splitFrame, text="Joseph", command=checkbox_event,
                                     variable=boxJ, onvalue=1, offvalue=0)
checkSha = customtkinter.CTkCheckBox(splitFrame, text="Shashank", command=checkbox_event,
                                     variable=boxS, onvalue=1, offvalue=0)
checkAka = customtkinter.CTkCheckBox(splitFrame, text="Akshar", command=checkbox_event,
                                     variable=boxA, onvalue=1, offvalue=0)
checkHarsh.pack(pady=10, padx=10, side='left')
checkJoe.pack(pady=10, padx=10, side='left')
checkAka.pack(pady=10, padx=10, side='left')
checkSha.pack(pady=10, padx=10)


# Frame for Tax
taxFrame = customtkinter.CTkFrame(app)
taxFrame.pack(pady=10)

box80 = customtkinter.StringVar(value="0")
box30 = customtkinter.StringVar(value="0")
box89 = customtkinter.StringVar(value="0")
box49 = customtkinter.StringVar(value="0")
check80 = customtkinter.CTkCheckBox(taxFrame, text="8.00%", command=checkbox_event,
                                     variable=box80, onvalue=8.0, offvalue=0)
check30 = customtkinter.CTkCheckBox(taxFrame, text="3.00%", command=checkbox_event,
                                     variable=box30, onvalue=3.0, offvalue=0)
check89 = customtkinter.CTkCheckBox(taxFrame, text="8.90%", command=checkbox_event,
                                     variable=box49, onvalue=8.90, offvalue=0)
check49 = customtkinter.CTkCheckBox(taxFrame, text="4.90%", command=checkbox_event,
                                     variable=box89, onvalue=4.90, offvalue=0)
check80.pack(pady=10, padx=10, side='left')
check30.pack(pady=10, padx=10, side='left')
check89.pack(pady=10, padx=10, side='left')
check49.pack(pady=10, padx=10, side='left')

# Custom Tax value
customTax = customtkinter.CTkEntry(taxFrame, placeholder_text="Custom Tax Value")
customTax.pack(pady=10, padx=10)

# Button Frame
buttonFrame = customtkinter.CTkFrame(app)
buttonFrame.pack(pady=10)

# Submit Button
submitButton = customtkinter.CTkButton(buttonFrame, text='Enter', command=submit)
submitButton.pack(pady=10, padx=10, side='left')

# Clear/Reset Button
clearButton = customtkinter.CTkButton(buttonFrame, text='Clear', command=clear)
clearButton.pack(pady=10, padx=10)

hTotal = customtkinter.CTkLabel(app, text='Harsh = ' + str(harsh.total))
hTotal.pack(pady=10)
jTotal = customtkinter.CTkLabel(app, text='Joseph = ' + str(joseph.total))
jTotal.pack(pady=10)
sTotal = customtkinter.CTkLabel(app, text='Shashank = ' + str(shashank.total))
sTotal.pack(pady=10)
aTotal = customtkinter.CTkLabel(app, text='Akshar = ' + str(akshar.total))
aTotal.pack(pady=10)

# Clear/Reset Button
clearButton = customtkinter.CTkButton(app, text='Clear', command=clear)
clearButton.pack(pady=10)


app.mainloop()


# Scope of Improvement
# 1. Add total value