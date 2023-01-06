#______________________________________________________________________________________________________________

def word_freq(fname):
    fp = open(fname, "r")
    counts = {}
    for line in fp:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] +=1
            else:
                counts[word] = 1
    fp.close()
    return counts


#______________________________________________________________________________________________________________
def convert_morse(hidden):
    morse_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}
    hidden = hidden.upper()
    coded_message = ""
    message = hidden.split()
    for word in message:
        for letter in word:
            coded_message = coded_message + morse_dictionary[letter] + " "

    return coded_message




#______________________________________________________________________________________________________________



costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}





def cheapest_costs(costs, origin, destination):
    list_of_prices = [float("inf")]
    for first_stop in costs[origin]:
        if first_stop == destination:
            first_price = costs[origin][destination]
            list_of_prices.append(first_price)
        elif first_stop != destination:
            if destination in costs[first_stop]:
                second_price = costs[origin][first_stop] + costs[first_stop][destination]
                list_of_prices.append(second_price)
    return min(list_of_prices)

#______________________________________________________________________________________________________________



def rank_suit_count(hand_string):
    counts = {"types":{}, "suits": {}}
    final_result = []
    card_string = "".join(hand_string)
    count = 1
    for letter in card_string:
        if count % 2 == 0:
            if letter in counts:
                counts["suits"][letter]+=1
            else:
                counts["suits"][letter] =1
        else:
            if letter in counts:
                counts["types"][letter]+=1
            else:
                counts["types"][letter] =1
        count+=1
    final_result.append(counts["types"])
    final_result.append(counts["suits"])
    return final_result
print(rank_suit_count([ 'AS', 'AD', '2C', 'TH', 'TS' ]))