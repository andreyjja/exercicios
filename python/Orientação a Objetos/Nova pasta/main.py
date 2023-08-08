endereco = "rua joao 23 , apartamento 32, Cotia, São Paulo,SP, 33322-222"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
achar = padrao.search(endereco)

if achar:
    cep = achar.group()
    print(cep)