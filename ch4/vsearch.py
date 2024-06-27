def search4vowels(word:str) -> set:
    """Выводит гласные, найденные во введенном слове."""
    vowers = set('аеиоуёяюэ')
    return vowers.intersection(set(word))
    