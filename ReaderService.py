
class ReaderService:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file_by_name(self):
        file = open(self.file_name, 'r')
        player_names = []
        for line in file.readlines():
            player_names.append(line.rstrip())

        file.close()

        return player_names
