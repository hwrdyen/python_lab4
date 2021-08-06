def gen_bot_text(token_list, bad_author):
    VALID_PUNCTUATION = ['?', '.' , '!', ',', ':', ';']
    END_OF_SENTENCE_PUNCTUATION = ['?', '.', '!']
    ALWAYS_CAPITALIZE = ["I", "Montmorency", "George", "Harris", "J", "London", "Thames", "Liverpool", "Flatland", "", "Mrs", "Ms", "Mr", "William", "Samuel"]
    if bad_author == True:
        for i in token_list:
            a = ' '.join(token_list)
        return a
    elif bad_author == False:
        a = []
        b = ' '.join(token_list)
        c = list(b)
        for j in range(1,len(c)+1):
            if c[j] in VALID_PUNCTUATION:
                c[j-1] = ''
                a = ''.join(c)
        return a






if __name__ == "__main__":
    token_list= ['this', 'is', 'a', 'string', 'of', 'text', '.', 'which', 'needs', 'to', 'be', 'created', '.']
    print(gen_bot_text(token_list, True))
    print(gen_bot_text(token_list, False))
