#for reading the csv
import pandas as pd

#for executing shell commands
import os, shutil

#for command line input
import getopt, sys

# Remove 1st argument from the list of command line arguments
argumentList = sys.argv[1:]

#input options
options = "hf:d:p:j:"
#input long options
long_options = ["help","file=","dir=","period=","jira="]

try:
  #default argument
  help_requested = False
  inputFile = 'rl.csv'   
  my_dir = '/home/ariffero/localccdb/MID/Calib/RejectList'
  in_dir = 'new'
  save_dir = '/home/ariffero/Desktop/rejectLists'
  upload_name = 'upload.sh'
  jira = '1'
  period = '24xx'

  # Parsing argument
  arguments, values = getopt.getopt(argumentList, options, long_options)
  # checking each argument
  for currentArgument, currentValue in arguments:
    if currentArgument in ("-h","--help"):
      print("\nOptions:")
      print("[-h, --help]:   display this message")
      print("[-f --file]:    input file")
      print("[-j --jira]:    jira ticket number")
      print("[-p, --period]: data taking period")
      print("[-d --dir]:     directory to look for the reject lists")
      print('\n')
      help_requested = True

    elif currentArgument in ("-f","--file"):
      inputFile = str(currentValue)
    
    elif currentArgument in ("-d","--dir"):
      in_dir = str(currentValue)

    elif currentArgument in ("-p","--period"):
      period = str(currentValue)

    elif currentArgument in ("-j","--jira"):
      jira = str(currentValue)      

  if not help_requested:

    # directory in which look for the lists
    directory = my_dir + '/' + in_dir

    # Load the csv file to examine its contents
    df = pd.read_csv(inputFile)
    csv_data = df.to_dict(orient='records')

    save_folder = save_dir + '/reject-list-' + period
    if not os.path.exists(save_folder):
      os.mkdir(save_folder)
    upload_name = save_folder + '/upload-' + period + '.sh'
    jira_name = save_dir + '/' + 'minutes-' + period + '.txt'

    up_script = open(upload_name,"w")
    up_script.write("#!/usr/bin/env bash\n\n")

    jira_minutes = open(jira_name,"w")
    jira_minutes.write('Dear all,\n')
    jira_minutes.write('please find in attachment the reject list for the period LHC' + period + '.\n')
    jira_minutes.write('Can you please upload them with:\n')
    jira_minutes.write('```\n')
    jira_minutes.write('tar -xvf reject-list-' + period + '.tar.xz\n')
    jira_minutes.write('cd reject-list-' + period + '\n')
    jira_minutes.write('./' + 'upload-' + period + '.sh\n')
    jira_minutes.write('```\n')
    jira_minutes.write('They correspond to the runs:\n')
    jira_minutes.write('run | start | stop\n')
    jira_minutes.write('----|-------|-----\n')

    for row in csv_data:
      start_tt = row['start']
      end_tt = row['stop']
      run = row['run']
      files = os.listdir(directory + '/' + str(start_tt))
      for file in files:
        base_name, extension = os.path.splitext(file)
        if extension == "":
          base_name = base_name + '.root'
          adj = ' -k "ccdb_object" --path /MID/Calib/RejectList --host alice-ccdb.cern.ch'
          jira_comm = ' -m "JIRA=[~~O2-' + jira + '~~](/jira/browse/O2-' + jira + ');comment=Reject list period LHC' + period + '"'
          command = 'o2-ccdb-upload -f "' + base_name + '" --starttimestamp ' + str(start_tt) + ' --endtimestamp ' + str(end_tt) + adj + jira_comm + '\n'
          up_script.write(command)

          jira_minutes.write(str(run) + '|' + str(start_tt) + '|' + str(end_tt) + '\n')

          copy_from = directory + '/' + str(start_tt) + '/' + file
          copy_to = save_folder + '/' + file
          shutil.copy2(copy_from, copy_to)
          os.rename(copy_to, copy_to + '.root')

    jira_minutes.write('\nThank you!\nBest regards,\nAndrea')

    print('Folder examided = ' + directory)
    print('Period = ' + period)
    print("Jira   = " + jira)

except getopt.error as err:
  print("error: " + str(err))
  print("use [-h, --help] to see available options")
