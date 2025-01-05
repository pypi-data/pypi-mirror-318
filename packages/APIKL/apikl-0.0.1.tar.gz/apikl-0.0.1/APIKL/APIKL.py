from os import listdir
from os.path import isfile, join, splitext
from APIKL.Found import Found
import math
import re


def get_chance(password):
    chance = 0
    if re.match(r"[\w:!@.#$%&*(\[\])=\-+]+", password) and len(password) >= 8:
        byte_values = password.encode()
        frequency_array = [0] * 256

        for byte_val in byte_values[:-1]:
            frequency_array[byte_val] += 1

        ent = 0
        total_bytes = len(byte_values) - 1

        for freq in frequency_array:
            if freq != 0:
                prob_byte = freq / total_bytes
                ent -= prob_byte * math.log2(prob_byte)
        chance += (math.log(ent) * 10 % 10 * 1.9 + 1) if ent >= 3 else 0
    return chance


class APIKL:
    def __init__(self, files_to_check=None, probability: int = 5):
        if files_to_check is None:
            files_to_check = ['.']
        self._found = []
        self._files_to_check = self.files(files_to_check)
        self._probability = probability

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, probability):
        self._probability = probability

    @property
    def files_to_check(self):
        return self._files_to_check

    @files_to_check.setter
    def files_to_check(self, files_to_check):
        self._files_to_check = files_to_check

    def files(self, files_to_check):
        out = []
        for file in files_to_check:
            if not isfile(file):
                out += self.rec_file(file)
            else:
                out.append(file.replace('\\', '/'))
        return out

    def rec_file(self, directory):
        files = []
        # Проверяем, является ли directory директорий
        if not isfile(directory):
            # Получаем список всех файлов и поддиректорий внутри текущей директории
            contents = [join(directory, f) for f in listdir(directory)]
            # Рекурсивный обход поддиректорий
            for item in contents:
                if isfile(item):
                    files.append(item.replace('\\', '/'))
                else:
                    files.extend(self.rec_file(item))
        else:
            # Если это файл, добавляем его в список
            files.append(directory)

        return files

    def check_file(self, file_path):
        try:
            _, extension = splitext(file_path)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = [line.lower().strip() for line in file]

            if extension == '.xml':
                for i, line in enumerate(lines):
                    self.check_xml_pass(line, i, file_path)
            else:
                for i, line in enumerate(lines):
                    self.check_pass(line, i, file_path)

        except FileNotFoundError as e:
            raise RuntimeError from e

    def check_pass(self, line, i, file):
        if '"' in line:
            sign = '"'
        elif "'" in line:
            sign = "'"
        else:
            return

        pass_to_add = ""
        chance = 0
        self.match_and_add(line, i, file, sign, pass_to_add, chance)

    def match_and_add(self, line, i, file, sign, pass_to_add, chance):
        pattern = rf"{sign}(.*?){sign}"
        matches = re.findall(pattern, line)

        for match in matches:
            password = match.strip()
            current_chance = get_chance(password)

            if current_chance > chance:
                chance = current_chance
                pass_to_add = password

        if chance >= 1:
            # Добавляем найденную информацию в список 'found'

            self._found.append(Found(str(file), i + 1, chance, pass_to_add))

    def check_xml_pass(self, line, i, file):
        count = line.count('<')

        if count >= 1:
            if '"' in line:
                sign = '"'
            elif "'" in line:
                sign = "'"
            else:
                sign = None

            pass_to_add = ""
            chance = 0

            if count == 2:
                password = line[line.find('>') + 1:line.rfind('<')].strip()
                current_chance = get_chance(password)

                if current_chance > chance:
                    chance = current_chance
                    pass_to_add = password

            if sign:
                self.match_and_add(line, i, file, sign, pass_to_add, chance)
        else:
            password = line.strip()
            chance = get_chance(password)

            if chance >= 1:
                # Добавить в список 'found'
                self._found.append(Found(str(file), i + 1, chance, password))

    def find_keys(self, files_to_check: list = None):
        if files_to_check is None:
            files = self._files_to_check
        else:
            files = self.files(files_to_check)
        for file in files:
            self.check_file(file)
        found = filter(lambda x: x.get_output_key_chance() >= self._probability,
                       sorted(self._found, key=lambda x: x.get_output_key_chance(), reverse=True))
        print('Found:')
        for f in found:
            print(f"      {f.password} at {f.file_name}:{f.line} with probability {f.get_output_key_chance()}")
