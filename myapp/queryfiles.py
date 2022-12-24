
#return all customer table

customer = Customer.objects.all()

# return first customer 
first = customers.first()
print(first)
--> Asif

# return last customer 
last= customers.last()
print(last)

#return single customer by name
a = customers.objects.get(name= 'asif')
print(a)
-->asif

x= a.email()
print(x)
--> asif@gmail.com