import json
import sys

datafile = sys.argv[1]
data = json.load(open(datafile))

print 'question_index\t ques\tfunction\tanswer\timage_index\tquestion_family_index'
for ques in data['questions']:
    functions = ','.join(list(map(lambda x: x['function'],ques['program'])));
    print '{question_index}\t"{ques}"\t{function}\t{answer}\t{image_index}\t{question_family_index}'.\
        format(ques=ques['question'], question_index=ques['question_index'],function=functions,answer=ques['answer'],
               image_index=ques['image_index'],question_family_index=ques['question_family_index']
               )
