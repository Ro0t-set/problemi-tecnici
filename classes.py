import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prenotazione_tecnico.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)


import math
import string
#from django.contrib.auth.models import User
from app.models import Aula
#from app.models import Corso
#from django.shortcuts import get_object_or_404


for classe in range(1,6):
    for sezione in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p"]:
        nome = str(classe) + sezione
        if (nome in ["1m", "2m", "1o", "2o", "4o", "1n", "2n", "1p", "2p", "4p", "5p", "2d", "2l"]) == False:
            Aula.objects.create(aule=nome)
            print('creating {0}'.format(nome))
