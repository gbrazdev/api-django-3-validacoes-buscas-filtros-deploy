import re
from validate_docbr import CPF



"""CPF"""
def validate_cpf(cpf_number):
    cpf = CPF()
    # Validar CPF
    return cpf.validate(cpf_number)  # True

"""NOME"""    
def validate_nome(nome):
        return nome.isalpha()

"""RG"""            
def validate_rg(rg):
        return len(rg) == 9

"""CEL"""           
def validate_cel(celular):
    """(00) 0 0000-0000"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    ansawer = re.findall(modelo, celular)
    return ansawer
           
        