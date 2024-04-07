import sys
import subprocess
import csv

input_file: str = "input.txt"

output_file: str = "output.csv"


with open(input_file, "r") as fin:
    for line in fin:
        curr_sum: int = 0
        command = line.strip()
        print(command)
        command_split = command.split(" ")
        dc_info = command_split[2]
        file_name = command_split[-1]

        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

        lines = result.stdout.splitlines()
        print(lines[5])
        wm = int(lines[5].split(" ")[-1])
        print(lines[6])
        rm = int(lines[6].split(" ")[-1])
        
        curr_sum: int = wm + rm
        print(f"the number of misses is: {curr_sum}")

        csv_line = f"{dc_info}, {file_name}, {curr_sum}"
        
        with open(output_file, "a") as fout:
            fout.write(csv_line+"\n")
            print(f"in {output_file}, the following has been written \"{csv_line}\"")
            print()


print("yeah!")
