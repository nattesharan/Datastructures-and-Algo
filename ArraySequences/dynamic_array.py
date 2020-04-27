import ctypes

class DynamicArray(object):
    def __init__(self):
        self.number_of_elemnts = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)
    
    def __len__(self):
        return self.number_of_elemnts
    
    def __getitem__(self, index):
        if not 0 <= index < self.number_of_elemnts:
            return IndexError("Index out of bounds")
        return self.array[index]
    
    def append(self, element):
        if self.number_of_elemnts == self.capacity:
            self._resize(2*self.capacity)
        self.array[self.number_of_elemnts] = element
        self.number_of_elemnts += 1
    
    def _resize(self, new_capacity):
        temp_array = self._make_array(new_capacity)
        for i in range(self.number_of_elemnts):
            temp_array[i] = self.array[i]
        self.array = temp_array
        self.capacity = new_capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()