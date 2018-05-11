import requests


def save_file(url, file_path):
    res = requests.get(url)
    with open(file_path, 'wb') as wf:
        wf.write(res.content)


def download_verse(surah_number, verse_number):

    pass


