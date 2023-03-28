# EBNF

**PROGRAM** = { STATEMENT } ";" ;  
**STATEMENT** = ASSIGNMENT | CONDITIONAL | LOOP | PRINT | FUNCTION_CALL ;  

------

**EXPRESSION** = TERM, { ("+" | "-"), TERM } ;  
**TERM** = FACTOR, { ("*" | "/"), FACTOR } ;  
**FACTOR** = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;  
**BOOL_EXPRESSION** = BOOL_TERM, { ("||" | "&&"), BOOL_TERM } ;  
**BOOL_TERM** = BOOL_FACTOR, { ("==" | "!=" | "<=" | ">=" | "<" | ">"), BOOL_FACTOR } ;  
**BOOL_FACTOR** = "true" | "false" | "(", BOOL_EXPRESSION, ")" | EXPRESSION;  

-------

**IDENTIFIER** = LETTER, { LETTER | DIGIT | "_" } ;  
**ASSIGNMENT** = IDENTIFIER, "<-", EXPRESSION | STRING ;  

**PRINT** = "print", (EXPRESSION | STRING | IDENTIFIER);  

**CONDITIONAL** = "if", BOOL_EXPRESSION, "{", { STATEMENT }, "}", [ "ELSE", "{", { STATEMENT }, "}" ] ;  
**WHILE_LOOP** = "while" , BOOL_EXPRESSION, "{", { STATEMENT }, "}" ;  
**FOR_LOOP** = "for", [ IDENTIFIER, "<-", ] EXPRESSION, "from", EXPRESSION, "to", EXPRESSION, [ "step", EXPRESSION ], "{", { STATEMENT }, "}" ;  

**FUNCTION_CALL** = "func", IDENTIFIER, "(", [ ARG_LIST ], ")", "->", { STATEMENT } ;  
**ARG_LIST** = EXPRESSION, { ",", EXPRESSION } ; 

------

**STRING** = SINGLE_QUOTE_STRING | DOUBLE_QUOTE_STRING | TEXT_STRING | NUMBER_STRING ;  

**SINGLE_QUOTE_STRING** = "' ", CHAR, { CHAR }, " '" ;  
**DOUBLE_QUOTE_STRING** = " " ", CHAR, { CHAR }, " " " ;  
**TEXT_STRING** = ("t" | "text"), " " ", LETTER, { LETTER }, " " " ;  
**NUMBER_STRING** = ("n" | "number"), " " ", NUMBER, " " " ;  

**LETTER** = (a | ... | z | A | ... | Z) ;  
**SPECIAL** = (- |  | # | & | ’ | ( | ) | * | + | , | . | / | : | ; | < | = | >) ;  
**CHAR** = LETTER | NUMBER | SPECIAL ;  
  
**NUMBER** = INTEGER | FLOAT ;  
**INTEGER** = DIGIT | NONZERO, { DIGIT } ;  
**FLOAT** = INTEGER, "." , INTEGER ;  
**DIGIT** = (0 | NONZERO ) ;  
**NONZERO** = (1|2|3|4|5|6|7|8|9) ;  
