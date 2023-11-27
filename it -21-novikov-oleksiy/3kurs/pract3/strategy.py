# Інтерфейс стратегії
class SortStrategy:
    def sort(self, data):
        pass

# Конкретна стратегія 1: Сортування за зростанням
class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Сортування за зростанням")
        return sorted(data)

# Конкретна стратегія 2: Сортування за спаданням
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Сортування за спаданням")
        return sorted(data, reverse=True)

# Контекст
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

# Використання патерну Стратегія
if __name__ == "__main__":
    data = [5, 2, 8, 1, 9, 3]

    bubble_sorter = Sorter(BubbleSort())
    sorted_data1 = bubble_sorter.sort_data(data)
    print("Відсортовані дані (за зростанням):", sorted_data1)

    quick_sorter = Sorter(QuickSort())
    sorted_data2 = quick_sorter.sort_data(data)
    print("Відсортовані дані (за спаданням):", sorted_data2)
