from car_management import CarManager

# print(f"car manager class{CarManager.all_cars} num cars {CarManager.total_cars}")

# ford = CarManager('ford','focus',200,100000,['oil change'])
# print(ford)
# ford.add_service('change tires')
# print(ford)

toyota = CarManager(make='toyota',model='prius',mileage=50000,year=2000)
toyota.add_service('change tires')
# print(toyota)

# print(f"car manager class{CarManager.all_cars} num cars {CarManager.total_cars}")

CarManager.prompt_user_to_add_car()

# CarManager.add_new_ford(model="F150","Wife's car")
print(CarManager.all_cars)

CarManager.get_car(1)
CarManager.remove_car(1)
print(CarManager.all_cars)