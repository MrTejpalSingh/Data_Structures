# lex_auth_01269442027919769669

# Global variables
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]


def calculate_total_chocolates():
    total_chocolates_received = 0
    for i in chocolates_received:
        total_chocolates_received = total_chocolates_received + i
    return total_chocolates_received

def reward_child(child_id_rewarded, extra_chocolates):
    flag = 0
    for i in child_id:
        if child_id_rewarded == i:
            flag = 1
    if flag == 0:
        print("Child id is invalid")
    else:
        if extra_chocolates < 1:
            print("Extra chocolates is less than 1")
        else:
            chocolates_received[child_id.index(child_id_rewarded)] = extra_chocolates + chocolates_received[child_id.index(child_id_rewarded)]
            print(chocolates_received)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work


print(calculate_total_chocolates())
# Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20, 2)