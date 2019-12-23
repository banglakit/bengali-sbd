import re

from spacy.lang.bn import Bengali

nlp = Bengali()
nlp.add_pipe(nlp.create_pipe('sentencizer'))
TERMINATING_PUNCT = re.compile(r'([^\u0980-\u09ff\s+])<=(।\?!)')


def process_terminating_punct(text):
    return TERMINATING_PUNCT.split(text)


def split(text: str):
    return [s.text for s in nlp(text).sents]

