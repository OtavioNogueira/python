class DynamicIntArray:
    def __init__(self, capacity=2):
        if capacity<=0:
            raise ValueError("Capacidade inicial tem que ser maior do que zero")
        self.capacity = capacity
        self.size = 0 
        self.data = [0] * self.capacity
        
    def is_empty(self):
        if self.size==0:
            return 1
        
    def get(self, value):
        print(self.data[value])
        
    def set(self, indc, value):
        self.data[indc] = value
        
    def append(self, value):
        if self.size == self.capacity:
            self._resize_up(2 * self.capacity)
            
        self.data[self.size] = value
        self.size += 1
        
    def _resize_up(self, new_capacity):
        print(f"Aumentando a capacidade {self.capacity} para {new_capacity}")
        new_data = [0] * new_capacity
        
        for i in range(self.size):
            new_data[i] = self.data[i]
            
        self.data = new_data
        self.capacity = new_capacity
        
    def __str__(self):
        return str(self.data[:self.size])
        
lista = DynamicIntArray()

print(lista)

if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")
    
print("--------------------------------")

lista.append(10)
lista.append(20)
lista.append(30)

print(lista)

print("--------------------------------")

print("Elemento na posição 2: ") 
lista.get(2)

print("--------------------------------")

print(lista)
print("Trocando elemento no índice 2 para 99.")  
lista.set(2, 99)
print(lista)

print("--------------------------------")
