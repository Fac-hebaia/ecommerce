class SerializerMixin:
    def to_dict(self):
        data = {}
        for column in self.__table__.columns: # type: ignore
            data[column.name] = getattr(self, column.name)
        return data
