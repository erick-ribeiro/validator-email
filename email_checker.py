import dns.resolver
import pandas as pd
from validate_email import validate_email

def check_mx_record(email):
    domain = email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        return True if records else False
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoNameservers) as e:
        # print(f"Erro ao verificar o MX record para {email}: {e}")
        return False

def validate_emails(email_list):
    results = []
    for email in email_list:
        is_valid_format = validate_email(email)
        has_mx_record = check_mx_record(email)
        
        # Exibe no console apenas os e-mails sem MX Record
        if not has_mx_record:
            print(f"E-mail sem MX Record: {email}")

        # Adiciona à lista apenas os e-mails válidos
        if is_valid_format and has_mx_record:
            results.append({
                'email': email,
                'is_valid_format': is_valid_format,
                'has_mx_record': has_mx_record
            })
    return results

def save_to_excel(results, filename='email_validation_results.xlsx'):
    df = pd.DataFrame(results)
    df.to_excel(filename, index=False)

# Lista de e-mails para validação
email_list = [
    "saude@divinopolis.mg.gov.br",
    "saude@itauna.mg.gov.br",
    "saude@parademinas.mg.gov.br",
    "saude@novaserrana.mg.gov.br",
    "saude@bomdespacho.mg.gov.br",
    "saude@formiga.mg.gov.br",
    "saude@lagoadaprata.mg.gov.br",
    "saude@papagaios.mg.gov.br",
    "saude@pompeu.mg.gov.br",
    "saude@oliveira.mg.gov.br",
    "saude@santoantoniodomonte.mg.gov.br",
    "saude@campobelo.mg.gov.br",
    "saude@arcos.mg.gov.br",
    "saude@claudio.mg.gov.br",
    "saude@pitangui.mg.gov.br",
    "saude@carmodocajuru.mg.gov.br",
    "saude@perdigao.mg.gov.br",
    "saude@itapecerica.mg.gov.br",
    "saude@luz.mg.gov.br",
    "saude@bambui.mg.gov.br",
    "saude@prefeitura.pbh.gov.br",
    "saude@uberlandia.mg.gov.br",
    "saude@contagem.mg.gov.br",
    "saude@pjf.mg.gov.br",
    "saude@betim.mg.gov.br",
    "saude@montesclaros.mg.gov.br"
]

# Validação dos e-mails
results = validate_emails(email_list)

# Salvar resultados em uma planilha Excel
save_to_excel(results, 'resultados_validacao_emails.xlsx')

print("Processo concluído. Planilha gerada com e-mails válidos.")
