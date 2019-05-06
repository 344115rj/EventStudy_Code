with open(r"C:\Users\rjoosten\PycharmProjects\Thesis_Split_Articles\Anadarko\Strategy\Anadarko Strategy.txt", 'r') as fo:
    for line in fo:
        line = line.lower()
        op = ''
        start = 0
        cntr = 1
        for x in fo.read().split("\n"):
            if (x == ' WC'):
                if (start == 1):
                    with open('article' + str(cntr) + '.txt', 'w') as opf:
                        opf.write(op)
                        opf.close()
                        op = ''
                        cntr += 1
                else:
                    start = 1
            else:
                op = op + '\n' + x

    fo.close()