from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, CHAR, VARCHAR, LargeBinary
from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column, Mapped

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    firstname: Mapped[str] 
    lastname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] 
    is_active: Mapped[bool] = mapped_column(default=False)

    #relationships
    tasks: Mapped[list["Task"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    goal: Mapped["Goal"] = relationship(back_populates="user")
    

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}(id={self.id!r}, username={self.username!r}, firstName={self.firstname!r}, lastName={self.lastname!r}, email={self.email!r}, goal={self.goal!r})"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    #relationships
    user: Mapped["User"] = relationship(back_populates="tasks") 


    def __repr__(self) -> str :
        class_name = type(self).__name__
        return f"{class_name}(id={self.id!r}, name={self.name!r}, completed={self.completed!r})"


class Goal(Base):
    __tablename__ = "goal"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    #raltionship
    user: Mapped["User"] = relationship(back_populates="goal")


    def __repr__(self) -> None:
        class_name = type(self).__name__
        return f"{class_name}(id={self.id!r}, title={self.title!r}, description={self.description!r}, startDate={self.start_date!r}, endDate={self.end_date!r}, task={self.task!r} )"
    

base_metadata = Base.metadata 