from os import listdir
from os.path import isfile, join

for dir in ['communities', 'culture', 'ideas', 'identities', 'releases']:

    files = ['{}/_posts/{}'.format(dir, f) for f in listdir('{}/_posts'.format(dir)) if isfile(join('{}/_posts'.format(dir), f))]

    for file in files:
        if 'permalink' not in open(file).read():
            input_file = open(file, 'r')
            line = input_file.readline() # read --- first
            string = file.split('/')[-1].split('-', 3)
            permalink = '/{}/{}/{}'.format(string[0], string[1], string[3].replace('.md', '.html'))
            input_file = open(file, 'r')
            lines = input_file.readlines()
            output_file = open(file, 'w')
            for line in lines:
                output_file.write(line)
                if '---' in line:
                    output_file.write(permalink)
            output_file.close()


            
        # input_file = open(file, 'r')
        # lines = input_file.readlines()

        # output_file = open(file, 'w')

        # for line in lines:
        #     output_file.write(line)
        #     if 'permalink' in line:
        #         slug = line.split('/')[-1].replace('.html', '')
        #         output_file.write('slug: {}'.format(slug))


        # output_file.close()