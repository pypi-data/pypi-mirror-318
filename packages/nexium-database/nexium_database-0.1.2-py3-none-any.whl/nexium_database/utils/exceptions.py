class NexiumDatabaseError(Exception):
    pass


class ModelDoesNotExist(NexiumDatabaseError):
    pass
