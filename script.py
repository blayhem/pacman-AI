import os
import subprocess as s

# layouts = {"capsuleClassic", "contestClassic", "mediumClassic", "mediumGrid", "minimaxClassic", "openClassic", "originalClassic", "smallClassic", "smallGrid", "smallGrid2", "testClassic", "trappedClassic", "trickyClassic"}
layouts = {"mediumGrid", "minimaxClassic", "smallGrid", "smallGrid2", "superSmallGrid", "testClassic", "trappedClassic"}
'''
discard: capsuleClassic, contestClassic, mediumClassic, openClassic, originalClassic, smallClassic, trickyClassic
format: Win Rate:      4/20 (0.20)

Recommended test cases:
- A ball of food and no ghost.
- A ball of food and a ghost
- A ball of food and two ghosts
'''
top = 0.0

for l in layouts:
    x = 100
    while x <= 1000:
        n = x + 10
        while n <= x + 100:
            i = 10
            while i <= 100:
                d = float(0.1)
                while d <= 1.0:
                    if l is 'smallGrid' or 'testClassic' or 'minimaxClassic' or 'mediumGrid':
                        k = 1
                    else:
                        k = 0
                    while k <= 2:
                        mean = 0.00
                        for i in range(1, 10, 1):
                            args = ''"iterations=%i,discount=%i"'' % (i, d)
                            ps1 = s.Popen(('python pacman.py -p EstimatePacmanMdpAgent -x %i -n %i -k %i -l %s -a %s -q' % (
                            x, n, k, l, args)).split(), stdout=s.PIPE)
                            ps2 = s.Popen("grep Rate".split(), stdin=ps1.stdout, stdout=s.PIPE)
                            ps3 = s.Popen(["cut", "-d", "(", "-f", "2"], stdin=ps2.stdout, stdout=s.PIPE)

                            out = s.check_output("cut -d ) -f 1".split(), stdin=ps3.stdout)
                            output = out.replace("\n", "")

                            ps1.wait()
                            ps2.wait()
                            ps3.wait()

                            mean += float(output)
                        mean /= 10
                        # print "win rate: %0.2f, x: %i, n: %i, k: %i, layout: %s, iterations: %i, discount: %0.1f" % (mean, x, n, k, l, i, d)
                        if mean > top:
                            top = mean
                            best_values = {x, n, k, l, i, d}
                            print "new top is: %0.2f; with values --> x: %i, n: %i, k: %i, layout: %s, iterations: %i, discount: %0.1f" % (top, x, n, k, l, i, d)

                        k += 1
                    d += 0.1
                i += 10
            n += 10
        x += 100
