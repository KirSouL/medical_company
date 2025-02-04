from django.core.cache import cache

from medical.models import Medical
from config.settings import CACHE_ENABLED


def get_medicals():
    """ Получение набора услуг либо из БД (в случае пустого кеша), либо из кеша """
    if not CACHE_ENABLED:
        return Medical.objects.all()

    key_medicals_list = "medicals_list"
    medicals = cache.get(key_medicals_list)

    if medicals is None:
        medicals_list = Medical.objects.all()
        cache.set(key_medicals_list, medicals_list)
        return medicals
    else:
        return medicals
