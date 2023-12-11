#!/usr/bin/python3

"""This is unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for testing Base class."""

    def setUp(self):
        """setup module for test base
        """
        Base._Base__nb_objects = 0
        pass

    def test_no_arguments_provided(self):
        """Test module in case no arguments provide
        """
        arg1 = Base()
        arg2 = Base()
        self.assertEqual(arg1.id, arg2.id - 1)

    def test_three_bases_created(self):
        """Test if three instance created
        """
        arg1 = Base()
        arg2 = Base()
        arg3 = Base()
        self.assertEqual(arg1.id, arg3.id - 2)

    class TestBase_to_json_string(unittest.TestCase):
        """Test to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(1, 4, 8, 9, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_length(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_length(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        q = Square(1, 3, 4, 2)
        self.assertEqual(str, type(Base.to_json_string([q.to_dictionary()])))

    def test_to_json_string_square_one_length(self):
        q = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([q.to_dictionary()])) == 39)

    def test_to_json_string_square_two_length(self):
        q1 = Square(10, 2, 3, 4)
        q2 = Square(4, 5, 21, 2)
        list_dicts = [q1.to_dictionary(), q2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_lists(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none_value(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args_provided(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg_provided(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_two_args(self):
        """Test that Base class raises TypeError when two arguments are provided."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_None_id_provided(self):
        """Test what base behave when id dosenot provides
        """
        arg1 = Base(None)
        arg2 = Base(None)
        self.assertEqual(arg1.id, arg2.id - 1)

    def test_unique_id_created(self):
        self.assertEqual(14, Base(14).id)

    def test_num_instances_after_unique_id(self):
        """Tis test the number of inst after id created
        """
        inst1 = Base()
        inst2 = Base(12)
        inst3 = Base()
        self.assertEqual(inst1.id, inst3.id - 1)

    def test_id_public_modify(self):
        """Test if modify id
        """
        ar = Base(15)
        ar.id = 12
        self.assertEqual(12, ar.id)

    def test_num_instances_private(self):
        """Test the number instance is private
        """
        with self.assertRaises(AttributeError):
            print(Base(15).__nb_instances)

    def test_str_with_id(self):
        """Test string created with id
        """

        self.assertEqual("days", Base("days").id)

    def test_float_id_value(self):
        """Test if id is flot value
        """
        self.assertEqual(4.5, Base(4.5).id)

    def test_complex_num_id(self):
        """Test if id work with complex number
        """
        self.assertEqual(complex(6), Base(complex(6)).id)

    def test_id_dict(self):
        """Test if id wotks with dictionary
        """
        self.assertEqual({"c": 10, "d": 4}, Base({"c": 10, "d": 4}).id)

    def test_bool_val_id(self):
        """Test if value is boolean num
        """
        self.assertEqual(True, Base(True).id)

    def test_lists_id(self):
        """Test if id work fine with list value
        """
        self.assertEqual([10, 20, 30], Base([10, 20, 30]).id)

    def test_tuples_id(self):
        """Test if id work with tuple
        """
        self.assertEqual((10, 20), Base((10, 20)).id)

    def test_set_val_id(self):
        self.assertEqual({10, 20, 30}, Base({10, 20, 30}).id)

    def test_frozensets_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_case_id(self):
        self.assertEqual(range(4), Base(range(4)).id)

    def test_bytes_val_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_val_id(self):
        self.assertEqual(bytearray(b'qwer'), Base(bytearray(b'qwer')).id)

    def test_memoryview_case_id(self):
        self.assertEqual(memoryview(b'qwer'), Base(memoryview(b'qwer')).id)

    def test_inf_val_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_val_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(2, 1)


class TestBase_save_to_file(unittest.TestCase):
    """Test save_to_file method of Base class."""

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

    def test_save_to_file_one_rectangle(self):
        q = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([q])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        q1 = Rectangle(10, 7, 2, 8, 5)
        q2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([q1, q2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        q = Square(10, 7, 2, 8)
        Square.save_to_file([q])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares_file(self):
        q1 = Square(10, 7, 2, 8)
        q2 = Square(8, 1, 2, 3)
        Square.save_to_file([q1, q2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        q = Square(10, 7, 2, 8)
        Base.save_to_file([q])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        q = Square(9, 2, 39, 2)
        Square.save_to_file([q])
        q = Square(10, 7, 2, 8)
        Square.save_to_file([q])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Test from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 20, "width": 21, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 20, "width": 21, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 4, "width": 10, "height": 8, "x": 7, "y": 8},
            {"id": 98, "width": 3, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 78, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 20, "size": 30, "height": 4},
            {"id": 17, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Test create method of Base class."""

    def test_create_rectangle_original(self):
        q1 = Rectangle(3, 5, 1, 2, 7)
        q1_dictionary = q1.to_dictionary()
        q2 = Rectangle.create(**q1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(q1))

    def test_create_rectangle_new(self):
        q1 = Rectangle(3, 5, 1, 2, 7)
        q1_dictionary = q1.to_dictionary()
        q2 = Rectangle.create(**q1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(q2))

    def test_create_rectangle_is(self):
        q1 = Rectangle(3, 5, 1, 2, 7)
        q1_dictionary = q1.to_dictionary()
        q2 = Rectangle.create(**q1_dictionary)
        self.assertIsNot(q1, q2)

    def test_create_rectangle_equals(self):
        q1 = Rectangle(3, 5, 1, 2, 7)
        q1_dictionary = q1.to_dictionary()
        q2 = Rectangle.create(**q1_dictionary)
        self.assertNotEqual(q1, q2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Test load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Remove any files created."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        q1 = Rectangle(10, 2, 7, 8, 1)
        q2 = Rectangle(4, 2, 5, 6, 2)
        Rectangle.save_to_file([q1, q2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(q1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        q1 = Rectangle(10, 7, 2, 8, 1)
        q2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([q1, q2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(q2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        q1 = Rectangle(10, 7, 2, 8, 1)
        q2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([q1, q2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        q1 = Square(5, 1, 3, 3)
        q2 = Square(9, 5, 2, 3)
        Square.save_to_file([q1, q2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(q1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        q1 = Square(1, 5, 3, 3)
        q2 = Square(5, 5, 2, 3)
        Square.save_to_file([q1, q2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(q2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Test save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Remove any files."""
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

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        q1 = Rectangle(10, 7, 2, 8, 5)
        q2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([q1, q2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        q1 = Square(10, 7, 2, 8)
        q2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([q1, q2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Test load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        q2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, q2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        q1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([q1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        q1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        q1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([q1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(q1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
