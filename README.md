# Python

> Anotações dos cursos de Python que realizei.
> 

## Print

Serve para imprimir um conteúdo:

```python
# Print
'Oi'
```

```python
# Print
print("Hello World")
```

Pode ser usado em sequências:

```python
# Draw triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
```

## Variáveis

As variáveis em Python não necessitam de definição de tipo, somente passar o conteúdo basta. Podem ser utilizadas em diferentes funções como o print.

```python
# Variáveis
a = 1
type(a)
```

int

---

```python
# Variables and data types
character_name = "John"
character_age = 50
isMale = True

print("There once was a man named George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didn't like being 70.")

print("There once was a man named", character_name, ",")
print("he was", character_age, "years old. ")
character_name = "Tom"
print("He really liked the name", character_name, ",")
print("but didn't like being", character_age)
```

There once was a man named George,
he was 70 years old.
He really liked the name George,
but didn't like being 70.

There once was a man named John ,
he was 50 years old.
He really liked the name Tom ,
but didn't like being 50

### String

Utilizado para guardar valores como frases. Apresenta diferentes funções de manipulação.

```python
# String
phrase = "Giraffe Academy"

print(phrase)
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[3])
print(phrase.index("G"))
print(phrase.index("Acad"))
print(phrase.replace("Giraffe","Elephant"))

print(phrase + " is cool")

print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\Academy")
```

Giraffe Academy
giraffe academy
GIRAFFE ACADEMY
False
True
15
G
a
0
8
Elephant Academy
Giraffe Academy is cool
Giraffe Academy
Giraffe
Academy
Giraffe"Academy
Giraffe\Academy

Podem também armazenar múltipas linhas em uma string.

```python
Palavra = '''Teste
huhfuf
dsjfjs
bdhfji'''
```

### F String

F Strings possibilitam apresentar os valores de variáveis de forma fácil

```python
# f string
print(f'Seu nome é: {nome}')
```

Seu nome é: Guilherme

### Concatenação

Pode ser realizada a concatenação entre duas strings diferentes:

```python
# Concatenação
'abc' + 'def'
```

### Números

Podem realizar operações básicas e com uso de funções importadas podem realizar processos complexos.

```python
num1 = 1
num2 = 5
num1 + num2
num1 - num2
num1 * num2
num1 / num2
num1 // num2
11 % 2
3 ** 2
```

```python
# Numbers
from math import *

my_num = -5
print(2)
print(2.3323)
print(3  + 4.5)
print(3 * 4)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)
print(my_num)
print(str(my_num) + " my favorite number")
print(abs(my_num))
print(pow(my_num, 2))
print(pow(45, 2))
print(max(4, 6))
print(min(4, 6))
print(round(3.2))
print(round(3.7))
print(floor(3.7))
print(ceil(3.1))
print(sqrt(36))
```

2
2.3323
7.5
12
17
27
1
-5
-5 my favorite number
5
25.0
2025.0
6
4
3
4
3
4
6.0

Também aceita números complexos:

```python
complexo = 3.1 + 4j

```

(3.1+4j)

---

### Boolean

Existem somente dois estados: true e false.

```
# True / False
1 == 2

# False
```

```python
h = True
j = False
type(h)

# bool
```

## Conversão de variáveis

Pode ser realizada a conversão de variáveis por meio de funções de conversão.

String para int:

```python
a = int('2')
```

String para float:

```python
float('10')
```

Int para string:

```python
str(10)
```

Int para bool

*Todos os valores que não são 0 resultam em true.

```python
bool(1)
```

## Inputs

Utilizados para a entrada de valores pelo usuário.

```python
# input()
nome = input("Digite seu nome: ")
print("Seu nome é:", nome)
```

Digite seu nome: Guilherme
Seu nome é: Guilherme

```python
# Inputs
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name + "! You are " + age)
```

Enter your name: Guilherme
Enter your age: 19
Hello Guilherme! You are 19

## Calculadora

```python
# Calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)
```

## Calculadora IMC

```python
peso = input('Qual o seu peso (kg)?: ')
altura = input('Qual a sua altura (m)?: ')
imc = float(peso) / (float(altura) * float(altura))
imc
print(f"O peso digitado foi {peso} e a altura foi {altura} e seu IMC é {imc}")
```

## Calculadora Média

```python
nota_portugues = float(input('Qual a sua nota em português?: '))
nota_matematica = float(input('Qual a sua nota em matemática?: '))
nota_ingles = float(input('Qual a sua nota em inglês?: '))
nota_historia = float(input('Qual a sua nota em história?: '))
media = (nota_portugues + nota_matematica + nota_ingles + nota_historia) / 4

print(f'''
As suas notas foram:
Português: {nota_portugues}
Matemática: {nota_matematica}
Inglês: {nota_ingles}
História: {nota_historia}

E sua média foi: {media}
''')
```

## Mad Libs

```python
# mad libs
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
```

## Listas

Utilizadas para salvar valores em diferentes posições em um conjunto.

```python
# Lists
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends[1])
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
```

Mike
['Kevin', 'Mike', 'Jim', 'Oscar', 'Toby']
Kevin
Toby
['Mike', 'Jim', 'Oscar', 'Toby']
['Mike', 'Jim']

As listas possuem diferentes funções de manipulação:

```python
# List functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends2 = friends,copy()

# friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
# friends.clear()
# friends.pop()
friends.sort()
print(friends.index("Kevin"))
print(friends)
print(friends.count("Jim"))
lucky_numbers.reverse()
print(lucky_numbers)
```

## Tuplas

Ao contrário das listas as tuplas não podem ser modificadas.

```python
# Tuples
coordinates = (4, 5)
 # coordinates[1] = 10
print(coordinates[1])
```

## Funções

As funções são blocos que são realizados por meio de chamadas e podem receber parâmetros para sua realização.

```python
# Functions
def say_hi(name, age):
  print("Hello " + name + ", you are " + str(age))

print("Top")
say_hi("Mike", 35)
say_hi("Steve", 70)
print("Bottom")
```

Top
Hello Mike, you are 35
Hello Steve, you are 70
Bottom

As funções também podem utilizar do return para retornar algum valor.

```python
# Return
def cube(num):
  return num*num*num

result = cube(3)
print(result)
```

27

## if/else

São utilizados como meios para a tomada de decisões com base em condições definidas.

```python
# If statements
is_male = False
is_tall = False

if is_male and is_tall:
  print("You are a tall male")
elif is_male and not(is_tall):
  print("You are a short male")
elif not(is_male) and is_tall:
  print("You are not a male but are tall")
else:
  print("You are not a male and not tall")
```

```python
# If statements (comparisons)
def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

print(max_num(300, 40, 5))
```

## Calculadora 2.0

```python
# Better calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
else:
  print("Invalid operator")
```

## Dicionários

Servem para guardar valores pares chave-valor.

```python
# Dictionaire
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions["Aug"])
```

## Loop while

Usado para repetição de um bloco enquanto ocorrer uma condição.

```python
# While loop
i = 1
while i <= 10:
  print(i)
  i += 1

print("Done with loop")
```

1
2
3
4
5
6
7
8
9
10
Done with loop

## Jogo Adivinhação

```python
# Guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
  if guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1
  else:
    out_of_guesses = True

if out_of_guesses:
  print("Out of guesses, YOU LOSE!")
else:
  print("You win!")
```

## Loop for

Executa o bloco de acordo com a quantidade de elementos em certo objeto.

```python
# For Loop
for letter in "Giraffe Academy":
  print(letter)
```

G
i
r
a
f
f
e

A
c
a
d
e
m
y

```python
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
  print(friend)
```

Jim
Karen
Kevin

```python
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
  print(friends[index])
```

Jim
Karen
Kevin

```python
for index in range(5):
  if index == 0:
    print("First iteration")
  else:
    print("Not first")
```

First iteration
Not first
Not first
Not first
Not first

```python
# Exponent function
def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result

print(raise_to_power(3 , 3))
```

27

```python
# List e nested loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(number_grid[2][1])

for row in number_grid:
  for col in row:
    print(col)
```

1
2
3
4
5
6
7
8
9
0

## Tradutor

```python
# Translator vowels -> g
def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "aeiou":
      if letter.isupper():
        translation = translation + "G"
      else:
        translation = translation + "g"
    else:
      translation = translation + letter
  return translation

print(translate(input("Enter a phrase: ")))
```

## Comentários

“#” Para uma única linha

‘’’ Para várias linhas

```python
# Comments
'''Multiple line comment'''
```

## Try except

Serve como medida para identificação de erros para não realizar a parada somente por um erro.

```python
# Try except
try:
  answer = 10 / 0
  number = int(input("Enter a number: "))
  print(number)
except ZeroDivisionError as err:
  print(err)
except ValueError:
  print("Invalid input")
```

## Leitura arquivos

Pode realizar a leitura do conteúdo de arquivos.

```python
# Reading files
name_file = open("Nomes.txt", "r")
# print(name_file.readable())
# print(name_file.read())
# print(name_file.readline())
for name in name_file.readlines():
  print(name)
# print(name_file.readlines())

name_file.close()
```

## Escrita arquivos

Pode realizar a escrita em arquivos.

```python
# Writing files
name_file = open("Nomes.txt", "w")
name_file.write("\nLeon")
name_file.close
```

## Quiz

```python
# Quiz
class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
```
