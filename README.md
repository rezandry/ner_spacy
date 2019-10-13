# This NER using spacy library 

Instuction to run:
1. make sure you have install python 3.x
2. install dependency in this way on your terminal: 
    - pip install spacy
    - python -m spacy download en_core_web_sm

Program Flow:
1. First, read each line from dataset
2. Create ner variable that instance of core model meta en_core_web_sm 
3. Then, input the content into ner, the result is text with label of text
4. Modify label from spacy into label that user want using dict
5. Set data for write into output file
You can see result data in NER_result.csv file

Note, this library sometimes fail to identify person, and sometimes identify person as organization

In this question noted that:
"Assume that there is no training data available and need to use linguistic features to tag the entities."
So, I use feature linguistic from spacy