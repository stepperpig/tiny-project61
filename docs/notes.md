[main.]main -> 
        (:fields ).
        (:actions <<notion>>
            hns <- [browser.]ngordnet_server()
            ngm <- [ngrams.]ngrammap() 
            hh <- [main.]historyhandler(ngm) 
            hns.start()
            hns.register(hh)
        ).
        (:methods
            ([self.]main(str)
                (:actions
                    <<notion>>
                ).
            ).
        ).

[browser.]ngordnet_server -> (:fields )
        (:actions ).
        (:methods
            ([self.]register(str:url, [browser.]ngordnet_queryhandler:nqh)
                (:actions
                    [!spark!]get(url, nqh)
                ).
            ),
            ([self.]start()
                (:actions <<notion, concrete>>
                    [!spark!]staticFiles.externalLocation("static folder containing html")
                    "allow for all origin requests"
                ).
            ).
        ).

[browser.]ngordnet_queryhandler<impl [!spark!]route> -> 
        (:fields 
            [!Gson!]gson
        ).
        (:cautions
            [@override?]handle([browser.]ngordnet_query q)
        ).
        (:methods
            (str<---commaSeparatedStringToList(str::s)
                <<notion>>
                "convert string to list"
            ).
            ([browser.]ngordnet_query<---readQueryMap([!spark!]QueryParamsMap::qm)
                <<notion>>
                "we receive a !spark! :querymap: and extract
                the values of the map. note that our words
                will have to be captured in a list. finally,
                we return in the form of an :ngordnetquery:"
            ).
            ([@override.]handle([!spark!]Request req, [!spark!]Response res)
                (:actions <<notion>>
                    [!spark!]QueryParamsMap qm <- req.[!spark!]queryMap()
                    [browser.]ngordnet_query nq <- [browser.]ngordnet_queryhandler.readQueryMap(qm)
                    queryResult <- [browser.]ngordnet_queryhandler.handle(nq)
                    return [!Gson!]gson.toJson(queryResult)
                ).
            ).
        )


::prose::
[main.] creates :server: and instantiates :ngrammap: model. 
        :server: starts and registers new :historyhandler:
        (which is just a superaltered :queryhandler:). this 
        process will effectively establish the bridge or
        link to our localhost server, which is defined
        in the ngordnet.js 
[?server.] provides methods for registering :queryhandlers:
        (by wrapping over !spark! get requests... we map
        the route for GET requests. good to note that our
        ngordnet_queryhandler is just an implementation
        of a !spark! Route) and for
        starting the :server: (by using !spark!'s 
        :staticfiles: interface).

::prose::
ok... we know we can handle our client side in python using something like
fastapi. on the server-side we could just use javascript fetch api.
we should keep our goal within view... ultimately we want to display various
visualizations. but for now we should take a tiny step back and focus on 
implementing our ngramviewer. 

we want to be able to input a list of words into a text box, press a button
to generate a D3 visualization. we could easily draw a visualization on our
client side. but how do we interact with our python backend? we send
our list of unigrams as an api request. we could use axios for handling this
frontend-to-backend exchange.

let's think about the backend. how do we construct our ngrammaps? do we 
instantiate with a static local file? for now we'll feed our ngrammap a 
single file. we'll parse our csv data stores into dictionaries that map 
words to timeseries. we'll also define some class methods that compute 
timeseries based on our specifications. this will essentially be the main 
object we use to generate the correct timeseries. 

