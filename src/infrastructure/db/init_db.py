from src.infrastructure.db import Base, engine


Base.metadata.create_all(bind=engine)




