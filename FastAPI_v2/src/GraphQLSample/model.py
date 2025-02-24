import strawberry


@strawberry.type
class User:
    id: int
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        print(self)
        return User(id=2, name="Patrick", age=100)
