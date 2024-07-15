import csv

def convert_digit_to_number(digit):
    # Convert a single digit string to its corresponding number
    if "30" <= digit <= "39":
        return str(int(digit) - 30)
    else:
        return digit

def main():
    input_filename = "./GR0005_TH1_MAGNUMV-2_INI_FTH1N3221AH_20231214143209_61.asc"
    input_temp_csv = "./C_KR0700.csv_temp"
    output_filename = "./output.asc"

    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file, open("./output_Test.txt", 'w') as output_file_test:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                   "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                   "W", "X", "Y", "Z"]

        digit = ["41", "42", "43", "44", "45", "46", "47", "48", "49", 
                 "4A", "4B", "4C", "4D", "4E", "4F", "4G", "4H", "4I", 
                 "4J", "4K", "4L", "4M", "4N", "4O", "4P", "4Q"]

        for line in reader:
            first_line = []
            all_line = []

            if "STN" in line:
                first_line.extend(line[:5])
            else:
                if len(line) == 23:
                    all_line.extend([line[0], line[1], line[3], line[4]])
                    # First character
                    for i in range(26):
                        if line[5] == digit[i]:
                            line[5] = letters[i]

                    # Second character
                    digit_value = int(line[6]) - 35
                    if 0 <= digit_value <= 26:
                        line[6] = letters[digit_value]

                    # From third character
                    line[7:22] = map(convert_digit_to_number, line[7:22])

                    all_line.append(line[22])

            string_compare = ''.join(line[5:22])
            output_file_test.write(string_compare + '\n')

            with open(input_temp_csv, 'r') as input_temp:
                for line2 in input_temp:
                    vec_find = line2.strip().split('=')
                    if len(vec_find) == 2:
                        output_file_test.write(f"{vec_find[0]} {vec_find[1]}\n")
                        if string_compare == vec_find[1]:
                            vec_found = vec_find[0]
                            all_line.append(vec_found + "000.00")
                        else:
                            all_line.append("unknown     ")

            if first_line:
                writer.writerow(first_line)

            if len(all_line) == 6:
                writer.writerow(all_line)

    print("Data write successfully, please check output file !")

if __name__ == "__main__":
    main()
