def vercmp(v1, v2):
    """
    Сравнивает две строки версий RPM.
    Возвращает:
     1, если v1 новее (больше) v2
    -1, если v1 старее (меньше) v2
     0, если версии равны
    """
    # Если строки идентичны, версии равны
    if v1 == v2:
        return 0

    # Преобразуем в строки, если переданы не строки
    s1 = str(v1)
    s2 = str(v2)

    p1, p2 = 0, 0
    l1, l2 = len(s1), len(s2)

    while p1 < l1 or p2 < l2:
        # 1. Пропускаем разделители (не буквенно-цифровые), кроме тильды (~)
        while p1 < l1 and not s1[p1].isalnum() and s1[p1] != '~':
            p1 += 1
        while p2 < l2 and not s2[p2].isalnum() and s2[p2] != '~':
            p2 += 1

        # 2. Обработка тильды (~). Она сортируется ДО конца строки и любых символов.
        # Версия с тильдой считается СТАРЕЕ.
        c1 = s1[p1] if p1 < l1 else None
        c2 = s2[p2] if p2 < l2 else None

        if c1 == '~' or c2 == '~':
            if c1 == '~' and c2 != '~':
                return -1  # s1 имеет тильду, значит она старее
            if c1 != '~' and c2 == '~':
                return 1  # s2 имеет тильду, значит s1 новее
            # Если у обоих тильда, пропускаем и идем дальше
            p1 += 1
            p2 += 1
            continue

        # 3. Обработка конца строки
        # Если одна строка закончилась, а другая нет (и это не тильда),
        # то более длинная версия считается новее.
        if p1 >= l1 and p2 >= l2: return 0
        if p1 >= l1: return -1
        if p2 >= l2: return 1

        # 4. Выделяем сегменты (числовые или буквенные)
        start1, start2 = p1, p2

        # Определяем тип сегмента: цифры или буквы
        is_digit1 = s1[p1].isdigit()
        is_digit2 = s2[p2].isdigit()

        # Если типы разные: цифры всегда "новее" букв
        if is_digit1 != is_digit2:
            return 1 if is_digit1 else -1

        # Читаем сегмент целиком
        if is_digit1:
            while p1 < l1 and s1[p1].isdigit(): p1 += 1
            while p2 < l2 and s2[p2].isdigit(): p2 += 1

            # Числовое сравнение (игнорируем ведущие нули)
            # Преобразуем в int для корректного сравнения (2 > 10 -> False)
            val1 = int(s1[start1:p1])
            val2 = int(s2[start2:p2])
            if val1 > val2: return 1
            if val1 < val2: return -1
        else:
            while p1 < l1 and s1[p1].isalpha(): p1 += 1
            while p2 < l2 and s2[p2].isalpha(): p2 += 1

            # Лексикографическое сравнение букв
            val1 = s1[start1:p1]
            val2 = s2[start2:p2]
            if val1 > val2: return 1
            if val1 < val2: return -1

    return 0