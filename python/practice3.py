def family(**kwargs):
    for key, value in kwargs.items():
        
        print(key, ":", value)

family(father='John', mother='Jane', me='John Jr.')


a = [{'d' : 'asd'}, {'g' : 'qwvd'}]
print(a[0]['d'])