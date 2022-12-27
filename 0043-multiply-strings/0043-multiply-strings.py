class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dictionary = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        num1_iterator = 0
        num2_iterator = 0
        for iterator in num1:
            num1_iterator = 10*num1_iterator+dictionary[iterator]
        for iterator in num2:
            num2_iterator = 10*num2_iterator+dictionary[iterator]
        return str(num1_iterator*num2_iterator)