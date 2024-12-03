def generate_sequence(num_seq):
    sequence = []
    number = 1
    while len(sequence) < num_seq:
        sequence.extend([number] * number)
        print(sequence)
        number += 1
    return sequence[:num_seq]


if __name__ == '__main__':
    num_elem = int(input("Введите число элементов последовательности:"))
    result = generate_sequence(num_elem)
    print(" ".join(map(str, result)))
