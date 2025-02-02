## pydoodle
pydoodle - desktop-игра, по мотивам известной мобильной игры doodle jump.

## Стек технологий
* Python - основной ЯП.
* Pygame - библиотека для создания игры
* Git - система контроля версий

## Ветки для разработки
* dev1 - ветка для разработчика "Азин И.А."
* dev2 - ветка для разработчика "Аликиличова С.Г."


## Быстрый старт
Игра запускается через `pydoodle.py`

## Core
В этой части постараюсь изложить в кратце - зачем нужен Core и его составляющие
В конечной реализации - Core будет предоставлять набор хелперов, используемых моделей, сущностей, констант - все, что нужно для качественного финального проекта.

Какие же здесь есть модули:
* сore/controls - набор контролов для отрисовки их на GUI
* core/examples - примеры с некоторыми сниппетами и задачами по python (для саморазвития и минишпаргалки для разработчиков)
* core/mixins - набор миксинов для расширения стандартных сущностей / моделей
* core/models - здесь хранятся реализованные (или отчасти) и используемые в игре модели-сущности (именно используемые, т.к. сущность Entity - не используется напрямую, в отличие от Effect, Platform, Player)
* core/modules - здесь хранятся модули, необходимые в разработке игры (см `console.py`, `UserInitializer.py`)
* core/scenes - набор сцен, используемых в игре (см. тажке scenes.py)
* core/types - пожалуй, самый интересный подмодуль.
Здесь хранятся все используемые типы в игре.
	* interfaces - интерфейсы и абстрактные классы, реализуемые в игре
	* entity - содержит сущности, используемые игре (большинство нужны для композиции/наследования, а так же реализации описанных интерфейсов)
	* built_in - содержит модули-хелперы, облегчающие работу с примитивными встроенными типами данных (path, date, ...) - пока что не был затронут в разработке

	А так же не забудем про:
	* consts - используемые константы в разработке (некоторые обернуты в class для типизации и структурированности, т.к. в  python нет чистых enum)
	* sounds - используемые в игре звуки (пока что их мало, т.к. добавлялись в последнюю очередь)


Ядро реализовано практически полностью и позволяет масштабировать игру, ее сущности, интерфейсы и другие составляющие.
Суть проста:
- У моделей есть render(отрисовка по атрибутам), update(обновление атрибутов => состояния в будущем), interact(определяет взаимодействие двух моделей => реализация на будущее)
- Эти методы вызываются в основном gameloop (game.py) в нужных секциях (update, render)
- Большинство моделей и сущностей - зависимы от состояния, и в зависимости от этого выполняют определенные действия / отрисовываются определенным образом в зависимости от состояния
(см. `IStateDependent.py`)
## Примечания от разработчиков
Увы, код получился все-таки достаточно грязый, архитектура - далеко не идеальная (так и не вышло использовать модель событий и событийной шины) и так и не удалось реализовать большинство дополнительных желаемых функций.
Также не все задокументировано, как хотелось бы.
Но базовый функционал разработан и есть куда стермиться
