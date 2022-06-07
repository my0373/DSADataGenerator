import random
from datetime import datetime, timedelta
import yaml
# from pprint import pprint
from dateutil.relativedelta import relativedelta


class DSADataGen():
    """

    """

    def __init__(self,
                 maleNameFile='./datasets/malenames.txt',
                 femaleNameFile='./datasets/femalenames.txt',
                 familyNameFile='./datasets/familynames.txt',
                 countryFile='./datasets/countries.yaml',
                 eventsFile='./datasets/events.txt'):

        self.familyname = ""
        self.eventsFile = eventsFile

        # Male names
        self.maleNameFile = maleNameFile
        self.maleNames = self._readfile(self.maleNameFile)

        # Female names
        self.femaleNameFile = femaleNameFile
        self.femaleNames = self._readfile(self.femaleNameFile)

        # family names
        self.familyNameFile = familyNameFile
        self.familyNames = self._readfile(self.familyNameFile)

        # countries names
        self.countryFile = countryFile
        self.countries = self._loadYaml(self.countryFile)

    def _readfile(self, filename):
        """
        A worker function to read a plain list of parameters and
        return them lowercase and stripped of trailing whitespace.
        """
        with open(filename, mode='r') as fh:
            return list({line.strip().lower() for line in fh.readlines() if line.strip().lower()})

    def getRandomCountry(self):
        self.country = random.choice(list(self.countries["countries"]))
        return self.country

    def getRandomRegion(self):

        self.county = random.choice(
            list(self.countries["countries"][self.country]["regions"]))
        return self.county

    def getEvents(self):

        self.events = {}
        for event in self._readfile(self.eventsFile):
            self.events[event] = random.randint(0, 1)

        return self.events

    def getRandomSex(self):
        return self._genSex()

    def getRandomCategory(self, min=1, max=3):
        self.min = min
        self.max = max
        return self._genCategory(self.min, self.max)

    def _genCategory(self, start, end):
        """
        Generate a category.
        """

        return random.randint(start, end)

    def _genSex(self):
        """
        Generate "m" or "f" based on a random integer.
        """

        if not random.randint(0, 1):
            return "m"
        else:
            return "f"

    def getRandomDOB(self, min_age=700, max_age=18250):
        """
        Generate a date of birth
        TODO: Update this code to use years rather than days.
        """
        self.min_age = min_age
        self.max_age = max_age
        self.dob = self._getDateOfBirth(self.min_age, self.max_age)

        return self.dob

    def _getDateOfBirth(self, min_age, max_age):
        days_to_subtract = random.randint(min_age, max_age)
        dob = datetime.now() - timedelta(days=days_to_subtract)
        return dob.date()

    def _loadYaml(self, filename):
        with open(filename, "r") as stream:
            return(yaml.safe_load(stream))

    def getRandomForename(self, sex):
        if sex == "m":
            return random.choice(list(self.maleNames))
        else:
            return random.choice(list(self.femaleNames))

    def getAge(self, dob):

        rdob = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        delta = today - rdob
        rdelta = relativedelta(today, rdob)
        return rdelta.years

    def getRandomFamilyName(self):
        fn = random.choice(list(self.familyNames))
        return fn

    def getRandomAthlete(self):
        self.athlete = {}
        self.sex = self.getRandomSex()
        self.forename = self.getRandomForename(self.sex)
        self.familyname = self.getRandomFamilyName()
        self.athlete["name"] = "{} {}".format(self.forename, self.familyname)
        self.athlete["sex"] = self.sex
        self.athlete["dob"] = self.getRandomDOB().isoformat()
        self.athlete["age"] = self.getAge(self.athlete["dob"])
        self.athlete["category"] = self.getRandomCategory()
        self.athlete["country"] = self.getRandomCountry()
        self.athlete["region"] = self.getRandomRegion()
        self.athlete.update(self.getEvents())

        return self.athlete

    def getAthletes(self, numathletes=200):

        self.athletes = {}
        headers = self.getRandomAthlete()
        for header in headers.keys():
            self.athletes[header] = []

        for x in range(0, numathletes):
            athlete = self.getRandomAthlete()
            for column, value in athlete.items():
                self.athletes[column].append(value)

        return self.athletes


class DSADataToken():
    pass
