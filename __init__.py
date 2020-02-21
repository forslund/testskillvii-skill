from mycroft import MycroftSkill, intent_file_handler


class Testskillvii(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testskillvii.intent')
    def handle_testskillvii(self, message):
        self.speak_dialog('testskillvii')


def create_skill():
    return Testskillvii()

