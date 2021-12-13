class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej i drzewa binarnego."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)