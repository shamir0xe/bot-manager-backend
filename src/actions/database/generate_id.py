import ulid


class GenerateId:
    """Generate ULID"""

    @staticmethod
    def generate() -> str:
        return str(ulid.new())
