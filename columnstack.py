
class Piece:
    def __init__(self, value):
        self.value = value
        self.next = None

class ColumnStack:
    def __init__(self):
        self.top = None
        self.length = 0
        self.maxlength = 7

    def push_piece(self,value):
        new_piece = Piece(value)
        if self.length == 0:
            self.head = new_piece
            self.tail = new_piece
            self.length +=1

        else:
            self.tail.next = new_piece
            self.tail = new_piece
            self.length += 1

    def pop_piece(self):
        if self.length < 2:
            self.head = None
            self.tail = None
            self.length = 0

        else:
          current = self.head

          while current.next != self.tail:
            current = current.next
          self.tail = current
          current.next = None
          self.length -=1

