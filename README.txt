# PythonByGirishPareek
=========================================================
Python Tutorial by Girish Pareek
=========================================================

Python (I'll be using 3.9.1): https://python.org/downloads

IDE:
An IDE : 
An IDE : https://code.visualstudio.com


Resources:
=========================================================
A. Know why
1. https://mailchimp.com/
2. https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
3. https://passwordsgenerator.net/sha1-hash-generator/

B. Regular expression: 
https://regex101.com/
https://regexone.com/lesson/matching_characters?


Image processing: 
1. https://unsplash.com/
2. https://pillow.readthedocs.io/en/stable/  
3. https://github.com/python-pillow/Pillow/blob/master/docs/installation.rst

Python Data Processing: 
conda create -n idc python=3.6 anaconda
conda install -c conda-forge keras==2.1.6
conda install -c anaconda pandas==0.23.4
conda install -c intel mkl
conda install mkl-service
conda install -c anaconda scikit-learn==0.19.1
conda install -c anaconda flask-cors
conda install -c anaconda nltk
conda install -c anaconda simplejson
conda install -c anaconda cherrypy==15.0.0
conda install -c anaconda configobj==5.0.6
conda install -c anaconda joblib==0.13.0
conda install -c anaconda xlsxwriter
conda install -c anaconda pymongo
conda install -c anaconda gensim==3.0.1
python -m nltk.downloader stopwords
python -m nltk.downloader punkt
pip install dplython
conda install -c anaconda scipy==1.0.0rc

======Create a project folder and go into it ===========
$ mkdir <project name>
# cd <project name>

======Once you're in the project folder, the next step is to create an environment in it.==================== 

$ conda create --prefix ./env pandas numpy matplotlib scikit-learn flask-cors nltk simplejson cherrypy configobj joblib xlsxwriter pymongo gensim
After running the line of code above, you'll be asked whether you want to proceed. Press y

========Now to activate this environment - use following command : ========

$ conda activate Users/Girish Pareek/desktop/project_1 

Running the line of code above activates our new environment. Activating the new environment changes (base) to (Users/daniel/desktop/project_1) because this is where the new environment lives.

$ conda install jupyter -- specifally for this new environment 
It's like saying, 'Hey conda install the jupyter package to the current environment'.

========To stop your Jupyter Notebook running, press control+c =======================
========To exit your environment you can use 
$ conda deactivate

========This will take you back to the (base) environment.

$ conda activate [ENV_NAME]





Section: Scraping Data with Python
===========================================================
https://www.excellarate.com/blogs/web-scraping-introduction-applications-and-best-practices/#:~:text=Web%20scraping%20typically%20extracts%20large,show%20data%20from%20a%20website.
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
pip or conda install beautifulsoup4 --- This is just a liberary
https://pypi.org/project/requests/  # Requests is a simple, yet elegant HTTP library.
pip or conda install requests
https://scrapy.org/ -- This is a framework - (Separate learning). 

Web Development with Python
========================================================
docs.python.org/
=>Http server: https://docs.python.org/3/library/http.server.html
flask.palletsprojects.com
djangoprojects.com

Python environment and shell:
=========================================================
https://docs.python.org/3/library/venv.html






