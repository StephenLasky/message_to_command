import sys # to get arguments

input_file_name = "input.txt"
if len(sys.argv) > 1:
    input_file_name = sys.argv[1]

with open("input.txt") as f:
    file = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
file = [x.strip() for x in file]

commands = []

for line in file:
    tokens = line.split()
    addresses = []

    for token in tokens:
        if "0x" in token:
            addresses.append(token)

    if len(addresses) == 4:     # this is done to ensure that we are reading a correct line
        address_start = addresses[0]
        address_size = int(addresses[2], 16)    # now an integer
        command = "x/"+str(address_size)+"i "+address_start
        commands.append(command)





