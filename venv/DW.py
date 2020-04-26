def prime_num(num):
    lst = []
    for num in range(1,num+1):
        for n in range(2,num+1):
            if num % n == 0 and num != n:
                break
        else:
            lst.append(num)
    return lst

print(prime_num(20))

def product_prime(num):
    lst = prime_num(num)
    product = []
    for i in lst[::-1]:
        if num % i == 0:
            other = num/i
            if other > i:
                product.append((i,other))
                break
            else:
                product.append((other,i))
                break
    return product

print(product_prime(38))