from __future__ import division
def prob(k, m, n):
    t = k+m+n #total numer
    prob = 0
    #case AA * AA
    prob += k/t * 1
    
    #case AA*Aa
    prob += m/t * k/(t-1) 
    
    #case AA * Aa
    prob += (m-1)/(t-1) * m/t * 0.75
    
    #case Aa*aa
    prob += n/(t-1) * m/t * 0.5
    
    #case aa * AA
    prob +=n/t * k /(t-1)
    
    #case aa * Aa
    prob += n/t * m/(t-1) *0.5
    
    return prob
    