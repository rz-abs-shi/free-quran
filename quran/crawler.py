import requests
from quran import SurahService
import os
import errno
import os.path


def save_file(url, file_path):
    res = requests.get(url)

    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(file_path, 'wb') as wf:
        wf.write(res.content)


def download_verse(surah_index, verse_index, ignore_if_exist=True):
    def index_to_code(index):
        code = str(index)
        return '0' * (3 - len(code)) + code

    surah_code = index_to_code(surah_index)
    verse_code = index_to_code(verse_index)

    file_path = 'source/media/alafasi/{surah_code}/{verse_code}.mp3'.format(
        surah_code=surah_code,
        verse_code=verse_code,
    )

    if ignore_if_exist and os.path.isfile(file_path):
        print ("ignored " + file_path)
        return
    else:
        print (file_path)

    url = 'http://www.clearquran.com/mp3_alafasy_64kbps/{surah_code}{verse_code}.mp3'.format(
        surah_code=surah_code, verse_code=verse_code
    )

    save_file(url, file_path)


def download_surah(surah_index, verse_start_index=0, ignore_if_verse_exist=True):

    surah_data = SurahService.get_instance().get_surah_data(surah_index - 1)

    for verse_index in range(verse_start_index, surah_data['count']):
        print("Downloading surah {surah_index}. {surah_title}; all: {all_verses}; "
              "progress: {progress}".format(
            surah_index=surah_data['index'],
            surah_title=surah_data['title'],
            all_verses=surah_data['count'],
            progress=verse_index
        ))

        try:
            download_verse(surah_index, verse_index, ignore_if_exist=ignore_if_verse_exist)

        except Exception as e:
            print('Error occurred in downloading verse {verse} of {surah} surah'.format(
                verse=verse_index, surah=surah_index
            ))
            print(e)

            return False

    print("Downloading finished successfully.")

    return True