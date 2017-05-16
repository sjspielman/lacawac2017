## Bash exercises


Launch a Terminal session and navigate to your home directory with the `cd` command. Remember, there are three ways to do this:

		cd
		cd ~
		cd /path/to/home/directory/ # replace your home directory's full path


Using the commands `cd`, `pwd`, and `ls` (Hint: which `ls` arguments are helpful?), examine the directory structure of your system. Spend a few minutes (no more than 5!!!) figuring out where different files and directories are located so that you understand your file system organization by navigating forward into sub-directories and back into parent directories and listing contents. \emph{The purpose of this task is to become comfortable with your computer's organization.}

    \begin{enumerate}
        \item Download today's course materials from the course website. Locate that folder on your computer (either with Finder or with terminal, depending on your preference). It should be called "day1\_materials". Once you find the directory that contains your downloaded materials, determine the directory's \emph{path} using the \code{pwd} command. Remember this information!
    
        \item Navigate to your home directory (you can type either \code{cd ~} or simply \code{cd} for this), and perform the following tasks:
        \begin{itemize}
            \item Use the command \code{mkdir} to create a new directory called "class1". Enter that directory using the command \code{cd}.
                        
            \item Use the command \code{cp} to copy the directory of today's course materials into current working directory ("class1"). Hint: When copying a folder, then you will need to use the argument \code{-r}, for example \code{cp -r <directory to copy, including path> <destination>}
        
            \item Once you have successfully performed the last step, navigate into the "day1\_materials" directory using \code{cd}. Use the \code{mv} command to rename the file called "original.txt" to "new.txt". Confirm that the file was renamed with with \code{ls}.
            
            \item Copy the file "new.txt" from its current directory into the directory "class1/", which is one level above the working directory, using \code{cp}. Confirm that the file has been successfully \emph{copied} (not moved!).
        
            \item Navigate back a directory into "class1/" (using the code \code{cd ..}) and remove the just-copied file "new.txt" using the \code{rm} command.
        
            \item Create a new directory called "temp" using the command \code{mkdir}. \emph{Move} the file whose current path is "class1/day1\_materials>/new.txt" into "temp/" \emph{from the "class1/" directory} (do not enter the course materials directory or temp!!). 
        
            \item Now, use \code{ls} to list the contents of "temp/". There should be a single file in this directory called "new.txt" if the previous step worked. Finally, remove the "temp/" directory with the command \code{rm -r} (think: why use \code{-r}?).        
        \end{itemize}
    \end{enumerate} 