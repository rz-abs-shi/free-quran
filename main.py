from quran.crawler import download_verse, download_surah


if __name__ == '__main__':

    for i in range(2, 114):
        download_surah(i)

