upper_word = input()
upper_word_list = list(upper_word)

def censorship(word):
    new_list=[]
    censor_word = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
    for i in word:
        if i not in censor_word:
            new_list.append(i)
    return ''.join(new_list)

print(censorship(upper_word_list))

