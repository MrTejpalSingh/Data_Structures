# step = 5
# def draw_square(length,angle):
#     for i in range (0,step):
#         for b in range (0,4):
#             print(length+i)
#             print(angle+b)
#
# draw_square(100,90)


# def draw_square(length,angle,step):
#     step -= 1
#     if step < 5 - 1:
#         return draw_square(length,angle,step)
#     else:
#         for i in range(0,4):
#             print(length+step)
#             print(angle+i)
# draw_square(100,90,5)



def draw_square(length,angle,step):
    step -= 1
    if step > 1:
        draw_square(length,angle,step)
        for b in range (0,4):
            turtle.forward(length+step)
            turtle.right(angle+b)

draw_square(100,90,100)


draw_square(100, 90, 1)
