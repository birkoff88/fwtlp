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



guest_list = ["Ivan", "Masha", "Sasha", "Georgi"]
print(f"Hello {guest_list[0]}, you are invited to dinner.")
print(f"Hello {guest_list[1]}, you are invited to dinner.")
print(f"Hello {guest_list[2]}, you are invited to dinner.")

print(f"{guest_list[1]} can't make it to dinner.")
guest_list[1] = "Pesho"

guest_list.pop(2)   
print(guest_list)