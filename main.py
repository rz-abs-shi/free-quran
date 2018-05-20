from tasks import download_surah_task


if __name__ == '__main__':

    for i in range(1, 115):
        if i > 1:
            surah_start_index = 0
        else:
            surah_start_index = 1

        download_surah_task.delay(i, surah_start_index)
