def even_numbers():
    for num in range (start,end):
        if num%2==0:
            print(num,end=" ")

start=2
end=int(input("Enter the number"))

even_numbers();