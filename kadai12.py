import re

urls = (
    'www.shibaura-it.ac.jp/',
    'https://www.dendai.ac.jp/',
    'https://www.tcu.ac.jp/',
    'https://www.kogakuin.ac.jp/',
)
def stand_for(word):
    m=re.split('\.',word)
    return str(m[1])
for n in urls:
    print('"{0}" stand for "{1}".'.format(stand_for(n), n))
