def part_one(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
    print("Not implemented yet")

def part_two(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
    print("Not implemented yet")

if __name__ == "__main__":
    YEAR = None
    DAY = None
    if YEAR is None or DAY is None:
        raise Exception("YEAR and DAY must be set")
    input_path = "./" + str(YEAR) + "/day_" + str(DAY).zfill(2) + "/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))