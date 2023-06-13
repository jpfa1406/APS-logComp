%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
void yyerror(const char *s) { printf("ERROR: %s\n", s); }
%}

%token STRING INT
%token LETTER DIGIT
%token SEMICOLON
%token IN ON
%token RETURN PRINT IF ELSE WHILE FUNC
%token LBRACE RBRACE LPAREN RPAREN
%token EQUAL COMMA
%token CEQ GREATER_THAN LESS_THAN
%token PLUS MINUS OR DOT
%token MULT DIV AND
%token NOT READIN

%start block

%%

block:
    statement_list
    ;

statement_list:
    statement | statement_list statement 
    ;

statement:
    assignment_statement SEMICOLON | print_statement SEMICOLON | while_loop_statement | if_statement 
	| function_statement | return_statement SEMICOLON | call_function_statement SEMICOLON;
    ;

indentifier:
	LETTER 
	| LETTER LETTER
	| LETTER DIGIT 

assignment_statement:
    indentifier IN create | indentifier IN assign;

create:
	LPAREN type RPAREN;

type:
	INT 
	| STRING;

assign:
	EQUAL relexpre;

print_statement:
	PRINT LPAREN relexpre RPAREN;

while_loop_statement:
	WHILE relexpre LBRACE statement_list RBRACE;

if_statement:
	IF relexpre LBRACE statement_list RBRACE
	| IF relexpre LBRACE statement_list RBRACE ELSE LBRACE statement_list  RBRACE;

function_statement:
	FUNC indentifier LPAREN RPAREN ON LBRACE statement_list RBRACE LPAREN type RPAREN
	| FUNC indentifier LPAREN arg_list RPAREN ON LBRACE statement_list RBRACE LPAREN type RPAREN

arg_list:
	indentifier
	| indentifier COMMA arg_list;

return_statement:
	RETURN relexpre;

call_lsit:
	relexpre
	| relexpre COMMA call_lsit;

call_function_statement:
	indentifier LPAREN RPAREN
	| indentifier LPAREN call_lsit RPAREN;

relexpre:
	expression
	| expression CEQ expression
	| expression GREATER_THAN expression
	| expression LESS_THAN expression;

expression:
	term
	| term PLUS term
	| term MINUS term
	| term OR term
	| term DOT term;

term:
	factor
	| factor MULT factor
	| factor DIV factor
	| factor AND factor;

factor:
	PLUS factor
	| MINUS factor
	| NOT factor
	| number
	| string
	| LPAREN relexpre RPAREN
	| call_function_statement
	| READIN LPAREN RPAREN;

number:
	DIGIT
	| DIGIT number;

string:
	LETTER
	| LETTER string
	| DIGIT string;
	


%%

int main() {
    yyparse();
    return 0;
}