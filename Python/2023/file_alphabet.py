def main(file = "./test1.txt",write="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    file = open(file,"w")
    for i in range(len(write)):
        #writing letter
        file.write(write[i])
        #new line if divisible by 3
        if (i+1)%3==0:
            file.write("\n")
    file.close()

if __name__ == "__main__":
    main()
