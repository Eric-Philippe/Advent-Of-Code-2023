def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        total_sum = 0

        last_value = int(lines[0])
        for i in range(1, len(lines)):
            new_value = int(lines[i])
            if new_value > last_value:
                total_sum += 1
            last_value = new_value

    return total_sum

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        last_sum = None
        total_sum = 0
        for i in range(0, len(lines) - 2):
            current_sum = get_sum_of_next_three(i, lines)
            if last_sum is not None:
                if current_sum > last_sum:
                    total_sum += 1
            last_sum = current_sum

    return total_sum


def get_sum_of_next_three(current_index, list):
    sum = 0
    for i in range(current_index, current_index + 3):
        sum += int(list[i])
    return sum

if __name__ == "__main__":
    input_path = "./2022/day_01/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))