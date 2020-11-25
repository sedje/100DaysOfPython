# from turtle import Turtle, Screen
#
#
# def main():
#     timmy = Turtle()
#     timmy.shape("turtle")
#     timmy.color("green")
#     my_screen = Screen()
#     timmy.forward(100)
#     my_screen.exitonclick()
#
#
# if __name__ == '__main__':
#     main()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon', ["Pikachu", "Squirtle", "Charmander"])
table.add_column('Type', ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)