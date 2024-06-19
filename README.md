### Hexlet tests and linter status:
[![Actions Status](https://github.com/Vladimir3110/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Vladimir3110/python-project-50/actions)  [![Maintainability](https://api.codeclimate.com/v1/badges/ec816e4a62081b73ea3b/maintainability)](https://codeclimate.com/github/Vladimir3110/python-project-50/maintainability) [![auto-tests](https://github.com/Vladimir3110/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Vladimir3110/python-project-50/actions/workflows/pyci.yml) [![Test Coverage](https://api.codeclimate.com/v1/badges/ec816e4a62081b73ea3b/test_coverage)](https://codeclimate.com/github/Vladimir3110/python-project-50/test_coverage)

Описание

Вычислитель отличий - программа принимающая путь к двум файлам и выводящая отличия между ними.

### Применение
```
gendiff -h


usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
### Для этого используйте следующие инструменты:

| Tools                                | Version |
|:------------------------------------:|:-------:|
| python                               |  3.11   |
| [poetry](https://python-poetry.org/) |  1.7.1  |
| [pytest](https://docs.pytest.org/)   |  8.2.1  |
| [flake8](https://flake8.pycqa.org/)  |  7.0.0  |

## Для начала вам необходимо выполнить следующие операции:

| шаг  |                                   инструкция                                                       |
|:----:|:--------------------------------------------------------------------------------------------------:|
|  1   | Клонируйте репозиторий на свой компьютер.:<br/>`git@github.com:Vladimir3110/python-project-50.git` |
|  2   | Перейти в репозиторий<br/>`cd python-project-50`                                                   |
|  3   | Установка приложения на ваш компьютер<br/>`make install`                                           |

*Альтернативный вариант установки::* `python3 -m pip install --user git+github.com/Vladimir3110/python-project-50.git`

[![asciicast](https://asciinema.org/a/664701.svg)](https://asciinema.org/a/664701)

[![asciicast](https://asciinema.org/a/664703.svg)](https://asciinema.org/a/664703)
