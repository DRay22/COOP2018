# Exercise 56
# Trimester 1 Exam
# Donovan Ray
#
#
#   Algorithm:
#       is_triangle:
#           use three checking equations:
#               check1 = a + b < c
#               check2 = c + a < b
#               check3 = b + c < a
#               if check1 is True
#                   return True
#               if check2 is True
#                   return True
#               if check3 is True
#                   return True
#               if check1 is False
#                   return False
#               if check2 is False
#                   return False
#               if check3 is False
#                   return False
#       main:
#           print introduction: "This program will check three user inputted lengths to see
#           print "if they would make a triangle"
#           get a as int (first side) with prompt: "What is the length of the first side?   "
#           get b as int (second side) with prompt: "What is the length of the second side?   "
#           get c as int (third side) with prompt: "What is the length of the third side? (Press Q to quit)  "
#           call is_triangle and define as tri
#           if tri returns False:
#               print "The sides would make a triangle"
#           if tri returns True:
#               print "The sides would not make a triangle"
#
#
# if __name__ == '__main__':
#   main()


def is_triangle(a, b, c):
    check1 = a + b < c
    check2 = c + b < a
    check3 = a + c < b
    if check1 is True:
        return True
    if check2 is True:
        return True
    if check3 is True:
        return True
    if check1 is False:
        return False
    if check2 is False:
        return False
    if check3 is False:
        return False


def main():
        print("This program will check three user inputted lengths to see if they would make a triangle")
        a = int(input("What is the length of the first side?   "))
        b = int(input("What is the length of the second side?   "))
        c = int(input("What is the length of the third side?   "))
        tri = is_triangle(a, b, c)
        if tri == False:
            print("The sides would make a triangle")
        if tri == True:
            print("the sides would not make a triangle")


if __name__ == '__main__':
    main()
