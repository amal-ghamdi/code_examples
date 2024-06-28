#%% Submit all the jobs to the cluster
# Usage: python3 submit_all.py
import os

# Function to submit a job to the cluster
def submit(jobid,cmd):
    #return os.system(cmd)
    id = str(jobid)
    jobname = 'job_' + id
    memcore = 7000
    maxmem = 8000
    email = '' # Add your email here
    ncores = 1
 
    # begin str for jobscript
    strcmd = '#!/bin/sh\n'
    strcmd += '#BSUB -J ' + jobname + '\n'
    strcmd += '#BSUB -q compute\n'
    strcmd += '#BSUB -n ' + str(ncores) + '\n'
    strcmd += '#BSUB -R "span[hosts=1]"\n'
    strcmd += '#BSUB -R "rusage[mem=' + str(memcore) + 'MB]"\n'
    strcmd += '#BSUB -M ' + str(maxmem) + 'MB\n'
    strcmd += '#BSUB -W 24:00\n'
    strcmd += '#BSUB -u ' + email + '\n'
    strcmd += '#BSUB -N \n'
    strcmd += '#BSUB -o hpc/output/output_' + id + '.out\n'
    strcmd += '#BSUB -e hpc/error/error_' + id + '.err\n'
    strcmd += 'module load python3/3.10.2\n'
    strcmd += 'source ../../../../BE_collab/bin/activate\n'
    strcmd += cmd
 
    jobscript = 'hpc/submit_'+ jobname + '.sh'
    f = open(jobscript, 'w')
    f.write(strcmd)
    f.close()
    os.system('bsub < ' + jobscript)


# All options used to run the experiments
version_list = ['-version '+ item for item in ['v4', 'v5']]
Ns_list = ['-Ns '+ item for item in ['10', '20', '50']]
sampler_list = ['-sampler '+item for item in ['MH', 'NUTS']]

# Create a list with all the possible combinations of the options
all_options = []
for version in version_list:
    for Ns in Ns_list:
        for sampler in sampler_list:
            all_options.append( version + ' ' + Ns + ' ' + sampler)

print('All options:')
print(all_options)

### Submit all the jobs to the cluster
for options in all_options:
    cmd = 'python3 driver.py ' + options
    tag = options.replace(' ', '_').replace('-','')
    print('Command:', cmd)
    print('Tag:', tag)
    print(submit(tag, cmd))

    