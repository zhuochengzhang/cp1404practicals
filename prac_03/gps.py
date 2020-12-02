from random import randrange


def main():
    population = 1000
    year = 10
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population:  {population}")
    for _ in range(year):
        print(f"Year {year}\n")
        population = simulate(population)


def simulate(population):
    born = int(population * (randrange(1, 2) / 10))
    die = int(population * (randrange(5, 25) / 100))
    population = population + born - die
    print(f"{born} gophers were born. {die} died.")
    print(f"Population: {population}")
    return population


if __name__ == '__main__':
    main()
