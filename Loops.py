countries = ["Deutschland", "Frankreich", "Italien", "Ukraine", "Osterreich"]

print(countries)
print(len(countries))

print(countries[0])
print(countries[-1])
print(countries[2].title())

countries[1] = "Spanien"
print(countries)
countries.append("Tschechien")
print(countries)
countries.insert(0, "Slovenien")
print(countries)
countries.append("russia")
deleted_country = countries.pop()
print("Deleted country is: " + deleted_country)

countries.sort()

print(countries)

countries.sort(reverse = True)
print(countries)

countries.reverse()

print(countries)
countries.reverse()
print(countries)