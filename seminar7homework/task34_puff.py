""" Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое.
 Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
 Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
 если с ритмом все не в порядке
*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  *** """

true_story = "пара-ра-рам рам-пам-папам па-ра-па-да"
false_story = "пара-ра-рам рам-пам-папам па-ра-па-да-да"

test_rythm = lambda story: "Парам пам-пам" if len(set(map(lambda item: item.count("а"),story.split())))==1 else "Пам парам"

print(test_rythm(true_story))
print(test_rythm(false_story))

"""
Просто для отработки: через лямпбду создаем функцию. В ней применяем конструцию "резлультат if условие else второй_результат"
внутри условия делим список на фразы, к каждую фразу map'им к count("а") получится список вроде [4,4,4] кидаем его в set, если в нем 1 элемент все фразы одинаковые
"""