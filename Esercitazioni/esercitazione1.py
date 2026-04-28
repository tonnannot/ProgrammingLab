class ExamException(Exception):
    pass


class MovingAverage:
    def __init__(self, window_length):
        # controllo 1, intero positivo
        if not isinstance(window_length, int) or window_length <= 0:
            raise ExamException("window_length must be a positive integer")
        self.window_length = window_length

    def compute(self, data):
        # controllo 2, lista
        if not isinstance(data, list):
            raise ExamException("data must be a list")

        # controllo 2, numeri nella lista
        for x in data:
            if not isinstance(x, (int, float)):
                raise ExamException("all elements in data must be numbers")

        # controllo 3, lunghezza lista almeno pari finestra
        if len(data) < self.window_length:
            raise ExamException("data length is smaller than window_length")

        result = []


        for i in range(len(data) - self.window_length + 1):
            window = data[i:i + self.window_length]
            avg = sum(window) / self.window_length
            result.append(avg)

        return result


moving_average = MovingAverage(2)
result = moving_average.compute([2, 4, 8, 16])
print(result)  # [3.0, 6.0, 12.0]