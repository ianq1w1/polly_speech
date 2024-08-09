import boto3
import sys

def text_to_speech(text, output_file):
    # Inicializa o cliente do Amazon Polly
    polly_client = boto3.Session(
        aws_access_key_id='YOUR_AWS_ACCESS_KEY',
        aws_secret_access_key='YOUR_AWS_SECRET_KEY',
        region_name='YOUR_AWS_REGION'
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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python script.py 'Seu texto aqui'")
        sys.exit(1)

    input_text = sys.argv[1]
    output_filename = 'output.mp3'
    text_to_speech(input_text, output_filename)
