import os
from quran import SurahService
from quran.crawler import get_path_of_verse


def fix_all_surah(reader, audio_base_path='source/media/'):
    surah_service = SurahService.get_instance()

    for index in range(surah_service.get_surah_count()):
        fix_verse_shift_for(reader, index + 1, audio_base_path)


def fix_verse_shift_for(reader, surah_index, audio_base_path='source/media/'):

    surah_service = SurahService.get_instance()

    if surah_index in [1, 9]:
        print("Ignored surah: %d" % surah_index)
        return

    if os.path.isfile(get_path_of_verse(reader, surah_index, 0, base_path=audio_base_path)):
        print("Ignored surah: %d" % surah_index)
        return

    surah_count = surah_service.get_surah_data_base1(surah_index)['count']

    for verse_index in range(1, surah_count + 2):

        current_path = get_path_of_verse(reader, surah_index, verse_index, base_path=audio_base_path)
        to_change_path = get_path_of_verse(reader, surah_index, verse_index - 1, base_path=audio_base_path)

        if not os.path.isfile(current_path):
            print("   Error: there is no file named: " + current_path)

        else:
            os.rename(current_path, to_change_path)

    print("Finished surah: %d" % surah_index)
