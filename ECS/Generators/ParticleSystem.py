import random

from ECS.Deleters.DeletionTimer import DeletionTimer
from ECS.Entity import Entity
from ECS.Physics.RigidBody import RigidBody
from ECS.Renderable.DisplacedCircle import DisplacedCircle
from Utils import MathUtils


class ParticleSystem():
    def __init__(self, position, renderable, amount, life_time, has_gravity, min_force, max_force):
        self.position = position
        self.renderable = renderable
        self.life_time = life_time
        self.has_gravity = has_gravity
        self.min_force = min_force
        self.max_force = max_force
        self.amount = amount

    def generate(self):
        particles_generated = []

        for i in range(self.amount):
            rigidbody = RigidBody(self.has_gravity)
            particle = Entity("particle", self.position, 0)

            particle.add_component(rigidbody)
            if isinstance(self.renderable, DisplacedCircle):
                particle.add_component(DisplacedCircle(self.renderable.pivotpoint_offset, self.renderable.color,
                                                       self.renderable.radius, self.renderable.displacement_factor,
                                                       self.renderable.num_points))
            else:
                particle.add_component(self.renderable)
            particle.add_component(DeletionTimer(self.life_time))
            rigidbody.velocity = MathUtils.random_direction().multiply(random.uniform(self.min_force, self.max_force))

            particles_generated.append(particle)

