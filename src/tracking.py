import numpy as np
class Tracker:
    def __init__(self):
        self.objects = {}
        self.id_count = 0
    def update(self, boxes):
        new_objects = {}
        for box in boxes:
            x, y, w, h = box
            cx = int(x + w/2)
            cy = int(y + h/2)
            new_objects[self.id_count] = (cx, cy)
            self.id_count += 1
        self.objects = new_objects
        return self.objects
