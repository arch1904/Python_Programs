# findRing
#
# You are a secret agent in the CIA tasked with finding a ring of Moles in the organization!
# Rumor has it that moles hang out at Red Lion (the bar). There's a whole row of agents seated at the bar.
# You start by talking to the agent seated on the left-most stool on the bar. However, the agent redirects you to another
# agent.  To your great annoyance, that agent redirects you to yet another agent!!
# And on and on it goes. Standard regulation requires each agent to have a tattoo on the back of his/her neck representing a unique integer and you
# decide to ID each agent by his/her number. Each agent redirects to a different agent, other than him/herself. Because of this,
# it is guaranteed that you will start going in loops talking to them.
# The moles are trying to trick you by creating an endless chain of references! Find the size of the ring and report
# back to headquarters.
# Write a function findRing(agents) which returns the number of agents which form a loop, given that you start by
# talking to the left-most agent, 0. numbers will be an array of non-negative integers such that number[m] is the
# number of the agent to whom agent m redirects. No agent redirects to himself. The left-most agent is number 0,
# the next is number 1, and so on. Each element in the numbers list will be in the range [0, n-1] where n is the length
# of the numbers list.
#
# Restriction(s)
# --------------
# The number of agents will be at least 2 and no more than 1000.
# You may not use recursion.
#
# Example(s)
# ----------
# Example 1:
# Suppose the numbers list were [1, 3, 0, 1]. Then agent 0 redirects to agent 1, who redirects to
# agent 3, who redirects back to agent 1. There is a loop of two agent: 1, 3. Thus the answer would be 2.
# Note that even though you started with agent 0, he is not part of the ring.
#
# Output: 2
#
# Parameters
# ----------
# agents: list
#   The list/array given with the sequence of agents in the bar.
#
# Returns
# -------
# int
#   The number of agents in the ring.
#
# Note
# ----
# This is a Google interview question. If you can solve this problem in under 30 minutes, you would have passed 1 of 2 rounds.
def findRing(agents):
    count=0
    i=0
    next1=0
    store=0
    agents1=list(agents)
    check=False
    while check==False:
        next1=agents1[i]
        if next1<0 and next1!=-1001:
            store=-next1
            check=True
        elif next1==-1001:
            store=agents.index(0)
            check=True
        else:
            if agents1[i]==0:
                agents1[i]=-1001
                i=next1
            else:
                agents1[i]=-agents1[i]
                i=next1
    i=store
    check=False
    while check==False:
        i=agents[i]
        count+=1
        #print i
        if i==store:
            check=True
        else:
            continue
    return count
