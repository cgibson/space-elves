from model import *

class HealthBarModel (Model
):
    def __init__(self, maxHealth):
        super(HealthBarModel, self).__init__()
        self.maxHealth = maxHealth
        self.curHealth = maxHealth