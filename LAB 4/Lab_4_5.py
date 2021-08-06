def probify_ngram_counts(counts):
    for i in counts:
        a = []
        sum1 = sum(counts[i][1])
        for j in counts[i][1]:
            value = j/sum1
            a.append(value)
        counts[i] = [[counts[i][0]],[a]]
    return counts
    






if __name__ == "__main__":
    ngram_counts2 = {('i', 'love'): [['js', 'py3', 'no'], [20, 20, 10]], ('toronto', 'is'): [['six', 'drake'], [2, 3]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]]}
    print(probify_ngram_counts(ngram_counts2))
