bicycles = ['trek', 'specialized', 'canyon', 'giant']

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)


motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles[1])
motorcycles.append('ducati')
print(f"added motorcycle: {motorcycles[3]}", motorcycles)
motorcycles.insert(0, 'harley')
print(motorcycles)
motorcycles.insert(3, 'bmw')
# insert at index 3
print(motorcycles)
del motorcycles[3]
# delete at index 3
print(motorcycles)  

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)



expensive_motorcycles = 'honda'
motorcycles.remove(expensive_motorcycles)
print(motorcycles)
