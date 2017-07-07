class Skill(object):
    """Class for skills of User"""

    def __init__(self, skill_name):
        """
        Takes in skill name

        :param skill_name: name of skill
        :type skill_name: str
        """
        if skill_name is None or skill_name == "":
            raise InvalidInputError("Please enter valid input!")

        self.name = skill_name
        self.is_done = False

    def finished(self):
        """
        Make skill as finished

        :return: None
        """

        self.is_done = True

    def un_finish(self):
        """
        Mark skill as not finished

        :return: None
        """

        self.is_done = False

class SkillErrors(Exception):
    def __init__(self, message):
        self.message = message

class InvalidInputError(SkillErrors):
    pass
