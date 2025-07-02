DEFAULT_CAPACITY = 10

class Node:
    """
    Nó simples para lista encadeada.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Lista encadeada simples para tratamento de colisões (chaining).
    Métodos: append (insere no início), search, remove, __str__.
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """Insere um novo nó no início da lista."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, value):
        """Retorna True se o valor existir na lista."""
        trav = self.head
        while trav:
            if trav.data == value:
                return True
            trav = trav.next
        return False

    def remove(self, value):
        """Remove o nó com o valor especificado. Retorna True se removido."""
        prev = None
        trav = self.head
        while trav:
            if trav.data == value:
                if prev:
                    prev.next = trav.next
                else:
                    self.head = trav.next
                return True
            prev = trav
            trav = trav.next
        return False

    def __str__(self):
        vals = []
        trav = self.head
        while trav:
            vals.append(str(trav.data))
            trav = trav.next
        return " -> ".join(vals) if vals else " "


class DynamicIntArray:
    """
    Array de tamanho fixo para armazenar buckets da HashTable.
    """
    def __init__(self, capacity=DEFAULT_CAPACITY):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity
        self.data = [None] * capacity

    def get(self, index):
        if index < 0 or index >= self.capacity:
            raise IndexError("Índice fora dos limites.")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.capacity:
            raise IndexError("Índice fora dos limites.")
        self.data[index] = value

    def __str__(self):
        return str([str(bucket) for bucket in self.data])


class HashTable:
    """
    Hash Table com chaining (listas encadeadas) para tratamento de colisões.
    Usa key % capacity como função de hash.
    """
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.buckets = DynamicIntArray(capacity)
        # inicialize cada bucket como LinkedList
        for i in range(capacity):
            self.buckets.set(i, LinkedList())

    def _hash(self, key):
        return key % self.buckets.capacity

    def insert(self, key):
        index = self._hash(key)
        bucket = self.buckets.get(index)
        bucket.append(key)

    def search(self, key):
        index = self._hash(key)
        bucket = self.buckets.get(index)
        if bucket.search(key):
            return index
        else:
            return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets.get(index)
        return bucket.remove(key)

    def __str__(self):
        lines = []
        for i in range(self.buckets.capacity):
            bucket = self.buckets.get(i)
            lines.append(f"{i}: {bucket}")
        return "\n".join(lines)


if __name__ == "__main__":
    ht = HashTable()

    # Inserção um a um
    ht.insert(33)
    ht.insert(14)
    ht.insert(7)
    ht.insert(73)
    ht.insert(23)

    print("Estado da Hash Table após inserções:")
    print(ht)

    # Buscas
    for key in [14, 23, 19]:
        idx = ht.search(key)
        if idx is not None:
            print(f"Buscar {key}: encontrado no índice {idx}")
        else:
            print(f"Buscar {key}: elemento não existe")

    # Remoções
    print(f"Remover 73: {'Sucesso' if ht.remove(73) else 'Falha'}")
    print(f"Remover 35: {'Sucesso' if ht.remove(35) else 'Falha'}")

    # Busca 73 após remoção
    idx73 = ht.search(73)
    if idx73 is not None:
        print(f"Buscar 73 após remoção: encontrado no índice {idx73}")
    else:
        print("Buscar 73 após remoção: elemento não existe")

    # Estado final
    print("\nEstado final da Hash Table:")
    print(ht)
