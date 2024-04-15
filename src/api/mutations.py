import strawberry


@strawberry.type
class Mutation:
    @strawberry.field
    def login(self) -> None:
        pass
