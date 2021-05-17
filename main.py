from RaffleService import RaffleService
from ReaderService import ReaderService


class Main:
    def __init__(self):
        self.reader_service = ReaderService('raffle_pool.txt')
        self.raffle_service = RaffleService('raffle_pool.txt')

    def application_loop(self):
        while(True):
            print("Welkom bij RaffleZeit! Kies een van de opties:")
            print("Kies 1 voor een Raffle!")
            print("Kies 2 voor inzien van een Raffle kans")
            print("Kies 3 voor inzien hoevaak je in de pot zit")
            print("Kies 4 om af te sluiten")

            user_input = input("Geef een keuze op: ")
            if user_input == "1":
                self.handle_raffle()
            if user_input == "2":
                self.handle_raffle_chances()
            if user_input == "3":
                self.handle_raffle_amount()
            if user_input == "4":
                    return False

            print("------------------------ \n \n")

    def handle_raffle(self):
        print("De lucky winnaar is....")
        print(self.raffle_service.handle_raffle(self.reader_service.read_file_by_name()))

    def handle_raffle_chances(self):
        player_name = input("Wat is jouw spelers naam?")
        raffle_chance = self.raffle_service.raffle_chance(player_name, self.reader_service.read_file_by_name())
        print("Jouw kans om gekozen te worden is " + str(raffle_chance) + "%")

    def handle_raffle_amount(self):
        player_name = input("Wat is jouw spelers naam?")
        raffle_amount = self.raffle_service.raffle_amount(player_name, self.reader_service.read_file_by_name())
        print(player_name + " zit " + str(raffle_amount) + " keer in de pool")


if __name__ == '__main__':
    main = Main()
    main.application_loop()

