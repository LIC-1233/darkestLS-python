from lark import Lark

grammar = r"""
start: (key_value_pair | comment | broken_line)*

key_value_pair: pkey ":" WS? (pvalue | comment | broken_line)*

pkey: PKEY
pvalue:skey [svalue+]
skey: SKEY
SKEY.1:WS?"."SKEY_CONTENT
svalue:svalue_digit
| svalue_escaped_str
| svalue_str
| svalue_bool

PKEY: /[a-zA-Z_]+/
SKEY_CONTENT: /[a-zA-Z_0-9]+/
svalue_digit:WS? SVALUE_DIGIT_CONTENT WS?
SVALUE_DIGIT_CONTENT:/[-|+]?[0-9]*\.?[0-9]+%?/
svalue_str: WS SVALUE_STR_CONTENT
SVALUE_STR_CONTENT: /[^\.\s"]+/
svalue_escaped_str: WS? "\"" SVALUE_ESCAPED_STR_CONTENT? "\"" WS?
SVALUE_ESCAPED_STR_CONTENT:  /[^"]+/ 
svalue_bool: WS? SVALUE_BOOL_CONTENT WS?
SVALUE_BOOL_CONTENT: "true"|"false"
comment: COMMENT
COMMENT.9: /\/[^\n]*/
broken_line: BROKEN_LINE
BROKEN_LINE: /.+/
NEWLINE1: (/\r\n|\r|\n/ /\s/+ /\r\n|\r|\n/?)+
NEWLINE2: (/\r\n|\r|\n/? /\s/* /\r\n|\r|\n/)+

%import common.WS_INLINE -> WS
%import common._STRING_INNER
%ignore NEWLINE1
%ignore NEWLINE2
"""

darkest_parser = Lark(grammar, parser="lalr", propagate_positions=True)
