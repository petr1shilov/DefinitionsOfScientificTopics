hello_message_text = 'Привет, я Умный бот 🤖'
start_message_text = ('Я создан, что бы определять категории в научных статей.\n'
                      'Работать со мной очень просто!\n'
                      'Просто отправьте мне файл с научной работой в формате excel, а дальше я сделаю все сам!\n')

pdf_message_text = 'Отправьте, пожалуйста, файл pdf'

warning_pdf_message = ('К сожалению, это не pdf ☹️\n'
                       'Отправьте, пожалуйста, файл в формате excel')

waiting_message = 'Идет фильтрация. Пожалуйста, подождите'


candidates_system_prompt = 'Тебе необходимо определить Перечень компетенций, областей научных интересов лаборатории или центра на русском языке\nОтвет должен быть на Русском языке\nВыведи ответ в виде list, Пример: [Образовательные программы и консалтинг в сфере организации образовательных программ в междичциплинарной области программирования и науки (исследований)","Программное обеспечение для научных исследований  / аналитики / моделирования","Разработка систем для моделирования физических процессов","Консалтинг и независимый аудит технологических решений / научного ПО программного кода и связи ПО с технологическими решениями (например, работоспособность ПО на конкретном оборудовании, эффективность ПО в конкретном бизнес-процессе)","Автономные и интегрированные системы моделирования","Моделирование методом Монте-Карло","Моделирование дискретных систем,"Распределенное и параллельное моделирование,"Гетерогенные распределительные системы","Новые системы моделирования на основе сетей Байесовских методов","Языки программирования: Kotlin, Python, Julia, Java"]'

total_system_prompt = 'Тебе необходимо подитожить список и вывести конечный вариант на русском языке\nОтвет должен быть на Русском языке\nВыведи ответ в виде list, Пример: [Образовательные программы и консалтинг в сфере организации образовательных программ в междичциплинарной области программирования и науки (исследований)","Программное обеспечение для научных исследований  / аналитики / моделирования","Разработка систем для моделирования физических процессов","Консалтинг и независимый аудит технологических решений / научного ПО программного кода и связи ПО с технологическими решениями (например, работоспособность ПО на конкретном оборудовании, эффективность ПО в конкретном бизнес-процессе)","Автономные и интегрированные системы моделирования","Моделирование методом Монте-Карло","Моделирование дискретных систем,"Распределенное и параллельное моделирование,"Гетерогенные распределительные системы","Новые системы моделирования на основе сетей Байесовских методов","Языки программирования: Kotlin, Python, Julia, Java"]'
