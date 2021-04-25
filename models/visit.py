class Visit:

    def __init__(self, goal, system, planet, achieved = False, id  = None):
        self.goal = goal
        self.system = system
        self.achieved = achieved
        self.id = id

    def mark_achieved(self):
        self.completed = True