# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:30:24 2018

@author: Administrator
"""
import sys, getopt

print('Number of arguments', len(sys.argv))
print('They are:', str(sys.argv))

def main(argv):
    inputfile = ""
    outputfile = ""
    
    try:
        #"hi:o:"表示命令参数：-h -i -o  h表示该选项无参数，i:表示i选项后需要有参数
        #["infile=", "outfile="]表示为--infile=  --outfile=
        opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "outfile="])
    except getopt.GetoptError:
        print('Error: test_arg.py -i <inputfile> -o <outputfile>') 
        print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
        sys.exit(2)
        
    for opt, arg in opts:   
        if opt == "-h":   
            print('test_arg.py -i <inputfile> -o <outputfile>')   
            print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')   

            sys.exit()   
        elif opt in ("-i", "--infile"):   
            inputfile = arg   
        elif opt in ("-o", "--outfile"):   
            outputfile = arg   

    print('Input file : ', inputfile)   
    print('Output file: ', outputfile)    

if __name__ == "__main__":
    main(sys.argv[1:])      
    
# sys.exc_info() 取得异常信息