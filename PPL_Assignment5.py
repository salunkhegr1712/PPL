class animals:
    
    def __init__(x,legs=4,eyes=2,tail=1):
        x.legs=legs
        x.eyes=eyes
        x.tail=tail

class wild_animals(animals):

    def place(x):
        print("Jungle")

class domestic_animals(animals):
   
    def place(x):
        print(("Area near human habbitat"))

class carnivores(wild_animals):
   
    def meal(x):
        print("meat")

class herbivores(wild_animals):

    def meal(x):
        print("Vegetarian Food")

class tiger(carnivores):

    def speak(x):

        print("Roar")

    def colour(x):

        print("Orange")

    def class_type(x):
        printf("Mammalia")

class lion(carnivores):

    def speak(x):

        print("Roar")

    def colour(x):

        print("Yellow")

    def class_type(x):
        print("Mammalia")

class cheetah(carnivores):
    
    def speak(x):
        print("purs")

    def colour(x):
        printf("Goldish Yellow")

    def class_type(x):
        print("Mammalia")


class hyena(carnivores):

    def speak(x):

        print("laugh")

    def colour(x):

        print("Grey")

    def class_type(x):
    
        print("Mammalia")

class deer(herbivores):

    def speak(x):

        print("click")

    def colour(x):

        print("Brown")
   
    def class_type(x):
        print("Mammalia")

class elephant(herbivores):

    def speak(x):

        print("trumpet")

    def colour(x):

        print("Grey")
    
    def class_type(x):
       
        print("Mammalia")

class zebra(herbivores):

    def speak(x):

        print("bray")

    def colour(x):

        print("Black and white")
            
    def class_type(x):

        print("Mammalia")


Maximum = hyena()

Maximum.speak()


Maximum.class_type()

Maximum.place()

Maximum.colour()

print(Maximum.eyes)

print(Maximum.legs)

print(Maximum.tail)




