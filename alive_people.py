# Alive People
#
# Write a function that, given a list of strings representing a person's birth year: age of death,
# will return the year that had the most people alive (inclusive). If there are multiple years that tie, return the earliest.
# You can think of a birthdate and a deathdate as a range of years. Of all the birth years in the list, find the one where the highest
# amount of people in the list were still alive.
#
# Examples
# ----------
# Example 1:
#   Input: ["1920: 80", "1940: 22", "1961: 10"]
#   Output: 1961
#
# Example 2:
#   Input: ["2000: 46", "1990: 17", "1200: 97", "1995: 20"]
#   Output: 2000
#
# Parameters
# ----------
# people : List[string]
#   A list of strings each representing a birth year and final age
#
#
# Returns
# -------
# int
#   Returns earliest year with the most people alive
#
def alive_people(people):
    '''
    returns earliest year with the most people alive
    '''
    result_dict={} #Empty Dictionary To Hold Years with no of people alive in the year
    for p in people: #iterate through dictionary
        start_year=int(p[0:p.index(':')]) #year person was born
        end_year=start_year+int(p[p.index(':')+1:]) #year person died
        for i in xrange(start_year,end_year+1):
            if i in result_dict: #If Someone else was alive during this year update count of that year
                result_dict[i]+=1
            else:
                result_dict[i]=1 #if no one else was alive during this year then initalise this year to 1
    max_people_alive=max(result_dict.values())
    min_year=5000000 #Extremely hight value which will be replaced ASAP
    for r in result_dict:
        if result_dict[r]==max_people_alive:
            if r<min_year: #find min year with max people alive
                min_year=r 
        else:
            continue
    return min_year