import unittest

from src.skill import InvalidInputError, Skill
from src.user import User
from src.task import Task


class TestSkillMethods(unittest.TestCase):
    """
        Test cases for the Skill class
    """

    def test_invalid_input(self):
        bad_input = None
        with self.assertRaises(InvalidInputError):
            skill = Skill(bad_input)
        bad_input = ""
        with self.assertRaises(InvalidInputError):
            skill = Skill(bad_input)

    def test_skill_is_initialized_as_unfinished(self):
        new_skill = Skill("learn agile")
        self.assertFalse(new_skill.is_done, msg="Should have the attribute 'is_done' set to true")


class TestUserClass(unittest.TestCase):
    """
        Test cases for the User class
    """

    def setUp(self):
        self.a_user = User("Homer")

    def test_username(self):
        self.assertEqual('Homer', self.a_user.name, msg="Should have Homer as the username")

    def test_user_instance(self):
        self.assertTrue(isinstance(self.a_user, User), msg="Should be an instance of the User class")


class TestTaskClass(unittest.TestCase):
    """
        Test cases for the Task class
    """

    def setUp(self):
        self.a_task = Task()
        self.a_task.Skill_Pool.clear()
        self.a_task.add_skill("python")
        self.python_skill = Skill('python')


    def test_add_skill(self):
        self.assertEqual('python', self.a_task.Skill_Pool[0].name, msg="There should be a skill named 'python' in tasks")

    def test_studied_invalid_input(self):
        self.assertEqual('Add skill first', self.a_task.studied('Javascript'), msg="Should first add a skill before marking it as studied")

if __name__ == '__main__':
    unittest.main()