from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    UserID = Column(Integer, primary_key=True, index=True)
    Password = Column(String, nullable=False)


class UserDetails(Base):
    __tablename__ = "userdetails"

    UserDetailsID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"))
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    DateOfBirth = Column(Date, nullable=False)
    Province = Column(String, nullable=False)
    Gender = Column(String, nullable=False)
    Facilitator = Column(Boolean, nullable=False)