def itemprice(barcode):
    li = []
    for i in barcode:
        n = ord(i)
        if n//10:
            maxi = 0
            while n>0:
                if n%10 > maxi:
                    maxi = n%10
                n=n//10
            li.append(maxi)
        else:
            li.append(n)
    return sum(li)

inp = input("Enter BARCODE: ")
price = itemprice(inp)
print("Price of an item is: ", price)
