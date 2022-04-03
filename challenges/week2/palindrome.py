import re


class Palindrome:
    # this is the palindrome initializer method
    def __init__(self, candidate):
        # input values
        self._candidate = candidate  # input string
        self._length = len(candidate)  # input length
        # analysis values
        self._is_a_palindrome = False  # initialize status
        self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  # alpha numeric characters
        self._analysis = []  # array of tests
        self._tests = 0  # counter of tests performed
        # evaluate for palindrome
        self.is_palindrome()

    # this is the palindrome tester method
    def is_palindrome(self):
        c = self._az09
        # Run loop from 0 to len/2 of string (middle is exit point)
        tests = int(len(c) / 2)
        for i in range(0, tests):
            front = c[i];
            back = c[len(c) - i - 1]
            if front.lower() == back.lower():
                self.logger(front, back, True)
                self._tests += 1
            else:
                self.logger(front, back, False)
                return
        self._is_a_palindrome = True
        return

    # this is palindrome logging
    def logger(self, front, back, result):
        self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

    # these are the getters
    @property
    def candidate(self):
        return self._candidate

    @property
    def tests(self):
        return self._tests

    @property
    def isPalindrome(self):
        return self._is_a_palindrome

    @property
    def analysis(self):
        return self._analysis

#Palindrome Tester code, 3 words at time
def driver():
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")
    word3 = input("Enter another another word: ")
    ls = [Palindrome(word1), Palindrome(word2), Palindrome(word3)]

    for l in ls:
        print(l.candidate, l.isPalindrome, l.tests, l.analysis)


# Tester Code (initial referencing fibonacci code
#if __name__ == "__main__":
 #   '''Value for testing'''
  #  candidate = "racecar"
   # '''Constructor of Class object'''
    #Palindrome = Palindrome(candidate)

    #'''Using getters to obtain data from object'''
    #print(f"The word is {candidate}")
    #print(f"Is a palindrome?: {Palindrome._is_a_palindrome}")
    #print(f"{Palindrome.analysis}")


