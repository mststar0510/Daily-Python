import re

urls = (
    'www.shibaura-it.ac.jp/',
    'https://www.dendai.ac.jp/',
    'https://www.tcu.ac.jp/',
    'https://www.kogakuin.ac.jp/',
)
m = re.split("\.",urls[0])
print(m[1])
