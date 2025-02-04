from django.core.cache import cache

from staff.models import StaffMedical
from config.settings import CACHE_ENABLED


def get_staffs():
    """ Получение списка персонала либо из БД (в случае пустого кеша), либо из кеша """
    if not CACHE_ENABLED:
        return StaffMedical.objects.all()

    key_staffs_list = 'staffs_list'
    staffs = cache.get(key_staffs_list)

    if staffs is None:
        staffs_list = StaffMedical.objects.all()
        cache.set(key_staffs_list, staffs_list)
        return staffs
    else:
        return staffs
