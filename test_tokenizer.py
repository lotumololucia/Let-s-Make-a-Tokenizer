"""
Test the tokenizer, grammar and exceptions.
"""
#import tokenizer
import grammar


#TOKENIZER = tokenizer.Tokenizer()
RULES = grammar.RULES

# Test rule regexes.
def test_inital_punctuation_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['initial_punctuation_token'].pattern
    assert test_regex == """^([\'"])([A-Z]+[\',!?":.]*)$"""

def test_final_punctuation_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['final_punctuation_token'].pattern
    assert test_regex == """^([A-Z]+)([',!?":.]+)$"""

def test_all_punctuation_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['punctuation_token'].pattern
    assert test_regex == """^([',!?":.])([',!?":.]+)$"""

def test_currency_regex():
    """Test the grammar generated regex."""
    test_regex = RULES['currency_token'].pattern
    assert test_regex == r"""^([$£¥€])([0-9]+\.?[0-9]{,2})([',!?":.]*)$"""
