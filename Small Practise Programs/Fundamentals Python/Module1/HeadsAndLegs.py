# lex_auth_012693810762121216155

def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0
    flag = 0

    for i in range(1, legs + 1):
        if legs/heads == 2:
            chicken_count = heads
            rabbit_count = 0
            print(chicken_count, rabbit_count)
            flag = 1
            break
        else:
            rabbit_count = i
            rabbit_legs = i * 4
            remaining_legs = legs - rabbit_legs
            chicken_count = heads - i
            if chicken_count * 2 == remaining_legs:
                print(chicken_count, rabbit_count)
                flag = 1
    if flag != 1:
        print(error_msg)


# Provide different values for heads and legs and test your program
solve(35, 94)