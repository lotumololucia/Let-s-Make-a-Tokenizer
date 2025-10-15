"""
Exception lexicon for tokenizer.
"""

LEXICON = {
    "don't" : ["do", "n't"],
    "isn't" : ["is", "n't"],
    "What's" : ["What", "'s"],
    "I'm" : ["I", "'m"],
}

'''
Si encuentra una de estas palabras completas, no usar regex.
En cambio, reemplazala por esta lista de tokens.
'''
