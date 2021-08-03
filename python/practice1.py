

a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)
    local(300)
    print(a, b, c)
enclosed()
print(a, b)


print(sum)
print(sum(range(2)))
sum = 5
print(sum)
print(sum(range(2)))
