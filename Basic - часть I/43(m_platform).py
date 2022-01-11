# Напишите программу на Python, чтобы получить имя ОС, платформу и информацию о выпуске.

import platform # включает в себя инструменты для получения сведений об аппаратной платформе,
                # операционной системе и интерпретаторе на которой выполняется программа.
import os # Модуль os предоставляет множество функций для работы с операционной системой

print(os.name)
print(platform.system())


