import unittest


class Dummy:
    pass


class Dummy2:
    @classmethod
    def __match__(cls, other):
        return isinstance(other, set)


class Dummy3:
    def __unpack__(self):
        return ('a', 'b', 'c')


class Dummy4:
    def __unpack__(self):
        return ('a', 'b', 'c')


class TryMatchTest(unittest.TestCase):
    """Tests the try match syntax"""

    @staticmethod
    def match_function(var_to_match):
        """A match statement with various branches to test matching behavior
        """
        # Normally it would not make sense to unpack an object while matching
        # to then just repack and return, but this is the most convienent way
        # to test
        try match var_to_match:
            as tuple(a, b, c):
                e = 6
                return (a, b, c)
            as tuple(a, b):
                return (a, b)
            as tuple:
                return var_to_match
            as Dummy:
                return var_to_match
            as Dummy2:
                return var_to_match
            as Dummy3(a, b, c):
                return (a, b, c)
            as Dummy4(a, b, c, d):
                # This branch should never be reached
                return (a, b, c, d)
            as Dummy4:
                return var_to_match
            else:
                return "Hello World"

    def test_match_type(self):
        """A test to verify that absent a match branch with the correct number
        of arguments, matching happens on the defined type (tuple) 
        """
        tup = (1, 2, 3, 4)
        self.assertIs(self.match_function(tup), tup)

    def test_match_type_length(self):
        """A test to verify that the match branch with the correct type and
        number of arguments is entered
        """
        tup = (1, 2, 3)
        self.assertEqual(self.match_function(tup), tup)

        tup2 = ('a', 'b')
        self.assertEqual(self.match_function(tup2), tup2)

    def test_match_usertype(self):
        """A test to verify that the match statement will match on a user
        defined type (that __match__ is defined on all objects)
        """
        dummy = Dummy()
        self.assertIs(self.match_function(dummy), dummy)

    def test_match_custom_match(self):
        """A test to verify that the match statement will match on a user
        defined type that contains a custom __match__ method, where the
        class can define matching to any interface it chooses
        """
        test = set()
        self.assertIs(self.match_function(test), test)

    def test_match_custom_with_unpack(self):
        """A test to verify that the match statement will match on a user
        defined type that defines an __unpack__ method and unpack it into
        arguments
        """
        dummy = Dummy3()
        self.assertEqual(self.match_function(dummy), ("a", "b", "c"))

    def test_match_custom_with_unpack_args(self):
        """A test to verify that the match statement will match on a user
        defined type that defines an __unpack__, but that the branch has the
        wrong number of arguments, so the type branch is executed
        """
        dummy = Dummy4()
        self.assertIs(self.match_function(dummy), dummy)

    def test_match_else(self):
        """Test that absent a corresponding match block, else will be executed
        """
        var = list()
        self.assertEqual(self.match_function(var), "Hello World")


if __name__ == "__main__":
    unittest.main()
