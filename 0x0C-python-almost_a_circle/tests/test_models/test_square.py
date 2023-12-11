#!/usr/bin/python3
"""this unittests for models/square.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle_class(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args_val(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg_al(self):
        q1 = Square(10)
        q2 = Square(11)
        self.assertEqual(q1.id, q2.id - 1)

    def test_two_args_val(self):
        q1 = Square(10, 2)
        q2 = Square(2, 10)
        self.assertEqual(q1.id, q2.id - 1)

    def test_three_args_val(self):
        x1 = Square(10, 2, 2)
        x2 = Square(2, 2, 10)
        self.assertEqual(x1.id, x2.id - 1)

    def test_more_than_four_args_val(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private_val(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_get_val(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_set_val(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_get_val(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_get_val(self):
        q = Square(4, 1, 9, 2)
        q.size = 8
        self.assertEqual(8, q.height)

    def test_x_get_val(self):
        self.assertEqual(0, Square(10).x)

    def test_y_get_val(self):
        self.assertEqual(0, Square(10).y)


class Test_size_for_square(unittest.TestCase):

    def test_None_size_get(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size_get(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(8))

    def test_dict_size_format(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Py')

    def test_bytearray_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'efg'))

    def test_memoryview_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'efg'))

    def test_inf_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size_val(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size_val(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size_val(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class Test_x_corrdinate_squ(unittest.TestCase):

    def test_None_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x_format(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"u": 1, "b": 2}, 2)

    def test_bool__valx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_range_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(8))

    def test_bytes_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Py')

    def test_bytearray_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'defg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'dfg'))

    def test_inf_x_val(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def test_negative_x_val(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class Test_y_coordinate(unittest.TestCase):

    def test_None_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complex_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dict_y_format(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_list_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_range_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(8))

    def test_bytes_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Py')

    def test_bytearray_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'defg'))

    def test_memoryview_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def test_inf_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y_val(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_negative_y_val(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -5)


class Test_order_of_init_square(unittest.TestCase):

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area_method(unittest.TestCase):

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large_num(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes_val(self):
        q = Square(2, 0, 0, 1)
        q.size = 7
        self.assertEqual(49, q.area())

    def test_area_one_arg_val(self):
        q = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            q.area(1)


class TestSquare_stdout(unittest.TestCase):

    @staticmethod
    def capture_stdout(sq, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        s = Square(4)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y_val(self):
        q = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(q.id)
        self.assertEqual(correct, str(q))

    def test_str_method_size_x_y_id(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        q = Square(7, 0, 0, [4])
        q.size = 15
        q.x = 8
        q.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(q))

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_display_size_val(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x_val(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y_val(self):
        s = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y_val(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg_val(self):
        q = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            q.display(1)


class Test_update_args_Square(unittest.TestCase):
    def test_update_args_zero(self):
        q = Square(10, 10, 10, 10)
        q.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(q))

    def test_update_args_one_val(self):
        q = Square(10, 10, 10, 10)
        q.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(q))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_more_than_four_val(self):
        q = Square(10, 10, 10, 10)
        q.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(q))

    def test_update_args_width_set_val(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_set_val(self):
        q = Square(10, 10, 10, 10)
        q.update(89, 2)
        self.assertEqual(2, q.height)

    def test_update_args_None_id(self):
        q = Square(10, 10, 10, 10)
        q.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(q.id)
        self.assertEqual(correct, str(q))

    def test_update_args_None_id_and_more_val(self):
        q = Square(10, 10, 10, 10)
        q.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(q.id)
        self.assertEqual(correct, str(q))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        q = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            q.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        q = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            q.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        q = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            q.update(89, "invalid", "invalid")

    def test_update_args_size_before_y_val(self):
        q = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            q.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y_val(self):
        a = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.update(89, 1, "invalid", "invalid")


class Test_update_kwargs_Square(unittest.TestCase):

    def test_update_kwargs_one(self):
        q = Square(10, 10, 10, 10)
        q.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(q))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative_val(self):
        q = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            q.update(x=-5)

    def test_update_kwargs_invalid_y_val(self):
        a = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            a.update(y="invalid")

    def test_update_args_and_kwargs_val(self):
        q = Square(10, 10, 10, 10)
        q.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(q))

    def test_update_kwargs_wrong_keys(self):
        q = Square(10, 10, 10, 10)
        q.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(q))


class Test_to_dictionary_Square(unittest.TestCase):

    def test_to_dictionary_output_val(self):
        x = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, x.to_dictionary())

    def test_to_dictionary_no_object_changes_val(self):
        q1 = Square(10, 2, 1, 2)
        q2 = Square(1, 2, 10)
        q2.update(**q1.to_dictionary())
        self.assertNotEqual(q1, q2)

    def test_to_dictionary_arg_val(self):
        a = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            a.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
