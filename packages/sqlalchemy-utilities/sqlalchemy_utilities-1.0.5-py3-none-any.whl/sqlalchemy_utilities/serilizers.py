class ModelSerializer:
    fields = ["__all__"]

    def __init__(self, connection, data, fields=None, context=None):
        self.connection = connection
        self.model = data
        self.data = []
        self.context = context
        if fields is not None:
            self.fields = fields

    async def serialize(self):
        for item in self.model:
            i = {}
            if "__all__" in self.fields:
                keys = item.__table__.columns.keys()
                for key in keys:
                    if hasattr(item, key):
                        i[key] = getattr(item, key)
            else:
                for field in self.fields:
                    if hasattr(item, field):
                        i[field] = getattr(item, field)
                    else:
                        if not hasattr(self, f"get_{field}"):
                            raise NotImplementedError(f"get_{field} method is not implemented")
                        method = getattr(self, f"get_{field}")
                        i[field] = await method(item=item)
            self.data.append(i)
        return self
