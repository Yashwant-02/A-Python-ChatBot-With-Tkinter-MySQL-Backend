Note=> 1. make sure before doing steps below you have installed vscode and anaconda in your system.

Creating a project:-
1. Create a folder with a project name.
2. Go inside the project folder.
3. Go to address bar and type cmd
3. Write "code ." command inside command prompt and hit enter.
4. VS code will appear with project.

Creating virtual environment variables:-
1. conda must be installed and configured properly.
2. In Vs Code, open terminal in cmd.
3. Activating the base environment using "conda activate" or "source activate" commands.
4. Create a virtal environment variable using "conda create --prefix envName python=version -y".
5. Activating the virtual environment you have created for project using "conda activate (envName/ or ./envName)".
6. Check the virtual environment using "conda info --envs".

python 3.8 or + .

We are using python 3.9

in virtual environment type "pip install -r requirements.txt"

run the python script using "python main.py"


