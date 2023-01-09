from os import listdir
from os.path import isfile, join

files = ['_posts/{}'.format(f) for f in listdir('_posts') if isfile(join('_posts', f))]

for file in files:
    input_file = open(file, 'r')
    lines = input_file.readlines()

    output_file = open(file, 'w')

    for line in lines:
        output_file.write(line)
        if 'permalink' in line:
            slug = line.split('/')[-1].replace('.html', '')
            output_file.write('slug: {}'.format(slug))


    output_file.close()