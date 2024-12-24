from lark import Lark

grammar = r"""
start: (darkest_dict | comment | broken_line)*

darkest_dict: pkey ":" WS? (pvalue | comment | broken_line)*

pkey: PKEY
pvalue:skey svalue
skey: SKEY
SKEY.1:WS?"."SKEY_CONTENT
svalue:(SVALUE_DIGIT
| SVALUE_ESCAPED_STR
| SVALUE_STR
| SVALUE_BOOL)*

PKEY: /[a-zA-Z_0-9]+/
SKEY_CONTENT: /[a-zA-Z_0-9]*[a-zA-Z_]+/
SVALUE_DIGIT:WS? SVALUE_DIGIT_CONTENT
SVALUE_DIGIT_CONTENT:/[-|+]?[0-9]*\.?[0-9]+%?(?=\s|\r\n|\r|\n|$)/
SVALUE_STR: WS SVALUE_STR_CONTENT
SVALUE_STR_CONTENT: /[^\.\s"]+(?=\s|\r\n|\r|\n|$)/
SVALUE_ESCAPED_STR: WS? "\"" SVALUE_ESCAPED_STR_CONTENT? "\""
SVALUE_ESCAPED_STR_CONTENT:  /[^"\n]+/ 
SVALUE_BOOL: WS? SVALUE_BOOL_CONTENT
SVALUE_BOOL_CONTENT: "true"|"false"
comment: COMMENT
COMMENT.9: /\/[^\n]*/
broken_line: BROKEN_LINE
BROKEN_LINE: /.+/
NEWLINE1: (/\r\n|\r|\n/ /\s/* /\r\n|\r|\n/?)+
NEWLINE2: (/\r\n|\r|\n/? /\s/* /\r\n|\r|\n/)+

%import common.WS_INLINE -> WS
%import common._STRING_INNER
%ignore NEWLINE1
%ignore NEWLINE2
"""

darkest_parser = Lark(grammar, parser="lalr", propagate_positions=True)
