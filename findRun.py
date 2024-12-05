#for reading the csv
import pandas as pd

#for executing shell commands
import os
#for command line input
import getopt, sys

def find_run_info(time_value, dataframe):
  # Filter the dataframe for rows where 'detector' contains 'MID'
  mid_detector_df = dataframe[dataframe['detectors'].str.contains('MID')]

  # Find the row where the time_value is between timeO2Start and timeO2End
  result = mid_detector_df[(mid_detector_df['timeO2Start'] <= time_value) & 
                           (mid_detector_df['timeO2End'] >= time_value)]
    
  # If a matching row is found, return the runNumber and lhcPeriod
  if not result.empty:
    # Extract the first matching row and return [runNumber, lhcPeriod, runQuality]
    first_match = result.iloc[0]
    return [str(first_match['runNumber']), first_match['lhcPeriod'], first_match['runQuality']]
  else:
    return ["No matching run found for the given time value.","",""]

# Remove 1st argument from the list of command line arguments
argumentList = sys.argv[1:]

#input options
options = "hf:t"
#input long options
long_options = ["help","file=","time="]

try:
  #default argument
  inputFile = 'runs.csv'
  timestemp = 1
  help_requested = False

  # Parsing argument
  arguments, values = getopt.getopt(argumentList, options, long_options)
  # checking each argument
  for currentArgument, currentValue in arguments:
    if currentArgument in ("-h","--help"):
      print("\nOptions:")
      print("[-h, --help]:   display this message")
      print("[-f --file]:    input file in which the run is searched")
      print("[-t --time]:    a timestemp during the run")
      print('\n')
      help_requested = True

    elif currentArgument in ("-f","--file"):
      inputFile = str(currentValue)

    elif currentArgument in ("-t","--time"):
      timestemp = int(currentValue)

  if help_requested == False:

    # Load the csv file to examine its contents
    df = pd.read_csv(inputFile)

    #print the run info
    run, period, quality = find_run_info(timestemp, df)
    print('timestemp..' + str(timestemp))
    print('run........' + run)
    print('period.....' + period)
    print('quality....' + quality)

except getopt.error as err:
  print("error: " + str(err))
  print("use [-h, --help] to see available options")
