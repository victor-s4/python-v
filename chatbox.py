#list of guests
guests = {'101':'Joe', '218':'k'}

#list of starters
starter_ls = ['Salad', 'Panini', 'Soup']
starter_dc = {'1':'Salad', '2':'Panini', '3':'Soup'}

#list of main course
main_course_ls = ['Beef', 'Chicken', 'Pork', 'Vegan']
main_course_dc = {'1':'Beef', '2':'Chicken', '3':'Pork', '4':'Vegan'}

#list of desserts 
#ds_ls = ['']
#ds_dc

#final order
order = {'Starter':'','Main course':'','Dessert':''}



#name and room input
name = input("Hello, what is your name? ")
room = input("What is your room number? ")

#guest verification
if  room in guests.keys():
    correct_info = True
else:
    correct_info = False
if correct_info and guests[room].lower() == name.lower():
    correct_info = True
    print('Hello,', name)
#starter input    
    print(starter_dc)
    starter = input("What would you like as your starter? Option 1, 2 or 3? ")
#starter verification   
    if starter in starter_dc.keys():
        correct_st = True
    else:
        correct_st = False
    if correct_st:
        order['Starter'] = starter_dc[starter]
#main course input        
        print(main_course_dc)
        main_course = input("What would you like for your main course? Option 1, 2, 3 or 4? ")
#main course verification        
        if main_course in main_course_dc.keys():
            correct_mc = True
        else:
            correct_mc = False
        if correct_mc:
            order['Main course'] = main_course_dc[main_course]
            
#dessert input
            
        else:
            print("Wrong information. Please try again.")
    else:
        print("That is not an option. Try again")
else:
    correct_info = False
    print('Wrong information.')
