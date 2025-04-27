cars = ["bmw", "audi", "mercedes", "toyota", "ford", "honda", "chevrolet", "nissan", "hyundai", "volkswagen"]
print("List of cars", cars)
cars.sort()
print("Sorted list of cars", cars)
cars.sort(reverse=True)
print("Reverse sorted list of cars", cars) 

print("Sorted list of cars", sorted(cars))
print("Original list of cars", cars)

print("length of the list", len(cars))
print("First three cars", cars[:3])