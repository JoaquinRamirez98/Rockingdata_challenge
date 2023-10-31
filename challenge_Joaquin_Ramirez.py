import boto3
import os

def descargar_datos_s3(aws_access_key, aws_secret_key, bucket_name, file_paths, local_directory):
    try:
        # Configurar el cliente de S3 con las credenciales proporcionadas
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        
        for file_path in file_paths:
            # Nombre del archivo local
            local_file_path = os.path.join(local_directory, file_path)
            
            # Descargar el archivo desde S3 al sistema local
            s3.download_file(bucket_name, file_path, local_file_path)
            print(f'Archivo {file_path} descargado exitosamente como {local_file_path}')
    except Exception as e:
        print(f'Error al descargar el archivo: {str(e)}')

# Define las credenciales y rutas de los archivos
aws_access_key = 'AKIA2NU5TZR6RVMXSOKK'
aws_secret_key = '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'
bucket_name = 'desafio-rkd'
file_paths = ['disney_plus_titles.csv', 'netflix_titles.csv']
local_directory = r'D:\cursos\challenge rockingdata'  # Directorio local donde se guardarán los archivos

# Llama a la función para descargar los archivos
descargar_datos_s3(aws_access_key, aws_secret_key, bucket_name, file_paths, local_directory)
