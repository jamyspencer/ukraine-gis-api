from server.model.railroad import Railroad
from server.data.util import DatabaseSession
from sqlalchemy import select
def get_all_railroads():
    session = DatabaseSession()
    result = session.scalars(select(Railroad))
    return result.all()