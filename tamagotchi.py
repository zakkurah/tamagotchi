# Tamagotchi

from random import randrange


class Pet (object):
    """A virtual pet"""
    excitement_reduce = 3
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab = ['"grrrrr"', '"hellowww"']

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]
        self.full_max = 7

    def __clock_tick(self):
        self.excitement -= 1
        self.food -= 1

    def mood(self):
        if self.food > self.food_warning and self.excitement > self.excitement_warning:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        return f"i'm {self.name}, i feel {self.mood()}."

    def teach(self, word):
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self):
        print(
            "i'm a ",
            self.animal_type,
            " named ",
            self.name,
            ".",
            "i feel ",
            self.mood(),
            " now.\n"
        )

        self.__clock_tick()

    def feed(self):
        print("**crunch** mmhhh. tanks! (♡˙︶˙♡) ")
        meal = randrange(self.food, self.full_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print(" i'm still hungry ๑•ૅㅁ•๑ ")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("i'm full")
        self.__clock_tick()

    def play(self):
        print("wooo!")
        fun = randrange(self.excitement, self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
            print("i'm bored ( ˘︹˘ ) ")
        elif self.excitement > self.excitement_max:
            self.excitement = self.excitement_max
            print("i'm happy!")
        self.__clock_tick()


def main():
    pet_name = input("what do u want to call ur tamagotchi? ")
    pet_type = input("what type of animal is ur tamagotchi? ")

    my_pet = Pet(pet_name, pet_type)

    choice = input(
        "heyhey! i'm " +
        my_pet.name +
        " and i'm new here!" +
        "\npress enter to start. "
    )

    while (choice := input("""
            ***✰ interact with ur tamagotchi ✰***

            1 - feed ur pet
            2 - talk to ur pet
            3 - teach ur pet a new word
            4 - play with ur pet
            0 - quit            
            """)) != "q":

        if choice == "0":
            print("goodbyeee!!")
        elif choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.talk()
        elif choice == "3":
            new_word = input("which word do u want to teach ur tamagotchi? ")
            my_pet.teach(new_word)
        elif choice == "4":
            my_pet.play()
        else:
            print("this isn't a valid option")


if __name__ == "__main__":
    main()
