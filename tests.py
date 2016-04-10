import unittest

import plate_reader


class TestApp(unittest.TestCase):
    def test(self):
        test_str_1 = 'Pan Jan zmienił tablicę rejestracyjną XY 12345 na YX67893'
        test_str_2 = 'FF8K3JD Bla bla costam costam alfdskj'
        test_str_3 = 'FF8K3JD Bla bla VFKKDDVV costam alfdskj'
        test_str_4 = 'FF8K3JD Bla bla VFKKDDVV costam alfdskjGF345BB'

        result_str_1 = 'Pan Jan zmienił tablicę rejestracyjną <TABLICA REJ> na <TABLICA REJ>'
        result_str_2 = '<TABLICA REJ> Bla bla costam costam alfdskj'
        result_str_3 = '<TABLICA REJ> Bla bla <TABLICA REJ>V costam alfdskj'
        result_str_4 = '<TABLICA REJ> Bla bla <TABLICA REJ>V costam alfdskj<TABLICA REJ>'

        self.assertEqual(result_str_1, plate_reader.replace_plates(test_str_1))
        self.assertEqual(result_str_2, plate_reader.replace_plates(test_str_2))
        self.assertEqual(result_str_3, plate_reader.replace_plates(test_str_3))
        self.assertEqual(result_str_4, plate_reader.replace_plates(test_str_4))


if __name__ == '__main__':
    unittest.main()