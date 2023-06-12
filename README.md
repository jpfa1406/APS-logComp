# EBNF

**BLOCK** = { STATEMENT } ";" ;  
**STATEMENT** = ( λ | ASSIGNMENT | PRINT | WHILE_LOOP | IF | FUNCTION | RETURN | CALL_FUNC ), ";" ;

------

**RELEXPRE** = EXPRESSION, { ("==" | ">" | "<"), EXPRESSION }
**EXPRESSION** = TERM, { ("+" | "-" | "||" | "."), TERM } ;  
**TERM** = FACTOR, { ("*" | "/" | "&&"), FACTOR } ;  
**FACTOR** = (("+" | "-" | "!"), FACTOR) | NUMBER | STRING | "(", RELEXPR, ")" | IDENTIFIER, ["(", RELEXPR, {",", RELEXPR} ,")"] | ("readin", "(", ")") ;

-------

**IDENTIFIER** = LETTER, { LETTER | DIGIT | "_" } ;  
**ASSIGNMENT** = IDENTIFIER, "<-", (CREATE | ASSING) ;  

**CREATE** = "(", TYPE, ")" ;
**TYPE** = "Int" | "String" ;

**ASSING** = "=",  RELEXPRE ;

-------

**PRINT** = "print", "(", RELEXPRE, ")" ;  

**WHILE_LOOP** = "while" , RELEXPRE, "{", { STATEMENT }, "}" ;  
**IF** = "if", RELEXPRE, "{", { STATEMENT }, "}", [ "else", "{", { STATEMENT }, "}" ] ;  

-> **FOR_LOOP** = "for", IDENTIFIER, "<-", RANGE, "do", "{", { STATEMENT }, "}" ;  
-> **RANGE** = EXPRESSION, "..", EXPRESSION;

**FUNCTION** = "func", IDENTIFIER, "(", [ ARG_LIST ], ")", "->", "{", { STATEMENT }, "}", "(", TYPE, ")" ;  
**ARG_LIST** = IDENTIFIER, "(", TYPE, ")", { ",", IDENTIFIER, "(", TYPE, ")" } ;
**RETURN** = "return", RELEXPRE ;
**CALL_FUNC** = IDENTIFIER, "(", [RELEXPRE, { ",", RELEXPRE}], ")" ;

------

**NUMBER** = DIGIT, { DIGIT } ;
**LETTER** = ( a | ... | z | A | ... | Z ) ;
**DIGIT** = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
