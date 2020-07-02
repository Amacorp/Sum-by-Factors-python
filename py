
def sum_for_list(lst):
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]


or


from collections import defaultdict
def sum_for_list(lst):

    def factors(x):
        p_facs = []
        i = 2
        while x > 1 or x < -1:
            if x % i == 0:
                p_facs.append(i)
                x //= i
            else:
                i += 1
        return list(set(p_facs))
    
    fac_dict = defaultdict(int)
    
    for i in lst:
        for fac in factors(i):
            fac_dict[fac] += i
            
    return sorted([[k,v] for k,v in fac_dict.items()])


or

def prime_factors(n):
    i = 2
    factors = []
    if n < 0:
        n *= -1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def combine(arr1, arr2):
    for a in arr1:
        if not a in arr2:
            arr2.append(a)
    return arr2

def sum_for_list(lst):
    #....
    factors = []
    sums = []
    for i in range(len(lst)):
        combine(prime_factors(lst[i]),factors)
    for i in range(len(factors)):
        msum = 0
        for j in range(len(lst)):
            if not lst[j]%factors[i]:
                msum += lst[j]
        sums.append([factors[i], msum])
    sums.sort(key=lambda factors:factors[0])
    return sums 
