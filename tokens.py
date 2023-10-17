#Módulo de tokens
tokens = {
    'PROGRAM': r'\bprogram\b',
    'VAR': r'\bvar\b',
    'BEGIN': r'\bbegin\b',
    'END': r'\bend\b',
    'READ': r'\bread\b',
    'WRITE': r'\bwrite\b',
    'IF': r'\bif\b',
    'THEN': r'\bthen\b',
    'ELSE': r'\belse\b',
    'WHILE': r'\bwhile\b',
    'DO': r'\bdo\b',
    'INTEGER': r'\binteger\b',
    'REAL': r'\breal\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'NUMBER': r'\d+',
    'REAL_NUMBER': r'\d+\.\d+',
    'OPERATOR': r'[\+\-\*\/]|<=?|>=?|:=',  
    'SEMICOLON': r';',
    'COMMA': r',',
    'OPEN_PAR': r'\(',
    'CLOSE_PAR': r'\)',
    'COMMENT': r'\{[^\}]*\}',
    'COLON': r':'
}