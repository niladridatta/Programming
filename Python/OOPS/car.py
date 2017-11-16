class Car:

    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if(self.speed > 0):
            self.speed -= 5
        else:
            print("The car is stopped")

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if(self.time == 0):
            print("Car is stopped")
        else:
            return self.odometer / self.time


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")

    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
            "show [O]dometer, or show average [S]peed?").upper()

        if action not in "ABOSX" or len(action) != 1:
            print("I don't know how to do that")
            continue

        if action == 'A':
            my_car.accelerate()

        elif action == 'B':
            my_car.brake()

        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))

        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))

        elif action == 'X':
            print("Exiting...")
            exit(0)

        my_car.step()
        my_car.say_state()
		