class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory



    def get_cpu(self):
        return self.__cpu

    def set_age(self, cpu):
        if type(cpu) == int and cpu > 0:
            self.__cpu = cpu
        else:
            raise ValueError('age must be positive number')



    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory


    def make_computers(self):
        return self.__cpu + self.__memory

    # @property
    # def cpu(self):
    #     return self.__cpu
    #
    # @cpu.setter
    # def cpu(self, value):
    #     self.__cpu = value
    #
    #
    # @property
    # def memory(self):
    #     return self.__memory
    #
    # @memory.setter
    # def memory(self, value):
    #     self.__memory = value

def __str__(self):
    return self.__cpu, self.__memory

class Telephone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    def get_sim_card_list(self):
        return self.__sim_card_list

    def set_sim_card_list(self, sim_card_list):
        self.__sim_card_list = sim_card_list


    def call(self, sim_card_number, call_to_number):
        print(f'We are calling to the number {call_to_number} from the sim card N{sim_card_number}')

    def __str__(self):
        return f'Sim Card list: {self.__sim_card_list}'
class SmartPhone(Computer, Telephone):

    def use_gps(self, location):
        print(f'rout to {location}')




















