def search4vowels(word:str) -> set:
    """Выводит гласные, найденные во введенном слове."""
    vowers = set('аеиоуёяюэaeiouy')
    return vowers.intersection(set(word))

def search4letters(phrase:str, letters:str='аеиоуёяюэaeiouy') ->set:
    """Возвращает множество букв из 'letters', найденных
      в указанной фразе."""
    # set(letters) - создаёт обьект множества из letters.

    # .intersection - находит пересечение множества созданного
    # из letters с множеством созданным из phrase.
    return set(letters).intersection(set(phrase))
    