
```  
  - category: NP
    rule: lex
    semantics: \E F. F(E)
    child0_category: N

  - category: N
    semantics: \E. E
    pos: NNP

  - category: NP
    semantics: \E P. -exists x. P(x)
    surf: nobody

  - category: S\NP
    semantics: \E Q. Q(\x.E(x))

  - category: .
    semantics: \E X. X
    surf: "."
```
