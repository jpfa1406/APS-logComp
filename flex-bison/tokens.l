%{
#include "parser.tab.h"
#include <stdio.h>
#include <stdlib.h>
%}

%option noyywrap

%%

";"				          		{return (SEMICOLON);}

"return"				        {return (RETURN);}
"print"				            {return (PRINT);}
"if"                            {return (IF);}
"else"                          {return (ELSE);}
"while"                         {return (WHILE);}
"func"                          {return (FUNC);}


"<-"                            {return (IN);}
"->"                            {return (ON);}

[a-zA-Z_]                       {return LETTER;}
[0-9] 					        {return DIGIT;}

"="						        {return (EQUAL);}
","				          		{return (COMMA);}

"=="				          	{return (CEQ);}
"<"				          		{return (LESS_THAN);}
">"				          		{return (GREATER_THAN);}

"!"	          				    {return (NOT);}
"readin"                        {return (READIN);}

"("	          					{return (LPAREN);}
")"					          	{return (RPAREN);}
"{"         					{return (LBRACE);}
"}"					          	{return (RBRACE);}

"."         					{return (DOT);}
"+"				          		{return (PLUS);}
"-"		          				{return (MINUS);}
"||"					        {return (OR);}


"*"		          				{return (MULT);}
"/"				          		{return (DIV);}
"&&"				          	{return (AND);}

"Int"		          			{return (INT);}
"String"				        {return (STRING);}

[\t\n\f\r ]+                        /* ignore whitespace */
.                                   { printf("Invalid character: %s\n", yytext); }

%%
