from ngrams.ngrammap import NGramMap 
from server.ngordnet_server import Server

def main():
    # wfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/words_that_start_with_q.csv"
    # cfile = "/Users/kaiwenli/Documents/projects/skeleton-sp24/data/ngrams/total_counts.csv"
    # map = NGramMap(wfile, cfile)
    server = Server()
    server.start()

main()