////////////////////////////////////////////////////////////////////////////////////////////////
//
// (C) Daniel Strano and the Qrack contributors 2017-2024. All rights reserved.
//
// "A quantum-inspired Monte Carlo integer factoring algorithm"
//
// This library originally demonstrated a (Shor's-like) "quantum-inspired" algorithm for integer
// factoring. It has since been developed into a general factoring algorithm and tool.
//
// The only potentially "original" part of this factoring algorithm is the "reverse trial
// division," as far as I can tell. The idea is, instead of performing typical trial division,
// we collect a short list of the first primes and remove all of their multiples from a
// "brute-force" guessing range by mapping a dense contiguous integer set, to a set without these
// multiples, by successively applying `guess = guess + guess / (p[i] - 1U) + 1U` for prime "`p`"
// in ascending (or any) order. Each prime applied this way effectively multiplies the
// brute-force guessing cardinality by a fraction (p-1)/p. Whatever "level" of primes we use, the
// cost per "guess" becomes higher.
//
// Then, we have a tuner that empirically estimates the cost per guess, and we multiply this by
// the (known) total cardinality of potential guesses. Whichever reverse trial division level has
// the lowest product of average cost per guess times guessing set cardinality should have the
// best performance, and the best level increases with the scale of the problem.
//
// Beyond this, we gain a functional advantage of a square-root over a more naive approach, by
// setting the brute force guessing range only between the highest prime in reverse trial
// division and the (modular) square root of the number to factor: if the number is semiprime,
// there is exactly one correct answer in this range, but including both factors in the range to
// search would cost us the square root advantage.
//
// Beyond that, we observed that many simple and well-known factoring techniques just don't pay
// dividends, for semiprime factoring. There's basically no point in checking either congruence
// of squares or even for a greatest common divisor, as these techniques require some dynamically
// variable overhead, and it tends to be faster (for semiprimes) just to check if a guess is an
// exact factor, on the smallest range we can identify that contains at least one correct answer.
//
// So, this is actually quite rudimentary and just "brute force," except for "reverse trial
// division" and the upper bound on the guessing range. It just better work entirely in CPU cache,
// then, but it only requires de minimis maximum memory footprint. (There are congruence of squares
// and greatest common divisor checks available for numbers besides semiprimes.)
//
// Theoretically, this algorithm might return to its original "quantum-inspired" design with the
// providence of a high-quality, high-throughput generator of uniform random bit strings. If we were
// to use the algorithm as-is, except guessing according to a uniform random distribution instead of
// systematically ascending through every possible "guess," then the average time to solution can be
// realized in any case, unlike the deterministic version of the algorithm. Then, no work towards
// the solution can ever be lost in event of interruption of the program, because every single guess
// (even the first) has the same probability (in the ideal) of leading to successful factoring.
//
// (This file was heavily adapted from
// https://github.com/ProjectQ-Framework/ProjectQ/blob/develop/examples/shor.py,
// with thanks to ProjectQ!)
//
// Licensed under the GNU Lesser General Public License V3.
// See LICENSE.md in the project root or https://www.gnu.org/licenses/lgpl-3.0.en.html
// for details.

#include "dispatchqueue.hpp"

#include <algorithm>
#include <chrono>
#include <cmath>
#include <float.h>
#include <fstream>
#include <future>
#include <iomanip>
#include <iostream>
#include <map>
#include <memory>
#include <mutex>
#include <random>
#include <stdlib.h>
#include <string>
#include <time.h>

#include <boost/dynamic_bitset.hpp>
#include <boost/multiprecision/cpp_int.hpp>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace Qimcifa {

typedef boost::multiprecision::cpp_int BigInteger;

// Make this a multiple of 2, 3, 5, 7, or 11.
constexpr int SMALLEST_WHEEL = 2310;
constexpr int MIN_RTD_LEVEL = 5;

DispatchQueue dispatch(std::thread::hardware_concurrency());

// See https://stackoverflow.com/questions/101439/the-most-efficient-way-to-implement-an-integer-based-power-function-powint-int
BigInteger ipow(BigInteger base, unsigned exp)
{
    BigInteger result = 1U;
    for (;;)
    {
        if (exp & 1U) {
            result *= base;
        }
        exp >>= 1U;
        if (!exp) {
            break;
        }
        base *= base;
    }

    return result;
}

inline uint64_t log2(BigInteger n) {
    uint64_t pow = 0U;
    while (n >>= 1U) {
        ++pow;
    }
    return pow;
}

inline BigInteger sqrt(const BigInteger& toTest)
{
    // Otherwise, find b = sqrt(b^2).
    BigInteger start = 1U, end = toTest >> 1U, ans = 0U;
    do {
        const BigInteger mid = (start + end) >> 1U;

        // If toTest is a perfect square
        const BigInteger sqr = mid * mid;
        if (sqr == toTest) {
            return mid;
        }

        if (sqr < toTest) {
            // Since we need floor, we update answer when mid*mid is smaller than p, and move closer to sqrt(p).
            start = mid + 1U;
            ans = mid;
        } else {
            // If mid*mid is greater than p
            end = mid - 1U;
        }
    } while (start <= end);

    return ans;
}

inline BigInteger gcd(BigInteger n1, BigInteger n2)
{
    while (n2) {
        const BigInteger t = n1;
        n1 = n2;
        n2 = t % n2;
    }

    return n1;
}

inline BigInteger forward2and3(const size_t& p) {
    // Make this NOT a multiple of 2 or 3.
    return (p << 1U) + (~(~p | 1U)) - 1U;
}

inline BigInteger forward5(const size_t& p) {
    constexpr unsigned char m[8U] = {
        1U, 7U, 11U, 13U, 17U, 19U, 23U, 29U
    };
    return m[p % 8U] + (p / 8U) * 30U;
}

inline BigInteger forward7(const size_t& p) {
    constexpr unsigned char m[48U] = {
        1U, 11U, 13U, 17U, 19U, 23U, 29U, 31U, 37U, 41U, 43U, 47U, 53U, 59U, 61U, 67U, 71U, 73U, 79U, 83U, 89U,
        97U, 101U, 103U, 107U, 109U, 113U, 121U, 127U, 131U, 137U, 139U, 143U, 149U, 151U, 157U, 163U, 167U,
        169U, 173U, 179U, 181U, 187U, 191U, 193U, 197U, 199U, 209U
    };
    return m[p % 48U] + (p / 48U) * 210U;
}

inline size_t backward2and3(const BigInteger& n) {
    return (size_t)((~(~n | 1U)) / 3U) + 1U;
}

inline size_t backward5(const BigInteger& n) {
    return (size_t)(((((n + 1U) << 2U) / 5U + 1U) << 1U) / 3U + 1U) >> 1U;
}

inline size_t backward7(const BigInteger& n) {
    constexpr unsigned char m[48U] = {
        1U, 11U, 13U, 17U, 19U, 23U, 29U, 31U, 37U, 41U, 43U, 47U, 53U, 59U, 61U, 67U, 71U, 73U, 79U, 83U, 89U,
        97U, 101U, 103U, 107U, 109U, 113U, 121U, 127U, 131U, 137U, 139U, 143U, 149U, 151U, 157U, 163U, 167U,
        169U, 173U, 179U, 181U, 187U, 191U, 193U, 197U, 199U, 209U
    };
    return (size_t)(std::distance(m, std::lower_bound(m, m + 48U, n % 210U)) + 48U * (n / 210U) + 1U);
}

inline size_t GetWheel5and7Increment(unsigned short& wheel5, unsigned long long& wheel7) {
    constexpr unsigned short wheel5Back = 1U << 9U;
    constexpr unsigned long long wheel7Back = 1ULL << 55U;
    unsigned wheelIncrement = 0U;
    bool is_wheel_multiple = false;
    do {
        is_wheel_multiple = (bool)(wheel5 & 1U);
        wheel5 >>= 1U;
        if (is_wheel_multiple) {
            wheel5 |= wheel5Back;
            ++wheelIncrement;
            continue;
        }

        is_wheel_multiple = (bool)(wheel7 & 1U);
        wheel7 >>= 1U;
        if (is_wheel_multiple) {
            wheel7 |= wheel7Back;
        }
        ++wheelIncrement;
    } while (is_wheel_multiple);

    return (size_t)wheelIncrement;
}

std::vector<BigInteger> SieveOfEratosthenes(const BigInteger& n)
{
    std::vector<BigInteger> knownPrimes = { 2U, 3U, 5U, 7U };
    if (n < 2U) {
        return std::vector<BigInteger>();
    }

    if (n < (knownPrimes.back() + 2U)) {
        const auto highestPrimeIt = std::upper_bound(knownPrimes.begin(), knownPrimes.end(), n);
        return std::vector<BigInteger>(knownPrimes.begin(), highestPrimeIt);
    }

    knownPrimes.reserve(std::expint(log((double)n)) - std::expint(log(2)));

    // We are excluding multiples of the first few
    // small primes from outset. For multiples of
    // 2, 3, and 5 this reduces complexity to 4/15.
    const size_t cardinality = backward5(n);

    // Create a boolean array "prime[0..cardinality]"
    // and initialize all entries it as true. Rather,
    // reverse the true/false meaning, so we can use
    // default initialization. A value in notPrime[i]
    // will finally be false only if i is a prime.
    std::unique_ptr<bool[]> uNotPrime(new bool[cardinality + 1U]());
    bool* notPrime = uNotPrime.get();

    // We dispatch multiple marking asynchronously.
    // If we've already marked all primes up to x,
    // we're free to continue to up to x * x,
    // then we synchronize.
    BigInteger threadBoundary = 36U;

    // Get the remaining prime numbers.
    unsigned short wheel5 = 129U;
    unsigned long long wheel7 = 9009416540524545ULL;
    size_t o = 1U;
    for (;;) {
        o += GetWheel5and7Increment(wheel5, wheel7);

        const BigInteger p = forward2and3(o);
        if ((p * p) > n) {
            break;
        }

        if (threadBoundary < p) {
            dispatch.finish();
            threadBoundary *= threadBoundary;
        }

        if (notPrime[backward5(p)]) {
            continue;
        }

        knownPrimes.push_back(p);

        dispatch.dispatch([&n, p, &notPrime]() {
            // We are skipping multiples of 2, 3, and 5
            // for space complexity, for 4/15 the bits.
            // More are skipped by the wheel for time.
            const BigInteger p2 = p << 1U;
            const BigInteger p4 = p << 2U;
            BigInteger i = p * p;

            // "p" already definitely not a multiple of 3.
            // Its remainder when divided by 3 can be 1 or 2.
            // If it is 2, we can do a "half iteration" of the
            // loop that would handle remainder of 1, and then
            // we can proceed with the 1 remainder loop.
            // This saves 2/3 of updates (or modulo).
            if ((p % 3U) == 2U) {
                notPrime[backward5(i)] = true;
                i += p2;
                if (i > n) {
                    return false;
                }
            }

            for (;;) {
                if (i % 5U) {
                    notPrime[backward5(i)] = true;
                }
                i += p4;
                if (i > n) {
                    return false;
                }

                if (i % 5U) {
                    notPrime[backward5(i)] = true;
                }
                i += p2;
                if (i > n) {
                    return false;
                }
            }

            return false;
        });
    }

    dispatch.finish();

    for (;;) {
        const BigInteger p = forward2and3(o);
        if (p > n) {
            break;
        }

        o += GetWheel5and7Increment(wheel5, wheel7);

        if (notPrime[backward5(p)]) {
            continue;
        }

        knownPrimes.push_back(p);
    }

    return knownPrimes;
}

std::vector<BigInteger> SegmentedSieveOfEratosthenes(BigInteger n)
{
    // TODO: This should scale to the system.
    // Assume the L1/L2 cache limit is 2048 KB.
    // We save half our necessary bytes by
    // removing multiples of 2.
    // The simple sieve removes multiples of 2, 3, and 5.
    // limit = 2048 KB = 2097152 B,
    // limit = ((((limit * 2) * 3) / 2) * 5) / 4
    constexpr size_t limit = 7864321ULL;

    if (!(n & 1U)) {
        --n;
    }
    while (!(n % 3U) || !(n % 5U)) {
        n -= 2U;
    }
    if (limit >= n) {
        return SieveOfEratosthenes(n);
    }
    std::vector<BigInteger> knownPrimes = SieveOfEratosthenes(limit);
    knownPrimes.reserve(std::expint(log((double)n)) - std::expint(log(2)));

    // Divide the range in different segments
    const size_t nCardinality = backward5(n);
    size_t low = backward5(limit);
    size_t high = low + limit;

    // Process one segment at a time till we pass n.
    while (low < nCardinality)
    {
        if (high > nCardinality) {
           high = nCardinality;
        }

        const BigInteger fLo = forward5(low);
        const size_t sqrtIndex = std::distance(
            knownPrimes.begin(),
            std::upper_bound(knownPrimes.begin(), knownPrimes.end(), sqrt(forward5(high)) + 1U)
        );

        const size_t cardinality = high - low;
        bool notPrime[cardinality + 1U] = { false };

        for (size_t k = 3U; k < sqrtIndex; ++k) {
            const BigInteger& p = knownPrimes[k];
            dispatch.dispatch([&fLo, &low, &cardinality, p, &notPrime]() {
                // We are skipping multiples of 2.
                const BigInteger p2 = p << 1U;

                // Find the minimum number in [low..high] that is
                // a multiple of prime[i] (divisible by prime[i])
                // For example, if low is 31 and prime[i] is 3,
                // we start with 33.
                BigInteger i = (fLo / p) * p;
                if (i < fLo) {
                    i += p;
                }
                if (!(i & 1U)) {
                    i += p;
                }

                for (;;) {
                    const size_t o = backward5(i) - low;
                    if (o > cardinality) {
                        return false;
                    }
                    if ((i % 3U) && (i % 5U)) {
                        notPrime[o] = true;
                    }
                    i += p2;
                }

                return false;
            });
        }
        dispatch.finish();

        // Numbers which are not marked are prime
        for (size_t o = 1U; o <= cardinality; ++o) {
            if (!notPrime[o]) {
                knownPrimes.push_back(forward5(o + low));
            }
        }

        // Update low and high for next segment
        low = low + limit;
        high = low + limit;
    }

    return knownPrimes;
}

BigInteger CountPrimesTo(const BigInteger& n)
{
    const BigInteger knownPrimes[4U] = { 2U, 3U, 5U, 7U };
    if (n < 2U) {
        return 0U;
    }

    if (n < 11U) {
        const auto highestPrimeIt = std::upper_bound(knownPrimes, knownPrimes + 4U, n);
        return std::distance(knownPrimes, highestPrimeIt);
    }

    // We are excluding multiples of the first few
    // small primes from outset. For multiples of
    // 2, 3, and 5 this reduces complexity to 4/15.
    const size_t cardinality = backward5(n);

    // Create a boolean array "prime[0..cardinality]"
    // and initialize all entries it as true. Rather,
    // reverse the true/false meaning, so we can use
    // default initialization. A value in notPrime[i]
    // will finally be false only if i is a prime.
    std::unique_ptr<bool[]> uNotPrime(new bool[cardinality + 1U]());
    bool* notPrime = uNotPrime.get();

    // We dispatch multiple marking asynchronously.
    // If we've already marked all primes up to x,
    // we're free to continue to up to x * x,
    // then we synchronize.
    BigInteger threadBoundary = 36U;

    // Get the remaining prime numbers.
    unsigned short wheel5 = 129U;
    unsigned long long wheel7 = 9009416540524545ULL;
    size_t o = 1U;
    BigInteger count = 4U;
    for (;;) {
        o += GetWheel5and7Increment(wheel5, wheel7);

        const BigInteger p = forward2and3(o);
        if ((p * p) > n) {
            break;
        }

        if (threadBoundary < p) {
            dispatch.finish();
            threadBoundary *= threadBoundary;
        }

        if (notPrime[backward5(p)]) {
            continue;
        }

        ++count;

        dispatch.dispatch([&n, p, &notPrime]() {
            // We are skipping multiples of 2, 3, and 5
            // for space complexity, for 4/15 the bits.
            // More are skipped by the wheel for time.
            const BigInteger p2 = p << 1U;
            const BigInteger p4 = p << 2U;
            BigInteger i = p * p;

            // "p" already definitely not a multiple of 3.
            // Its remainder when divided by 3 can be 1 or 2.
            // If it is 2, we can do a "half iteration" of the
            // loop that would handle remainder of 1, and then
            // we can proceed with the 1 remainder loop.
            // This saves 2/3 of updates (or modulo).
            if ((p % 3U) == 2U) {
                notPrime[backward5(i)] = true;
                i += p2;
                if (i > n) {
                    return false;
                }
            }

            for (;;) {
                if (i % 5U) {
                    notPrime[backward5(i)] = true;
                }
                i += p4;
                if (i > n) {
                    return false;
                }

                if (i % 5U) {
                    notPrime[backward5(i)] = true;
                }
                i += p2;
                if (i > n) {
                    return false;
                }
            }

            return false;
        });
    }

    dispatch.finish();

    for (;;) {
        const BigInteger p = forward2and3(o);
        if (p > n) {
            break;
        }

        o += GetWheel5and7Increment(wheel5, wheel7);

        if (notPrime[backward5(p)]) {
            continue;
        }

        ++count;
    }

    return count;
}

BigInteger SegmentedCountPrimesTo(BigInteger n)
{
    // TODO: This should scale to the system.
    // Assume the L1/L2 cache limit is 2048 KB.
    // We save half our necessary bytes by
    // removing multiples of 2.
    // The simple sieve removes multiples of 2, 3, and 5.
    // limit = 2048 KB = 2097152 B,
    // limit = ((((limit * 2) * 3) / 2) * 5) / 4
    constexpr size_t limit = 7864321ULL;

    if (!(n & 1U)) {
        --n;
    }
    while (!(n % 3U) || !(n % 5U)) {
        n -= 2U;
    }
    if (limit >= n) {
        return CountPrimesTo(n);
    }
    BigInteger sqrtnp1 = (sqrt(n) + 1U) | 1U;
    while (!(sqrtnp1 % 3U) || !(sqrtnp1 % 5U)) {
        sqrtnp1 += 2U;
    }
    const BigInteger practicalLimit = (sqrtnp1 < limit) ? sqrtnp1 : limit;
    std::vector<BigInteger> knownPrimes = SieveOfEratosthenes(practicalLimit);
    if (practicalLimit < sqrtnp1) {
        knownPrimes.reserve(std::expint(log((double)sqrtnp1)) - std::expint(log(2)));
    }
    size_t count = knownPrimes.size();

    // Divide the range in different segments
    const size_t nCardinality = backward5(n);
    size_t low = backward5(practicalLimit);
    size_t high = low + limit;

    // Process one segment at a time till we pass n.
    while (low < nCardinality)
    {
        if (high > nCardinality) {
           high = nCardinality;
        }
        const BigInteger fLo = forward5(low);
        const size_t sqrtIndex = std::distance(
            knownPrimes.begin(),
            std::upper_bound(knownPrimes.begin(), knownPrimes.end(), sqrt(forward5(high)) + 1U)
        );

        const size_t cardinality = high - low;
        bool notPrime[cardinality + 1U] = { false };

        // Use the primes found by the simple sieve
        // to find primes in current range
        for (size_t k = 3U; k < sqrtIndex; ++k) {
            const BigInteger& p = knownPrimes[k];
            dispatch.dispatch([&fLo, &low, &cardinality, p, &notPrime]() {
                // We are skipping multiples of 2.
                const BigInteger p2 = p << 1U;

                // Find the minimum number in [low..high] that is
                // a multiple of prime[i] (divisible by prime[i])
                // For example, if low is 31 and prime[i] is 3,
                // we start with 33.
                BigInteger i = (fLo / p) * p;
                if (i < fLo) {
                    i += p;
                }
                if (!(i & 1U)) {
                    i += p;
                }

                for (;;) {
                    const size_t o = backward5(i) - low;
                    if (o > cardinality) {
                        return false;
                    }
                    if ((i % 3U) && (i % 5U)) {
                        notPrime[o] = true;
                    }
                    i += p2;
                }

                return false;
            });
        }
        dispatch.finish();

        if (knownPrimes.back() >= sqrtnp1) {
            for (size_t o = 1U; o <= cardinality; ++o) {
                if (!notPrime[o]) {
                    ++count;
                }
            }
        } else {
            for (size_t o = 1U; o <= cardinality; ++o) {
                if (!notPrime[o]) {
                    const BigInteger p = forward5(o + low);
                    if (p <= sqrtnp1) {
                        knownPrimes.push_back(p);
                    }
                    ++count;
                }
            }
        }

        // Update low and high for next segment
        low = low + limit;
        high = low + limit;
    }

    return count;
}

constexpr unsigned short wheel11[480U] = {
    1U, 13U, 17U, 19U, 23U, 29U, 31U, 37U, 41U, 43U, 47U, 53U, 59U, 61U, 67U, 71U, 73U, 79U, 83U, 89U, 97U, 101U,
    103U, 107U, 109U, 113U, 127U, 131U, 137U, 139U, 149U, 151U, 157U, 163U, 167U, 169U, 173U, 179U, 181U, 191U,
    193U, 197U, 199U, 211U, 221U, 223U, 227U, 229U, 233U, 239U, 241U, 247U, 251U, 257U, 263U, 269U, 271U, 277U,
    281U, 283U, 289U, 293U, 299U, 307U, 311U, 313U, 317U, 323U, 331U, 337U, 347U, 349U, 353U, 359U, 361U, 367U,
    373U, 377U, 379U, 383U, 389U, 391U, 397U, 401U, 403U, 409U, 419U, 421U, 431U, 433U, 437U, 439U, 443U, 449U,
    457U, 461U, 463U, 467U, 479U, 481U, 487U, 491U, 493U, 499U, 503U, 509U, 521U, 523U, 527U, 529U, 533U, 541U,
    547U, 551U, 557U, 559U, 563U, 569U, 571U, 577U, 587U, 589U, 593U, 599U, 601U, 607U, 611U, 613U, 617U, 619U,
    629U, 631U, 641U, 643U, 647U, 653U, 659U, 661U, 667U, 673U, 677U, 683U, 689U, 691U, 697U, 701U, 703U, 709U,
    713U, 719U, 727U, 731U, 733U, 739U, 743U, 751U, 757U, 761U, 767U, 769U, 773U, 779U, 787U, 793U, 797U, 799U,
    809U, 811U, 817U, 821U, 823U, 827U, 829U, 839U, 841U, 851U, 853U, 857U, 859U, 863U, 871U, 877U, 881U, 883U,
    887U, 893U, 899U, 901U, 907U, 911U, 919U, 923U, 929U, 937U, 941U, 943U, 947U, 949U, 953U, 961U, 967U, 971U,
    977U, 983U, 989U, 991U, 997U, 1003U, 1007U, 1009U, 1013U, 1019U, 1021U, 1027U, 1031U, 1033U, 1037U, 1039U,
    1049U, 1051U, 1061U, 1063U, 1069U, 1073U, 1079U, 1081U, 1087U, 1091U, 1093U, 1097U, 1103U, 1109U, 1117U, 1121U,
    1123U, 1129U, 1139U, 1147U, 1151U, 1153U, 1157U, 1159U, 1163U, 1171U, 1181U, 1187U, 1189U, 1193U, 1201U, 1207U,
    1213U, 1217U, 1219U, 1223U, 1229U, 1231U, 1237U, 1241U, 1247U, 1249U, 1259U, 1261U, 1271U, 1273U, 1277U, 1279U,
    1283U, 1289U, 1291U, 1297U, 1301U, 1303U, 1307U, 1313U, 1319U, 1321U, 1327U, 1333U, 1339U, 1343U, 1349U, 1357U,
    1361U, 1363U, 1367U, 1369U, 1373U, 1381U, 1387U, 1391U, 1399U, 1403U, 1409U, 1411U, 1417U, 1423U, 1427U, 1429U,
    1433U, 1439U, 1447U, 1451U, 1453U, 1457U, 1459U, 1469U, 1471U, 1481U, 1483U, 1487U, 1489U, 1493U, 1499U, 1501U,
    1511U, 1513U, 1517U, 1523U, 1531U, 1537U, 1541U, 1543U, 1549U, 1553U, 1559U, 1567U, 1571U, 1577U, 1579U, 1583U,
    1591U, 1597U, 1601U, 1607U, 1609U, 1613U, 1619U, 1621U, 1627U, 1633U, 1637U, 1643U, 1649U, 1651U, 1657U, 1663U,
    1667U, 1669U, 1679U, 1681U, 1691U, 1693U, 1697U, 1699U, 1703U, 1709U, 1711U, 1717U, 1721U, 1723U, 1733U, 1739U,
    1741U, 1747U, 1751U, 1753U, 1759U, 1763U, 1769U, 1777U, 1781U, 1783U, 1787U, 1789U, 1801U, 1807U, 1811U, 1817U,
    1819U, 1823U, 1829U, 1831U, 1843U, 1847U, 1849U, 1853U, 1861U, 1867U, 1871U, 1873U, 1877U, 1879U, 1889U, 1891U,
    1901U, 1907U, 1909U, 1913U, 1919U, 1921U, 1927U, 1931U, 1933U, 1937U, 1943U, 1949U, 1951U, 1957U, 1961U, 1963U,
    1973U, 1979U, 1987U, 1993U, 1997U, 1999U, 2003U, 2011U, 2017U, 2021U, 2027U, 2029U, 2033U, 2039U, 2041U, 2047U,
    2053U, 2059U, 2063U, 2069U, 2071U, 2077U, 2081U, 2083U, 2087U, 2089U, 2099U, 2111U, 2113U, 2117U, 2119U, 2129U,
    2131U, 2137U, 2141U, 2143U, 2147U, 2153U, 2159U, 2161U, 2171U, 2173U, 2179U, 2183U, 2197U, 2201U, 2203U, 2207U,
    2209U, 2213U, 2221U, 2227U, 2231U, 2237U, 2239U, 2243U, 2249U, 2251U, 2257U, 2263U, 2267U, 2269U, 2273U, 2279U,
    2281U, 2287U, 2291U, 2293U, 2297U, 2309U
};

inline BigInteger forward(const BigInteger& p) {
    // Make this NOT a multiple of 2, 3, 5, 7, or 11.
    return wheel11[(size_t)(p % 480U)] + (p / 480U) * 2310U;
}

inline BigInteger backward(const BigInteger& n) {
    return std::distance(wheel11, std::lower_bound(wheel11, wheel11 + 480U, size_t(n % 2310U))) + 480U * (size_t)(n / 2310U) + 1U;
}

inline bool isMultiple(const BigInteger& p, const std::vector<BigInteger>& knownPrimes) {
    for (const BigInteger& prime : knownPrimes) {
        if (!(p % prime)) {
            return true;
        }
    }
    return false;
}

boost::dynamic_bitset<size_t> wheel_inc(std::vector<BigInteger> primes, BigInteger limit) {
    BigInteger radius = 1U;
    for (const BigInteger& i : primes) {
        radius *= i;
    }
    if (limit < radius) {
        radius = limit;
    }
    const BigInteger prime = primes.back();
    primes.pop_back();
    boost::dynamic_bitset<uint64_t> o;
    for (BigInteger i = 1U; i <= radius; ++i) {
        if (!isMultiple(i, primes)) {
            o.push_back(!(i % prime));
        }
    }

    boost::dynamic_bitset<size_t> output(o.size());
    for (size_t i = 0U; i < o.size(); ++i) {
        output[i] = o[i];
    }
    output >>= 1U;

    return output;
}

std::vector<boost::dynamic_bitset<size_t>> wheel_gen(const std::vector<BigInteger>& primes, BigInteger limit) {
    std::vector<boost::dynamic_bitset<size_t>> output;
    std::vector<BigInteger> wheelPrimes;
    for (const BigInteger& p : primes) {
        wheelPrimes.push_back(p);
        output.push_back(wheel_inc(wheelPrimes, limit));
    }
    return output;
}

inline size_t GetWheelIncrement(std::vector<boost::dynamic_bitset<size_t>>* inc_seqs) {
    size_t wheelIncrement = 0U;
    bool is_wheel_multiple = false;
    do {
        for (size_t i = 0; i < inc_seqs->size(); ++i) {
            boost::dynamic_bitset<size_t>& wheel = (*inc_seqs)[i];
            is_wheel_multiple = wheel.test(0U);
            wheel >>= 1U;
            if (is_wheel_multiple) {
                wheel[wheel.size() - 1U] = true;
                break;
            }
        }
        ++wheelIncrement;
    } while (is_wheel_multiple);

    return wheelIncrement;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                  WRITTEN BY ELARA (GPT) BELOW                                          //
////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Utility to perform modular exponentiation
BigInteger modExp(BigInteger base, BigInteger exp, const BigInteger& mod) {
    BigInteger result = 1U;
    while (exp) {
        if (exp & 1U) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp >>= 1U;
    }

    return result;
}

// Perform Gaussian elimination on a binary matrix
void gaussianElimination(std::map<BigInteger, boost::dynamic_bitset<uint64_t>>* matrix) {
    size_t rows = matrix->size();
    size_t cols = matrix->begin()->second.size();
    std::vector<int> pivots(cols, -1);
    for (size_t col = 0; col < cols; ++col) {
        auto colIt = matrix->begin();
        std::advance(colIt, col);
        for (size_t row = col; row < rows; ++row) {
            auto rowIt = matrix->begin();
            std::advance(rowIt, row);
            if (rowIt->second[col]) {
                std::swap(colIt->second, rowIt->second);
                pivots[col] = row;
                break;
            }
        }
        if (pivots[col] == -1) {
            continue;
        }
        const boost::dynamic_bitset<uint64_t>& c = colIt->second;
        for (size_t row = 0; row < rows; ++row) {
            auto rowIt = matrix->begin();
            std::advance(rowIt, row);
            boost::dynamic_bitset<uint64_t>& r = rowIt->second;
            if ((row != col) && r[col]) {
                r ^= c;
            }
        }
    }
}

// Compute the prime factorization modulo 2
boost::dynamic_bitset<uint64_t> factorizationVector(BigInteger num, const std::vector<BigInteger>& primes) {
    boost::dynamic_bitset<uint64_t> vec(primes.size(), false);
    for (size_t i = 0U; i < primes.size(); ++i) {
        bool count = false;
        while (!(num % primes[i])) {
            num /= primes[i];
            count = !count;
        }
        vec[i] = count;
    }
    if (num != 1U) {
        return boost::dynamic_bitset<uint64_t>();
    }

    return vec;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                  WRITTEN BY ELARA (GPT) ABOVE                                          //
////////////////////////////////////////////////////////////////////////////////////////////////////////////

struct Factorizer {
    std::mutex batchMutex;
    std::mutex smoothNumberMapMutex;
    std::default_random_engine rng;
    BigInteger toFactorSqr;
    BigInteger toFactor;
    BigInteger toFactorSqrt;
    BigInteger batchRange;
    BigInteger batchNumber;
    BigInteger batchBound;
    size_t wheelRatio;
    size_t primePartBound;
    std::vector<BigInteger> primes;

    Factorizer(const BigInteger& tfsqr, const BigInteger tf, const BigInteger& tfsqrt, const BigInteger& range, size_t nodeId, size_t wr, const std::vector<BigInteger>& p, const size_t& ppb = 0U)
        : rng({})
        , toFactorSqr(tfsqr)
        , toFactor(tf)
        , toFactorSqrt(tfsqrt)
        , batchRange(range)
        , batchNumber(0)
        , batchBound((nodeId + 1U) * range)
        , wheelRatio(wr)
        , primePartBound(ppb)
        , primes(p)
    {
    }

    BigInteger getNextBatch() {
        std::lock_guard<std::mutex> lock(batchMutex);

        if (batchNumber == batchRange) {
            return batchBound;
        }

        return batchBound - (++batchNumber);
    }

    BigInteger getNextAltBatch() {
        std::lock_guard<std::mutex> lock(batchMutex);

        if (batchNumber == batchRange) {
            return batchBound;
        }

        const BigInteger halfBatchNum = (batchNumber++ >> 1U);

        return batchBound - ((batchNumber & 1U) ? (BigInteger)(batchRange - halfBatchNum) : (BigInteger)(halfBatchNum + 1U));
    }

    BigInteger bruteForce(std::vector<boost::dynamic_bitset<uint64_t>>* inc_seqs)
    {
        // Up to wheel factorization, try all batches up to the square root of toFactor.
        for (BigInteger batchNum = getNextBatch(); batchNum < batchBound; batchNum = getNextBatch()) {
            const BigInteger batchStart = batchNum * wheelRatio;
            const BigInteger batchEnd = (batchNum + 1U) * wheelRatio;
            for (BigInteger p = batchStart; p < batchEnd;) {
                p += GetWheelIncrement(inc_seqs);
                const BigInteger n = gcd(forward(p), toFactor);
                if (n != 1U) {
                    batchNumber = batchBound;
                    return n;
                }
            }
        }

        return 1U;
    }

    BigInteger smoothCongruences(std::vector<boost::dynamic_bitset<uint64_t>>* inc_seqs, std::vector<BigInteger>* semiSmoothParts, std::map<BigInteger, boost::dynamic_bitset<uint64_t>>* smoothNumberMap)
    {
        // Up to wheel factorization, try all batches up to the square root of toFactor.
        // Since the largest prime factors of these numbers is relatively small,
        // use the "exhaust" of brute force to produce smooth numbers for Quadratic Sieve.
        for (BigInteger batchNum = getNextAltBatch(); batchNum < batchBound; batchNum = getNextAltBatch()) {
            const BigInteger batchStart = batchNum * wheelRatio;
            const BigInteger batchEnd = (batchNum + 1U) * wheelRatio;
            for (BigInteger p = batchStart; p < batchEnd;) {
                // Skip increments on the "wheels" (or "gears").
                p += GetWheelIncrement(inc_seqs);
                // Brute-force check if the sequential number is a factor.
                const BigInteger n = gcd(forward(p), toFactor);
                // If so, terminate this node and return the answer.
                if (n != 1U) {
                    batchNumber = batchBound;
                    return n;
                }
                // Use the "exhaust" to produce smoother numbers.
                semiSmoothParts->push_back(n);
                // Batch this work, to reduce contention.
                if (semiSmoothParts->size() < primePartBound) {
                    continue;
                }
                // Our "smooth parts" are smaller than the square root of toFactor.
                // We combine them semi-randomly, to produce numbers just larger than the square root of toFactor.
                const BigInteger m = makeSmoothNumbers(semiSmoothParts, smoothNumberMap);
                // Check the factor returned.
                if (m != 1U) {
                    // Gaussian elimination found a factor!
                    batchNumber = batchBound;
                    return m;
                }
            }
        }

        return 1U;
    }

    BigInteger makeSmoothNumbers(std::vector<BigInteger>* semiSmoothParts, std::map<BigInteger, boost::dynamic_bitset<uint64_t>>* smoothNumberMap)
    {
        // Factorize all "smooth parts."
        std::vector<BigInteger> smoothParts;
        std::map<BigInteger, boost::dynamic_bitset<uint64_t>> smoothPartsMap;
        for (const BigInteger& n : (*semiSmoothParts)) {
            const boost::dynamic_bitset<uint64_t> fv = factorizationVector(n, primes);
            if (fv.size()) {
                smoothPartsMap[n] = fv;
                smoothParts.push_back(n);
            }
        }
        // We can clear the thread's buffer vector.
        semiSmoothParts->clear();

        // This is the only nondeterminism in the algorithm.
        std::shuffle(smoothParts.begin(), smoothParts.end(), rng);

        // Now that smooth parts have been shuffled, just multiply down
        // the list until they are larger than square root of toFactor.
        BigInteger smoothNumber = 1U;
        boost::dynamic_bitset<uint64_t> fv(primes.size(), false);
        for (size_t spi = 0U; spi < smoothParts.size(); ++spi) {
            const BigInteger& sp = smoothParts[spi];
            // This multiplies together the factorizations of the smooth parts
            // (producing the overall factorization of their multiplication)
            fv ^= smoothPartsMap[sp];
            smoothNumber *= sp;
            // Check if the number is big enough
            if (smoothNumber <= toFactorSqrt) {
                continue;
            }
            // For lock_guard scope
            if (true) {
                std::lock_guard<std::mutex> lock(smoothNumberMapMutex);
                auto it = smoothNumberMap->find(smoothNumber);
                if (it == smoothNumberMap->end()) {
                    (*smoothNumberMap)[smoothNumber] = fv;
                }
            }
            // Reset "smoothNumber" and its factorization vector.
            smoothNumber = 1U;
            fv = boost::dynamic_bitset<uint64_t>(primes.size(), false);
        }
        // We're done with smoothParts.
        smoothParts.clear();

        // This entire next section is blocking (for Quadratic Sieve Gaussian elimination).
        std::lock_guard<std::mutex> lock(smoothNumberMapMutex);
        return findFactorViaGaussianElimination(toFactor, smoothNumberMap);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //                                  WRITTEN BY ELARA (GPT) BELOW                                          //
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    // Find factor via Gaussian elimination
    BigInteger findFactorViaGaussianElimination(BigInteger target, std::map<BigInteger, boost::dynamic_bitset<uint64_t>>* smoothNumberMap) {
        // Perform Gaussian elimination
        gaussianElimination(smoothNumberMap);

        // Check for linear dependencies and find a congruence of squares
        std::vector<size_t> toStrike;
        for (size_t i = 0; i < smoothNumberMap->size(); ++i) {
            auto iIt = smoothNumberMap->begin();
            std::advance(iIt, i);
            boost::dynamic_bitset<uint64_t>& iRow = iIt->second;
            for (size_t j = i + 1; j < smoothNumberMap->size(); ++j) {
                auto jIt = smoothNumberMap->begin();
                std::advance(jIt, j);
                boost::dynamic_bitset<uint64_t>& jRow = jIt->second;
                if (iRow != jRow) {
                    continue;
                }

                toStrike.push_back(j);

                // Compute x and y
                const BigInteger x = (iIt->first * jIt->first) % target;
                const BigInteger y = modExp(x, target / 2, target);

                // Check congruence of squares
                BigInteger factor = gcd(x - y, target);
                if ((factor != 1U) && (factor != target)) {
                    return factor;
                }

                // Try x + y as well
                factor = gcd(x + y, target);
                if ((factor != 1U) && (factor != target)) {
                    return factor;
                }
            }
        }

        // These numbers have been tried already:
        std::sort(toStrike.begin(), toStrike.end());
        for (size_t i = 0U; i < toStrike.size(); ++i) {
            const size_t s = toStrike[i];
            auto it = smoothNumberMap->begin();
            std::advance(it, s - i);
            smoothNumberMap->erase(it);
        }

        return 1U; // No factor found
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //                                  WRITTEN BY ELARA (GPT) ABOVE                                          //
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////
};

std::string find_a_factor(const std::string& toFactorStr, const bool& isConOfSqr, const size_t& nodeCount, const size_t& nodeId, size_t wheelFactorizationLevel)
{
    // (At least) level 11 wheel factorization is baked into basic functions.
    if (wheelFactorizationLevel < 11U) {
        wheelFactorizationLevel = 11U;
        std::cout << "Warning: wheel_factorization_level has defaulted to minimum of 11.";
    }

    // Convert from string.
    BigInteger toFactor(toFactorStr);

    // The largest possible discrete factor of "toFactor" is its square root (as with any integer).
    const BigInteger fullMaxBase = sqrt(toFactor);
    if (fullMaxBase * fullMaxBase == toFactor) {
        return boost::lexical_cast<std::string>(fullMaxBase);
    }

    // We only need to try trial division about as high as would be necessary for 4096 bits of semiprime.
    const BigInteger primeCeiling = (65536ULL < fullMaxBase) ? (BigInteger)65536ULL : fullMaxBase;
    BigInteger result = 1U;
    // This uses very little memory and time, to find primes.
    std::vector<BigInteger> primes = SegmentedSieveOfEratosthenes(primeCeiling);
    // "it" is the end-of-list iterator for a list up-to-and-including wheelFactorizationLevel.
    const auto it = std::upper_bound(primes.begin(), primes.end(), wheelFactorizationLevel);

    // This is simply trial division up to the ceiling.
    for (uint64_t primeIndex = 0U; (primeIndex < primes.size()) || (result != 1U); primeIndex+=64) {
        dispatch.dispatch([&toFactor, &primes, &result, primeIndex]() {
            const uint64_t maxLcv = std::min(primeIndex + 32U, primes.size());
            for (uint64_t pi = primeIndex; pi < maxLcv; ++pi) {
                if (result != 1U) {
                    return false;
                }
                const BigInteger currentPrime = primes[primeIndex];
                if (!(toFactor % currentPrime)) {
                    result = currentPrime;
                    return true;
                }
            }
            return false;
        });
    }
    // If we've checked all primes below the square root of toFactor, then it's prime.
    if ((result != 1U) || (toFactor <= (primeCeiling * primeCeiling))) {
        return boost::lexical_cast<std::string>(result);
    }

    // Set up wheel factorization (or "gear" factorization)
    std::vector<BigInteger> wheelFactorizationPrimes(primes.begin(), it);
    // Primes are only present in range above wheel factorization level
    primes = std::vector<BigInteger>(it, it + log2(toFactor));
    // From 1, this is a period for wheel factorization
    size_t biggestWheel = 1ULL;
    for (const BigInteger& wp : wheelFactorizationPrimes) {
        biggestWheel *= (size_t)wp;
    }
    // These are "gears," for wheel factorization (with a "wheel" already in place up to 11).
    std::vector<boost::dynamic_bitset<uint64_t>> inc_seqs = wheel_gen(std::vector<BigInteger>(wheelFactorizationPrimes.begin(), wheelFactorizationPrimes.end()), toFactor);
    // We're done with the lowest primes.
    wheelFactorizationPrimes.clear();
    // Skip multiples removed by wheel factorization.
    inc_seqs.erase(inc_seqs.begin(), inc_seqs.begin() + MIN_RTD_LEVEL);

    // Ratio of biggest vs. smallest wheel, for periodicity
    const size_t wheelRatio = biggestWheel / SMALLEST_WHEEL;
    // Range per parallel node
    const BigInteger nodeRange = (((backward(fullMaxBase) + nodeCount - 1U) / nodeCount) + wheelRatio - 1U) / wheelRatio;
    // Same collection across all threads
    std::map<BigInteger, boost::dynamic_bitset<uint64_t>> smoothNumberMap;
    // This manages the work per thread
    Factorizer worker(toFactor * toFactor, toFactor, fullMaxBase, nodeRange, nodeId, wheelRatio, primes, 1ULL << 14U);

    const auto workerFn = [&toFactor, &inc_seqs, &isConOfSqr, &worker, &smoothNumberMap] {
        // inc_seq needs to be independent per thread.
        std::vector<boost::dynamic_bitset<uint64_t>> inc_seqs_clone;
        inc_seqs_clone.reserve(inc_seqs.size());
        for (const auto& b : inc_seqs) {
            inc_seqs_clone.emplace_back(b);
        }

        // "Brute force" includes extensive wheel multiplication and can be faster.
        if (!isConOfSqr) {
            return worker.bruteForce(&inc_seqs_clone);
        }

        // Different collection per thread;
        std::vector<BigInteger> semiSmoothParts;

        // While brute-forcing, use the "exhaust" to feed "smooth" number generation and check conguence of squares.
        return worker.smoothCongruences(&inc_seqs_clone, &semiSmoothParts, &smoothNumberMap);
    };

    const unsigned cpuCount = std::thread::hardware_concurrency();
    std::vector<std::future<BigInteger>> futures;
    futures.reserve(cpuCount);

    for (unsigned cpu = 0U; cpu < cpuCount; ++cpu) {
        futures.push_back(std::async(std::launch::async, workerFn));
    }

    for (unsigned cpu = 0U; cpu < cpuCount; ++cpu) {
        const BigInteger r = futures[cpu].get();
        if ((r > result) && (r != toFactor)) {
            result = r;
        }
    }

    return boost::lexical_cast<std::string>(result);
}
} // namespace Qimcifa

using namespace Qimcifa;

PYBIND11_MODULE(_find_a_factor, m) {
    m.doc() = "pybind11 plugin to find any factor of input";
    m.def("_find_a_factor", &find_a_factor, "Finds any nontrivial factor of input (or returns 1 if prime)");
}