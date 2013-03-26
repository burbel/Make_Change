#!/usr/bin/python

def create_list_of_testcases(filename):
# The first line of testcaseinput has the number of testcases to run (can be less than the total tests in the file)
# After the first line every 2 lines has a testcase - the first line is the set of denomiations
#  The second line is the amount to make change for followed by the answer you should generate
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
# Runs through test_cases[0] tests, performing the calculation for each test and printing the results
# Intermediate and final Results are timed and number of failures are tracked and reported at the end
    import time
    total_start = time.clock()
    count_fail = 0
    print
    for count in xrange(1,test_cases[0] +1):
        start_time = time.clock()
        actual = makeChange(test_cases[(count * 2) - 1], test_cases[(count * 2)][0])
        end_time = time.clock()
        if (actual == test_cases[count*2][1]):
            print "pass: test case #%2d  found %8d in %.3f ms" % (count, test_cases[count*2][1], (end_time - start_time)*1000)
        else:
            print "FAIL: test case #%2d !found %8d in %.3f ms (it found %8d)" % (count, test_cases[count*2][1], (end_time - start_time)*1000, actual)
            count_fail += 1
        pass
    total_end = time.clock()
    print
    print "Processed %d test cases in %.3f ms" % (test_cases[0], (total_end - total_start)*1000)
    if (count_fail > 0):
        print " * but there were %d failures *" % count_fail

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

    if (dictionary[amount] != sys.maxint):
        return dictionary[amount]
    else:
        return -1

def main():    
# From stackoverflow, don't leave the code in the global namespace, it runs slower
# Executes run_tests with the list of testcases created by calling create_list_of_testcases with parameter
    import sys
    if len(sys.argv) != 2:
        print "Usage: ./makeChange.py sample.in"
        exit(1)
    run_tests(create_list_of_testcases(sys.argv[1]))

main()
