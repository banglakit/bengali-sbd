from spacy.lang.bn import Bengali

nlp = Bengali()
nlp.add_pipe(nlp.create_pipe('sentencizer'))


def _split(text: str):
    return map(lambda x: x.text, nlp(text).sents)


def split(text: str):
    yield from _split(text)