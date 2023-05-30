import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicjalizacja przeglądarki - przykład dla Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)  # Czekaj maksymalnie 10 sekund na pojawienie się elementów

    def test_add_tasks(self):
        # Krok 1: Przejdź do strony z aplikacją
        self.driver.get("https://todolist.james.am/#/")

        # Krok 2: Dodanie nowego elementu do listy
        new_task_input = self.driver.find_element(By.CLASS_NAME, "new-todo")
        new_task_input.send_keys("Newtask")
        new_task_input.send_keys('\ue007')

        new_task_input.send_keys("Newtask2")
        new_task_input.send_keys('\ue007')

        # Sprawdź, czy zadania zostały prawidłowo dodane
        task_list = self.driver.find_element(By.CLASS_NAME, "todo-list")
        tasks = task_list.find_elements(By.TAG_NAME, "li")
        self.assertEqual(len(tasks), 2)  # Oczekujemy, że są dokładnie 2 zadania na liście
        self.assertEqual(tasks[0].text, "Newtask")  # Oczekujemy, że pierwsze zadanie ma tekst "Newtask"
        self.assertEqual(tasks[1].text, "Newtask2")  # Oczekujemy, że drugie zadanie ma tekst "Newtask2"

        # Potwierdzenie poprawności testu
        print("Test zakończony sukcesem. Zadania zostały prawidłowo dodane.")

        # Zapisz zrzut ekranu
        self.driver.save_screenshot("screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Zamknij przeglądarkę po zakończeniu testów
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
