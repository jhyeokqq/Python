# import another
# print(another.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = Prettytable()
table.add_column("Pokemon Name", ["피카츄", "꼬북이", "리자몽"])
table.add_column("Type", ["전기", "물", "불"])


print(table)