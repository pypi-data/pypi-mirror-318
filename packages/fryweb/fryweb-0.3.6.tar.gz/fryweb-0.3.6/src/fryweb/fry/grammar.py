from parsimonious import Grammar
from pathlib import Path

def load_grammar():
    grammar_file = Path(__file__).parent / 'fry.ppeg'
    with grammar_file.open('r', encoding='utf-8') as gf:
        grammar_text = gf.read()
    return Grammar(grammar_text)

grammar = load_grammar()
