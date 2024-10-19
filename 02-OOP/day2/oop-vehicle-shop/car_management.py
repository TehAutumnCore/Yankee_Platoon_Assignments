class CarManager:
    all_cars = {}
    total_cars = 0
    id_counter = 1
    current_year = 2024

    @staticmethod
    def is_valid_make(make):
        return make.lower() in ['toyota', 'ford', 'honda']

    @staticmethod
    def is_valid_year(year):
        _year = int(year)
        return _year > 1800


    @classmethod
    def get_car(cls, id):
        return cls.all_cars.get(id)

    @classmethod
    def get_car_by_name(cls, nickname):
        for car in cls.all_cars.values():
            if car.nickname == nickname:
                return car

    @classmethod
    def remove_car(cls, id):
        car = cls.get_car(id)
        if car:
            del cls.all_cars[id] # delete from dict
            cls.total_cars -= 1
        else:
            print('Car not found')

    @classmethod
    def add_new_ford(cls, model, nickname=''):
        cls(make='Ford', year=cls.current_year, model=model, mileage=0, nickname='')

    @classmethod
    def prompt_user_to_add_car(cls):
        print('Enter info for car to add below:')
        make = input('Make?')
        model = input('Model?')
        nickname = input('Car name?')
        year = int(input('Year?'))
        mileage = int(input('Mileage?'))
        service_item = input('Most recent service?')

        # CarManager()
        cls(make=make, model=model, year=year, mileage=mileage, service=[service_item], nickname=nickname)


    def __init__(self, make='', model='', year=None, mileage=None, service=[], nickname=''):
        self._make = make.lower()
        self._model = model.lower()
        self._year = year
        self._mileage = mileage
        self._service = service
        self._nickname = nickname
        self._id = CarManager.id_counter

        CarManager.all_cars[self.id] = self
        CarManager.total_cars += 1
        CarManager.id_counter += 1

    
    # TODO: Make setters for getters?

    @property
    def id(self):
        return self._id

    @property
    def make(self):
        return self._make.capitalize()

    @property
    def model(self):
        return self._model.capitalize()

    @property
    def year(self):
        return self._year

    @property
    def mileage(self):
        return self._mileage
    
    @property
    def service(self):
        return self._service

    def add_service(self, service_type):
        self._service.append(service_type)
        print(f'Service added, services: {self.service}')

    def __repr__(self):
        return f'ID: {self.id} | {self.make} | {self.model} | {self.year} | {self.mileage} | {self.service} | Nickname: {self._nickname}'

    # all_cars, dict. class attribute
    # all_cars gets updated
    # total_cars gets updated
    # total_cars, int. class attribute
    #x make
    #x model
    #x year
    #x mileage
    #x service