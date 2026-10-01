# try:
#     num1=int(input("Enter a number:"))
#     mum2=int(input("Enter a number:"))
#     result=num1/mum2
#     print("The result is:",result)
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")  
# 
# 
# 



try:
    l=["Ayesha", "Fatima", "Hina"]
    index=int(input("Enter an index:"))
    print("Element at index", index, "is:", l[index])
except IndexError:
    print("Index out of bounds.")
except ValueError:
    print("Invalid input. Please enter a valid index.")    