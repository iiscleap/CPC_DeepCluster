import numpy as np
import pandas as pd
import torch
import argparse


def arguments():
   parser = argparse.ArgumentParser(description = "Takes quantized outputs and creates the pseudo labels for each file")
   parser.add_argument('--input_file',type=str,help = "give the path of quantized_outputs.txt file")
   parser.add_argument('--out_path',type=str,help = "path where .pt files are dumped")
   return parser.parse_args()


def main(args):
   data = pd.read_csv(args.input_file,header = None,delimiter = '\t')

   for ind,row in data.iterrows():
      name = row[0] + '.pt'
      vec = [int(i) for i in row[1].split(',')]
      vec = torch.LongTensor(vec)
      torch.save(vec,args.out_path+'/'+name) 



if __name__ == '__main__' :
   args = arguments()
   main(args) 
