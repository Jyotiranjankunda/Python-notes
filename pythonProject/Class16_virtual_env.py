'''
VIRTUAL ENVIRONMENT
A virtual environment is a tool to isolate specific python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.
'''

'''
What virtual environment does?
Virtual Environment saves the current state of our compiler along with the state of their modules and libraries. So in this way even if Python has made certain changes in its module, our virtual environment can still work as before even after years. We can also install different packages and “dataframes” in our virtual environment.

To be more clear, the virtual environment works exactly the same way as the Python we have installed on our windows/mac/Linux currently because a virtual environment is just a clone of the original product.
'''

'''
Using Virtual Environments

> To get started, install the virtualenv tool with pip:
$ pip install virtualenv

> virtualenv is a tool. It is used to create isolated Python environments. 

To create a virtual environment, use command :
virtualenv myenv
OR
python -m venv myenv

> After running this command, a directory named myenv will be created. This directory will contain all the necessary executables to use the packages that the Python project would need. Python packages will be installed in this directory.

> Now, after creating a virtual environment, you need to activate it. When you open the directory, it contains folders like include, lib, script, and tcl. When you open the script folder, you'll find a file activate.bat. You can activate the virtual environment by simply clicking on this file or using the command prompt and writing the following command.

$ .\myenv\Scripts\activate

> Once the virtual environment is activated, the name of your virtual environment will appear on the terminal's left side.

> When you are done working in the virtual environment for the moment, you can deactivate it:

(virtualenv_name) $ deactivate
'''

'''
requirements.txt

We run a command "pip freeze > requirements.txt",  a file will be generated in the directory where our virtual environment is based. The file will contain all the details related to the external packages that we have installed along with their versions. By having the requirement.txt file, we can create our virtual machine again easily by downloading all the same libraries, having the same versions by a simple command. 

The requirement.txt file will contain data like this:-

numpy==1.15.4
scikit-learn==0.20.1
scipy==1.1.0
sklearn==0.0

We can install all the packages one by one by a command:
$ pip install package_name == version

To install all the packages at once :-
$ pip install -r .\requirements.txt
'''