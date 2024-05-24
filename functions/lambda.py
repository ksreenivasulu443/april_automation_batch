
# map(function, iterable)
#
# def square(x):
#     return x**2
# numbers=[1,2,3,4,5]
# squared_numbers=list(map(square,numbers))
# print(squared_numbers)
#
# squared_nums=list(map(lambda x:x**2,numbers))
# print(squared_nums)

from itertools import chain

def flatmap(func, iterable):
    return chain.from_iterable(map(func, iterable))

# Example usage
def split_words(sentence):
    return sentence.split()

sentences = ["Hello world", "Python is awesome"]

# Applying flatmap to split words in each sentence and flatten the result
words = list(flatmap(split_words, sentences))
print(words)  # Output: ['Hello', 'world', 'Python', 'is', 'awesome']
