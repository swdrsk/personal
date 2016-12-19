from brian2 import *

def sample():
    eqs = '''
    dv/dt  = (ge+gi-(v+49*mV))/(20*ms) : volt
    dge/dt = -ge/(5*ms)                : volt
    dgi/dt = -gi/(10*ms)               : volt
    '''
    P = NeuronGroup(4000, eqs, threshold='v>-50*mV', reset='v=-60*mV')
    P.v = -60*mV
    Pe = P[:3200]
    Pi = P[3200:]
    Ce = Synapses(Pe, P, on_pre='ge+=1.62*mV')
    Ce.connect(p=0.02)
    Ci = Synapses(Pi, P, on_pre='gi-=9*mV')
    Ci.connect(p=0.02)
    M = SpikeMonitor(P)
    run(1*second)
    plot(M.t/ms, M.i, '.')
    show()
    
def izhikevich_model():
    def draw_normals(n,start,stop):
        mu,sigma,numbers = start+(stop-start)/2, (stop-start)/6, zeros(n)
        for i in range(n):
            s = -1
            while (s<start) or (s>stop) :
                s = numpy.random.normal(mu,sigma,1)
                numbers[i]=s
        return numbers

    n = 2000 # number of neurons
    R = 0.8  # ratio about excitory-inhibitory neurons

    eqs = Equations(''' 
    dv/dt = (0.04/ms/mV)*v**2 + (5/ms) * v + 140*mV/ms - u + I_syn/ms + I_in/ms : volt
    du/dt = a*((b*v) - u) : volt/second
    dx/dt = -x/(1*ms) : 1
    I_in = ceil(x)*(x>(1/exp(1)))*amplitude : volt
    dI_syn/dt = - I_syn/tau : volt
    a : 1/second
    b : 1/second
    c : volt
    d : volt/second
    amplitude : volt
    tau : second
    ''')
    
    #reset specification of the Izhikevich model
    reset = '''
    v = c
    u += d
    '''
    
    #2nd: Define the Population of Neurons P
    P = NeuronGroup(n, model=eqs, threshold='v>30*mvolt', reset=reset, method='euler')
    
    #3rd: Define subgroups of the neurons (regular spiking/fast spiking)
    Pe = P[:int(n*R)]
    Pi = P[int(n*R):]

    #4th: initialize starting neuronal p"""!!!<<<nicht wie im Paper>>>!!!"""arameters for the simulation
    Pe.a = 0.02/msecond
    Pe.b = 0.2/msecond
    Pe.c = (15*draw_normals(int(n*R),float(0),1) - 65) * mvolt
    Pe.d = (-6*draw_normals(int(n*R),float(0),1) + 8) * mvolt/msecond
    Pe.tau = draw_normals(int(n*R),float(3),15) * msecond
    Pi.a = (0.08*draw_normals(n-int(n*R),float(0),1) + 0.02) * 1/msecond
    Pi.b = (-0.05*draw_normals(n-int(n*R),float(0),1) + 0.25) * 1/msecond
    Pi.c = -65 * mvolt
    Pi.d = 2 * mvolt/msecond
    Pi.tau = draw_normals(n-int(n*R),float(3),15) * msecond
    P.x = 0
    P.v = draw_normals(n,float(-50),float(-25)) * mvolt
    P.amplitude = draw_normals(n,0,8) * mvolt
    
    #5th: Connect synapses
    Ce = Synapses(Pe, P, on_pre='I_syn+=1.5*mV')
    Ce.connect(p=0.05)
    Ci = Synapses(Pi, P, on_pre='I_syn-=8*mV')
    Ci.connect(p=0.05)
    
    #6th: Run & monitor
    M = SpikeMonitor(P)
    V = StateMonitor(P,'v',record=True)
    run(500*ms)
    subplot(211)
    plot(M.t/ms, M.i, '.')
    subplot(212)
    plot(V.t[:200]/ms, V.v[0][:200]/mV, 'r')
    plot(V.t[:200]/ms, V.v[100][:200]/mV, 'g')
    plot(V.t[:200]/ms, V.v[200][:200]/mV, 'b')
    show()

    
if __name__=="__main__":
    izhikevich_model()