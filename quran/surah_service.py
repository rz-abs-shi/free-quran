import json


class SurahHandler:

    def __init__(self, path_to_data):
        with open(path_to_data, 'r') as f:
            surah_data = f.read()
            self.__surah_json__ = json.loads(surah_data)

    def get_surah_data(self, i):
        return self.__surah_json__[i]

    def get_surah_data_base1(self, i):
        return self.__surah_json__[i - 1]

    def get_all_surah_data(self):
        return self.__surah_json__

    def get_surah_count(self):
        return len(self.__surah_json__)


class SurahService:
    path_to_surah_data = 'source/surah.json'

    __instance = SurahHandler(path_to_surah_data)

    @classmethod
    def get_instance(cls):
        return cls.__instance