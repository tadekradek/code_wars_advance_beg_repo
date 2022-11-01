"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False


"""
#mysolution
#good solution, but with bad performance, so forced to do better

def scramble(s1, s2):
    s1_set = s1
    counter = 0
    for i in s2:
        if i in s1_set:
            s1_set = s1_set.replace(i,"",1)
            print(s1_set)
            counter += 1
            continue

    if counter == len(s2):
        return True
    else:
        return False

# mysolution          
# another good solution, but still inefficient
def scramble(s1,s2):
    return all([True if s1.count(i)>= s2.count(i) else False for i in s2])

# mysolution
# another solution, passed in the page
def scramble(s1,s2):
    word_dict_2 = {key: s2.count(key) for key in set(s2)}
    word_dict_1 = {key: s1.count(key) for key in set(s1)}
    print(word_dict_1)
    print(word_dict_2)
    return all(True if i in word_dict_1.keys() and word_dict_1.get(i) >= word_dict_2.get(i) else False for i in word_dict_2.keys())




#another solutions
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))



