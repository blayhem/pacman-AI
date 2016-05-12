import subprocess as s

# layouts = {"capsuleClassic", "contestClassic", "mediumClassic", "mediumGrid", "minimaxClassic", "openClassic", "originalClassic", "smallClassic", "smallGrid", "smallGrid2", "testClassic", "trappedClassic", "trickyClassic"}
layouts = {"mediumGrid", "minimaxClassic", "smallGrid2", "superSmallGrid", "testClassic", "trappedClassic"}
'''
discard: capsuleClassic, contestClassic, mediumClassic, openClassic, originalClassic, smallClassic, trickyClassic
discard2: smallgrid (max rate around 10%)
discard3: discount values between 0.1 and 0.5
format: Win Rate:      4/20 (0.20)

Recommended test cases:
- A ball of food and no ghost.
- A ball of food and a ghost
- A ball of food and two ghosts
'''
top = 0.0

for l in layouts:
    l = "testClassic"
    x = 100
    while x <= 500:
        n = x + 20
        while n <= x + 50:
            i = 50
            while i <= 200:
                d = float(0.6)
                while d <= 1.0:
                    if l is 'testClassic' or 'minimaxClassic' or 'mediumGrid':
                        k = 1
                    else:
                        k = 0
                    while k <= 2:
                        # mean = 0.00
                        # for j in range(1, 10, 1):
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

                        # mean += float(output)
                        # mean /= 10
                        mean = float(output)
                        print "mean win rate: %0.2f, x: %i, n: %i, k: %i, layout: %s, iterations: %i, discount: %0.1f" % (mean, x, n, k, l, i, d)
                        f = open('data.csv', 'a')
                        f.write('%0.2f,%i,%i,%i,%s,%i,%0.1f\n' % (mean, x, n, k, l, i, d))
                        f.close()
                        if mean > top:
                            top = mean
                            best_values = {x, n, k, l, i, d}
                            print "### NEW TOP is: %0.2f; with values --> x: %i, n: %i, k: %i, layout: %s, iterations: %i, discount: %0.1f" % (top, x, n, k, l, i, d)

                        k += 1
                    d += 0.2
                i += 50
            n += 10
        x += 100

