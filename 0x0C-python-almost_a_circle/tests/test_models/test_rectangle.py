#!/usr/bin/python3

"""Thisunittests for rectangle.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
	"""Testing instantiation of Rectangle class."""

	def test_rectangle_is_base(self):
		self.assertIsInstance(Rectangle(10, 2), Base)

	def test_no_args_val(self):
		with self.assertRaises(TypeError):
			Rectangle()

	def test_one_arg_val(self):
		with self.assertRaises(TypeError):
			Rectangle(1)

	def test_two_args_val(self):
		q1 = Rectangle(10, 2)
		q2 = Rectangle(2, 10)
		self.assertEqual(q1.id, q2.id - 1)

	def test_three_args_val(self):
		q1 = Rectangle(2, 2, 4)
		q2 = Rectangle(4, 4, 2)
		self.assertEqual(q1.id, q2.id - 1)

	def test_four_args_val(self):
		q1 = Rectangle(1, 2, 3, 4)
		q2 = Rectangle(4, 3, 2, 1)
		self.assertEqual(q1.id, q2.id - 1)

	def test_five_args(self):
		self.assertEqual(7, Rectangle(20, 20, 0, 0, 7).id)

	def test_more_than_five_args(self):
		with self.assertRaises(TypeError):
			Rectangle(10, 20, 30, 40, 50, 60)

	def test_width_private_val(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(4, 4, 0, 0, 1).__width)

	def test_height_private_val(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(4, 4, 0, 0, 1).__height)

	def test_x_private(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(4, 4, 0, 0, 1).__x)

	def test_y_private_val(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(4, 5, 0, 0, 1).__y)

	def test_width_getter(self):
		r = Rectangle(5, 7, 7, 5, 1)
		self.assertEqual(5, r.width)

	def test_width_setter_val(self):
		r = Rectangle(5, 7, 7, 5, 1)
		r.width = 10
		self.assertEqual(10, r.width)

	def test_height_getter_val(self):
		r = Rectangle(5, 7, 7, 5, 1)
		self.assertEqual(7, r.height)

	def test_height_setter_val(self):
		r = Rectangle(5, 7, 7, 5, 1)
		r.height = 10
		self.assertEqual(10, r.height)

	def test_x_getter_val(self):
		r = Rectangle(5, 7, 7, 5, 1)
		self.assertEqual(7, r.x)

	def test_x_setter_val(self):
		q = Rectangle(5, 7, 7, 5, 1)
		q.x = 10
		self.assertEqual(10, q.x)

	def test_y_getter(self):
		q = Rectangle(5, 7, 7, 5, 1)
		self.assertEqual(5, q.y)

	def test_y_setter(self):
		q = Rectangle(5, 7, 7, 5, 1)
		q.y = 10
		self.assertEqual(10, q.y)


class TestRectangle_width(unittest.TestCase):
	"""Test const of Rectangle width attribute."""

	def test_None_width(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(None, 2)

	def test_str_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle("invalid", 2)

	def test_float_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(5.5, 1)

	def test_complex_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(complex(5), 2)

	def test_dict_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle({"a": 1, "b": 2}, 2)

	def test_bool_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(True, 2)

	def test_list_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle([1, 2, 3], 2)

	def test_set_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle({1, 2, 3}, 2)

	def test_tuple_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle((1, 2, 3), 2)

	def test_frozenset_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(frozenset({1, 2, 3, 1}), 2)

	def test_range_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(range(5), 2)

	def test_bytes_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(b'Python', 2)

	def test_bytearray_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(bytearray(b'abcdefg'), 2)

	def test_memoryview_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(memoryview(b'abcedfg'), 2)

	def test_inf_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(float('inf'), 2)

	def test_nan_width_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle(float('nan'), 2)

	def test_negative_width_val(self):
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			Rectangle(-1, 2)

	def test_zero_width_val(self):
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
	"""Test construct of Rectangle height attribute."""

	def test_None_height(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, None)

	def test_str_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, "invalid")

	def test_float_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, 5.5)

	def test_complex_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, complex(5))

	def test_dict_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, {"a": 1, "b": 2})

	def test_list_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, [1, 2, 3])

	def test_set_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, {1, 2, 3})

	def test_tuple_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, (1, 2, 3))

	def test_frozenset_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, frozenset({1, 2, 3, 1}))

	def test_range_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, range(5))

	def test_bytes_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, b'Python')

	def test_bytearray_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, bytearray(b'qwert'))

	def test_memoryview_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, memoryview(b'qwerty'))

	def test_inf_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, float('inf'))

	def test_nan_height_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, float('nan'))

	def test_negative_height_val(self):
		with self.assertRaisesRegex(ValueError, "height must be > 0"):
			Rectangle(1, -1)

	def test_zero_height_val(self):
		with self.assertRaisesRegex(ValueError, "height must be > 0"):
			Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
	"""Test construct of Rectangle x attribute."""

	def test_None_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, None)

	def test_str_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, "invalid", 2)

	def test_float_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, 5.5, 9)

	def test_complex_x(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, complex(5))

	def test_dict_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, {"a": 1, "b": 2}, 2)

	def test_bool_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, True, 2)

	def test_list_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, [1, 2, 3], 2)

	def test_set_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, {1, 2, 3}, 2)

	def test_tuple_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, (1, 2, 3), 2)

	def test_frozenset_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, frozenset({1, 2, 3, 1}))

	def test_range_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, range(5))

	def test_bytes_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, b'Python')

	def test_bytearray_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, bytearray(b'abcdefg'))

	def test_memoryview_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, memoryview(b'abcedfg'))

	def test_inf_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, float('inf'), 2)

	def test_nan_x_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, float('nan'), 2)

	def test_negative_x_val(self):
		with self.assertRaisesRegex(ValueError, "x must be >= 0"):
			Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
	"""Test construct of Rectangle y attribute."""

	def test_None_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, None)

	def test_str_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 1, "invalid")

	def test_float_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, 5.5)

	def test_complex_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, complex(5))

	def test_dict_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 1, {"a": 1, "b": 2})

	def test_list_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 1, [1, 2, 3])

	def test_set_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 1, {1, 2, 3})

	def test_tuple_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 1, (1, 2, 3))

	def test_frozenset_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

	def test_range_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, range(5))

	def test_bytes_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, b'Python')

	def test_bytearray_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, bytearray(b'abcdefg'))

	def test_memoryview_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 3, memoryview(b'abcedfg'))

	def test_inf_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 1, float('inf'))

	def test_nan_y_val(self):
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			Rectangle(1, 2, 1, float('nan'))

	def test_negative_y_val(self):
		with self.assertRaisesRegex(ValueError, "y must be >= 0"):
			Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
	"""Test Rectangle order of attribute."""

	def test_width_before_height_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle("invalid width", "invalid height")

	def test_width_before_x_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle("invalid width", 2, "invalid x")

	def test_width_before_y_val(self):
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			Rectangle("invalid width", 2, 3, "invalid y")

	def test_height_before_x_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, "invalid height", "invalid x")

	def test_height_before_y_val(self):
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			Rectangle(1, "invalid height", 2, "invalid y")

	def test_x_before_y_val(self):
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area_val(unittest.TestCase):
	"""Unittests for testing the area method of the Rectangle class."""

	def test_area_small_val(self):
		r = Rectangle(10, 2, 0, 0, 0)
		self.assertEqual(20, r.area())

	def test_area_large_val(self):
		q = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
		self.assertEqual(999999999999998999000000000000001, q.area())

	def test_area_changed_attributes(self):
		q = Rectangle(2, 10, 1, 1, 1)
		q.width = 7
		q.height = 14
		self.assertEqual(98, q.area())

	def test_area_one_arg(self):
		q = Rectangle(2, 10, 1, 1, 1)
		with self.assertRaises(TypeError):
			q.area(1)


class TestRectangle_stdout(unittest.TestCase):
	"""Test __str__ and display methods of Rectangle."""

	@staticmethod
	def capture_stdout(rect, method):
		cap = io.StringIO()
		sys.stdout = cap
		if method == "print":
			print(rect)
		else:
			rect.display()
		sys.stdout = sys.__stdout__
		return cap

	def test_str_method_print_width_height_val(self):
		r = Rectangle(4, 6)
		cap = TestRectangle_stdout.capture_stdout(r, "print")
		rs = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
		self.assertEqual(rs, cap.getvalue())

	def test_str_method_width_height_x(self):
		y = Rectangle(5, 5, 1)
		correct = "[Rectangle] ({}) 1/0 - 5/5".format(y.id)
		self.assertEqual(correct, y.__str__())

	def test_str_method_width_height_x_y_val(self):
		y = Rectangle(1, 8, 2, 4)
		correct = "[Rectangle] ({}) 2/4 - 1/8".format(y.id)
		self.assertEqual(correct, str(y))

	def test_str_method_width_height_x_y_id_val(self):
		y = Rectangle(13, 21, 2, 4, 7)
		self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(y))

	def test_str_method_changed_attributes_val(self):
		w = Rectangle(7, 7, 0, 0, [4])
		w.width = 15
		w.height = 1
		w.x = 8
		w.y = 10
		self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(w))

	def test_str_method_one_arg_val(self):
		w = Rectangle(1, 2, 3, 4, 5)
		with self.assertRaises(TypeError):
			w.__str__(1)

	def test_display_width_height_val(self):
		q = Rectangle(2, 3, 0, 0, 0)
		cap = TestRectangle_stdout.capture_stdout(q, "display")
		self.assertEqual("##\n##\n##\n", cap.getvalue())

	def test_display_width_height_x_val(self):
		q = Rectangle(3, 2, 1, 0, 1)
		cap = TestRectangle_stdout.capture_stdout(q, "display")
		self.assertEqual(" ###\n ###\n", cap.getvalue())

	def test_display_width_height_y_val(self):
		x = Rectangle(4, 5, 0, 1, 0)
		cap = TestRectangle_stdout.capture_stdout(x, "display")
		display = "\n####\n####\n####\n####\n####\n"
		self.assertEqual(display, cap.getvalue())

	def test_display_width_height_x_y(self):
		x = Rectangle(2, 4, 3, 2, 0)
		cap = TestRectangle_stdout.capture_stdout(x, "display")
		dis = "\n\n   ##\n   ##\n   ##\n   ##\n"
		self.assertEqual(dis, cap.getvalue())

	def test_display_one_arg(self):
		x = Rectangle(5, 1, 2, 4, 7)
		with self.assertRaises(TypeError):
			x.display(1)


class TestRectangle_update_args(unittest.TestCase):
	"""Test update args method of the Rectangle."""

	def test_update_args_zero_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update()
		self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(q))

	def test_update_args_one(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(89)
		self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(q))

	def test_update_args_two(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(89, 2)
		self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(q))

	def test_update_args_three_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(89, 2, 3)
		self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(q))

	def test_update_args_four_va(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(89, 2, 3, 4)
		self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(q))

	def test_update_args_five_va(self):
		r = Rectangle(10, 10, 10, 10, 10)
		r.update(89, 2, 3, 4, 5)
		self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

	def test_update_args_more_than_five_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(89, 2, 3, 4, 5, 6)
		self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(q))

	def test_update_args_None_id_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(None)
		correct = "[Rectangle] ({}) 10/10 - 10/10".format(q.id)
		self.assertEqual(correct, str(q))

	def test_update_args_None_id_and_more_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(None, 4, 5, 2)
		correct = "[Rectangle] ({}) 2/10 - 4/5".format(q.id)
		self.assertEqual(correct, str(q))

	def test_update_args_twice_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(89, 2, 3, 4, 5, 6)
		q.update(6, 5, 4, 3, 2, 89)
		self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(q))

	def test_update_args_invalid_width_type_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			q.update(89, "invalid")

	def test_update_args_width_zero_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			q.update(89, 0)

	def test_update_args_width_negative_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			q.update(89, -5)

	def test_update_args_invalid_height_type_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			q.update(89, 2, "invalid")

	def test_update_args_height_zero_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "height must be > 0"):
			q.update(89, 1, 0)

	def test_update_args_height_negative_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "height must be > 0"):
			q.update(89, 1, -5)

	def test_update_args_invalid_x_type_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			q.update(89, 2, 3, "invalid")

	def test_update_args_x_negative_val(self):
		r = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "x must be >= 0"):
			r.update(89, 1, 2, -6)

	def test_update_args_invalid_y_val(self):
		x = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			x.update(89, 2, 3, 4, "invalid")

	def test_update_args_y_negative_val(self):
		x = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "y must be >= 0"):
			x.update(89, 1, 2, 3, -6)

	def test_update_args_width_before_height_val(self):
		y = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			y.update(89, "invalid", "invalid")

	def test_update_args_width_before_x_val(self):
		y = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			y.update(89, "invalid", 1, "invalid")

	def test_update_args_width_before_y_val(self):
		x = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			x.update(89, "invalid", 1, 2, "invalid")

	def test_update_args_height_before_x_val(self):
		x = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			x.update(89, 1, "invalid", "invalid")

	def test_update_args_height_before_y_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			q.update(89, 1, "invalid", 1, "invalid")

	def test_update_args_x_before_y_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			q.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
	"""Test update kwargs method of the Rectangle."""

	def test_update_kwargs_one(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(id=1)
		self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(q))

	def test_update_kwargs_two_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(width=2, id=1)
		self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(q))

	def test_update_kwargs_three_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(width=2, height=3, id=89)
		self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(q))

	def test_update_kwargs_four_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(id=89, x=1, height=2, y=3, width=4)
		self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(q))

	def test_update_kwargs_five(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(y=5, x=8, id=99, width=1, height=2)
		self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(q))

	def test_update_kwargs_None_id_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(id=None)
		correct = "[Rectangle] ({}) 10/10 - 10/10".format(q.id)
		self.assertEqual(correct, str(q))

	def test_update_kwargs_None_id_and_more_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(id=None, height=7, y=9)
		correct = "[Rectangle] ({}) 10/9 - 10/7".format(q.id)
		self.assertEqual(correct, str(q))

	def test_update_kwargs_twice_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(id=89, x=1, height=2)
		q.update(y=3, height=15, width=2)
		self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(q))

	def test_update_kwargs_invalid_width_type_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "width must be an integer"):
			q.update(width="invalid")

	def test_update_kwargs_width_zero_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			q.update(width=0)

	def test_update_kwargs_width_negative_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "width must be > 0"):
			q.update(width=-5)

	def test_update_kwargs_invalid_height_type_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "height must be an integer"):
			q.update(height="invalid")

	def test_update_kwargs_height_zero_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "height must be > 0"):
			q.update(height=0)

	def test_update_kwargs_height_negative_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "height must be > 0"):
			q.update(height=-5)

	def test_update_kwargs_inavlid_x_type_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "x must be an integer"):
			q.update(x="invalid")

	def test_update_kwargs_x_negative_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "x must be >= 0"):
			q.update(x=-5)

	def test_update_kwargs_invalid_y_type_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(TypeError, "y must be an integer"):
			q.update(y="invalid")

	def test_update_kwargs_y_negative_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		with self.assertRaisesRegex(ValueError, "y must be >= 0"):
			q.update(y=-5)

	def test_update_args_and_kwargs_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(89, 2, height=4, y=6)
		self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(q))

	def test_update_kwargs_wrong_keys_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(a=5, b=10)
		self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(q))

	def test_update_kwargs_some_wrong_keys_val(self):
		q = Rectangle(10, 10, 10, 10, 10)
		q.update(height=5, id=89, a=1, b=54, x=19, y=7)
		self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(q))


class TestRectangle_to_dictionary(unittest.TestCase):
	"""Test to_dictionary method of the Rectangle."""

	def test_to_dictionary_output_val(self):
		rq = Rectangle(10, 2, 1, 9, 5)
		correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
		self.assertDictEqual(correct, q.to_dictionary())

	def test_to_dictionary_no_object_changes_val(self):
		q1 = Rectangle(10, 2, 1, 9, 5)
		q2 = Rectangle(5, 9, 1, 2, 10)
		q2.update(**q1.to_dictionary())
		self.assertNotEqual(q1, q2)

	def test_to_dictionary_arg_val(self):
		q = Rectangle(10, 2, 4, 1, 2)
		with self.assertRaises(TypeError):
			q.to_dictionary(1)


if __name__ == "__main__":
	unittest.main()
