Skill_Pool = []
skills = {'Not studied': [], 'Studied': []}


def add_skill(skill):
    if isinstance(skill, str):
        Skill_Pool.append(skill)
        return 'Skill added'


def view_skills():
    return Skill_Pool


def studied(skill):
    if skill not in Skill_Pool:
        return 'Add skill first'
    else:
        skills['Studied'].append(skill)


def not_studied(skill):
    if skill not in Skill_Pool:
        return 'Add a skill'
    else:
        skills['Not yet studied'].append(skill)


def view_studied_skill():
    return skills['You have studied this skill']


def view_not_studied():
    return skills['Not yet studied this skill']
