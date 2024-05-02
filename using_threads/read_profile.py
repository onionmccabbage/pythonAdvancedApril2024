import pstats

def main():
    '''read in a profile file and show the results'''
    p = pstats.Stats('prof_out')
    p.print_stats()

if __name__ == '__main__':
    main()