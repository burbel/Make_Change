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
        pass
# This is where I process things
        actual = 1
# And done
        pass
        end_time = time.clock()
        if (actual == test_cases[count*2][0]):
            pass
            print "pass: test case #%2d  found %8d in %8d ms" % (count, test_cases[count*2][0], (end_time - start_time))
        else:
            pass
            print "FAIL: test case #%2d !found %8d in %8d ms (it found %8d)" % (count, test_cases[count*2][0], (end_time - start_time), actual)
            count_fail += 1
        pass

    total_end = time.clock()
    print
    print "Processed %d test cases in %d ms" % (test_cases[0], (total_end - total_start))
    if (count_fail > 0):
        print " * but there were %d failures *" % count_fail

def main():    # Don't leave the code in the global namespace, it runs slower

    import sys

    if len(sys.argv) != 2:
        print "ERROR: please run makeChange.py with the inputfilename parameter"
        print "Example: python makeChange.py sample.in"
        exit(1)

    run_tests(create_list_of_testcases(sys.argv[1]))

main()

"""
<html>
<head>
<script type="text/javascript">

function pop(array) {
  if (array.length > 0) {
    var last = array[array.length - 1];
    array.splice(array.length-1, 1);
    return last;
  }
  return -1;
}

function makeChange(denominations, amount)
{
  if (amount < 0) {
    return -1;
  }
  for (var i = 0; i < denominations.length; i++) {
    if (denominations[i] <= 0) {
      return -1;
    }
  }

  var min = new Object();
  min[0] = 0;
  for (var i = 1; i <= amount; i++) {
    min[i] = Number.MAX_VALUE;
    for (var j = 0; j < denominations.length; j++) {
      var d = denominations[j];
      if(d <= i && min[i - d] != Number.MAX_VALUE) {
        var c = 1 + min[i - d];
        if (c < min[i]) {
          min[i] = c;
        }
      }
    }
  }
  var retval = min[amount];
  if (retval == Number.MAX_VALUE) {
    retval = -1;
  }
  return retval;
}

/*
function makeChange(denominations, amount)
{
  denominations = denominations.slice(); // copy the array so we don't modify the original
  denominations.sort(function(a,b){return b - a}); // javascript sucks...

  var cache = new Object();
  return _makeChange(denominations, amount, cache);
}

function _makeChange(denominations, amount, cache)
{
  //alert("makeChange: [" + denominations + "], " + amount + ", cacheAmount = " + cache[amount]);

  if (amount == 0) {
    return 0;
  } else if (cache[amount] != undefined) {
    return cache[amount];
  } else {
    var min = Number.MAX_VALUE;
    for (var i = 0; i < denominations.length; i++) {
      var d = denominations[i];
      if (d <= amount) {
        var c = 1 + _makeChange(denominations, amount - d, cache);
        if (c != 0 && c < min) {
          min = c;
        }
      }
    }
    if (min == Number.MAX_VALUE) {
      min = -1;
    }
    cache[amount] = min;
    return min;
  }
}
*/

function test(denominations, amount, expected) {
  try {
    var startTime = new Date();
    var actual = makeChange(denominations, amount);
    var endTime = new Date();
    var totalTime = endTime.getTime() - startTime.getTime();
    if (actual == expected) {
      document.getElementById("results").innerHTML += "PASS: [" + denominations + "], " + amount + " = " + expected + " in " + totalTime + "ms<br>";
    } else {
      document.getElementById("results").innerHTML += "FAIL: [" + denominations + "], " + amount + " = " + expected + " (returned " + actual + ")<br>";
    }
  } catch (ex) {
    document.getElementById("results").innerHTML += "FAIL: [" + denominations + "], " + amount + " = " + expected + " (threw exception: " + ex + ")<br>";
  }
}

function runTests() {
/*
  test([1, 5, 10, 25], 75, 3);
  test([10, 25, 1, 5], 75, 3);
  test([1, 41, 42], 82, 2);
  test([1, 5, 10, 25, 50, 100, 100, 500, 1000, 2000, 5000, 10000, 100000], 123456, 12);
  test([1, 5, 10, 25], 75, 3);
  test([10, 25, 1, 5], 75, 3);
  test([4,5], 7, -1);
  test([1,4,5], 8, 2);
  test([], 20, -1);
  test([25], 1, -1);
  test([1, 2, 5], 4, 2);
  test([1, 2, 3, 3], 20, 7);
  test([1, 41, 42], 82, 2);
  test([1, 41, 42, 600, 700], 82, 2);
  test([1, 41, 42, 65, 70], 82, 2);
  test([-1, -2, -3], 5, -1);
  test([-1, -2, -3], -5, -1);
  test([1,2,3,4,5], -5, -1);
  test([1, 41, 42], 172200, 4100);
  */
  /*
  test([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,167, 173], 123456, 714);
  test([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997], 123456, 124);
  test([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571], 1234567, 347);
  */
    test([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,167, 173], 123456, 714);

    test([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997], 123456, 124); // Bill's old version 832ms, new version 247ms

    test([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571], 123456, 36); // 772ms for Bill - beat a second on that, and i'll buy ya dinner, if ya didn't cheat
}

</script>
</head>
<body onload="runTests()">
  <div id="results">Results:<br></div>
</body>
</html>
"""


"""

Skype chat transcript with Bill [2011/7/29]:
     [7/29/11 1:14:30 AM] Brian Bibeault: I was thinking you said that in Java there was an O(N) difference or something.
     [7/29/11 1:14:30 AM] Brian Bibeault: Ok
     [7/29/11 1:14:33 AM] Brian Bibeault: WTF that's it?
     [7/29/11 1:14:35 AM] Brian Bibeault: :P
     [7/29/11 1:14:46 AM] 1. Bill Johnson: well...there's no error checking
     [7/29/11 1:14:54 AM] Brian Bibeault: You have globals?
     [7/29/11 1:15:02 AM] Brian Bibeault: No nvm.
     [7/29/11 1:15:10 AM] Brian Bibeault: Number.MAX_VALUE must be something defined.
     [7/29/11 1:15:33 AM] 1. Bill Johnson: "constants", not "globals" :-P
     [7/29/11 1:15:36 AM] 1. Bill Johnson: which are perfectly okay
     [7/29/11 1:15:46 AM] Brian Bibeault: I only used a global for the error count.
     [7/29/11 1:16:31 AM] Brian Bibeault: Can save a bit of iteration if you move that <= 0 check to after sorted, and just check element #1.
     [7/29/11 1:16:52 AM] 1. Bill Johnson: meh
     [7/29/11 1:17:01 AM] 1. Bill Johnson: it's O(n)...it doesn't change the complexity :-P
     [7/29/11 1:17:07 AM] Brian Bibeault: (I spent too much time doing assembly)
     [7/29/11 1:17:14 AM] Brian Bibeault: Ooh, I'd give you suck a dirty look.
     [7/29/11 1:17:21 AM] Brian Bibeault: Ok I don't see how yours works.
     [7/29/11 1:17:30 AM] Brian Bibeault: But having a hard time parsing it, maybe will check tomorrow AM.
     [7/29/11 1:17:37 AM] Brian Bibeault: I am having a hard time even reading.
     [7/29/11 1:17:45 AM] 1. Bill Johnson: you look at a single coin and decide whether or not to use it
     [7/29/11 1:17:56 AM] 1. Bill Johnson: i look at all of the coins and decide which one to use
     [7/29/11 1:18:19 AM] Brian Bibeault: Oh God that is similar to the weird idea I had about 15m ago.
     [7/29/11 1:18:29 AM] Brian Bibeault: Werll wait, no.
     [7/29/11 1:18:45 AM] Brian Bibeault: And this is faster than what I have already?
     [7/29/11 1:19:39 AM] 1. Bill Johnson: in constant time, maybe a little bit, because it's got a shallower stack.  in algorithmic complexity, no.
     [7/29/11 1:20:03 AM] 1. Bill Johnson: i stripped out the parts that make it go fast
     [7/29/11 1:20:09 AM] Brian Bibeault: :)
     [7/29/11 1:20:21 AM] Brian Bibeault: And then even after that you refactored and got a newer faster solution, right?
     [7/29/11 1:20:34 AM] 1. Bill Johnson: rewrote, not refactored
     [7/29/11 1:20:39 AM] Brian Bibeault: ok
     [7/29/11 1:20:52 AM] 1. Bill Johnson: you would probably look at it compared to this, and say "WTF?"
     [7/29/11 1:21:16 AM] Brian Bibeault: This one already has me saying wtf.
     [7/29/11 1:21:25 AM] Brian Bibeault: You'd get WTFBBQ!!!!11
     [7/29/11 1:21:50 AM] 1. Bill Johnson: it's actually only one line of code longer than this slow version :-P
     [7/29/11 1:22:01 AM] Brian Bibeault: This is faster than mine.
     [7/29/11 1:22:22 AM] Brian Bibeault: some significant factor of N, I think.
     [7/29/11 1:22:32 AM] Brian Bibeault: You are not doing all the duplicates that I am doing.
     [7/29/11 1:22:38 AM] 1. Bill Johnson: compared to 4 extra lines for the faster version of this first variant
     [7/29/11 1:22:47 AM] Brian Bibeault: Lemme see if I can figure that out.
     [7/29/11 1:27:23 AM] Brian Bibeault: I am just seeing trivial speedups.
     [7/29/11 1:28:28 AM] Brian Bibeault: Before you do the for loop, if (denominations.indexOf(amount) != -1) return 1;
     [7/29/11 1:29:04 AM] 1. Bill Johnson sent file "hint.png"
     [7/29/11 1:30:11 AM] 1. Bill Johnson: and that last suggestion would probably actually slow it down
     [7/29/11 1:30:12 AM] Brian Bibeault: Ok, I wish that hint was hinty.
     [7/29/11 1:30:16 AM] Brian Bibeault: Really?
     [7/29/11 1:30:56 AM] Brian Bibeault: Would think avoiding the case where you recurse 25 times to try splitting a quarter into 25 pennies, 20 pennies and a nickel in between any of the two pennies, etc, would be slower.
     [7/29/11 1:31:00 AM] 1. Bill Johnson: so, in mine, because I'm not popping and changing the array, the only thing that changes is the amount
     [7/29/11 1:31:40 AM] Brian Bibeault: You will never be more efficient finishing a quarter than with a single quarter.
     [7/29/11 1:31:41 AM] 1. Bill Johnson: it could be, but if you call denominations.indexOf 5 times when you don't need to, it's a wash
     [7/29/11 1:32:12 AM] Brian Bibeault: Hrm I guess so.
     [7/29/11 1:32:33 AM] Brian Bibeault: But that would only be a wash if you had some method of breaking out IMO, because you'll always have amount recursions around the "1" case.
     [7/29/11 1:32:42 AM] Brian Bibeault: Just brainstorming, no clue.
     [7/29/11 1:32:58 AM] 1. Bill Johnson: so this diagram is showing the various recursive calls I make...the edges show the coin I chose in my loop, and the nodes show the resulting amount I passed down
     [7/29/11 1:33:06 AM] Brian Bibeault: Right
     [7/29/11 1:33:20 AM] Brian Bibeault: Did I say hash table earlier?
     [7/29/11 1:33:31 AM] Brian Bibeault: That's what I meant to see, as I saw this.
     [7/29/11 1:33:39 AM] Brian Bibeault: say, whatever.
     [7/29/11 1:34:01 AM] 1. Bill Johnson: nope, you did not mention that
     [7/29/11 1:34:07 AM] Brian Bibeault: Mean to type that.
     [7/29/11 1:34:15 AM] Brian Bibeault: Was too focused on that other thingy.
     [7/29/11 1:34:23 AM] 1. Bill Johnson: you can use any object in javascript as a hashtable
     [7/29/11 1:34:34 AM] Brian Bibeault: I was thinking that with mine, too, but had no clue how to do it, because the denomination list itself was changing.
     [7/29/11 1:34:41 AM] 1. Bill Johnson: var foo = new Object();
     foo[7] = 37829;
     [7/29/11 1:34:49 AM] 1. Bill Johnson: var foo7 = foo[7];
     [7/29/11 1:35:02 AM] Brian Bibeault: Dude I am spent.
     [7/29/11 1:35:05 AM] Brian Bibeault: I cannot parse that.
     [7/29/11 1:35:12 AM] Brian Bibeault: I am sorry.
     [7/29/11 1:35:28 AM] Brian Bibeault: This not typing stuff is killing me.
     [7/29/11 1:35:41 AM] 1. Bill Johnson: var myHashtable = new Object();
     myHashtable[myKey] = myValue; // add
     [7/29/11 1:35:48 AM] Brian Bibeault: So var foo = new Object(); foo is now a variable with a memory address.
     [7/29/11 1:36:04 AM] Brian Bibeault: how is that 2nd piece there not an out of bounds something?
     [7/29/11 1:36:24 AM] 1. Bill Johnson: if (myHashtable[myKey] != undefined) { // if myHashtable contains myKey
     alert(myHashtable[myKey]); // shows alert with myValue
     }
     [7/29/11 1:36:47 AM] 1. Bill Johnson: because it's a hashtable, not an array
     [7/29/11 1:37:10 AM] Brian Bibeault: It just uses array-like syntax, and you never cast it as a hashthingy?
     [7/29/11 1:37:26 AM] Brian Bibeault: It figures out from my thing[x] = value; that it's a hash?
     [7/29/11 1:37:32 AM] 1. Bill Johnson: yes.  as does every language that is not C, including C++, C#, Java, JavaScript and more...
     [7/29/11 1:37:38 AM] Brian Bibeault: Whoa
     [7/29/11 1:38:03 AM] Brian Bibeault: Oh that's crazy, never thought of a hash as something included as a default library/function.
     [7/29/11 1:38:07 AM] Brian Bibeault: Although I guess it makes sense.
     [7/29/11 1:38:09 AM] 1. Bill Johnson: well, in other languages, you'd do
     Hashtable myHashtable = new Hashtable();
     [7/29/11 1:38:19 AM] 1. Bill Johnson: but javascript is a funky prototype language
     [7/29/11 1:38:28 AM] 1. Bill Johnson: and every object is a hashtable, basically
     [7/29/11 1:38:52 AM] Brian Bibeault: So I *think* I could speed up your version a bit by having a hash table of values.
     [7/29/11 1:39:48 AM] Brian Bibeault: For each test, whenever I solve any amount, I would check to see if there was an entry for that amount, and the entry would be the previous lowest.  If I was lower I would replace it with my solution.
     [7/29/11 1:39:58 AM] Brian Bibeault: Except that's not right, even as I typed that, that's not looking right.
     [7/29/11 1:39:55 AM] 1. Bill Johnson: i just realized i made a horrible mistake in my old fast version :-P
     [7/29/11 1:39:58 AM] Brian Bibeault: :P
     [7/29/11 1:40:06 AM] 1. Bill Johnson: maybe my new version isn't that much faster
     [7/29/11 1:40:21 AM] Brian Bibeault: But my version is fucked, because of my changing denominations idea.
     [7/29/11 1:40:21 AM] Brian Bibeault: Grr.
     [7/29/11 1:40:33 AM] Brian Bibeault: And using yours is like a warm shower (cheating)
     [7/29/11 1:40:53 AM] Brian Bibeault: Ok, so your super-new version is nothing at all like this, right?
     [7/29/11 1:41:13 AM] Brian Bibeault: I might see if, since I failed the test, I can implement a working version of your version, and then see if I can get it to go faster.
     [7/29/11 1:41:40 AM] 1. Bill Johnson: argh.
     [7/29/11 1:41:45 AM] Brian Bibeault: What's wrong?
     [7/29/11 1:41:47 AM] 1. Bill Johnson: new old version:
     
     PASS: [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173], 123456 = 714 in 242ms
     PASS: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997], 123456 = 124 in 832ms
     [7/29/11 1:42:14 AM] Brian Bibeault: New new version blows it away.
     [7/29/11 1:42:34 AM] 1. Bill Johnson: new version:
     PASS: [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173], 123456 = 714 in 68ms
     PASS: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997], 123456 = 124 in 247ms
     [7/29/11 1:42:41 AM] Brian Bibeault: Whoa wtf.
     [7/29/11 1:42:44 AM] Brian Bibeault: Balls.
     [7/29/11 1:43:05 AM] 1. Bill Johnson: so, new version is only about 3-4x faster, not 50x :-P
     [7/29/11 1:43:11 AM] 1. Bill Johnson: which makes a hell of a lot more sense
     [7/29/11 1:43:17 AM] Brian Bibeault: And mine won't even execute.  Grr.
     [7/29/11 1:43:30 AM] Brian Bibeault: Dude it's 2am, I cannot do another late night, especially not with jennifer here.
     [7/29/11 1:43:38 AM] Brian Bibeault: I have to crash and consider this tomorrow if I can, or Monday.
     [7/29/11 1:43:39 AM] 1. Bill Johnson: i accidentally sorted the damn array on every recursive call
     [7/29/11 1:43:54 AM] Brian Bibeault: Yeah that's why I brought that bit out.
     [7/29/11 1:44:13 AM] Brian Bibeault: And also did my error checking separately, in that same function.  I thought that made sense and was good practice.
     [7/29/11 1:44:20 AM] Brian Bibeault: But you sure as hell didn't need to do that to win.  :P
     [7/29/11 1:44:38 AM] Brian Bibeault: So I have to make a version that goes faster than 
     PASS: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997], 123456 = 124 in 247ms
     [7/29/11 1:45:23 AM] Brian Bibeault: Gnight, Bill.
     [7/29/11 1:45:29 AM] 1. Bill Johnson: one sec
     [7/29/11 1:45:32 AM] Brian Bibeault: Hope I can go to sleep and won't have constant nightmares about this.
     [7/29/11 1:45:32 AM] Brian Bibeault: :P
     [7/29/11 1:45:38 AM] Brian Bibeault: Ok, whatcha got?
     [7/29/11 1:46:50 AM] Brian Bibeault: Still holding...
     [7/29/11 1:47:40 AM] 1. Bill Johnson: PASS: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571], 123456 = 36 in 772ms
     [7/29/11 1:47:42 AM] 1. Bill Johnson: :-P
     [7/29/11 1:48:12 AM] 1. Bill Johnson: beat a second on that, and i'll buy ya dinner, if ya didn't cheat
     [7/29/11 1:48:22 AM] Brian Bibeault: What counts as cheating?
     [7/29/11 1:48:26 AM] Brian Bibeault: Google?
     [7/29/11 1:48:33 AM] 1. Bill Johnson: yes
     [7/29/11 1:48:39 AM] Brian Bibeault: What about hard-coding the solution, a wait 800ms, and a return pass?  :P
     [7/29/11 1:48:56 AM] 1. Bill Johnson: i'll randomly remove one of the primes.
     [7/29/11 1:49:02 AM] Brian Bibeault: D'oh.
     [7/29/11 1:49:08 AM] Brian Bibeault: I promise I won't cheat - how long do I have?
     [7/29/11 1:49:10 AM] Brian Bibeault: 1 hour?
     [7/29/11 1:49:16 AM] Brian Bibeault: 4?
     [7/29/11 1:49:36 AM] Brian Bibeault: I assume if you give me 40 hours I'd get it on principle.
     [7/29/11 1:49:37 AM] 1. Bill Johnson: 'til tomorrow evening
     [7/29/11 1:49:41 AM] Brian Bibeault: Fuck dude.
     [7/29/11 1:49:44 AM] Brian Bibeault: I already fail.
     [7/29/11 1:49:54 AM] Brian Bibeault: Bed now, work tomorrow with a massive maintenance release that still isn't even building.
     [7/29/11 1:50:01 AM] Brian Bibeault: Meetings, come home and clean for Jennifer.
     [7/29/11 1:50:15 AM] Brian Bibeault: Will not get to touch this again till Sunday I bet, Sunday afternoon.
     [7/29/11 1:50:19 AM] Brian Bibeault: (depending on work)
     [7/29/11 1:50:50 AM] Brian Bibeault: Will just see but I think I'm not even going to get to try.
     [7/29/11 1:50:50 AM] 1. Bill Johnson: i have to get up to 8 digits now to get the "wait" dialog to come up :-D
     [7/29/11 1:50:53 AM] Brian Bibeault: Oh well, night Bill.
     [7/29/11 1:50:57 AM] Brian Bibeault: :P
     [7/29/11 1:52:12 AM] 1. Bill Johnson: PASS: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571], 1234567 = 347 in 7005ms
     [7/29/11 1:52:16 AM] 1. Bill Johnson: :-D
     [7/29/11 1:52:17 AM] 1. Bill Johnson: good night
     [7/29/11 2:03:40 AM] Brian Bibeault: Fuck now I am more alert than I was 15 minutes ago.  Damnit.
     [7/29/11 2:04:02 AM] Brian Bibeault: Too bad I cannot call in sick.
     
     ADD A HASH TABLE.  NEED TO DO UPDATES AND WHATNOT, but if I do that, it might fail completely to increase performance.
     */
"""