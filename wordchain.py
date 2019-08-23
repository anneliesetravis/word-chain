def words_list(filename):
    """
    Opens and reads a given file and creates a lowercase list of words from it.

    Arguments:
    :param filename: the file to be opened
    :return: a lowercase list of the words in the file
    """
    words = open(filename,'r').readlines()
    wordlist = []
    
    for word in words:
        word = word.strip()
        wordlist.append(word)
 
    return(wordlist)

                   
def longest_chain(chain, V, longest):
    """
    Recursively return the longest chain in a list of words V
    that satisfies the given chaining condition.

    Arguments:

    :param chain: the previous chain
    :param V: the list of words to be used
    :param longest: the current longest chain
    """    
    extended = False
    
    for word in V:
        
        lowercase = word.lower()

        #comparing a lowercase version of the word with the last letter in the
        #last word of the current chain
        if chain[-1][-1] == lowercase[0]:
            new_v = V.copy()
            new_v.remove(word)
            longest = longest_chain(chain + [word], new_v, longest)

            #indicates that a longer chain has been found this iteration
            extended = True
     
    if extended == False:
        if len(chain) > len(longest):
            longest = chain
    
    return longest


def find_longest(file):
    """
    Uses my longest_chain function on a file to find the longest legal chain possible.

    Arguments:

    :param file: the file containing the words to be used
    :return: the longest legal word chain from the words in the file
    
    """
    V = words_list(file)
    longest = []

    #finding the longest chain for every possible starting word in the file
    for word in V:
        chain = [word]      
        final_chain = longest_chain(chain, V, longest)
       
        if len(final_chain) > len(longest):
            longest = final_chain
    
    return longest

print("Longest word chain in animals.txt is:")
print(", ".join(find_longest("animals.txt")), "\n")
print("Longest word chain in lotr.txt is:")
print(", ".join(find_longest("lotr.txt")))




  
                
            
