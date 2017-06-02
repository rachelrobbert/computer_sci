#program 0

#name =  input("enter your name")
#print ("Hello", name)

#end Program 0

#program 1
t = input("enter a temperature in Celcius")

f = float(t)

f = float(t) * 9/5 + 32

print("The temp in Fahrenheit is:", f)

# end program 1

#program 2

t = input("enter a temperature in Fahrenheit")

c = float(t)

c = float(t) - 32.0

ce = float(c) / 1.8

print("The temp in Celsius is:", ce)

#end program 2

#program 3

cost = input("Type in the item's cost:")

state = input("Type in the state tax:")

fed = input("Type in the federal tax:")

totaltaxrate =  float(fed) + float(state)

totaltax = totaltaxrate*float(cost)

totalcost = float(totaltax) + float(cost)
 
print("The item's total tax is:", totaltax)

print("The item's total cost is:", totalcost)
 #end program 3

#program 4

distance = input("Enter the distance between two cities in miles:")

speed1 = input("Enter the speed of bike one in mph:")

speed2 = input("Enter the speed of bike two in mph:")

meeting_distance = (float(distance) * float(speed1))/ (float(speed1)+float(speed2))
 
print = ("they meet", float(distance) - meeting_distance, "from the second city")



















