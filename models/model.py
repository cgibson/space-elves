
class Model (object):

    _current_id = 0

    def __init__(self):
        _id = Model._current_id
        Model._current_id += 1