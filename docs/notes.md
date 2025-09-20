[main.]main -> (:fields [browser.]ngordnet_server [ngrams.]ngrammap)
        (:actions <<notion>>
            [browser.]ngordnet_server() hns
            [ngrams.]ngrammap() ngm
            [main.]historyhandler(ngm) hh
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