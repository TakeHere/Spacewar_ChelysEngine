from abc import ABC, abstractmethod


class Component:

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def destroy(self):
        pass