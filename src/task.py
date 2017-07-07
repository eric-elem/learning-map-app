from src.skill import Skill


class Task(object):

    def __init__(self):

        self.Skill_Pool = []
        self.skills = {'Not studied': [], 'Studied': []}


    def add_skill(self, skill):
        if isinstance(skill, str):
            self.Skill_Pool.append(Skill(skill))
            return 'Skill added'


    def view_skills(self):
        skill_str = ""
        for i, skill in enumerate(self.Skill_Pool):
            skill_str +=  "\n" + str(i+1) + ". " + skill.name

        return skill_str




    def studied(self, skill):
        if skill not in self.Skill_Pool:
            return 'Add skill first'
        else:
            self.skills['Studied'].append(skill)


    def not_studied(self, skill):
        if skill not in self.Skill_Pool:
            return 'Add a skill'
        else:
            self.skills['Not yet studied'].append(skill)


    def view_studied_skill(self):
        return self.skills['You have studied this skill']


    def view_not_studied(self):
        return self.skills['Not yet studied this skill']

    def progress_bar(self):

        skills_finished = sum([skill.is_done for skill in self.Skill_Pool])
        number_of_skills_added = len(self.Skill_Pool)
        progress = skills_finished // number_of_skills_added
        stars_to_print = progress * 20
        progress_str = "[{done}{not_done}] {percent}%".format(done="#"*stars_to_print,
                                                            not_done=" "*(20-stars_to_print),
                                                            percent=progress*100)
        return progress_str




if __name__ == "__main__":
    n = Task()
    n.add_skill("python")
    n.add_skill("agile")
    print(n.view_skills())