class ProgrammingLanguage:
    def __init__(self, language_name="", typing="", reflection=False, year=0):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.language_name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False



