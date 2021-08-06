import random

def gen_next_token(current_ngram, ngram_model):
    '''
    (tup, Dict{tup: List[List[int]]}) -> str

    Randomly generates the next token from the current_ngram based on the 
    frequency of each word stored in ngram_model by sampling from the
    distribution of possible next words.
    
    The function assumes that check_open_ngram(ngram_model, current_ngram) is True, 
    i.e. that the array of words corresponding to ngram_model[current_ngram] 
    is not empty. The function also assumes that current_ngram is in ngram_model.
    '''
    curr_prob = random.random()
    prob_to_index = 0

    words = ngram_model[current_ngram][0]
    # create a copy that the code below does not modify the ngram model
    # Note: shallow copy is sufficient for a list of numbers
    cdf = ngram_model[current_ngram][1].copy()
    
    for i in range(1, len(cdf)):
        cdf[i] += cdf[i-1]

    while cdf[prob_to_index] < curr_prob:
        prob_to_index += 1

    return words[prob_to_index]

def gen_bot_list(ngram_model,seed,num_tokens):
    e = []
    rest = (num_tokens)-len(seed)
    a = []
    if seed in ngram_model:
        for i in ngram_model:
            print(i)
            while i == seed:
                print('yes')
                b = gen_next_token(seed,ngram_model)
                print(b)

                if len(seed) >= num_tokens:
                    for j in range(0,len(seed)):
                        a.append(seed[j])

                else:
                    for j in seed:
                        a.append(j)
                    a.append(b)
                    
                    
                    
            return a
                        

    elif seed not in ngram_model: 
        if len(seed) <= num_tokens:
            for j in range(0,len(seed)):
                a.append(seed[j])
        elif len(seed) > num_tokens:
            for j in range(0,num_tokens):
                a.append(e[j])
    return a
        




if __name__ == "__main__":
    ngram_model = {('the', 'child'):[['will', 'can','may'], [0.5, 0.25, 0.25]],('child', 'will'): [['the'], [1.0]],('will', 'the'): [['child'], [1.0]],('child', 'can'): [['the'], [1.0]],('can', 'the'): [['child'], [1.0]],('child', 'may'): [['go'], [1.0]],('may', 'go'): [['home'], [1.0]],('go', 'home'): [['.'], [1.0]]}
    print(gen_next_token(('the','child'),ngram_model))
    print(gen_bot_list(ngram_model,('child','will'),1))
    print(gen_bot_list(ngram_model,('hello','world'),3))
