#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):

    data = data.lower()
    data = data.split()
    data_set = set(data)
    word_dict = {}
    max_list = []
    
    for i in data_set:
        no_of_items = data.count(i)
        word_dict.update({i : no_of_items})

    maximum = max(word_dict.values())
    for i in word_dict.keys():
        if(word_dict.get(i) == maximum):
            max_list.append(i)

    print(max(max_list, key=len), word_dict[max(max_list, key=len)] )
    #Populate the variables: word and frequency

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)

#Provide different values for data and test your program.
data="WORLD welco welco world leave"
max_frequency_word_counter(data)