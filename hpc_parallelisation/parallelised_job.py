
'''
====================================================
    Comments: Parallelisation.py is a script to run a function in parallel across different threads.
    The number of threads is set by the user.
    The function to be run in parallel is defined in the my_function() function.
    The function takes two arguments, b and c, and returns the sum of the two.


    This script should be runned in the HPC cluster for parallelisation. 
    To call this script, we use the parallelised_job.pbs script which calls:
    python parallelised_job.py Number_of_Threads
    where Number_of_Threads is an integer argument to the parallelised_job.py function.
====================================================
'''



'''
====================================================
    Imports
====================================================
'''
import sys
import multiprocessing
import pandas as pd
import numpy as np
import pickle as pkl
'''
====================================================
    Code
====================================================
'''

# Set number of threads to 1 if no valid number provided
if len(sys.argv) > 1:
    Number_of_Threads = int(sys.argv[1])
else:
    Number_of_Threads = 1
print('Number of Threads set to ', Number_of_Threads)

# Define function to run in parallel
def my_function(df_batch, path, filename, batch_count):
    df_batch["sum a+b"] = df_batch["a"] + df_batch["b"]
    with open(path + f'{filename}{batch_count}.pkl', 'wb') as f:
        pkl.dump(df_batch, f)
    print(df)


# Create dataframe for input
df = pd.DataFrame(np.random.normal(size=(1000,2)), columns=['a', 'b'])
print(df)
print(f'Length of original dataframe = {len(df)}')

# Define batch size
batch_size = int(len(df)/Number_of_Threads) + 1
batch_indices = list(range(0, len(df), batch_size))
print(f'Length of batched dataframes = {batch_size}')

# Create a pool of workers
pool = multiprocessing.Pool(Number_of_Threads)

# Run my_function in parallel across different threads
pool_output = []
path = ''
filename = 'output_file_'
for batch_count, start_batch_index in enumerate(batch_indices):
    print('main' + str(start_batch_index))
    df_batch = df.iloc[start_batch_index:start_batch_index+batch_size]
    pool_output.append(pool.apply_async(my_function, args=(df_batch, path, filename, batch_count)))


# Close the parallel processing job
pool.close()
pool.join()


