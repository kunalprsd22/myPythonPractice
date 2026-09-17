from tkinter import *

# window initialise
application = Tk()

# window size
application.geometry('1020x630+0+0')

#window resize
application.resizable(width=False, height=False)

#window title
application.title('Hello World')

#window backgruond color
application.configure(background='burlywood')

#top pannel
top_panel = Frame(application, bd=5, relief=FLAT)
top_panel.pack(side=TOP)

#title tag
title_tag = Label(top_panel, text='Hello World' ,fg='azure4', bg='burlywood', font=('Arial', 58), width=30)
title_tag.grid(row=0, column=0)

#left panel
left_panel = Frame(application, bd=5, relief=FLAT)
left_panel.pack(side=LEFT)

#cost panel
cost_panel = Frame(application, bd=5, relief=FLAT)
cost_panel.pack(side=BOTTOM)

#food panel
food_panel = LabelFrame(left_panel, bd=1, relief=FLAT, text='Food', font= ('Arial', 18, 'bold'),fg='azure4')
food_panel.pack(side=LEFT)

#drink panel
drink_panel = LabelFrame(left_panel, bd=1, relief=FLAT, text='drink', font= ('Arial', 18, 'bold'),fg='azure4')
drink_panel.pack(side=LEFT)

#desert panel
desert_panel = LabelFrame(left_panel, bd=1, relief=FLAT, text='desert', font= ('Arial', 18, 'bold'),fg='azure4')
desert_panel.pack(side=LEFT)

#right panel
right_panel = Frame(application, bd=5, relief=FLAT)
right_panel.pack(side=RIGHT)

#calculator panel
calculator_panel = Frame(right_panel, bd=5, relief=FLAT)
calculator_panel.pack()

#invoice panel
invoice_panel = Frame(right_panel, bd=5, relief=FLAT)
invoice_panel.pack()

#button panel
button_panel = Frame(right_panel, bd=5, relief=FLAT)
button_panel.pack()

food_list = ["item1", "item2", "item3", "item4", "item5", "item6"]
drink_list = ["item1", "item2", "item3", "item4", "item5", "item6"]
desert_list = ["item1", "item2", "item3", "item4", "item5"]


#create food items
food_variable = []
counter = 0

for food in food_list:
     food_variable.append('')
     food_variable[counter] = int()
     check = Checkbutton(food_panel, text=food.title(),
                        font=('Arial', 18, 'bold'), onvalue= 1, offvalue=0, variable=food_variable[counter])

     check.grid(row=counter, column=0, sticky=W)
     counter = counter + 1

#create drink items
drink_variable = []
counter = 0

for drink in drink_list:
     drink_variable.append('')
     drink_variable[counter] = int()
     check = Checkbutton(drink_panel, text=drink.title(),
                        font=('Arial', 18, 'bold'), onvalue= 1, offvalue=0, variable=drink_variable[counter])

     check.grid(row=counter, column=0, sticky=W)
     counter = counter + 1


#create desert items
desert_variable = []
counter = 0

for desert in desert_list:
     desert_variable.append('')
     desert_variable[counter] = int()
     check = Checkbutton(desert_panel, text=desert.title(),
                        font=('Arial', 18, 'bold'), onvalue= 1, offvalue=0, variable=desert_variable[counter])

     check.grid(row=counter, column=0, sticky=W)
     counter = counter + 1

# present
application.mainloop()