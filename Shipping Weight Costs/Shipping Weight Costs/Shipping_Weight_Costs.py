#Jason Luis 
#December 22, 2023 
#This application shows the different shipping costs depending on the weight of each box 

#Variables 

from tokenize import Double


cost_ground = 0 #Ground shipping cost 

cost_ground_premium = 125.00 #Premium Ground Shipping cost 

cost_drone = 0

# Input 

weight = float(input("Input the weight of the package: "))

#Ground shipping 

if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3.00 + 20.00 
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4.00 + 20.00
elif weight > 10:
    cost_ground = weight * 4.75 + 20.00

print("\nThe cost of Ground Shipping is: ", cost_ground) 

#Premium Ground Shipping
print("\nThe Cost of Premium Ground Shipping is: ", cost_ground_premium) 

#Drone Shipping 

if weight <= 2:
    cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
    cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
    cost_drone = weight * 12.00
elif weight > 10:
    cost_drone = weight * 14.25 

print("\nThe Cost of Drone Shipping is: ",cost_drone, "\n")