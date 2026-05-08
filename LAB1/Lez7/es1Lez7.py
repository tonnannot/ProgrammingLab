class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            my_file = open(self.name, 'r')
        except:
            print('errore file non trovato')
        my_list = []
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1].strip()
                my_list.append([date, value])
        my_file.close()
        return my_list

    def read(self):
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

