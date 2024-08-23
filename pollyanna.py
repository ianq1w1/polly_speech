import boto3

def get_voice_id(language_option):
    """Retorna o VoiceId com base na opção de idioma selecionada pelo usuário."""
    voices = {
        1: {
            'name': 'Camila',  # Voz em português
            'idioma': 'Português - Brasil'
        },
        2: {
            'name': 'Danielle',  # Voz em inglês
            'idioma': 'Inglês - Americano'
        },
        3: {
            'name': 'Conchita',  # Voz em espanhol
            'idioma': 'Espanhol - Espanha '
        },
        4: {
            'name': 'Celine',  # Voz em francês
            'idioma': 'Francês - França'
        }
    }
    
    return voices.get(language_option, {'name': 'Camila', 'language': 'pt-BR'})  # Valor padrão

def text_to_speech(text, output_file, voice_id):
    """Converte o texto em fala e salva no arquivo especificado usando a voz selecionada."""
    # Inicializa o cliente do Amazon Polly
    polly_client = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name=''
    ).client('polly')

    try:
        # Chama o Amazon Polly para sintetizar o texto
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_id
        )

        # Salva o áudio no arquivo especificado
        with open(output_file, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f"Arquivo salvo como {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def show_language_options():
    """Exibe as opções de idiomas e vozes disponíveis para o usuário escolher."""
    print("Escolha o idioma:")
    print("1: Português")
    print("2: Inglês")
    print("3: Espanhol")
    print("4: Francês")

def main():
    show_language_options()
    
    try:
        language_option = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Opção inválida. Por favor, insira um número.")
        return

    if language_option not in [1, 2, 3, 4]:
        print("Opção inválida. Escolha um número entre 1 e 4.")
        return
    
    voice_info = get_voice_id(language_option)
    voice_id = voice_info['name']

    print(f"Você selecionou a voz: {voice_id} ({voice_info['idioma']})")

    print("Modo de operação:")
    print("1: Leitura de arquivo")
    print("2: Leitura direta do texto")
    
    mode = input("Escolha o modo (1 ou 2): ")
    
    if mode == '1':
        file_path = input("Digite o caminho do arquivo de texto: ")
        try:
            with open(file_path, 'r') as file:
                input_text = file.read()
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return
    elif mode == '2':
        input_text = input("Digite o texto para conversão: ")
    else:
        print("Modo inválido. Use 1 para leitura de arquivo ou 2 para leitura direta.")
        return
    
    output_filename = input("Digite o nome do arquivo de saída: ")
    output_filename = output_filename + ".mp3"
    text_to_speech(input_text, output_filename, voice_id)

if __name__ == '__main__':
    main()