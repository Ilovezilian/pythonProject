import http.client


class music:
    __music_download_pre_url = "https://www.hifini.com/get_music.php?key="

    def getDownLoadPreUrl(self):
        return self.__music_download_pre_url

    def getDownLodUrl(self, key: str):
        return self.getDownLoadPreUrl() + key

    __music_download_file_path = ""

    def getStoreFilePath(self):
        return self.__music_download_file_path

    def downLoadMusic(self):
        http.client.HTTPSConnection(self.getDownLodUrl(key=""))
