Dependented Librarys Installtion
================================
Please have a look the requirement.txt and also install the Certificates.command as following step:

1. Change directory to the python folder: cd /Applications/Python 3.6/
2. Run the command: ./Install Certificates.command
3. Open python: python3
4. Import nltk: import nltk
5. Download: nltk.download()
6. nltk.download('punkt')
7. Exit Python shell
8. Run command: python -m textblob.download_corpora


Part A task
===========
To get the Symptom for dizziness, please run "./get_symptom.sh"
To get the disease list for dizziness, please run "./get_disease.sh"

More complex usage:
a) Get disease list for a specific combination category
scrapy crawl healthline -L WARNING -a opt=disease -a category=dizziness/shortness-of-breath/fainting

b) Get disease list for all combination categroy
scrapy crawl healthline -L WARNING -a opt=disease_list -a category=dizziness

c) Get disease list for all combination categroy, combination based on 3
scrapy crawl healthline -L WARNING -a opt=disease_list -a category=dizziness -a max_combine=3

d) Get symptom list for a specific categroy
scrapy crawl healthline -L WARNING -a opt=symptom -a category=dizziness

Part B task
===========
Please run "python3 start_doctor.py" to start a doctor to talk.
Input symptom description: Input the description here, for example, input < pain in stomach>
Available symptom: Return a matched symptom. If can't find one return "Unknown"

doctory.py  ---- Doctor which identify the symptom according to user input sentence.
trainer.py  ---- Include the trainer_data which is used to identify the symptom according to the user input description. More training data in it, more accurate for the classfication.
