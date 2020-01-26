from distribuicao_binomial import P
import sys

def main():
    arguments = sys.argv[1:]

    if len(arguments) == 3:
        print(P(float(arguments[0]), int(arguments[1]), int(arguments[2])))
    else:
        print("Operação invalida.")
        print("Para o funcionamento correto do script, execute: python3 main.py prob n k")
        print("prob, n e k são números")


if __name__ == "__main__":
    main()
