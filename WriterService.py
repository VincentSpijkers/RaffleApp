from ReaderService import ReaderService


class WriterService:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, file, data_list):
        for item in data_list:
            file.write(item + "\n")

    def reset_player(self, player_name, players):
        open(self.file_name, 'w').close()
        file = open(self.file_name, 'a')

        filtered_player_list = [i for i in players if i != player_name]

        reader = ReaderService('participants.txt')

        original_pool = reader.read_file_by_name()

        self.write_to_file(file, original_pool)
        self.write_to_file(file, filtered_player_list)
