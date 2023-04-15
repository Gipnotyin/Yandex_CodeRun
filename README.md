# Yandex_CodeRun
<h1 align="center">Hi there, I'm <a href="https://vk.com/gipnotyin" target="_blank">Ruslan</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Разбор задачек, которые получилось решить :)</h3>


<details>

<summary>Уникальные элементы</summary>

<summary>Условие задачи</summary>

   Задан массив a размера n. Необходимо посчитать количество уникальных элементов в данном массиве. Элемент называется уникальным, если встречается в массиве ровно один раз.
   
<summary>Формат ввода</summary>
   В первой строке входных данных подается одно целое число n. Во второй строке входных данных подается n целых чисел, разделенных пробелами.
   
<summary>Формат вывода</summary>
   В единственной строке выведите ответ на задачу.
   
<summary>Решение</summary>
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Ввод          | Вывод         |
| ------------- | ------------- |
| 5             | 5             |
|1 2 3 4 5      |               |
	
```python
import sys
from collections import defaultdict

def main():
  size = int(input())
  arr = [int(a) for a in input().split()]
  unic = defaultdict(int)
  count = 0
  for a in arr:
    unic[a] += 1
  for a in unic.values():
    if a == 1:
      count+=1
  print(count)


if __name__ == '__main__':
	main()
```
</details>

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Ввод          | Вывод         |
| ------------- | ------------- |
| 5             | 5             |
|1 2 3 4 5      |               |


