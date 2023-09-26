from server.model.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry


class Railroad(Base):
    __tablename__='railroads'
    __table_args__ = {'schema': 'ukraine'}
    gid = Column(Integer, primary_key=True)
    fid = Column(Integer)
    fid_rail_d = Column(Integer)
    f_code_des = Column(Integer)
    exs_descri = Column(String)

    geom = Column(Geometry('MULTILINESTRING'))



    