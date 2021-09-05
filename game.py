print("Choose one option given below and keep it in mind :-\n1. apple\n2. mango\n3. orange\n4. pear")
print("is the chosen one in the following :-\n1. apple\n2. mango")
a = str(input("type 'y' for 'yes' and 'n' for 'no'. : "))
print("is the chosen one in the following :-\n1. apple\n2. orange")
b = str(input("type 'y' for 'yes' and 'n' for 'no'. : "))
print("is the chosen one in the following :-\n1. mango\n2. pear")
c = str(input("type 'y' for 'yes' and 'n' for 'no'. : "))
print("is the chosen one in the following :-\n1. pear\n2. orange")
d = str(input("type 'y' for 'yes' and 'n' for 'no'. : "))
if a == "y" and b == "y" and c == "n" and d == "n":
    print("you have chosen 1. apple.")
elif a == "y" and b == "n" and c == "y" and d == "n":
    print("you have chosen 2. mango.")
elif a == "n" and b == "y" and c == "n" and d == "y":
    print("you have chosen 3. orange.")
elif a == "n" and b == "n" and c == "y" and d == "y":
    print("you have chosen 4. pear.")
else:
    print("oops! please try again.")