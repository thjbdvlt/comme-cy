__commecy__ -- a normalizer for french for spaCy.

|x|y|
|--|--|
|chuuuuut!!!!!|chut!|
|bateâu|bateau|
|HO|ho|
|PEùùùT-èTRE|peut-être|
|comencer|commencer|
|auteur-rice-s|auteur·rices|
|peut—être|peut-être|
|autre[ment]|autrement|
|désœuvrement|désoeuvrement|

# installation

```bash
pip install git+https://github.com/thjbdvlt/commecy
```

# usage

```python
import spacy

nlp = spacy.blank('fr')
nlp.add_pipe('commecy_normalizer')

for i in nlp("PEEUUUT-étre"):
    print i.norm_
```
