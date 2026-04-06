import math


#UNIT 5 -> MOMENTUM
#MOMENTUM: p = m*dv (mass times velocity)
#MOMENTUM: m*v = f*t (force times time)
def momentum_solve(    m=None,dv=None,     f=None,dt=None,     solve="p")->float:
    
    #solving for the momentum if at least 2 needed values are solved
    if solve == "p" and f is not None and dt is not None:
        return f*dt
    elif solve == "p" and m is not None and dv is not None:
        return m*dv

    
    #solving for the other values, checking for what is instructed to be solved and plugging in
    
    elif solve == "m" and dv is not None and f is not None and dt is not None:
        return f*dt/dv
    
    elif solve == "dv" and t is not None and f is not None and dt is not None:
        return f*dt/m
    
    elif solve == "f" and m is not None and dv is not None and dt is not None:
        return m*dv/dt

    elif solve == "dt" and m is not None and dv is not None and f is not None:
        return m*dv/f

    else:
        return 0


#main loop
