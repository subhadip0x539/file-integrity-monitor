import yara

def match(file):
    rules = yara.compile(filepath='rules/index.yar')
    return rules.match(file)

