#!/usr/bin/python3
"""This defines untest for base class.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Defines untest for Base class."""

    def test_no_arg_provided(self):
        """Test base works if no args provided"""
        x1 = Base()
        x2 = Base()
        self.assertEqual(x1.id, x2.id - 1)

    def test_three_bases_val(self):
        x1 = Base()
        x2 = Base()
        x3 = Base()
        self.assertEqual(x1.id, x3.id - 2)

    def test_None_id_val(self):
        """Test if id works when no val"""
        x1 = Base(None)
        x2 = Base(None)
        self.assertEqual(x1.id, x2.id - 1)

    def test_unique_id_val(self):
        """Test if id is unique"""
        self.assertEqual(12, Base(12).id)

    def test_num_instances_after_unique_id_val(self):
        x1 = Base()
        x2 = Base(12)
        x3 = Base()
        self.assertEqual(x1.id, x3.id - 1)

    def test_id_public_val(self):
        x = Base(12)
        x.id = 15
        self.assertEqual(15, x.id)

    def test_num_instances_private_val(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id_val(self):
        self.assertEqual("days", Base("days").id)

    def test_float_id_val(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_dict_id_val(self):
        self.assertEqual({"d": 1, "e": 2}, Base({"d": 1, "e": 2}).id)

    def test_bool_id_val(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id_val(self):
        self.assertEqual([3, 2, 1], Base([3, 2, 1]).id)

    def test_tuple_id_val(self):
        self.assertEqual((10, 30), Base((10, 30)).id)

    def test_set_id_val(self):
        self.assertEqual({3, 2, 1}, Base({3, 2, 1}).id)

    def test_range_id_val(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id_val(self):
        self.assertEqual(b'hello', Base(b'hello').id)

    def test_bytearray_id_val(self):
        self.assertEqual(bytearray(b'asdf'), Base(bytearray(b'asdf')).id)

    def test_memoryview_id_val(self):
        self.assertEqual(memoryview(b'asdf'), Base(memoryview(b'asdf')).id)

    def test_inf_id_val(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id_val(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args_val(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string_val(unittest.TestCase):
    def test_to_json_string_rectangle_type(self):
        q = Rectangle(10, 9, 2, 8, 1)
        self.assertEqual(str, type(Base.to_json_string([q.to_dictionary()])))

    def test_to_json_string_rectangle_one_length(self):
        q = Rectangle(10, 9, 2, 8, 1)
        self.assertTrue(len(Base.to_json_string([q.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_length(self):
        """Test the dimention of rectangle"""
        q1 = Rectangle(2, 3, 5, 19, 2)
        q2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [q1.to_dictionary(), q2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type_val(self):
        x = Square(10, 20, 30, 40)
        self.assertEqual(str, type(Base.to_json_string([x.to_dictionary()])))

    def test_to_json_string_square_two_length(self):
        q1 = Square(10, 2, 3, 4)
        q2 = Square(4, 5, 21, 2)
        list_dicts = [q1.to_dictionary(), q2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_list_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none_val(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args_val(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg_val(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class Test_save_to_file_val(unittest.TestCase):

    @classmethod
    def tearDown(self):
        """Remove any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle_cre(self):
        x = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([x])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        q1 = Rectangle(10, 7, 2, 8, 5)
        q2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([q1, q2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square_val(self):
        x = Square(10, 7, 2, 8)
        Square.save_to_file([x])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        q1 = Square(10, 7, 2, 8)
        q2 = Square(8, 1, 2, 3)
        Square.save_to_file([q1, q2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_filename(self):
        q = Square(10, 7, 2, 8)
        Base.save_to_file([q])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file(self):
        x = Square(9, 2, 39, 2)
        Square.save_to_file([x])
        x = Square(10, 7, 2, 8)
        Square.save_to_file([x])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None_cre(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list_val(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class Test_from_json_string(unittest.TestCase):

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class Test_create(unittest.TestCase):

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        q1 = Rectangle(3, 5, 1, 2, 7)
        q1_dictionary = q1.to_dictionary()
        q2 = Rectangle.create(**q1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(q2))

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):

    @classmethod
    def tearDown(self):
        """remove created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class Test_save_to_csv(unittest.TestCase):

    @classmethod
    def tearDown(self):
        """remove created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_tocsv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class Test_load_file_csv(unittest.TestCase):

    @classmethod
    def tearDown(self):
        """Remove created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
