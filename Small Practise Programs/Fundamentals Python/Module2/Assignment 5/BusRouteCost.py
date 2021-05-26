#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    fuel_cost = (distance/10) * 70
    ticket_cost = no_of_passengers * 80
    if ticket_cost >= fuel_cost:
        return ticket_cost - fuel_cost
    else:
        return -1



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))