
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self,prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
    
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        input_prompt = """
                    {name} has ${prizeMoney}
                    Category: {category}
                    Phrase:  {obscured_phrase}
                    Guessed: {guessed}
            Guess a letter, phrase, or type 'exit' or 'pass':
        """.format(name=self.name, prizeMoney=self.prizeMoney,
                   category=category,obscured_phrase=obscuredPhrase,
                   guessed=guessed)
        
        response = input(input_prompt)       
        return response
        
            
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty
        
    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        if rand_number > self.difficulty:
            return False
        else:
            return True
    
    def getPossibleLetters(self, guessed):   
        if self.prizeMoney >= 250:
            return list(set(LETTERS).difference(set(guessed)))
        else:
            return list(set(LETTERS).difference(set(VOWELS)).difference(set(guessed)))
    
    def getMove(self, category, obscuredPhrase, guessed):
        lst = self.getPossibleLetters(guessed)
        if len(lst) == 0:
            return 'pass'
        else:
            if self.smartCoinFlip():
                for l in self.SORTED_FREQUENCIES:
                    if l in lst:
                        return l
            else:
                return random.choice(lst)
    
    

