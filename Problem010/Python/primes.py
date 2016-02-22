def prime_gen(n):
    for i in xrange(2, n):
        prime = True
        if i % 2 == 0 and i != 2:
            continue
        sqrtp = int(i ** 1 / 2)
        for j in xrange(2, sqrtp):
            if j % 2 == 0:
                continue
            if i % j == 0:
                prime = False
                break
        if prime:
            yield i


def prime_gen_eff(n):
    pp = 2
    yield pp
    pp += 1
    tp = [pp]
    ss = [2]
    while pp < n:
        pp += ss[0]
        test = True
        sqrtpp = pp ** 1/2
        for a in tp:
            if a > sqrtpp:
                break
            if pp % a == 0:
                test= False
                break
        if test:
            tp.append(pp)
            yield pp
def primes_list(lim):
    from math import sqrt
    """ Get an upper limit from the user to determine the generator's termination point. """
    sqrtlim=sqrt(float(lim))
    """ Get the square root of the upper limit. This will be the upper limit of the test prime array 
    for primes used to verify the primacy of any potential primes up to (lim). Primes greater than 
    (sqrtlim) will be placed in an array for extended primes, (xp), not needed for the verification 
    test. The use of an extended primes array is technically unnecessary, but helps to clarify that we 
    have minimized the size of the test prime array. """
    pp=2
    """ Initialize the variable for the potential prime, setting it to begin with the first prime 
    number, (2). """
    ss=[pp]
    """ Initialize the array for the skip set, setting it at a single member, being (pp=2). Although 
    the value of the quantity of members in the skip set is never needed in the program, it may be 
    useful to understand that future skip sets will contain more than one member, the quantity of which 
    can be calculated, and is the quantity of members of the previous skip set multiplied by one less 
    than the value of the prime which the new skip set will exclude multiples of. Example - the skip 
    set which eliminates multiples of primes up through 3 will have (3-1)*1=2 members, since the 
    previous skip set had 1 member. The skip set which eliminates multiples of primes up through 5 will 
    have (5-1)*2=8 members, since the previous skip set had 2 members, etc. """
    ep=[pp]
    """ Initialize the array for primes which the skip set eliminate multiples of, setting the first 
    member as (pp=2) since the first skip set will eliminate multiples of 2 as potential primes. """
    pp+=1
    """ Advance to the first potential prime, which is 3. """
    rss=[ss[0]]
    """ Initialize an array for the ranges of each skip set, setting the first member to be the range 
    of the first skip set, which is (ss[0]=2). Future skip sets will have ranges which can be 
    calculated, and are the sum of the members of the skip set. Another method of calculating the range 
    will also be shown below. """
    tp=[pp]
    """ Initialize an array for primes which are needed to verify potential primes against, setting the 
    first member as (pp=3), since we do not yet have a skip set that excludes multiples of 3. Also note 
    that 3 is a verified prime, without testing, since there are no primes less than the square root of 
    3. """
    i=0
    """ Initialize a variable for keeping track of which skip set range is current. """
    rss.append(rss[i]*tp[0])
    """ Add a member to the array of skip set ranges, the value being the value of the previous skip 
    set range, (rss[0]=2), multiplied by the value of the largest prime which the new skip set will 
    exclude multiples of, (tp[0]=3), so 2*3=6. This value is needed to define when to begin 
    constructing the next skip set. """
    xp=[]
    """ Initialize an array for extended primes which are larger than the square root of the user 
    defined limit (lim) and not needed to verify potential primes against, leaving it empty for now. 
    Again, the use of an extended primes array is technically unnecessary, but helps to clarify that we 
    have minimized the size of the test prime array. """
    pp+=ss[0]
    """ Advance to the next potential prime, which is the previous potential prime, (pp=3), plus the 
    value of the next member of the skip set, which has only one member at this time and whose value is 
    (ss[0]=2), so 3+2=5. """
    npp=pp
    """ Initialize a variable for the next potential prime, setting its value as (pp=5). """
    tp.append(npp)
    """ Add a member to the array of test primes, the member being the most recently identified prime, 
    (npp=5). Note that 5 is a verified prime without testing, since there are no TEST primes less than 
    the square root of 5. """
    while npp<int(lim):
        """ Loop until the user defined upper limit is reached. """
        i+=1
        """ Increment the skip set range identifier. """
        while npp<rss[i]+1:
            """ Loop until the next skip set range is surpassed, since data through that range is
            needed before constructing the next skip set. """
            for n in ss:
                """ Loop through the current skip set array, assigning the variable (n) the value 
                of the next member of the skip set. """
                npp=pp+n
                """ Assign the next potential prime the value of the potential prime plus 
                the value of the current member of the skip set. """
                if npp>int(lim): break
                """ If the next potential prime is greater than the user defined limit, 
                then end the 'for n' loop. """
                if npp<=rss[i]+1: pp=npp
                """ If the next potential prime is still within the range of the next skip 
                set, then assign the potential prime variable the value of the next 
                potential prime. Otherwise, the potential prime variable is not changed 
                and the current value remains the starting point for constructing the next 
                skip set. """
                sqrtnpp=sqrt(npp)
                """ Get the square root of the next potential prime, which will be the 
                limit for the verification process. """
                test=True
                """ Set the verification flag to True. """
                for q in tp:
                    """ Loop through the array of the primes necessary for verification of the 
                    next potential prime. """
                    if sqrtnpp<q: break

                    elif npp % q == 0:
                        """ If the test prime IS a factor of the next potential prime. """
                        test=False
                        """ Then set the verification flag to False since the next 
                        potential prime is not a prime number. """
                        break
                        """ And end testing through the 'for q' loop. """
                    """ Otherwise, continue testing through the 'for q' loop. """
                if test:
                    """ If the next potential prime has been verified as a prime number. """
                    if npp<=sqrtlim: tp.append(npp)
                    else: xp.append(npp)
                    """ Otherwise, add it to the array of primes not needed to verify 
                    potential primes against. """
                """ Then continue through the 'for n' loop. """
            if npp>int(lim): break
            """ If the next potential prime is greater than the user defined limit, then end 
            the 'while npp<rss[i]+1' loop. """
            """ Otherwise, continue the 'while npp<rss[i]+1' loop. """
        if npp>int(lim): break
        """ If the next potential prime is greater than the user defined limit, then end the 'while 
        npp<int(lim)' loop. """
        """ At this point, the range of the next skip set has been reached, so we may begin
        constructing a new skip set which will exclude multiples of primes up through the value of 
        the first member of the test prime set, (tp[0]), from being selected as potential 
        primes. """
        lrpp=pp
        """ Initialize a variable for the last relevant potential prime and set its value to the 
        value of the potential prime. """
        nss=[]
        """ Initialize an array for the next skip set, leaving it empty for now. """
        while pp<(rss[i]+1)*2-1:
            """ Loop until the construction of the new skip set has gone through the range of the new 
            skip set. """
            for n in ss:
                """ Loop through the current skip set array. """
                npp=pp+n
                """ Assign the next potential prime the value of the potential prime plus 
                the value of the current member of the skip set. """
                if npp>int(lim): break
                """ If the next potential prime is greater than the user defined limit, 
                then end the 'for n' loop. """
                sqrtnpp=sqrt(npp)
                """ Get the square root of the next potential prime, which will be the 
                limit for the verification process. """
                test=True
                """ Set the verification flag to True. """
                for q in tp:
                    """ Loop through the array of the primes necessary for verification of the 
                    next potential prime. """
                    """ If the test prime is greater than the square root of the next 
                    potential prime, then end testing through the 'for q' loop. """
                    if sqrtnpp<q: break
                    elif npp%q==0:
                        """ If the test prime IS a factor of the next potential prime. """
                        test=False
                        """ Then set the verification flag to False since the next 
                        potential prime is not a prime number. """
                        break
                        """ And end testing through the 'for q' loop. """
                        """ Otherwise, continue testing through the 'for q' loop. """
                if test:
                    """ If the next potential prime has been verified as a prime number. """
                    if npp<=sqrtlim: tp.append(npp)
                    else: xp.append(npp)
                    """ And if the next potential prime is less than or equal to the 
                    square root of the user defined limit, then add it to the array of 
                    primes which potential primes must be tested against. """
                    
                    """ Otherwise, add it to the array of primes not needed to verify 
                    potential primes against. """
                if npp%tp[0]!=0:
                    """ If the next potential prime was NOT factorable by the first member of 
                    the test array, then it is relevant to the construction of the new skip set 
                    and a member must be included in the new skip set for a potential prime to 
                    be selected. Note that this is the case regardless of whether the next 
                    potential prime was verified as a prime, or not. """
                    nss.append(npp-lrpp)
                    """ Add a member to the next skip set, the value of which is the 
                    difference between the last relevant potential prime and the next 
                    potential prime. """
                    lrpp=npp
                    """ Assign the variable for the last relevant potential prime the 
                    value of the next potential prime. """
                pp=npp
                """ Assign the variable for the potential prime the value of the next 
                potential prime. """
                """ Then continue through the 'for n' loop. """
            if npp>int(lim): break
            """ If the next potential prime is greater than the user defined limit, then end 
            the 'while npp<(rss[i]+1)*2-1' loop. """
            """ Otherwise, continue the 'while npp<(rss[i]+1)*2-1' loop. """
        if npp>int(lim): break
        """ If the next potential prime is greater than the user defined limit, then end the 'while 
        npp<int(lim)' loop. """
        ss=nss
        """ Assign the skip set array the value of the new skip set array. """
        ep.append(tp[0])
        """ Add a new member to the excluded primes array, since the newly constructed skip set 
        will exclude all multiples of primes through the first member of the test prime array. """
        del tp[0]
        """ Delete the first member from the test prime array since future potential primes will 
        not have to be tested against this prime. """
        rss.append(rss[i]*tp[0])
        """ Add a member to the skip set range array with the value of the range of the next skip 
        set. """
        npp=lrpp
        """ Assign the next potential prime the value of the last relevant potential prime. """
        """ Then continue through the 'while npp<int(lim)' loop. """
    """ At this point the user defined upper limit has been reached and the generator has completed 
    finding all of the prime numbers up to the user defined limit. """
    ep.reverse()
    """ Flip the array of excluded primes. """
    [tp.insert(0,a) for a in ep]
    """ Add each member of the flipped array into the beginning of the test primes array. """
    tp.reverse()
    """ Flip the array of test primes. """
    [xp.insert(0,a) for a in tp]
    """ Add each member of the flipped array into the beginning of the extended primes array. """
    return xp
    """ Send the completed array of all primes up to the user defined limit back to the function call. """

def sieve5(n):
    """Return a list of the primes below n."""
    """from http://codereview.stackexchange.com/questions/42420/sieve-of-eratosthenes-python"""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1    # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n - p*p - 1) // (2*p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result