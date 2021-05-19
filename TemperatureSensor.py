

class TemperatureSensor:
    def __init__(self, sensor_type, sensor_name):
        self.sensor_type = sensor_type
        self.sensor_name = sensor_name

    def read_temp_sensor(self):
        f = open(self.sensor_name, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_sensor()
        temp_reading_as_string = lines[1].find('t=')
        temp_in_celsius = 0
        if temp_reading_as_string != -1:
            temp_data = lines[1][temp_reading_as_string + 2:]
            temp = float(temp_data) / 1000.0
        return temp_in_celsius
