import argparse
import datetime
from rich.prompt import Prompt, IntPrompt

class argsClass:
   current_time = datetime.datetime.now().strftime("%m%d%Y%H%M%S")

   def __init__(self):
      self.input_text = None
      self.output_text = None
      self.special_characters = False
      self.char_and_num_replace = False
      self.min_len = None
      self.max_len = None

   def parse_args(self):
      # ARG PARSE INFO 
      parser = argparse.ArgumentParser(description="Password Generator")

      group = parser.add_mutually_exclusive_group(required=True)
      group.add_argument("-i",
                          "--input-file",
                          type=str,
                          help="Name of the input file name")
      group.add_argument("-c",
                          "--custom-input",
                          action='store_true',
                          help="Program will ask user to input data")
      parser.add_argument("-o",
                          "--output-file",
                          default=f"pass_output-{self.current_time}.txt",
                          type=str,
                          help="Name of the output file. Default file is ouput-<DATE-TIME>.txt")
      parser.add_argument("-R",
                          "--char_and_num_replace",
                          action='store_false',
                          help="Swap common letters and numbers like o-O, s-5, i-1, etc...")
      parser.add_argument("-s",
                          "--special-characters",
                          action='store_true',
                          help="Include the options for Special Characters in Passwords. This can significanlty increase process time")

      # Setting Arguments
      arguments = parser.parse_args()
      self.input_text = arguments.input_file
      self.output_file = arguments.output_file
      self.custom_input = arguments.custom_input
      self.special_characters = arguments.special_characters
      self.char_and_num_replace = arguments.char_and_num_replace

   def get_user_data(self):
      print("Please enter a name, place, word, etc. that you'd like to base your password list off of.")
      self.input_text = Prompt.ask(">>>", default="password")
      self.special_characters = Prompt.ask("Special Characters (ie. !@#$%_)?:", default="n", choices=["y","n"])
      self.char_and_num_replace = Prompt.ask("Replace common letters and numbers (ie o-0, i-1, s-5)", default="y", choices=["y", "n"])
      if self.char_and_num_replace == "y":
         self.char_and_num_replace = True
#     self.min_len = IntPrompt.ask("Min Password Length:", default="6")
#     self.max_len = IntPrompt.ask("Max Password Length:", default="12")
      self.output_file = Prompt.ask("Output File Name:", default=f"pass_output-{self.current_time}.txt")

def get_args():
   arguments = argsClass()
   arguments.parse_args()
   if arguments.custom_input:
      arguments.get_user_data()
   return arguments