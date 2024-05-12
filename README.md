## Порівняння алгоритмів пошуку 
### Time Complexity (TC) of Search Algorithms
#### Алгоритм Кнута-Морріса-Пратта (kmp_search), Алгоритм Боєра-Мура (boyer_moore_search) та Алгоритм Рабіна-Карпа (rabin_karp_search)

| Algorithm  | TC best        | TC worst       |
|------------|----------------|----------------|
| kmp_search | O(n+m)         |  O(n+m)        |
| boyer_moore| O(n/m)         |  O(m*n)        |
| rabin_karp | O(n+m)         |  O(m*n)        |

### Результати тестування

|Pattern             |Area      |kmp_search, sec     |boyer_moore, sec    |rabin_karp, sec     |
|--------------------|----------|--------------------|--------------------|--------------------|
|Existing            |text1     |0.0010666658        |0.0002949704        |0.0022057829        |
|Non-Existing        |text1     |0.0008389979        |0.0005403129        |0.0024201321        |
|--------------------|----------|--------------------|--------------------|--------------------|
|Existing            |text2     |0.0012876400        |0.0004319704        |0.0030851467        |
|Non-Existing        |text2     |0.0012428283        |0.0007878279        |0.0035636058        |

### Висновки:
#### Для тексту 1: 
Як для існуючого патерна, так і для неіснуючого патерна найшвидшим в моєму випадку виявився алгоритм Боєра-Мура.

#### Для тексту 2: 
Як для існуючого патерна, так і для неіснуючого патерна найшвидшим в моєму випадку виявився алгоритм Боєра-Мура.

#### Загальний висновок
Найшвидшим алгоритмом для пошуку підрядка у рядку в моєму випадку виявився алгоритм Боєра-Мура. 
Однак слід зауважити, що мій тест відображаює типовий сценарій використання. У найгіршому випадку даний алгоритм, скоріш за все, не буде оптимальним вибором, бо згідно теоритичної часової складності, наданої вище, найкращу часову складність у найгаршому випадку має Алгоритм Кнута-Морріса-Пратта. Але щоб дослідіти поведінку згаданих алгоритмів у найгіршому випадку, слід протестувати їх на спеціально підготовлених текстах і патернах, які викликають максимально складні випадки для кожного алгоритму.