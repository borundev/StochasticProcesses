import numpy as np

def mask_data(data,*args):
    mask_and=np.array(args).all(0)
    return data[mask_and]

class Paths(object):
    
    def __init__(self,T,npaths):
        self.T=T
        self.npaths=npaths
    
    def __setup__(self):
        self.time=np.linspace(0,self.T,self.nsteps)
        self.paths=np.zeros(shape=(self.npaths,self.nsteps))    
    
    def get_paths(self):
        return self.paths
    
    def get_timeline(self):
        return self.time
    
    def __getitem__(self,index):
        return self.paths[index]
    
    def get_step(self,k):
        return self.paths[:,k]
    
class BinaryPaths(Paths):
    
    # The BinaryPath takes the total time and the time after which the increment is to be made
    def __init__(self,T,dt,npaths,p=.5):
        super(BinaryPaths,self).__init__(T,npaths)
        self.p=p
        
        self.dt=dt
        self.nsteps=int(self.T/self.dt)
        Paths.__setup__(self)
        
        self.randoms=2*(np.random.binomial(1,self.p,self.npaths*(self.nsteps-1))-.5)
        self.randoms.shape=[self.npaths,self.nsteps-1]
        
        for i in range(self.nsteps-1):
            self.paths[:,i+1]=self.paths[:,i]+self.randoms[:,i]
    
class WeinerPaths(Paths):
    
    
    def __init__(self,T,nsteps,npaths,mu=0,sigma=1,seed=False):
        super(WeinerPaths,self).__init__(T,npaths)
        
        self.nsteps=nsteps
        self.dt=1.0*self.T/self.nsteps
        Paths.__setup__(self)
        
        self.mu=mu
        self.sigma=sigma
        
        self.dW=np.sqrt(self.dt)

        if type(seed) != bool:
            np.random.seed(seed)
        self.randoms=np.random.normal(0,1,npaths*(nsteps-1))
        self.randoms.shape=[npaths,nsteps-1]

      

        for i in range(nsteps-1):
            self.paths[:,i+1]=self.paths[:,i]+self.mu*self.dt+self.sigma*self.dW*self.randoms[:,i]
        

class GeometricWeinerPaths(Paths):
    
    
    def __init__(self,T,nsteps,npaths,S0=1,mu=0,sigma=1,seed=False):
        super(GeometricWeinerPaths,self).__init__(T,npaths)
        
        self.nsteps=nsteps
        self.dt=1.0*self.T/self.nsteps
        Paths.__setup__(self)
        
        self.mu=mu
        self.sigma=sigma
        
        self.dW=np.sqrt(self.dt)
        if type(seed) != bool:
            np.random.seed(seed)
        self.randoms=np.random.normal(0,1,npaths*(nsteps-1))
        self.randoms.shape=[npaths,nsteps-1]

            
        self.paths[:,0]=S0
        

        for i in range(nsteps-1):
            self.paths[:,i+1]=self.paths[:,i]*(1+self.mu*self.dt+self.sigma*self.dW*self.randoms[:,i])

class LevyWeinerPaths(Paths):
    def __init__(self,xi,xf,T,nsteps,npaths,mu=0,sigma=1,seed=False):
        super(LevyWeinerPaths,self).__init__(T,npaths)
        
        self.nsteps=nsteps
        self.dt=1.0*self.T/self.nsteps
        Paths.__setup__(self)
        
        self.mu=mu
        self.sigma=sigma
        
        self.dW=np.sqrt(self.dt)

        
        self.paths[:,0]=xi
        self.paths[:,-1]=xf
    
        if type(seed) != bool:
            np.random.seed(seed)
        self.randoms=np.random.normal(0,1,npaths*(nsteps-1))
        self.randoms.shape=[npaths,nsteps-1]

        

        for k in range(1,self.nsteps-1):
            delta_t=1   # because we are always realizing the step right after the previous one in this method
            delta_tp=(self.nsteps-k) # the number of steps remaining to the end
            mu=(delta_tp*self.paths[:,k-1]+delta_t*self.paths[:,-1])/(delta_t+delta_tp)
            Sigma=sigma*(delta_t**(-1) + delta_tp**(-1))**(-1/2.0)
            self.paths[:,k]=mu+ Sigma*self.dW*self.randoms[:,k]
    
    

