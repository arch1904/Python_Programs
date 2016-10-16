# Lazy Trainer
#
# Recently, there has been extensive research done on Pokomon's (don't sue us) training method.
# Turns out, we have made a rapid advancements in how Pokomon gain experience! We can now gain
# experience base on our Pokomon's current strength.
#
# Now the Pokomon we are training can either
# 1. Tackle -- This will defeat the enemy Pokomon and
#              increase our Experience by Current Strength * The Enemy's hitpoints.
# 2. Belly Drum -- This will increase our Pokomon's Strength by 1, and the battle ends
#    (I guess Pokomon are afraid of belly drums).
#
# But as a 8th Time Entrier in the Hall of Fame, we have become very very lazy.
#
# Given a sequence of Pokomons to fight (with corresponding Hit Points), return the maximum
# experience we can gain with our new battle method! (Correction: ) You can fight the Pokomon in any order.
# i.e. You can fight Pokomon #4 without fighting Pokomon #1.
#
# The Pokomon starts with Strength = 1 and Experience = 0. We are interested in training lots of
# Pokomon after all!
#
# Restriction(s)
# --------------
# All Enemy Pokomons will have positive hitpoints!
# You may not use recursion.
#
# Example(s)
# ----------
# Example 1:
#   Input 1: [3, 2, 2]
#   We should use Belly Drum on the second Pokomon to get Strength = 2.
#   Then we should use Tackle to defeat the the rest to get Experience = 10.
#   This is the maximum experience we can gain from the series of battles.
#
#   Output:
#   10
#
# Parameters
# ----------
# pokomon: list
#   The list/array given with the sequence of Pokomons we must fight.
#
# Returns
# -------
# int
#   The maximum experience a Pokomon can gain.
#
# Note
# ----
# This is a difficult question. Come to office hours *wink wink* for help!
def lazy_trainer(pokomon):
    arr=[]
    arr=sorted(pokomon)
    Max=0
    exp=0
    s=1
    for i in xrange(len(arr)-1,-1,-1):
        s=s+1*(i+1)
        exp+=arr[i]
        if exp*(i+1)>Max:
            Max=exp*(i+1)
        else:
            continue
    return Max