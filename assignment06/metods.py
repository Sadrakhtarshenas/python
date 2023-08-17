#copy
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print(x)


#insert
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)


#index
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)


#extend
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)