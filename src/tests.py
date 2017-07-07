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

    def test_skill_is_initialized_as_unfinished(self):
        new_skill = Skill("learn agile")
        self.assertFalse(new_skill.is_done)


if __name__ == '__main__':
    unittest.main()