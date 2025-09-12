[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZDVj26Jg)
# Python Basics Practice

It is okay to look up help for parts of these problems (e.g., how to I determine if a letter is upper or lower case?).
If an outside source is used, please include the reference. The purpose of these exercises is for your review and learning,
please do not look up entire solutions! For this lab, DO NO USE ANY AI TOOLS! (E.g., ChatGPT, Copilot, etc.)

# Submission:

Include all functions in the functions.py file. Commit to your repository to submit.

---
## Python review questions.

**1.  Write a Python function called *euclidean_distance* that will compute the Euclidean distance between any two points.  The function should accept as input two tuples in the form of ((x<sub>1</sub>, y<sub>1</sub>),(x<sub>2</sub>, y<sub>2</sub>)) and return the Euclidean distance.**

*Example output:*

```
In [1]: euclidean_distance((1,3),(7,11))
out[1]: 10
```

-----
**2. Write a Python function called *sum_ns* that computes the value of ``n + nn + nnn`` where ``n`` is an integer.  For example if,  ``n=2``, the function should return ``246`` (which is the sum of 2+22+222).  Ensure that the only valid inputs are integers between 0-9.**  

*Example output:*

```
In [1]: sum_ns(2)
Out[1]: 246
```

-----
**3. Write a Python function called *perfect_square* that determines if ``n`` is a perfect square, where ``n`` is an integer.  The function return either "False" or "n is a perfect square of x"  (where ``n`` and ``x`` are appropriate for the input).**

*Example output:*

```
In [1]: perfect_square(24)
Out[1]: False

In [2]: perfect_square(25)
Out[2]: 25 is a perfect square of 5
```

----
**4. Write a Python function called *is_palindrome* that checks whether a string is a palindrome or not (ignoring spacs). A palindrome is a word or phrase that reads the same forwards and backwards, such as "madam" or "nurses run".**

*Example output:*

```
In [1]: is_palindrome('madam')
Out[1]: True

In [2]: is_palindrome('nurses run')
Out[2]: True

In [3]: is_palindrome('starlight')
Out[3]: False
```

----
**5. Write a Python function called *count_letter_types* that accepts a string and calculates the number of upper case letters, the number of lower case letters, and the number of spaces (ignoring other punctionation).  The function should return a dictionary where the keys are "upper", "lower", and "space" and the value is the number of occurences.  See the example output below.**    
(Hint:  check out what methods are available for strings.)  

 *Example output:*

```
In [1]: count_letter_types("HELLO!! How are you today?")
Out[1]: {'upper': 6, 'lower': 13, 'space': 4}

```


----
**6. Write a Python function called *word_length* that accepts a string and returns a dictionary where the key word is a word length and the value is a list of all the words that are that word length.  See the example output below.**  

*Example output: (note, it's okay if the keys of your dictionary are in a different order)*

```
In [1]: s = "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife"

In [2]: word_lengths(s)

Out[2]: {1: ['a', 'a', 'a', 'a'],
         2: ['It', 'is', 'in', 'of', 'be', 'in', 'of'],
         3: ['man'],
         4: ['that', 'good', 'must', 'want', 'wife'],
         5: ['truth'],
         6: ['single'],
         7: ['fortune'],
         10: ['possession'],
         11: ['universally'],
         12: ['acknowledged']}
```


----
**7.  Write a python function called *n_list* that accepts an integer `n` (where 2 $\le$ `n` $\le$ 9) and returns a list of all the numbers between 0 and `n`00 that have an `n` in them AND are divisible by `n`. If the input is invalid, the function should print "Invalid input: enter an integer between 2 and 9"" and return None**  

```
In [1]: n_list(3)
Out[1]: [0,
         3,
         30,
         33,
         36,
         39,
         63,
         ...
         300]

In [2]: n_list(10)
Out[2]: None
```



----
**8.  Use a *dictionary comprehension* to create a dictionary where the keys are the numbers between 100 and 200 (inclusive) that are divisible by 10 and the value associated with each key is the key divided by 100. Wrap the dictionary comprehension in a function called *tens_dict* which doesn't take any arguments.**

*Desired result*
```
In [1]: tens_dict()
Out[1]: {100: 1.0,
         110: 1.1,
         120: 1.2,
         130: 1.3,
         140: 1.4,
         150: 1.5,
         160: 1.6,
         170: 1.7,
         180: 1.8,
         190: 1.9,
         200: 2.0}
 ```



