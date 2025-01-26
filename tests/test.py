# commecy -- normalizer for french for spacy.
# Copyright (C) 2024,2025  thjbdvlt
#
# commecy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# commecy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with commecy.  If not, see <https://www.gnu.org/licenses/>.


from commecy.normalizer import CommeCyNormalizer
import spacy
from spacy.tokens import Doc
import os
import csv
import json


ERR_MSG = "Failed normalization: {form}. Waits: {norm}. Gets: {result}"


def check(form, norm, result):
    """Check that a form is correctly normalized."""

    if norm != result:
        raise ValueError(
            ERR_MSG.format(form=form, norm=norm, result=result)
        )


def test():
    """Tests the normalizer."""

    normalizer = CommeCyNormalizer(None, None)

    filepath = os.path.join(os.path.dirname(__file__), "words.csv")

    with open(filepath) as csvfile:
        csvreader = csv.reader(csvfile)

        for form, norm in csvreader:
            result = normalizer.normalize(form)
            check(form, norm, result)


def test_with_vocab():

    nlp = spacy.blank("fr")
    normalizer = CommeCyNormalizer(nlp.vocab, None)  # mhhhhh this fails, too

    filepath = os.path.join(os.path.dirname(__file__), "words.csv")

    with open(filepath) as csvfile:
        csvreader = csv.reader(csvfile)

        for form, norm in csvreader:
            result = normalizer.normalize(form)
            check(form, norm, result)


def test_on_docs():
    """Test on a few Docs."""

    nlp = spacy.blank("fr")
    nlp.add_pipe("commecy_normalizer")
    pipe = nlp.get_pipe('commecy_normalizer')

    filepath = os.path.join(os.path.dirname(__file__), "sents.json")
    with open(filepath, 'r') as f:
        sents = json.load(f)

    for sent in sents:
        forms = sent['forms']
        norms = sent['norms']
        doc = Doc(vocab=nlp.vocab, words=forms)
        doc = pipe(doc)
        for token, norm in zip(doc, norms):
            result = token.norm_
            check(token.text, norm, result)


if __name__ == "__main__":
    test()
    test_with_vocab()
    test_on_docs()
