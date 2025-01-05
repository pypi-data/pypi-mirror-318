# python exceptions

# LIST
# typecast error
class TypeCastError(Exception):
    pass
class ListError(Exception):
    pass

# STACK
# overflow
class StackOverFlow(Exception):
    pass
# underflow
class StackUnderFlow(Exception):
    pass
# Stack Func Err
class StackError(Exception):
    pass

# LinkedList Node
class NodeError(Exception):
    pass
class LinkedListError(Exception):
    PARAM_GT_ZERO = "{} parameter must be an integer and greater than zero."
    PARAM_NOT_ZERO_OR_LESS = "{} parameter cannot be less than zero."
    PRAM_GT_EQ_ZERO = "{} parameter must be an integer and greater than or equal to zero"
    PARAMS_NOT_NONE = "All parameters cannot be None."

class HashMapError(Exception):
    pass

class TreeError(Exception):
    pass

class QueueError(Exception):
    pass

# all
__all__ = [
    "TypeCastError",
    "ListError",
    "StackError",
    "StackOverFlow",
    "StackUnderFlow",
    "NodeError",
    "LinkedListError",
    "HashMapError",
    "TreeError",
    "QueueError",
]