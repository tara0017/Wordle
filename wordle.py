def count_letters(x):
    global letter_count
    
    for c in x:
            
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1

def evaluate_word(word):
    global letter_count
    score = 0
    
    for letter in word:
        score += letter_count[letter]
    return score

def has_duplicates(word):
    for i in range(len(word) - 1):
        if word[i] in word[i+1:]:
            return True
    return False


def has_one_vowel(w):
    vowels = 'aeiou'
    count = 0
    
    for c in w[0]:
        if c in vowels:
            count += 1
            if count > 1:
                return False
    return True


def get_top_words(word_dict, num_words):
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    count = 0

    print('Remaining top words:')
    for w in sorted_words:
        if has_duplicates(w[0]) == False:
            print(w)
            count += 1
            if count == num_words:
                return

    
def get_top_words_w_one_vowel(word_dict, num_words):
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    count = 0
    
    for w in sorted_words:
        if has_one_vowel(w) and has_duplicates(w[0]) == False:
            print(w)
            count += 1
            if count == num_words:
                return


def rescore(dict_of_words):
    local_letter_count = dict()

    # get adjusted letter count based on remaining words
    for word in dict_of_words:
        for c in word:
            if c in local_letter_count:
                local_letter_count[c] += 1
            else:
                local_letter_count[c] = 1

    # rescore each word
    adjusted_dict = dict()
    for word in dict_of_words:
        score = 0
        for letter in word:
            score += local_letter_count[letter]
        adjusted_dict[word] = score

    return adjusted_dict
                    

def get_words_containing(letters, dict_of_words):
    ####  doesn't take duplicates into account yet
    new_dict_of_words = dict()
    for word in dict_of_words.items():
        
        word_meets_criteria = True
        
        for letter in letters:
            if letter not in word[0]:
                word_meets_criteria = False
                break
            
        if word_meets_criteria:
            new_dict_of_words[word[0]] = word[1]
        
    new_dict_of_words = rescore(new_dict_of_words)
    return new_dict_of_words


def get_words_without(letters_to_avoid, dict_of_words):
    new_dict_of_words = dict()
    for word in dict_of_words.items():
        word_meets_criteria = True
        
        for letter in letters_to_avoid:
            if letter in word[0]:
                word_meets_criteria = False
                break
            
        if word_meets_criteria:
            new_dict_of_words[word[0]] = word[1]
            
    new_dict_of_words = rescore(new_dict_of_words)
    return new_dict_of_words


def get_words_in_order(order, w):
    
    for i in range(5):
        updated_dict = dict()
        if order[i] == '-':
            continue
        else:
            letter = order[i].lower()
            for word in w:
                if word[i] == letter:
                    updated_dict[word] = 0
            w = updated_dict

    w = rescore(w)
    return w
            

    

words = set()
letter_count = dict()
top_scoring_words = dict()
top_scoring_words_no_duplicates = dict()


f = open('words.txt', 'r')
for x in f:
    x = x.strip()
    x = x.replace('"', '')
    x = x.split(',')
    for word in x:
        word = word.lower()
        words.add(word)
        count_letters(word)

words_dict = dict()
for word in words:
    score = evaluate_word(word)
    words_dict[word] = score

while True:
    contains_letters = input('What letters apear in word? ')
    exclude_letters  = input('What letters do not appear in word? ')
    order = input('Type the letters in the appropriate location if known (otherwise type "-") ')

    words_dict = get_words_containing(contains_letters, words_dict)
    words_dict = get_words_without(exclude_letters, words_dict)
    words_dict = get_words_in_order(order, words_dict)


    print('\n', len(words_dict), 'possible words left')


    if len(words_dict) < 10:
        for w in words_dict:
            print(w, words_dict[w])
        break
    else:
        get_top_words(words_dict, 10)





"""
get_top_words_w_one_vowel(words_dict, 20)

for word in words:
    score = evaluate_word(word)
    if score > 20000:
        top_scoring_words[word] = score
        

print(len(top_scoring_words))


for k,v in top_scoring_words.items():
    if has_duplicates(k) == False:
        top_scoring_words_no_duplicates[k] = v

sorted_top_words_no_duplicates = sorted(top_scoring_words_no_duplicates.items(), key=lambda x: x[1], reverse=True)


  
for word in sorted_top_words_no_duplicates:
    common_letters = 'rsnlt' #'arose' 'unlit' 'pdhbcmgk'
    #print(word)
    #break
    no_common_letters = True
    
    for letter in common_letters:
        if letter in word[0]:
            no_common_letters = False
            break

    if no_common_letters:    
        print(word)
    
"""        




