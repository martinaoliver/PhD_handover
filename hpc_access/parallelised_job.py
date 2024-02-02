
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
def my_function(b,c):
    a = b+c
    print(f'a = {a}')

# Run my_function in parallel across different threads
pool = multiprocessing.Pool(Number_of_Threads)
pool_output = []
for job in range(Number_of_Threads):
    print('job' + str(job))
    pool_output.append(pool.apply_async(my_function, args=(b,c)))

# Close the parallel processing job
pool.close()
pool.join()


# Check for errors: prints errors in output file
for count,start_batch_index in enumerate(Number_of_Threads):
    print('error' + str(start_batch_index))
    pool_output[count].get()