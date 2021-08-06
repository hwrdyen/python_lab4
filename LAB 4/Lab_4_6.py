def build_ngram_model(words,n):
    b = {}
    for i in range(0,(len(words)-n)):
        a = []
        for j in range(0,(n)):
            a.append(words[i+j])
        if tuple(a) not in b:
            b[tuple(a)] = [[],[]]
        if words[i+n] not in b[tuple(a)][0]:
            b[tuple(a)][0].append(words[i+n])
            b[tuple(a)][1].append(1)
        elif words[i+n] in b[tuple(a)][0]:
            order = b[tuple(a)][0].index(words[i+n])
            b[tuple(a)][1][order] += 1
    for a in b:
        z = []
        sum1 = sum(b[a][1])
        for c in b[a][1]:
            value = c/sum1
            z.append(value)
        b[a] = [[b[a][0]],[z]]
    return b
        


if __name__ == "__main__":
    words = ['the','child','will','the','child','can','the','child','will','the','child','may','go','home','.']
    print(build_ngram_model(words, 2))
