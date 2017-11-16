import unittest

from car import Car


class TestCar(unittest.TestCase):
      def setUp(self):
          self.car = Car()


class TestInit(TestCar):
      def test_initial_speed(self):
          self.assertEqual(self.car.speed, 0)

      def test_initial_odometer(self):
          self.assertEqual(self.car.odometer, 0)

      def test_initial_time(self):
          self.assertEqual(self.car.time, 0)


class TestAccelerate(TestCar):
      def test_accelerate_from_zero(self):
          self.car.accelerate()
          self.assertEqual(self.car.speed, 5)

      def test_multiple_accelerates(self):
          for _ in range(3):
            self.car.accelerate()
          self.assertEqual(self.car.speed, 15)


class TestBrake(TestCar):
       def test_brake_once(self):
           self.car.accelerate()
           self.car.brake()
           self.assertEqual(self.car.speed, 0)

       def test_multiple_brakes(self):
            for _ in range(3):
                self.car.accelerate()
            for _ in range(3):
                self.car.brake()
            self.assertEqual(self.car.speed, 0)

       def test_should_not_allow_negative_speed(self):
           self.car.brake()
           self.assertEqual(self.car.speed, 0)

       def test_multiple_brakes_at_zero(self):
           for _ in range(3):
              self.car.brake()
              self.assertEqual(self.car.speed, 0)

if __name__ == '__main__':
    unittest.main()

## ============================ UNIT TESTING ==================================== ##

# c:\Workspaces\git_ws\Programming\Python\OOPS>dir
#  Volume in drive C has no label.
#  Volume Serial Number is F0D9-E2BA

#  Directory of c:\Workspaces\git_ws\Programming\Python\OOPS

# 11/16/2017  12:51 PM    <DIR>          .
# 11/16/2017  12:51 PM    <DIR>          ..
# 11/16/2017  12:50 PM             1,482 car.py
# 11/16/2017  12:51 PM             1,495 test_car.py
#                2 File(s)          2,977 bytes
#                2 Dir(s)  25,472,929,792 bytes free

# c:\Workspaces\git_ws\Programming\Python\OOPS>python test_car.py
# ....The car is stopped
# The car is stopped
# The car is stopped
# .The car is stopped
# ....
# ----------------------------------------------------------------------
# Ran 9 tests in 0.000s

# OK