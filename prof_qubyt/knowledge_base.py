topics = {
    'Variáveis':
        '''Variáveis em Python são usadas para armazenar dados.
        Por exemplo:
        
        nome = João
        idade = 20
        
        Você pode depois utilizar as variáveis novamente apenas as chamando em seu código.
        ''',

    'Loops':
        '''Loops permitem repetir ações.
        Por exemplo utilizando for:
        
        for i in range(5):
            print(i)
        
        
        Exemplo utilizando while:
        
        x = 0
        while x < 5:
        print(x)
        x += 1
        ''',

    'Funções':
        '''Funções são blocos de código reutilizáveis.
        Exemplo:
        def saudacao(nome):
            print(f'Olá, {nome}.)
        
        saudacao('Ale')
        
        '''
}

def get_topic_content(topic):
    return topics.get(topic)