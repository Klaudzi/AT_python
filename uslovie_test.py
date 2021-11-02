from uslovie import *
import unittest


class MyTest_unit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Начинаем !")
        print("=//=//=//=//=//=//=//=//=//=")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Уже закончили!")

    def setUp(self):
        """Set Up Method!"""
        print(self.id()  + "   --- [" + self.shortDescription() + "]")
        print("----------------------------")


    def test_dz_01(self):
        """Во введенном числе присутствует 0 или 9"""
        self.assertEqual(dz_01('901'),'ОК')

    def test_dz_01a(self):
        """в числе нет 0 или 9"""
        self.assertNotEqual(dz_01('891'),'NO')

    def test_dz_02(self):
        """Ваша прибыль учеличится!!!"""
        self.assertEqual(dz_02(1000,2000),2032)

    def test_dz_02_01(self):
        """Некорректные данные!!!"""
        self.assertEqual(dz_02(2000,1000),'NaN')

    def test_dz_2(self):
        """ -- Решение найдено! """
        self.assertEqual(dz_2(23,8),10)

    def test_dz_2_01(self):
        """ -- Введенные значения не корректны! """
        self.assertEqual(dz_2(-23,8),0)


if __name__ == '__main__':
    unittest.main()
