guests = ["bobbert", "chuckles", "fruples"]
guests.insert(0, "frinkadoon")
guests.insert(2, "fuzzles")
guests.append("chumbawumba")
print(guests)
print("unfortunately my new table won't arrive in time, so i have to kick some people out")
first_pop = guests.pop()
print(f"sorry about that {first_pop}")
second_pop = guests.pop()
print(f"sorry about that {second_pop}")