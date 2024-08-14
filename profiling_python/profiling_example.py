#%% Example of profiling code (here we use the CUQIpy package) to extract the number of calls to a specific function (here we want to extract the number of logpdf calls in the posterior object)

#%% Importing the necessary packages
import cuqi
import cProfile, pstats, io
from pstats import SortKey

#%% Create a profile object
pr = cProfile.Profile()

#%% Profile the code
# Enable the profiler (start profiling)
pr.enable()

# CUQIpy code
x = cuqi.distribution.Gaussian(0, 1)
A = cuqi.model.Model(forward = lambda x:x,
                     range_geometry = 1,
                     domain_geometry = 1)
y = cuqi.distribution.Gaussian(A(x), 1)
joint = cuqi.distribution.JointDistribution(x, y)
posterior = joint(y=2)
MH = cuqi.sampler.MH(posterior)
samples = MH.sample_adapt(305)

# Disable the profiler (stop profiling)
pr.disable()

#%% Print the profiling results
s = io.StringIO()
sortby = SortKey.PCALLS
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

#%% Extract the number of calls to the function we are interested in

# extract row with string /Users/amal/Documents/research_code/CUQI-DTU/CUQIpy/cuqi/distribution/_posterior.py:84(logpdf)
lines = s.getvalue().split('\n')
idx = ['distribution/_posterior.py:84(logpdf)' in line for line in lines].index(True)

print("Index")
print(idx)
print("Line")
lines[idx]
print("Number of calls")
print(lines[idx].split()[0])

