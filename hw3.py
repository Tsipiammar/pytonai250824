# # question 1:
#
# # firstName: str = input("enter your first name?")
# # lastName: str = input("enter your last name?")
# # height: float = float(input("enter your height?"))
# # yearOfBirth: int = int(input("enter your year of birth?"))
# #
# # print(f'name: {lastName} ,{firstName} height: {height} year of birth:{yearOfBirth}')
#
# firstName1: str = input("enter your first name?")
# lastName1: str = input("enter your last name?")
# height1: float = float(input("enter your height?"))
# yearOfBirth1: int = int(input("enter your year of birth?"))
#
# firstName2: str = input("enter your first name?")
# lastName2: str = input("enter your last name?")
# height2: float = float(input("enter your height?"))
# yearOfBirth2: int = int(input("enter your year of birth?"))
#
# firstName3: str = input("enter your first name?")
# lastName3: str = input("enter your last name?")
# height3: float = float(input("enter your height?"))
# yearOfBirth3: int = int(input("enter your year of birth?"))
#
# print(f'name: {lastName1:<7} ,{firstName1:<7}. height: {height1:<4} year of birth:{yearOfBirth1:<4}')
# print(f'name: {lastName2:<7} ,{firstName2:<7}. height: {height2:<4} year of birth:{yearOfBirth2:<4}')
# print(f'name: {lastName3:<7} ,{firstName3:<7}. height: {height3:<4} year of birth:{yearOfBirth3:<4}')

# # question 2:
#
# score: int = int(input("enter yuor score?"))
#
# if 0 <= score <= 40:
#     print("try harder next time...")
# elif 41 <= score <= 60:
#     print("you're getting there, need some more work")
# elif 61 <= score <= 80:
#     print("pretty good")
# elif 81 <= score <= 95:
#     print("awesome!")
# elif 96 <= score <= 100:
#     print("excellent!!! You're a Star!")
# else:
#     print("illegal grade")

# score: int = int(input("enter yuor score?"))
#
# match score:
#     case score if 0<= score <= 40:
#         print("try harder next time...")
#     case score if 41 <= score <= 60:
#         print("you're getting there, need some more work")
#     case score if 61 <= score <= 80:
#         print("pretty good")
#     case score if 81 <= score <= 95:
#         print("awesome!")
#     case score if 96 <= score <= 100:
#         print("excellent!!! You're Star!")
#     case _:
#         print("illegal score")

# question 3:
volume: int = int(input("enter volume level? (0-10)"))

match volume:
    case 0:
        print("mute")
    case 1 | 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9 | 10:
        print("extremely loud")
