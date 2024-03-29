# Міністерство освіти та науки України
# Львівський Національний Університет Природокористування
# Факультет механіки та енергетики
# Кафедра інформаційних систем та технологій

# Звіт про виконання практичної роботи №3
# "Поведінкові" паттерни.

# Мета роботи - освоїти роботу з породжвальними паттернами в Python3.

# Завдання
1. Дати теоретичний опис "Поведінкових" паттернів.
2. Дати теоретичний опис вибраного шаблону з групи паттернів.
3. Зобразити UML-діаграму даного шаблону.
4. Створюємо простеньку, щоб наприкладі продемонструвати роботу паттерна "Спостерігач". 


# Хід роботи
Породжувальні паттерни - це шаблони проектування, які вирішують завдання ефективної та безпечної взаємодії між об'єктами програми. Ось кілька з найвідоміших породжувальних паттернів:

   - Ланцюжок обов'язків (Chain of Responsibility): Цей паттерн дозволяє створити ланцюжок обробників (об'єктів), кожен з яких може спробувати обробити запит перед передачею його наступному обробнику у ланцюжку.

   - Команда (Command): Паттерн "Команда" вкладає запити у об'єкти, що дозволяє вас створювати інкапсульовані об'єкти-команди, які можна виконувати, відкладати або скасовувати.

   - Ітератор (Iterator): Цей паттерн надає уніфікований спосіб доступу до елементів колекції, не розголошуючи її внутрішньої структури.

   - Посередник (Mediator): Паттерн "Посередник" визначає об'єкт-посередник, який сприяє взаємодії між об'єктами в системі, замість того, щоб дозволяти їм взаємодіяти напряму.

   - Знімок (Memento): Паттерн "Знімок" дозволяє зберігати стан об'єкта і відновлювати його в майбутньому до попереднього стану.

   - Спостерігач (Observer): В цьому паттерні визначається відношення "один до багатьох", де об'єкт-спостерігач стежить за змінами в інших об'єктах-суб'єктах і автоматично отримує повідомлення про їхні зміни.

   - Стан (State): Паттерн "Стан" дозволяє об'єкту змінювати свою поведінку при зміні внутрішнього стану, при цьому це змінює зовнішній вигляд, що робить його схожим на замінувачі об'єкта.

   - Стратегія (Strategy): Цей паттерн визначає набір алгоритмів і дозволяє вибирати один з них на льоту, залежно від ситуації.

   - Шаблонний метод (Template Method): Паттерн "Шаблонний метод" надає загальну структуру алгоритму, дозволяючи підкласам перевизначити окремі кроки алгоритму, не змінюючи його загальної структури.

   - Відвідувач (Visitor): Цей паттерн дозволяє додавати нові функціональність до групи об'єктів, не модифікуючи їхніх класів, шляхом визначення зовнішнього об'єкта-відвідувача, який обчислює нову функціональність для кожного об'єкта.

Кожен з цих паттернів розв'язує конкретні проблеми в проектуванні програмного коду та сприяє покращенню його якості та структури.

2. Поведінковий паттерн "Спостерігач" -  це поведінковий патерн проектування, який створює механізм підписки, що дає змогу одним об’єктам стежити й реагувати на події, які відбуваються в інших об’єктах. Основними учасниками цього паттерну є:

   - Суб'єкт (Subject): Це об'єкт, який веде список спостерігачів і надсилає їм повідомлення про зміни свого стану. Суб'єкт може бути конкретним суб'єктом, який реалізує логіку додавання та видалення спостерігачів та повідомлення їх.

   - Спостерігач (Observer): Це об'єкт, який слухає зміни в суб'єкті і реагує на них. Спостерігачі реалізують певний інтерфейс або абстрактний клас, який містить методи для отримання оновлень від суб'єкта.

   - Конкретний суб'єкт (Concrete Subject): Це реалізація суб'єкта, який має конкретну логіку та структуру. Він веде список спостерігачів та надсилає їм повідомлення про зміни.

   - Конкретний спостерігач (Concrete Observer): Це реалізація спостерігача, яка визначає, як реагувати на оновлення від суб'єкта. Конкретні спостерігачі можуть мати власний стан та логіку обробки повідомлень.

   - Інтерфейс або абстрактний клас спостерігача (Observer Interface/Abstract Class): Це інтерфейс або абстрактний клас, який визначає методи, які повинні бути реалізовані всіма конкретними спостерігачами.

Учасники паттерну "Спостерігач" працюють разом для створення механізму підписки та сповіщення про зміни в об'єктах. Спостерігачі підписуються на суб'єкта, а коли стан суб'єкта змінюється, вони отримують сповіщення та відповідають на нього відповідно до своєї логіки. Цей паттерн дозволяє реалізувати реактивну модель програмування, де об'єкти реагують на події та зміни стану інших об'єктів.

Основна ідея паттерну "Спостерігач" (Observer) полягає в тому, щоб встановити залежність "один до багатьох" між об'єктом-суб'єктом і об'єктами-спостерігачами таким чином, щоб при зміні стану суб'єкта всі спостерігачі, які підписані на цей суб'єкт, автоматично отримували сповіщення та могли реагувати на ці зміни.

Основні переваги паттерну "Спостерігач" (Observer) включають:

   - Зменшення залежностей: Суб'єкти та спостерігачі взаємодіють через абстрактний інтерфейс, що дозволяє підтримувати слабке зв'язування між ними. Зміни в одному компоненті не вимагають змін в інших компонентах.

   - Легка розширюваність: Ви можете додавати нові спостерігачі та суб'єкти без змін у існуючому коді. Це спрощує розширення системи.

   - Інкапсуляція: Спостерігачі і суб'єкти інкапсулюють свою логіку, що дозволяє розділити відповідальності та зробити код більш читабельним.

   - Автоматичне сповіщення: Спостерігачі автоматично отримують сповіщення від суб'єкта при зміні його стану. Це робить можливим автоматичну реакцію на події без необхідності активно опитувати суб'єкт.

   - Системи реакції на події: Паттерн "Спостерігач" широко використовується в системах, що реагують на події (Event-Driven Systems), таких як графічні інтерфейси користувача, системи повідомлень та інші, де важливо слідкувати за змінами стану об'єктів.

   - Збереження часу та ресурсів: Спостерігачі активуються лише при виникненні подій, тобто вони не виконують зайвої роботи, якщо нічого не змінилося.

Паттерн "Спостерігач" дозволяє створювати більш гнучкі та реактивні програми, а також полегшує обробку подій та оновлень у системах.

3. ![UML-діаграма паттерна "Спостерігач"](./structure-indexed.png)

4. Створимо [простеньку програму](./oop0910.py), щоб на прикладі продемонструвати роботу паттерна "Спостерігач".

# Висновок
У цій практичній роботі ми успішно вивчили паттерн "Спостерігач" (Observer) і його застосування в програмуванні, а також розглянули основні переваги цього паттерна, такі як зменшення залежностей між компонентами, легка розширюваність системи, інкапсуляція логіки, автоматичне сповіщення та його використання у системах реакції на події. Ми також побудували UML-діаграму паттерна "Спостерігач" і створили прикладну програму, яка ілюструє роботу цього паттерна в практиці. Паттерн "Спостерігач" є корисним інструментом для реалізації реактивної моделі програмування, де об'єкти можуть реагувати на події та зміни стану інших об'єктів. Він дозволяє створювати більш гнучкі, реактивні та підтримувані системи, що реагують на події та оновлення. Важливо підкреслити, що вивчення паттернів проектування допомагає підвищити якість та гнучкість програмного коду, а паттерн "Спостерігач" є одним з важливих інструментів для реалізації реактивної логіки у програмах. 