#!/usr/bin/python3


from tkinter import *
from tkinter import ttk
import base64

def calculate(*args):
    ResultArea.delete(1.0,END)
    choiceFlag = bool(choice.get()=='Comma Separated')
    print(choiceFlag)
    if(topic.get()=='Encode'):
        cnt = 0
        topicValue=topic.get()
        inputValue=TextArea.get("1.0","end-1c")
        print("Here")
        print(inputValue)
        inputValue=(inputValue.split("\n"))
        result=""
        for s in range(len(inputValue)):
            item = inputValue[s].strip('"')
            try:
                data = base64.b64encode(item.encode('ascii')).decode('ascii')
                print(item,data)
                data=('"')+data+('"')
                result=result+(data)
                if s < len(inputValue)-1 and choiceFlag:
                    result=result+(",")
                result=result+("\n")
            except ValueError:
                result=result+'Error Encoding the value='+item
                if s < len(inputValue)-1:
                    result=result+(",")
                result=result+("\n")

        ResultArea.insert(str(float(cnt)), result)



    if(topic.get()=='Decode'):
        cnt = 0
        topicValue=topic.get()
        inputValue=TextArea.get("1.0","end-1c")
        print("Here")
        print(inputValue)
        inputValue=(inputValue.split("\n"))
        result=""
        for s in range(len(inputValue)):
            try:
                data = base64.b64decode(inputValue[s]).decode('ascii')
                print(inputValue[s],data)
                result=result+(data)
                if s < len(inputValue)-1 and choiceFlag:
                    result=result+(",")
                result=result+("\n")
            except ValueError:
                result=result+'Error Decoding the value='+inputValue[s]
                if s < len(inputValue)-1:
                    result=result+(",")
                result=result+("\n")

        ResultArea.insert(str(float(cnt)), result)

def reset():
    topic.set('Encode')
    choice.set('Comma Separated')
    TextArea.delete(1.0,END)
    ResultArea.delete(1.0,END)

def on_option_change1(*args):
    desc1=ttk.Label(page1, text=topic.get()+" Function Selected")
    desc1.grid(column=2, row=2, sticky=W)
    desc1.config(font=("Courier", 9))

def on_option_change2(*args):
    desc2=ttk.Label(page1, text=choice.get()+" Selected         ")
    desc2.grid(column=4, row=7, sticky=W)
    desc2.config(font=("Courier", 9))




root = Tk()
root.resizable(width=False, height=False)
root.title("Base64 Encode/Decode")

universal_height = 500
topic = StringVar()
choice = StringVar()
result_row_global= IntVar()
result_row_global.set(1)
duration = StringVar()
dur_value = IntVar()
topic_val = StringVar()
time1 = ''
currentDate1 = ''

# Dictionary with options
topics = {'Encode' , 'Decode'}
topic.set('Encode')


# Dictionary with choices
choices = {'Comma Separated' , 'Without Comma Separated'}
choice.set('Comma Separated')


nb = ttk.Notebook(root)
defaultPage = ttk.Frame(nb, width=300 ,height = universal_height)
page1 = ttk.Frame(nb, width= 300 ,height = universal_height)
page2 = ttk.Frame(nb, width = 300 ,height = universal_height)


nb.add(page1, text='Encode/Decode')
nb.grid(column=0)



#PAGE1    PAYLOAD
#ROW=1 TOPIC
ttk.Label(page1, text="Function").grid(column=1, row=1, sticky=W)
popupMenu = OptionMenu(page1, topic, *topics, command=on_option_change1)
popupMenu.grid(column=2, row=1, sticky=W)

desc1=ttk.Label(page1, text=topic.get()+" Function Selected")
desc1.grid(column=2, row=2, sticky=W)
desc1.config(font=("Courier", 9))

topic_entry1 = ttk.Entry(page1, width=7, textvariable=topic_val)
def payload_topic(*args):
    print(topic.get())
    topic_entry1.grid_forget()
topic.trace('w', payload_topic)

#ROW=5 Original String
ttk.Label(page1, text="Original String").grid(column=1, row=5, sticky=W)
desc=ttk.Label(page1, text="Outside Double quotes in the input string is ignored")
desc.grid(column=1, row=6, sticky=W)
desc.config(font=("Courier", 9))
TextArea = Text(page1, relief=GROOVE ,wrap=WORD, height=20, width=40, borderwidth=2)
TextArea.pack(expand=True)
TextArea.pack(side="left")
TextArea.insert(END, "")
TextArea.grid(column=1, row=10, sticky=(W, E))

#ROW=5 COL=4 Result
ttk.Label(page1, text="Results").grid(column=4, row=5, sticky=W)
popupMenu1 = OptionMenu(page1, choice, *choices, command=on_option_change2)
popupMenu1.grid(column=4, row=6, sticky=W)

desc2=ttk.Label(page1, text=choice.get()+" Selected          ")
desc2.grid(column=4, row=7, sticky=W)
desc2.config(font=("Courier", 9))

ResultArea = Text(page1, relief=GROOVE ,wrap=WORD, height=20, width=40, borderwidth=2)
ResultArea.pack(expand=True)
ResultArea.pack(side="left")
ResultArea.insert(END, "")
ResultArea.grid(column=4, row=10, sticky=(W, E))



#ROW=14 RESET, EXIT AND CALCULATE

ttk.Button(page1, text="Reset",command=reset).grid(column=1, row=60)
ttk.Button(page1, text="Result", command=calculate).grid(column=4, row=60)
ttk.Button(page1, text="Exit",command=page1.quit).grid(column=4, row=61)


root.mainloop()