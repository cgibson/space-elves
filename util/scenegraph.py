
class SceneGraph (object):

    def __init__(self):
        self.root = None

    def initControllers(self):
        pass

    def raycast(self, view, pos):

        intersections = []

        if view.cursorInteract and view.inBounds(pos):
            intersections.append(view)

            for child in view.children:
                result = self.raycast(child, pos)
                if result:
                    intersections.append(result)

            return intersections[-1]

        return None
