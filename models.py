from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///users.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # kev_user = User(name='Kevin', fullname='Kevin Stradtman', nickname='Lee')
    # session.add(kev_user)
    # session.commit()

    # users = [
    #     User(name='Jim', fullname='Jim Smith', nickname='jims'),
    #     User(name='Joe', fullname='Jim Blow', nickname='jbow'),
    #     User(name='Chuck', fullname='Chuck Snider', nickname='chaz'),
    #     User(name='Allie', fullname='Allie Cross', nickname='cross'),
    #     User(name='Jill', fullname='Jill Malone', nickname='Jill'),
    # ]
    # session.add_all(users)
    # session.commit()
