class Point:
    __pi = 3.141596
    # magic methods

    def __init__(self, **kwargs):
        self.__dimintions = kwargs

    def __str__(self) -> str:
        formated_point = ''
        for key, value in self.__dimintions.items():
            formated_point += f'{key} : {value}\n'
        return formated_point

    def __eq__(self, other: object) -> bool:
        flag = False
        print(f'**********"_eq/ not eq magic method_"**********')
        for key in self.__dimintions.keys():
            if self.__dimintions.get(key) == other.__dimintions.get(key):
                print(
                    f'*{key} comparing : {self.__dimintions.get(key)} equil {other.__dimintions.get(key)}')
                flag = True
            else:
                print(
                    f'{key} comparing : {self.__dimintions.get(key)} not equil {other.__dimintions.get(key)}')
                flag = False
        print(f'***********************************************')
        return flag

    def __gt__(self, other: object, show_info: bool = False) -> bool:
        flag = False
        print(f'**********"_gt/lt magic method_"**********')

        for key in self.__dimintions.keys():
            if self.__dimintions.get(key) > other.__dimintions.get(key):
                flag = True
                print(
                    f'{key} comparing : {self.__dimintions.get(key)} greater {other.__dimintions.get(key)}'
                )
            else:
                flag = False
                print(
                    f'*{key} comparing : {self.__dimintions.get(key)} less {other.__dimintions.get(key)}'
                )
        print(f'***************************************')

        return flag

    def __add__(self, other: object) -> dict:
        result = {}
        print(f'**********"_add magic method_"**********')

        for key in self.__dimintions.keys():
            if str(self.__dimintions.get(key)).isdigit() and str(other.__dimintions.get(key)).isdigit():
                print(
                    f'{key} : {self.__dimintions.get(key)} + {other.__dimintions.get(key)} = {self.__dimintions.get(key) + other.__dimintions.get(key)}'
                )
                result.update({key: self.__dimintions.get(
                    key) + other.__dimintions.get(key)})

            else:
                print(
                    f'Can\'t apply arithmitic on {key},because it is not int')

        print(f'****************************************')

        return result

    def __sub__(self, other: object) -> dict:
        result = {}
        print(f'**********"_sub magic method_"**********')

        for key in self.__dimintions.keys():
            if str(self.__dimintions.get(key)).isdigit() and str(other.__dimintions.get(key)).isdigit():
                print(
                    f'{key} : {self.__dimintions.get(key)} - {other.__dimintions.get(key)} = {self.__dimintions.get(key)-  other.__dimintions.get(key)}'
                )
                result.update({key: self.__dimintions.get(
                    key) - other.__dimintions.get(key)})

            else:
                print(
                    f'Can\'t apply arithmitic on {key},because it is not int')
        print(f'****************************************')

        return result

    def __mul__(self, other: object) -> dict:
        result = {}
        print(f'**********"_mul magic method_"**********')

        for key in self.__dimintions.keys():
            if str(self.__dimintions.get(key)).isdigit() and str(other.__dimintions.get(key)).isdigit():
                print(
                    f'{key} : {self.__dimintions.get(key)} * {other.__dimintions.get(key)} = {self.__dimintions.get(key)*  other.__dimintions.get(key)}'
                )
                result.update({key: self.__dimintions.get(key)
                               * other.__dimintions.get(key)})

            else:
                print(
                    f'Can\'t apply arithmitic on {key},because it is not int')
        print(f'****************************************')

        return result

    def __div__(self, other: object) -> dict:
        result = {}
        print(f'**********"_div magic method_"**********')

        for key in self.__dimintions.keys():
            if str(self.__dimintions.get(key)).isdigit() and str(other.__dimintions.get(key)).isdigit():
                print(
                    f'{key} : {self.__dimintions.get(key)} / {other.__dimintions.get(key)} = {self.__dimintions.get(key)/  other.__dimintions.get(key)}'
                )
                result.update({key: self.__dimintions.get(
                    key) / other.__dimintions.get(key)})

            else:
                print(
                    f'Can\'t apply arithmitic on {key},because it is not an int')
        print(f'****************************************')

        return result
    # Class methods

    @classmethod
    def init_empty(cls):
        dic = {'x': 0,
               'y': 0}
        return cls(**dic)
    # Object methods

    def draw(self):
        for key, value in self.__dimintions.items():
            print(f'{key} value is : {value}')

    def calc(self):
        x, y = self.__dimintions.values()
        print(Point.__pi*x+y)

    def setter(self, **v):  # {'z' : 25}
        self.__dimintions.update(v)


p = Point(x=25, y=810)
print(p)
p4 = p
p.setter(z=25)
print(p)
p3 = Point(x=5, y=1000)
print(p3)
print(p == p3)
print(p * p3)
