
class Singleton(type):
    '''
    singleton consiste em básicamente garantir que uma classe possua somente uma instância durante todo o ciclo de vida\
    de uma aplicação assim como somente um ponto de acesso a essa instância.
    Fonte: http://design-patterns-ebook.readthedocs.io/en/latest/creational/singleton/
    '''
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]
