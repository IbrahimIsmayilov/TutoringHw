# Question
# What is a CPU?
# Central Processing Unit is responsible for carrying out instructions, performing mathematical operations, and executing programs one line at a time. It gets the instruction, or which line to execute, from the Random Access Memory and then sends the result back to the RAM which is then sent to the Permanent Storage. A CPU can have many cores, meaning they can do more tasks at once and this is often the determining factor in the price.

# Question
# What is RAM?
# RAM or Random Access Memory is a temporary storage that communicates between the Permanent Storage and the Central Processing Unit. Unlike Permanent Storages, Random Access Memory gets wiped after a session. Whenever any code is executed, there is a constant communication between RAM and the CPU, until the whole program is run. Programs are stored in the RAM while they are run. 

# Question
# What is computer storage?
# Computer storage is a physical piece of hardware within a computer where data can be stored permanently throughout different sessions. Unlike RAM, it does not lose any of its data when the computer is powered off, and it sends data to the RAM which is then sent to the CPU whenever the computer runs any program.  

# Question
# Where are computer files saved at?
# Computer files are saved in the computer storage, within a local hard drive. 

# Question
# Where are process variables saved at?
# Process variables are saved in the RAM or Random Access Memory.


# Question
# What is the difference between a program and a process?
# Give an example for each.
# A program is compromised of instructions for the computer and when it is run, a process or an instance of the program is created. Each instance has it owns dedicated memory space and resources allocated. Multiple processes can be created from a single program. An example of a program would be Visual Studio Code which is an IDE in which typically one folder and files within are available to code in. If I were to code in 2 different folders, I would have to open Visual Studio Code again and choose a different folder, hence causing there to now be 2 processes running of the same program, Visual Studio Code.

# Question
# Explain the interaction between CPU, RAM and Storage during the program's execution.
# When any process is created, the RAM must get necessary files from the Storage that will need the logical abilities of the CPU. Line by line, the CPU processes and performs necessary calculations for the RAM and sends it back. The RAM then either has the choice to keep the file processed by CPU if any further operations are needed by the CPU or to send it back to storage for permanent use.

# Question
# Name couple of companies that produced CPUs.
# Give example of CPUs for each such company.
# Intel, Example: Intel Core CPUS, Core 3, Core 5, Core 7 and the latest Core 9
# AMD, Example: Ryzen 9000 series, Ryzen 7000 series
# Qualcomm, Example: Snapdragon models in phones
# Samsung, Example: Exynos phone processors which are technically cpus

# Question
# 1. What CPU does your computer have?
# M2
# 2. How much memory does your computer have?
# 8 GB
# 3. How much storage does your computer have?
# 245.11 GB

# However you found answer to the above, good job. Now search the internet to find if there exists a command line tool to answer above 3 
# questions. Use them an try to understand their output.

# For CPU, Memory: system_profiler SPHardwareDataType
# For storage: df -h


# Question
def count_occurence(lst: list[int], target: int) -> int:
    pass

# Below are 2 ways in which you can implement count_occurence in a reccursive manner. Implement each of them individually.
# As everything else, even if you cannot get the final answer, I expect you to submit the code that does not work (something is better than nothing).
# Option 1
# 1. figure out the smaller questions. The smaller question is, how many occurences of the target occurs in the first and second half 
# of the given list. Instead of checking a list by itself, divide into 2 lists or 2 smaller problems
# 2. when you find an answer to smaller questions, how do u use them to find the answer to the current question.
# Add the occurrences to return the total amount of occurences in the list
# 3. when do we stop? Hitting the bottom of the reccursion. When the length of the given list is 1: Check if it is the 
# target, if so return 1. Else return 0. If we continue dividing a list with a length of 1 element into 2 elements, we will run into an error

def count_occurence(lst: list[int], target: int) -> int:
    """
    Returns total amount of target's occurences in the given list
    """
    if len(lst) == 1:
        if lst[0] == target:
            return 1
        else:
            return 0
        
    return count_occurence(lst[0:1], target) + count_occurence(lst[1:], target)

print(count_occurence([1, 3, 4, 5, 3, 2, 1, 3, 4], 3))  # 3


# Option 2
# 1. How many times does target occur in the rest of the list after the first element? The problem gets divided into 2 sub problems: how many times does target occur in the first element of the list, how many times does the target occur in the rest of the list after the first element
# 2. The results of both sub problems are added to get the total occurences of the target
# 3. when do we stop? Hitting the bottom of the reccursion. When the length of the given list is 1 (we are checking the first element): Check if it is the target, if so return 1. Else return 0

# Leetcode
# 1. https://leetcode.com/problems/baseball-game/description/