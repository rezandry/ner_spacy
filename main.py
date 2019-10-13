import en_core_web_sm
import csv

class NER:
    __is_exist = []
    __tag_map = {
        'ORG': 'Organization',
        'PERSON': 'Person',
        'GPE': 'Location'
    }

    def __get_tag(self, text, label):
        if self.__tag_map.get(label):
            return '<{}>{}<{}>'.format(self.__tag_map.get(label), text, self.__tag_map.get(label))
        return text

    def __get_format_write(self, raw_data):
        data = ''
        for key, value in raw_data.items():
            data += '"{}",'.format(value)
        return data+'\n'
    
    def __tagging_content(self, content):
        ner = en_core_web_sm.load()
        doc = ner(content)
        for entity in doc.ents:
            if entity.text not in self.__is_exist:
                content = content.replace(entity.text, self.__get_tag(entity.text, entity.label_))
                self.__is_exist.append(entity.text)
        self.__is_exist = []
        return content 

    def modify_data(self):
        file_result = open('NER_result.csv','w')        
        with open('news.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    row['content'] = self.__tagging_content(row['content'])            
                    data_write = self.__get_format_write(row)
                else:
                    data_write = ',id,title,publication,author,date,year,month,url,content'+'\n'
                file_result.write(data_write)
                line_count += 1
        file_result.close()

ner = NER()
ner.modify_data()