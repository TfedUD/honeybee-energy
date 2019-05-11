from honeybee.properties import Properties
from honeybee.writer import Writer
from honeybee.facetype import Wall
from .properties import EnergyProperties
from .constructionlib import generic_wall
from .faceutil import face_to_idf


# TODO: Add default construction type for all types.
Wall.energy_construction = property(lambda self: generic_wall)

# add energy properties to Properties class
Properties.energy =  property(lambda self: EnergyProperties(self.face_type))

# add energy writer to idf
Writer.energy = face_to_idf