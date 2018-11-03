from threading import Thread
from queue import Queue, Empty
from .file import Download
from requests import get, post
from .errors import InvalidResponseError
from tempfile import TemporaryFile
from shutil import copyfileobj


class DownloadManager:
    def __init__(self, max_downloads=10):
        self.queue = Queue()
        self.workers = []
        self.max_downloads = max_downloads

    def enqueue(self, file: Download = None, url: str = None, location: str = None):
        assert ((file is None) and (None in (url, location))) or ((file is not None) and (not all((i is None for i in (url, location)))))

        if file is None:
            file = Download(url=url, location=location)

        self.queue.put(file)
        self._next_download()

    def _next_download(self):
        if len(self.workers) >= self.max_downloads:
            return

        try:
            download = self.queue.get()
        except Empty:
            return


        def do_download():

            try:
                fx = {
                    'GET': lambda: get(download.url, stream=True),
                    'POST': lambda: post(download.url, data=download.data, stream=True),
                }[download.method]
            except KeyError:
                raise KeyError('{method} is not a supported method. Use GET or POST'.format(method=download.method))

            download.on_start(download.url, download.location)

            tf = TemporaryFile()

            size = 0

            try:
                r = fx()
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        tf.write(chunk)
                        size += len(chunk)
            except Exception as e:
                download.on_fail(download.url, download.location, e)
                return

            if not download.verify_response_code(r.status_code):
                download.on_fail(download.url, download.location, InvalidResponseError(r))
                return

            with open(download.location, 'w+b') as rf:
                copyfileobj(tf, rf)

            download.on_complete(download.url, download.location, size)
            self._next_download()

        Thread(target=do_download).start()
