from mycroft import MycroftSkill, intent_file_handler


class Launch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('launch.intent')
    def handle_launch(self, message):
        self.speak_dialog('launch')


def create_skill():
    return Launch()

