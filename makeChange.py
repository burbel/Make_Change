#! /usr/bin/env python

def create_list_of_testcases(filename):
# testcaseinput file has on the first line the number of testcases to run
# after the first line every 2 lines has a testcase - the first line is the set of denomiations
# the second line is the amount to make change for followed by the answer you should generate

    testcaselist = []
   
    with open(filename, 'r') as f:
        testcaseinput = f.readlines()

    for count in xrange(len(testcaseinput)):
        testcaseinput[count] = testcaseinput[count].replace('\n','')

    testcaselist.append(int(testcaseinput[0]))

    for count in xrange(1, len(testcaseinput)):
        if (count % 2) == 1:
            testcaselist.append(list(set(map(int, testcaseinput[count].split(' ')))))
        else:
            testcaselist.append(map(int, testcaseinput[count].split(' ')))

    return testcaselist

def run_tests(test_cases):
# runs through test_cases[0] tests, performing the calculation for each test and printing the results
# results are timed and number of failures are tracked and reported at the end as well as intermediate

    import time

    total_start = time.clock()
    count_fail = 0
    print

    for count in xrange(1,test_cases[0] +1):
        start_time = time.clock()
        actual = makeChange(test_cases[(count * 2) - 1], test_cases[(count * 2)][0])
        end_time = time.clock()
        if (actual == test_cases[count*2][1]):
            pass
            print "pass: test case #%2d  found %8d in %.0f ms" % (count, test_cases[count*2][1], (end_time - start_time)*1000)
        else:
            pass
            print "FAIL: test case #%2d !found %8d in %.0f ms (it found %8d)" % (count, test_cases[count*2][1], (end_time - start_time)*1000, actual)
            count_fail += 1
        pass

    total_end = time.clock()
    print
    print "Processed %d test cases in %.0f ms" % (test_cases[0], (total_end - total_start)*1000)
    if (count_fail > 0):
        print " * but there were %d failures *" % count_fail

def main():    # Don't leave the code in the global namespace, it runs slower

    import sys

    if len(sys.argv) != 2:
        print "ERROR: please run makeChange.py with the inputfilename parameter"
        print "Example: python makeChange.py sample.in"
        exit(1)

    run_tests(create_list_of_testcases(sys.argv[1]))


def makeChange(denominations, amount):

    import sys

    if amount < 0:
        return -1

    denominations = sorted(denominations)

    if denominations[0] < 0:
        return -1

    dictionary = {}

    dictionary[0] = 0

    for count in xrange(1, amount+1):
        dictionary[count] = sys.maxint    

    for denom in denominations:
        dictionary[denom] = 1

    for count in xrange(1, amount+1):
        for denom in denominations:
            #print "denomination %r" % denomination
            #print "dictionary[denomination] %r" % dictionary[denomination]
            #d = dictionary[denomination]
            if ((denom <= count) and (dictionary[count - denom] != sys.maxint)):
                c = 1 + dictionary[count - denom]
                if (c < dictionary[count]):
                    dictionary[count] = c

    if (dictionary[amount] != None):
        return dictionary[amount]
    else:
        return -1

main()

