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
        
    def get(self, index):
        if 0 <= index < len(self.data):
            print(self.data[index])
            
    def set(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value

    def contains(self, value):
        return value in self.data
    
    def remove_at(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
    
    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

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

lista.append(0)
print(lista)
print("Verificando se 0 existe;")
print("0 existe na lista? ", "Sim" if lista.contains(0) else "Não")

print("--------------------------------")

print(lista)
lista.remove_at(3)
print("Removendo elemento no indice 3 se existir.")
print(lista)

print("--------------------------------")

print(lista)
print("Removendo elemento 99 se existir.")
lista.remove(99)
print(lista)

print("--------------------------------")
