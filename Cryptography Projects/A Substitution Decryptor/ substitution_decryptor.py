
def letter_freq(mess : str, x):
    """Given a string and character, this function calulates the frequecy in which 
    the character appears in the string

    Parameters
    ----------

    mess : str 
        the message 
    x 
        a character in the latin alphabet

    Returns
    ----------
    int
        the frequency in which the character x appears in mess NOT INCLUDING WHITESPACES OR 
        WHITESPACE CHARACTERS
    

    """
    mess = mess.strip() 
    length_no_ws = len(mess.replace(" ", ""))
    x_split = mess.lower().split(x)
    num_x = len(x_split)-1
    freq = num_x/length_no_ws
    return freq

#####################################


#Contruct a list of letters in the latin alphabet (english alphabet)
eng_alphabet_str ='abcdefghijklmnopqrstuvwxyz'
eng_alphabet = list(eng_alphabet_str)

#####################################

# A list of frequencies associated to each letter in the alphabet starting from "a"
frequencies =[0.0817,0.0150,0.0278,0.0425,0.1270,
              0.0223,0.0202,0.0609,0.0697,0.0015,
              0.0077,0.0403,0.0241,0.0675,0.0751,
              0.0193,0.0010,0.0599,0.0633,0.0906,
              0.0276,0.0098,0.0236,0.0015,0.0197,
              0.0007]

#####################################

# Create a list where an element of the list is a list consisting of an english character
# as the first element and the english character's frequency in the english language as the second element.

eng_alphabet_freq = list(map(lambda i,j: [i,j], eng_alphabet, frequencies))

#####################################

# Sort the list eng_alphabet_freq by alphabetical order
def func_key(X):
    return X[1]


eng_alphabet_freq.sort(reverse = True, key = func_key)

####################################


#letters with in-message frequencies 

def letters_to_freq(mess):
    """ Returns a list of consisting of each english characters frequency in a given message

    Parametrers
    ---------------
    mess : str
        a string

    Returns
    --------------
    lst(lst) :
        a list of lists, where each sublist consists of the a character from the english alphabet and its frequency in the message
        as the first element and second element of the sublist, respectively

    """
    L = list( map( lambda i : [i, letter_freq(mess,i)], eng_alphabet))
    L.sort(reverse = True, key = func_key)
    return L


################################

def initial_possible_key(mess):
    """ Returns a dictionary representing a possible key for encryption/decryption. The possible key is obtained
     by assuming that the frequency of letters used in the english language corresponds exactly to the frequency 
     of letters used in the message. This is likely to not be the correct key. This will be used as a decryption key in that 
     each character in the message will be mapped to the characters value as given in the dictionary returned by this function.

    Parametrers
    ---------------
    mess : str
        a string

    Returns
    --------------

    dict

        returns a dictionary where each key (not in the cryptography sense) is a character in the english alphabet
        whose value is another character in the english alphabet. 
    """
    
    A = eng_alphabet_freq
    B = letters_to_freq(mess)
    L = list(map(lambda i,j : [i[0],j[0]], B, A))
    diction = {}
    for x in L:
        diction[x[0]]=x[1]
    return diction


###############################

def try_possible_key(mess,key):
    """ Given a message and a crypt key, this function returns the resulting decryption of the message
    using the give key.

    Parameters
    --------------
    mess : str
        a message

    key :
        a encryption/decryption key

    Returns
    -------------

    str
        the result of applying the given key to the given message in addition to the encrypted message for comparision.

    """
    copy_mess = mess.lower()
    possible_decript_list = []
    empty_mess = ""
    # the following process avoids changing a character twice.
    for ch in copy_mess:
        if ch in key.keys():
            possible_decript_list.append(key[ch])
        else:
            # avoids errors with /n or white space
            possible_decript_list.append(ch)
    possible_decript = empty_mess.join(possible_decript_list)
    final_string = "Encrypted Message: \n\n\n " + mess + "\n\n\n" + "Key Applied to Encrypted Message: \n\n\n" + possible_decript
    return  final_string


###############################

# A helper function to assist in making changes to a given encryption/decryption key

def transpose(bijection, a,b):
    """ Given a bijection (in the mathematical sense) represented as a dictionary.

    Parameters
    --------------
    bijection : dict
        a dictionary for which every key has a unique value 

    a,b
        a and b are objects of any desired type provided that "a" is a key in bijection

    Returns
    -------------

    dict 
        returns the dictionary obtained by enforcing the value of the key a to be b. 
        This dictionary will also represent a bijection.

    """
    #assertion to make sure that "a" is a key
    assert( a in bijection.keys())
    #assertion to make sure we start with a bijection.
    assert (len(bijection.keys()) == len(set(bijection.values())))
    for x in bijection:
        if bijection[x] != b:
            pass
        else:
            bijection[x] = bijection[a]
            bijection[a] = b
            break
    #assertion to make sure we end with a bijection
    assert (len(bijection.keys()) == len(set(bijection.values())))
    return bijection
        
####################################

def old_to_new_key(old_key,new_pairs):
    """ Given an old encryption/decryption key and desired changes to be made to the old key, this function
    return a new encryption/decryption key with the desired changes made to the old key. 

    Parameters
    ---------------

    old_key : dict
        the old encrpytion/decryption key which represents a bijection

    new_pairs : dict
        desired changes to be made to the old key. For example if "a : c" is a key-value pair in old_key, if "{a : d}" is 
        new_pairs, then this represents the desire to map a to d rather than a to c

    Returns
    ---------------
    dict

        returns a new encryption/decryption key in the form of a dictionary, where in this new dictionary 
        any key-value pair in new_pairs replaces the corresponding key-value (same key) in old_pair in such a way
        that the resulting dictionary still represents a bijection.
        
    """
    new_pairs_list = new_pairs.items()
    for x in new_pairs_list:
        transpose(old_key, x[0],x[1])
    return old_key

