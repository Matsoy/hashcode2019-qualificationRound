import copy
import datetime
import math
import time
import sys
from   photo import Photo
from   algo import Algo

class Main:
    def __init__(self, file_prefix):
        """
        Constructor

        :param file_prefix: The prefix of the input file. e.g. "a"
        """
        self.file_prefix     = file_prefix
        self.input_file_path = "inputs/" + file_prefix + ".txt"
        self.photos_list      = []
        self.read_input_file()


    def read_input_file(self):
        """
        Reads the input file and initialize Main attributes
        """
        print("read_input_file : " + self.input_file_path)

        with open(self.input_file_path,'r') as f:
            nb_photos = int(f.readline())
            for i in range(0, nb_photos):
                photo_params                      = f.readline().split(" ")
                photo_params[len(photo_params)-1] = photo_params[len(photo_params)-1][:-1]
                self.photos_list.append(
                    Photo(
                        i,
                        photo_params[2:],
                        photo_params[0]
                    )
                )


    def write_output_file(self, slides, score):
        """
        Writes the output file ./outputs/<file_prefix>_<score>_<timestamp>.out
        
        :param slides: Slides list
        :param score:  The score after the simulation
        """
        output_file_path = "outputs/"+self.file_prefix+"_"+str(score)+"_"+str(time.time())+".out"
        file             = open(output_file_path, "w")
        print("write_output_file : " + output_file_path)

        file.write(str(len(slides))+"\n")

        for slide in slides:
            file.write(str(slide.photo1.id))
            if slide.photo2 is not None:
                file.write(" "+str(slide.photo2.id))
            file.write("\n")

        file.close()

# initialize Main instance
main = Main(sys.argv[1])

# initialize Algo instance
Algo(main)
