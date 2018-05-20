from celery import Celery

from quran.crawler import download_surah

app = Celery('tasks', broker='pyamqp://localhost')

@app.task
def download_surah_task(surah_index, verse_start_index):
    while not download_surah(surah_index, verse_start_index):
        pass
