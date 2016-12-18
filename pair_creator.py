verb_file = open("popular_verbs.txt", 'r')
prep_file = open("popular_prepositions.txt", 'r')
pair_file = open("popular_pairs.txt", 'w+')
verb_lines = verb_file.readlines()
prep_lines = prep_file.readlines()
for i in verb_lines:
    for j in prep_lines:
        pair_file.write(i.strip() + ' ' + j.strip() + '\n')
verb_file.close()
prep_file.close()
pair_file.close()
