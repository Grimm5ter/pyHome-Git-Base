class Device:
    def __init__(self, manufacturer, serial , power, weight, material, lifetime):
        self.manufacturer = str(manufacturer)
        self.serial = str(serial)
        self.power = float(power)
        self.weight = float(weight)
        self.material = str(material)
        self.lifetime = float(lifetime)

    def __str__(self):
        class_name = self.__class__.__name__
        return f"""
        {class_name}
Производитель: {self.manufacturer}
Серийный номер: {self.serial}
Потребляемая мощность: {self.power} Вт
Вес: {self.weight} Кг
Матириал: {self.material}
Срок слуюбы: {self.lifetime} лет"""

    def _check_type(self, other):
        if not isinstance(other, Device):
            raise TypeError(
                "Ожидается экземпляр класса WaterDrop, "
                f"но получен тип {type(other)}."
            )


class CofeeMachine(Device):
    def __init__(self, **kwargs):
        super(CofeeMachine, self).__init__(**kwargs)
        self.case_color = "Не задано"
        self.used_cofee_type = "Не задано"
        self.beverage_volume = float() #Объем напитка
        self.bean_container_capacity = float() #Объем контейнера для зерен
        self.pump_pressure = float() #Давлеине помпы
        self.control_type = "Не задано"

    def additioanl_information(self):
        return f"""
                Цвет корпуса:{self.case_color}
                Объем напитка:{self.beverage_volume} л
                Объем зернового контейнераз: {self.bean_container_capacity} г
                Давление помпы: {self.pump_pressure} бар
                Тип управления: {self.control_type}"""

class Blender(Device):
    def __init__(self,manual_type,jug_material,jug_capacity,speed_amount,chopper_capacity, **kwargs):
        super(Blender, self).__init__(**kwargs)
        self.manual_type = str(manual_type)
        self.speed_amount = int(speed_amount)
        self.jug_material = str(jug_material)
        self.jug_capacity = float(jug_capacity)
        self.chopper_capacity = float(chopper_capacity)

    def blender_bio(self):
        return f"""Тип:{self.manual_type}
                    Кол-во скоростей:{self.speed_amount}
                    Материал кувшина:{self.jug_material}
                    Объем кувшина:{self.jug_capacity} л
                    Объем измельчителя:{self.chopper_capacity} л"""

class MeatGrinder(Device):
    def __init__(self,capacity,nozzles,tray_material,num_of_speed,cord_length, **kwargs):
        super(MeatGrinder, self).__init__(**kwargs)
        self.capacity = float(capacity)
        self.nozzles = int(nozzles)
        self.tray_material = str(tray_material)
        self.num_of_speed = int(num_of_speed)
        self.cord_length = float(cord_length)

    def grinder_spec(self):
        return f"""
                    Производительность:{self.capacity} кг/мин
                    Кол-во насадок: {self.nozzles}
                    Материал лотка: {self.tray_material}
                    Кол-во скоростей работы: {self.num_of_speed}
                    Длинна сетевого шнура: {self.cord_length} м
                    """

if __name__ == '__main__':
    tool = Device(manufacturer="Завод", serial="BCF-5000" , power=45, weight=5.5, material="Картоний", lifetime=33.3)

    print(tool)
    print("----------------------------------------------")

    tool1 = CofeeMachine(manufacturer="Rondell", serial="RDE-1104", power=1350, weight=10.3, material="Plastic", lifetime=10)
    tool1.case_color = "Вишневый"
    tool1.used_cofee_type = "Зерновой"
    tool1.beverage_volume = 1.8
    tool1.bean_container_capacity = 160
    tool1.pump_pressure = 19
    tool1.control_type = "Сенсорное"

    print(tool1)
    print(tool1.additioanl_information())
    print("----------------------------------------------")

    tool2 = Blender(manufacturer="Phillips",serial="HR3571",power=1000,weight=3.9,material="Металл", lifetime=3.5,
                    manual_type="Стационарный",speed_amount=10 ,jug_material="Стекло",jug_capacity=1.5,chopper_capacity=1.5)
    print(tool2)
    print(tool2.blender_bio())
    print("----------------------------------------------")

    tool3 = MeatGrinder(manufacturer="Kenwood",serial="MG-700", power=2000, weight=7.3,material="Металл",lifetime=5,
                        capacity=3, nozzles=5,tray_material="Металл", num_of_speed=2, cord_length=1.6)

    print(tool3)
    print(tool3.grinder_spec())