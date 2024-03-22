import matplotlib
import matplotlib.pyplot as plt


def van_der_corput(n_sample, base):
    """Van der Corput sequence.
    :param int n_sample: number of element of the sequence.
    :param int base: base of the sequence.
    :return: sequence of Van der Corput.
    :rtype: list (n_samples,)
    """
    sequence = []
    for i in range(n_sample):
        n_th_number, denom = 0., 1.
        while i > 0:
            i, remainder = divmod(i, base)
            denom *= base
            n_th_number += remainder / denom
        sequence.append(n_th_number)

    return sequence


if __name__ == '__main__':
    matplotlib.use('TkAgg')

    n = [7, 35, 100, 151, 181, 1267, 22499]
    basePair = [[3, 5], [2, 3], [5, 7], [149, 151], [7, 181]]

    for elN in n:

        for bPair in basePair:
            x = van_der_corput(elN, bPair[0])
            y = van_der_corput(elN, bPair[1])

            fig = plt.figure()
            plt.plot(x, y, '.', color="black", markersize=1)
            plt.axis([0, 1, 0, 1])
            plt.savefig("n=" + str(elN) + "b1=" + str(bPair[0]) + "b2=" + str(bPair[1]) + '.png')
            plt.close(fig)
