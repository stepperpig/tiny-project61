from ngrams.ngrammap import NGramMap 

def main():
    wfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/top_14377_words.csv"
    cfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"
    map = NGramMap(wfile, cfile)
    map.print()
    
main()