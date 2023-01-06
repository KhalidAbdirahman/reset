def repeat_odd(fname):
    with open (fname) as fp:
        with open ("dup." + fname, 'w') as fn:
            fp = fp.readlines()
            print (fp)
            for i in range(len(fp)):
                print (fp[i])
                if i % 2 == 0:
                    fn.write(fp[i])
                    fn.write(fp[i])
                else:
                    fn.write(fp[i])


#repeat_odd('pokemon.txt')





def write_csv(lst):
    file = open('data.csv', 'w')
    for row in lst:
        line = '\n'.join(str[row])
        file.write(line)
    file.close()

write_csv([[1,2,3], [4,5,6]])
