
class Piece:
    def __init__(self, value):
        self.value = value
        self.next = None

class ColumnStack:
    def __init__(self):
        self.top = None
        self.length = 0
        self.maxlength = 7

    def push_piece(self, value):
        if self.length < self.maxlength:
            new_piece = Piece(value)
            new_piece.next = self.top
            self.top = new_piece
            self.length += 1
        else:
            raise Exception("Column is full")

    def pop_piece(self):
        if self.top is not None:
            self.top = self.top.next
            self.length -= 1
        else:
            raise ValueError("Column is empty")

    def length(self):
        return self.length

    def is_full(self):
        return self.length >= self.maxlength

    def peek(self):
        if self.top != None:
            return self.top
        else: return None

