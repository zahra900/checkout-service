from src.infrastructure.db.database import Base, engine
from src.infrastructure.db import models

def init_db():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)

if __name__=="__main__":
  init_db()




