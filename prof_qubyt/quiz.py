questions = [
    {
        'question': 'Qual é a palavra-chave para definir uma função em Python?',
        'options': ['fun', 'define', 'def', 'function'],
        'answer': 'def'
    },
    {
        'question': 'Qual dessas estruturas é usada para repetição?',
        'options': ['if', 'for', 'try', 'import'],
        'answer': 'for'
    }
]

def start_quiz():
    print('\n Iniciando o quiz!')
    score = 0
    for q in questions:
        print(f'\n{q['question']}')
        for i, opt in enumerate(q['options'],1):
            print(f'{i}. {opt}')
        choice = input('Escolha a opção correta (1-4): ')
        try:
            if q['options'][int(choice)-1] == q['answer']:
                print('Correto!')
                score += 1
            else:
                print(f'Errado! Alternativa certa: {q['answer']}')
        except:
            print('Opção inválida.')
    print(f'\nVOcê acertou {score}/{len(questions)} perguntas.')