



def main():
    with open("b_small.in") as f:
        #read params
        params = f.readline().split()
        #dataset
        raw_dataset = f.readlines()
        dataset = []
        for line in raw_dataset:
            dataset.append(list(line))
        #print for info
        print(params[0]," number of rows")
        print(params[1]," number of columns")
        print(params[2]," minimum of each ingredient par slice")
        print(params[0]," maximum number of cell per slice")

        for i in range(len(dataset)):
            for j in range(len(dataset[i])):
                print(dataset[i][j], end=' ')


# Call main
main()
