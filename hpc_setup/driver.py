# Read command line argument:
# Number of samples
# Sampler type
import argparse
import os

myargparser = argparse.ArgumentParser()
myargparser.add_argument('-version', type=str, default='v1', help='Version')
myargparser.add_argument('-Ns', type=int, default=20, help='Number of samples')
myargparser.add_argument('-sampler', type=str, default='MH', help='Sampler type (MH or NUTS)')

args = myargparser.parse_args()

print('Version:', args.version)
print('Number of samples:', args.Ns)
print('Sampler type:', args.sampler)


### Create output directory

# Create tag 
tag = 'version_' + args.version +\
      '_Ns_' + str(args.Ns) +\
      '_sampler_' + args.sampler

# Output directory
output_dir = 'results/' + tag + '/'

# Check if the directory exists, otherwise create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
else:
    raise Exception('Output directory already exists:', output_dir)

# Create a parameter file and save it in the output directory
param_file = output_dir + 'parameters.txt'
with open(param_file, 'w') as f:
    f.write('Version: ' + args.version + '\n')
    f.write('Number of samples: ' + str(args.Ns) + '\n')
    f.write('Sampler type: ' + args.sampler + '\n')

print('Parameter file saved:', param_file)




