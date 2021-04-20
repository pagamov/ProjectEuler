#include <iostream>
#include <ctime>

long long P(long long x) {
    return x * (3*x-1) / 2;
}

double diffclock(clock_t clock1,clock_t clock2) {
    double diffticks=clock2-clock1;
    double diffms=(diffticks)/(CLOCKS_PER_SEC);
    return diffms;
}

int main() {
    long long i = 286;
    clock_t start = clock();
    while (true) {
        // std::cout << "\r" << b << ' ' << P(b) << std::endl;
        long long Ti = i*(i+1)/2;

        for (long long n=1;n<i;n++) {
            long long Hn = n*(2*n-1);
            if (Hn == Ti) {
                break;
            } else if (Hn > Ti) {
                goto next;
            }
        }

        for (long long n=1;n<i;n++) {
            long long Pn = n*(3*n-1)/2;
            if (Pn == Ti) {
                break;
            } else if (Pn > Ti) {
                goto next;
            }
        }

        std::cout << "Ti = " << Ti << std::endl;
        goto ext;

        next:
        i += 1;
    }

    ext:
    clock_t end = clock();
    std::cout << diffclock(start,end)<<std::endl;
    return 0;
}
