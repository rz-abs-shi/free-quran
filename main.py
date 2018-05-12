from quran.crawler import download_verse, download_surah


if __name__ == '__main__':

    for i in range(1, 115):
        if i > 1:
            surah_start_index = 0
        else:
            surah_start_index = 1

        while not download_surah(i, surah_start_index):
            pass
