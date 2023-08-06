import time

from ECS.Component import Component


class DeletionTimer(Component):
    def __init__(self, life_time):
        self.life_time = life_time
        self.start_time = time.time()

    def update(self, entity):
        elapsed_time = time.time() - self.start_time

        if elapsed_time >= self.life_time:
            entity.destroy()

    def destroy(self):
        pass
