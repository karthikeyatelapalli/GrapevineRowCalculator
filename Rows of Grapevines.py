#Rows of Grapevines
#Description 
#This program takes the user input to compute the formula to know how many grapevines to plant in each row. 


R = float(input("Enter the length of the row, in feet: "))

#By using input function the program takes user input for the length of row in vineyard

E = float(input("Enter the amount of space, in feet, used by an end-post assembly: "))

#By using input function the program takes user input for the space used by end post assembly

S = float(input("Enter the distance, in feet, between each vine: "))

#By using input function the program takes user input for the space between the vines

V = R - 2*E / S

#This formula calculates the number of grapevines that will fit in the row

print("you have enough space for", V ,"vines")
