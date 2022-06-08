class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def is_domain_invalid(domain_for_check, valid_domains):
    result = True
    for valid_domain in valid_domains:
        if domain_for_check.endswith(valid_domain):
            result = False
            break
    return result


domains = ['.com', '.bg', '.org', '.net']

while True:
    data = input()

    if data == 'End':
        break

    email = data
    symbol = '@'

    if symbol not in email:
        raise MustContainAtSymbolError('Email must contain @')

    username, domain = email.split('@')

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if is_domain_invalid(domain, domains):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(domains)}")

    print('Email is valid')


