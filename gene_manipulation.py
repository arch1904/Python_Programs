# Gene Manipulation
#
# It's year 2050, and we have gotten advanced technology to manipulate genes at will.
# We consider a good gene to be when the "ATCG"s are balanced. That is for a gene length n,
# there are n/4 A's, T's, C's, and G's. Our technology allows us to "flash" the genes,
# replacing a subsequence of a gene with anything we want.
#
# Given a arbiturary gene, find the length of the minimum subsequence of the gene we need to flash
# to get a good gene.
#
#
# Restrictions
# ------------
# Inputs are only given as a string containing uppercase A, T, C, and Gs.
# The input size is always a multiple of 4 (or else we will never get a good gene)
# The genes can appear in any order.
#
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "ATCGGATT"
#   We can remove the last T and change it to a C in order to make it a good gene.
#   Output:
#   1
#
# Example 2:
#   Input: "ATCGAAAAATCG"
#   We can remove the "AAA" and change it to a "CTG" in order to make it a good gene.
#   Output:
#   3
#
# Parameters
# ----------
# gene: str
#   The gene that we must find the subsequence to switch it out for
#
# Returns
# -------
# int
#    The length of the minimum subsequence in order to make the gene a good gene.
def smallest_substr(str1, str2):
    from collections import defaultdict
    '''
    for each starting index, finds the least ending index such that the substring contains all of the necessary letters.
    '''
    check_occurence = defaultdict(int)
    neg = 0  # number of negative entries in check_occurence
    for c in str2: #iterate char by char in str_to_check
        if check_occurence[c] == 0: 
            neg += 1
        check_occurence[c] -= 1
    minlen = len(str1) + 1
    j = 0
    for i in xrange(len(str1)):
        while neg > 0:
            if j >= len(str1):
                return minlen
            check_occurence[str1[j]] += 1
            if check_occurence[str1[j]] == 0:
                neg -= 1 #decrease negative occurence as count for that char has reached 0
            j += 1
        minlen = min(minlen, j - i) #get smaller of the two and assign to minlen
        if check_occurence[str1[i]] == 0: 
            neg += 1 
        check_occurence[str1[i]] -= 1
    return minlen

def gene_manipulation(gene):
    '''
    returns the length of the minimum subsequence in order to make the gene a good gene
    '''
    count_genomes={'A':0,'T':0,'C':0,'G':0} #new dict with initialised with ATCG as keys and their occurences which is currently 0
    count_changes=0
    to_be_found={}
    for c in gene:
        if c not in count_genomes or len(gene)%4!=0: #Invalid Gene
            return None
        count_genomes[c]+=1 #Count Occurences Of Each Genome
    ideal_count=len(gene)/4 #ideal occurence of each genome
    str_to_check=""
    for c in count_genomes:
        if count_genomes[c]>ideal_count: #if the char occurs more times than ideal
            while count_genomes[c]>ideal_count:
                str_to_check+=c #create str of all chars to be replaced
                count_genomes[c]-=1 #decrease the occurence of the char which is to be replaced
    return smallest_substr(gene,str_to_check) #find and return min length of subsequence to be removed