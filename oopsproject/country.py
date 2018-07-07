from operator import attrgetter

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population,self.area))


countries = [Country('in',1200,100),
                  Country('as',13200,1100),
                  Country('chi',12080,1002)]

countries.append(Country('rss',56, 567))

countries.sort(key=attrgetter('population'), reverse=True)

#print(countries[0:2])