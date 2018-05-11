import requests
from quran import SurahService
import os
import errno


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


def download_verse(surah_index, verse_index):

    surah_data = SurahService.get_instance()

    def index_to_code(index):
        code = str(index + 1)
        return '0' * (3 - len(code)) + code

    surah_code = index_to_code(surah_index)
    verse_code = index_to_code(verse_index)

    url = 'http://www.clearquran.com/mp3_alafasy_64kbps/{surah_code}{verse_code}.mp3'.format(
        surah_code=surah_code, verse_code=verse_code
    )

    file_path = 'source/media/alafasi/{surah_code}/{verse_code}.mp3'.format(
        surah_code=surah_code,
        verse_code=verse_code,
    )

    save_file(url, file_path)
