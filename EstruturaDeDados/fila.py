from stack import Stack

class QueueUsingStacks:
    def __init__(self):
        self.pilha1 = Stack()  
        self.pilha2 = Stack()  

    def enqueue(self, data):
        self.pilha1.push(data)

    def dequeue(self):
        if self.pilha2.is_empty():
            while not self.pilha1.is_empty():
                self.pilha2.push(self.pilha1.pop())
        return self.pilha2.pop()

    def is_empty(self):
        return self.pilha1.is_empty() and self.pilha2.is_empty()


fila = QueueUsingStacks()

fila.enqueue("Maçã")
fila.enqueue("Banana")
fila.enqueue("Pera")

print("Removido:", fila.dequeue()) 
print("Removido:", fila.dequeue()) 
print("Removido:", fila.dequeue()) 

print("Fila vazia?", fila.is_empty())
