from knowledge_base import get_topic_content
from progress import save_progress, load_progress
from quiz import start_quiz

def show_menu():
    print('\nOlá! Eu sou o prof QuByt, seu tutor de programação!')
    print('O que você quer fazer hoje?')
    print('1 - Estudar um tópico novo')
    print('2 - Continuar de onde parei')
    print('3 - Fazer um quiz')
    print('0 - Sair')

def main():
    progress = load_progress()

    while True:
        show_menu()
        choice = input('Digite a opção: ').strip()

        if choice == '1':
            topic = input('Digite o tópico que deseja estudar: ').strip().lower()
            content = get_topic_content(topic)

            if content:
                print(f'\nTópico: {topic.title()}\n{content}')
                progress['last_topic'] = topic
                save_progress(progress)

            else:
                print('Tópico não encontrado.')

        elif choice == '2':
            topic = progress.get('last_topic')
            if topic:
                print(f'\nRetomando o tópico: {topic.title()}')
                print(get_topic_content(topic))
            else:
                print('Nenhum progresso anterior encontrado')

        elif choice == '3':
            start_quiz()

        elif choice == '0':
            print('Até mais! Bons estudos!')
            break

        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()