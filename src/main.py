from ngrams.ngrammap import NGramMap 

def main():
    wfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/words_that_start_with_q.csv"
    cfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"
    map = NGramMap(wfile, cfile)

    w = map.words()
    print(w)

    
main()