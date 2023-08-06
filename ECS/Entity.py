from ECS.Component import Component

_entities = []


def list_entities():
    return _entities


def get_entities_named(name):
    return_entities = []

    for entity in _entities:
        if entity.name.casefold() == name.casefold():
            return_entities.append(entity)
    return return_entities


class Entity:

    def __init__(self, name, position, rotation):
        self.name = name
        self.position = position
        self.rotation = rotation
        self._components = []
        _entities.append(self)

    def add_component(self, component):
        if isinstance(component, Component):
            self._components.append(component)
        else:
            print("ERROR WHILE ADDING COMPONENT - The component parameter was not passed a component")

    def remove_component(self, component_class):
        for component in self._components:
            if isinstance(component, component_class):
                component.destroy()
                return

        print("ERROR WHILE REMOVING COMPONENT - No component of this class found")

    def update_components(self):
        for component in self._components:
            component.update()

    def list_components(self):
        return self._components

    def has_component(self, component):
        for currentComponent in self._components:
            if isinstance(currentComponent, component):
                return True

        return False

    def get_component(self, component):
        for currentComponent in self._components:
            if isinstance(currentComponent, component):
                return currentComponent

        print("ERROR WHILE GETTING COMPONENT - The entity does not have the component queried")

    def destroy(self):
        for component in self._components:
            component.destroy()
            self._components.remove(component)

        self._components.clear()
