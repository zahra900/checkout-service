class DomainError(Exception):
    """Base domain exception."""
    pass


class OrderNotFoundError(DomainError):
    pass


class DuplicateOrderError(DomainError):
    pass


class OptimisticLockError(DomainError):
    pass
