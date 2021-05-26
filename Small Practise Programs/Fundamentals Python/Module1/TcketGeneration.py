# lex_auth_012693763253788672132

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    ticket_number = []
    if no_of_passengers >= 5:
        for i in range(0, 5):
            n = 4
            while n >= 0:
                ticket_number.append((no_of_passengers + 100) - n)
                n -= 1
            ticket_number_list.append(airline + ":" + source[0:3] + ":" + destination[0:3]+":"+str(ticket_number[i]))
    else:
        for i in range(0, no_of_passengers):
            ticket_number_list.append(airline + ":" + source[0:3] + ":" + destination[0:3]+":10"+str(i+1))

    return ticket_number_list


# Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI", "Bangalore", "London", 4))