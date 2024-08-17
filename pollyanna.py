import boto3

def text_to_speech(text, output_file):
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
            VoiceId='Camila'  # Você pode escolher a voz que preferir
        )

        # Salva o áudio no arquivo especificado
        with open(output_file, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f"Arquivo salvo como {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
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
    
    output_filename = input("Digite o nome do arquivo de saída : " )
    output_filename = output_filename + ".mp3"
    text_to_speech(input_text, output_filename)

if __name__ == '__main__':
    main()

