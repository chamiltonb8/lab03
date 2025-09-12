import functions

def test_euclidean_distance():
    assert functions.euclidean_distance((1, 3), (7, 11)) == 10


def test_sum_ns():
    assert functions.sum_ns(9) == 1107


def test_perfect_square():
    test1 = functions.perfect_square(36) == '36 is a perfect square of 6'
    test2 = functions.perfect_square(35) == False

    assert all([test1, test2])

def test_is_palindrome():
    test1 = functions.is_palindrome('madam') == True
    test2 = functions.is_palindrome('nurses run') == True
    test3 = functions.is_palindrome('my name is Jack') == False
    assert all(([test1, test2, test3]))


def test_count_letter_types():
    s = "HELLOOO!! How are you today?"
    assert functions.count_letter_types(s) == {'upper': 8, 'lower': 13, 'space': 4}


def test_word_lengths():
    s = "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife"
    d = {1: ['a', 'a', 'a', 'a'],
         2: ['It', 'is', 'in', 'of', 'be', 'in', 'of'],
         3: ['man'],
         4: ['that', 'good', 'must', 'want', 'wife'],
         5: ['truth'],
         6: ['single'],
         7: ['fortune'],
         10: ['possession'],
         11: ['universally'],
         12: ['acknowledged']}
    
    assert functions.word_lengths(s) == d


def test_n_list():
    test1 = functions.n_list(3) == [3,
                              30,
                              33,
                              36,
                              39,
                              63,
                              93,
                              123,
                              132,
                              135,
                              138,
                              153,
                              183,
                              213,
                              231,
                              234,
                              237,
                              243,
                              273,
                              300]
    
    test2 = functions.n_list(-1)  == None
    test3 = functions.n_list(2.5) == None
    test4 = functions.n_list(10)  == None
    assert all([test1, test2, test3, test4])

def test_tens_dict():
    assert functions.tens_dict() == {100: 1.0,
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
