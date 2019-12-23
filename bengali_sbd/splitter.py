from spacy.lang.bn import Bengali

nlp = Bengali()
nlp.add_pipe(nlp.create_pipe('sentencizer'))


def split(text: str):
    return [s.text for s in nlp(text).sents]
