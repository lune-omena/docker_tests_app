# Second Step
import argparse
import os

# Run docker run, and the docker logs
# Ex of docker run:
#sudo docker run -d --name cont_torta \
#  image \
# -i /home/lune/Desktop/pasta/docker_tests_app/requirements.txt \
# -o /data/output 

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
