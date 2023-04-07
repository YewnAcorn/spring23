'''
computing averages and 1-armed bandit

3 ways to compute averages
The third method uses temporal difference
see Sutton and Barto
Q = Q + a*(R - Q), where in this case Q is the average
and R is the new value to be averaged

also use rand.gauss(0, 1) instead of i

continued on thrusday: working
in class in breakout rooms with
briana, damian, andrew, davis,
duc, jadyn
pretty confused, I thought I
had an idea what these things
were, but the people in
the group have other ideas and
now I don't know.

talked to richard in office hours
and got a better idea of alpha that
was confusing me. I thought it was
a constant but for this it changes
with each step and adds the division
for the average in a way like in average2()

took me a while to figure out the last part
of the equation, where its subtracting the 
previous average. I kept trying to do it as
the previous element. I think this works well now
it computed the non-gaussian average as 499.5
as opposed to 500 like the other 2. I don't know
why it was 

'''

import random as rand

N = 1000

def average1():
    sum = 0
    for i in range(1, N):
        sum += i
    avg = sum / (N-1)
    print('avg1', avg)

def average2():
    avg = 0
    for i in range(1, N):
        avg = avg * (i-1)/i + i/i
    print('avg2', avg)

def average3():
    avg = 0
    data = []
    for i in range(N):
        # Q = Q + a*(R - Q)
        # where Q is the avg and R is the new value to be averaged
        # or as the book says
        # V(s) <- V(s) + a * ( V(s') - V(s) )
        alpha = 1/(1+i)
        data.append(rand.gauss(0, 1))
        avg += (alpha * (data[i] - avg))


    print('avg3', avg)


if __name__ == '__main__':
    average1()
    average2()
    average3()

