def prune_ngram_counts(counts, prune_len):
    for i in counts:
        a = counts[i][1]
        b = counts[i][0]
        c = []
        d = []
        if len(a) >= prune_len:
            for j in range(0,len(a)):
                for k in range(j+1,len(a)):
                    if a[j] < a[k]:
                        (a[j], a[k]) = (a[k], a[j])
                        (b[j], b[k]) = (b[k], b[j])
            if len(counts[i][1]) > prune_len:
                    for o in range(0,len(counts[i][1])):
                        print(counts[i][1][o])
                        if counts[i][1][o] >= counts[i][1][prune_len-1]:
                            c.append(counts[i][1][o])
                            d.append(counts[i][0][o])
                    counts[i] = [c,d]
    return counts
                        
                       
                    



if __name__ == "__main__":
    ngram_counts1 = {('i','love'):[['js','a','b','py3','c','no'],[20,3,2,20,2,10]],('u','r'):[['cool','nice','lit','kind'],[8,7,5,5]],('toronto','is'):[['six','drake'],[2,3]]}
    print(prune_ngram_counts(ngram_counts1, 3))
