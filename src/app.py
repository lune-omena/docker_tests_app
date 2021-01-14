# Third Step
import argparse
import pandas as pd
import os

# Run docker run, and then docker logs to see the output
# Ex: 
# sudo docker run -d \
# -v /home/path/docker_tests_app/data:/data/ \
# --name torta imagem \
# -i /data/input/data.csv  \
# -o /data/output

def data_transform(input_file, output_path):
    df = pd.read_csv(input_file, sep='\t')
    df['changed_number'] = df.random_number % 100
    print(df)

    df.to_csv(output_path+str("/changed_data.csv"), sep='\t', index=False)
    
def hello(**args):
    result = ""

    if args['input']:   
        result += args['input'] + str("\n")

        if os.path.isfile(args['input']):
            print(f"{args['input']} é arquivo input válido.")

    if args['output']:
        result += args['output'] + str("\n")

        if os.path.isdir(args['output']):
            print(f"{args['output']} é output válido.")

            if os.path.isfile(args['input']):
                data_transform(args['input'], args['output'])

    print("Cheguei aqui!")
    result += "Hello World!"

    print(result)

if __name__ == "__main__":
    # Pegando argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", help="Input path file")
    parser.add_argument("--output", "-o", help="Output path file")
    # Transformando em dicionario
    args = vars(parser.parse_args())
    print(args)

    # passando argumentos para funcao principal
    hello(**args)
