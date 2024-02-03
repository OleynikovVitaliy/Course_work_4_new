from abc import ABC, abstractmethod

import requests as requests
import os

from config import URL_HH, URL_SJ


class WorkApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_info(self):
        pass


class HeadHunter(WorkApi):
    """Класс для работы с API HeadHunter"""

    def __init__(self, text: str, per_page: int, city: int):
        self.text = text
        self.per_page = per_page
        self.area = city

    def get_info(self):
        """
        Получает список вакансий
        :return: list
        """
        response = requests.get(URL_HH, params=self.__dict__)
        info = response.json()['items']
        return info


class SuperJob(WorkApi):
    """Класс для работы с API SuperJob"""

    API_KEY = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}

    def __init__(self, text: str, t=None, c=None):
        self.keyword = text
        self.t = t
        self.c = c

    def get_info(self):
        """
        Получает список вакансий
        :return: list
        """
        response = requests.get(URL_SJ, headers=self.API_KEY, params=self.__dict__)
        info = response.json()['objects']
        return info
