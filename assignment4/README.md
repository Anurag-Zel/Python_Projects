- # **Task_1** :
  - ## Objective - Read a File and Handle Errors
    - Create a file in your directory as "Sample.txt", with some text input.
    - Store the relative file path.
    - Define a file object with *read* mode.
    - Function now checks if the file exists at the given path.
    - If file doesn't exists, a **FileNotFoundError** is raised, which is caught in the except statement. This avoids any abdrupt termination of program.
    - If file exist, output is displayed line by line.
    - Finally the program is terminated after closing the file.

<br>

- # **Task_2** :
  - ## Objective - Write and Append Data to File
    - Provide name to output file as "output.txt", to store result.
    - Define the relative path to file.
    - Define a file object with *write*(truncate) mode. This allows to truncate the existing file and override the input.
    - Allow the user to enter an input, and append it to output file. Repeat this twice.
    - Handle exception, that can occur during appending in except statement.
    - Close the existing file object, and open a new file object with *read* mode.
    - Display the output of putput file.