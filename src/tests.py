import unittest

from src.skill import InvalidInputError, Skill


class TestSkillMethods(unittest.TestCase):

    def test_invalid_input(self):
        bad_input = None
        with self.assertRaises(InvalidInputError):
            skill = Skill(bad_input)
        bad_input = ""
        with self.assertRaises(InvalidInputError):
            skill = Skill(bad_input)


if __name__ == '__main__':
    unittest.main()