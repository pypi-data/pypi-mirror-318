from collections.abc import Callable, Iterable
from threading import Thread
from typing import Optional
from random import randint


class _FunctionCall() :
    def __init__(self, Function : Callable, *Arguments, **Kwarguments) -> None :
        self.__Function : dict = {
            'Function' : Function,
            'Arguments' : Arguments,
            'Kwarguments' : Kwarguments
        }
    
    @property
    def Function(self) -> Callable :
        return self.__Function['Function']
    
    @property
    def Arguments(self) -> list :
        return list(self.__Function['Arguments'])
    
    @property
    def Kwarguments(self) -> dict :
        return dict(self.__Function['Kwarguments'])

def _MakeThreadName(Function, Name) -> str :
    if Name is not None and not isinstance(Name, str) :
        raise TypeError('The name for the thread must be a string.')
    
    return f'Thread-{Function.__name__}-{randint(0, 999)}'

class ThreadGroup() :
    def __init__(self) -> None :
        """
        Initializes a new instance of the ThreadGroup class.

        This constructor initializes an empty list to store MThread instances 
        that will be managed by this thread group.
        """

        self.__Threads : list[MThread] = []
    
    def Add(self, Thread : MThread) -> None :
        self.__Threads.append(Thread)
    
    def StartAll(self) -> None :
        for Thread in self.__Threads :
            Thread.Start()
    
    def JoinAll(self) -> None :
        for Thread in self.__Threads :
            Thread.Join()
    
    def Outputs(self) -> list[object] :
        ThreadOutputs = []
        
        for ThisThread in self.__Threads :
            try :
                ThreadOutputs.append(ThisThread.Output)
            except RuntimeError :
                ThreadOutputs.append(None)
        
        return ThreadOutputs

class MThread() :
    def __init__(self,
        Function : Callable,
        Arguments : Optional[Iterable] = None,
        Kwarguments : Optional[dict] = None,
        ThreadName : Optional[str] = None,
        ThreadGroup : ThreadGroup = None,
        Daemon : bool = False,
        UncaughtExceptionHandler : bool = False,
        AutoStart : bool = False
    ) -> None :
        """
        Initializes a new MThread instance.

        Parameters:
            Function (Callable): The function that the thread will run.
            Arguments (Optional[Iterable]): The arguments to pass to the function.
            Kwarguments (Optional[dict]): The keyword arguments to pass to the function.
            ThreadName (Optional[str]): The name for the thread.
            ThreadGroup (ThreadGroup): The thread group to add the thread to.
            Daemon (bool): Whether the thread should run as a daemon.
            UncaughtExceptionHandler (bool): Whether the thread should catch and store any unhandled exceptions.
            AutoStart (bool): Whether the thread should start automatically.

        Returns:
            None
        """

        if Arguments is None :
            Arguments = ()
        
        if Kwarguments is None :
            Kwarguments = {}
        
        self.__Function = _FunctionCall(
            Function,
            *Arguments,
            **Kwarguments
        )
        
        self.__HandleExceptions = UncaughtExceptionHandler
        
        self.__InternalThread = Thread(
            target=self._Run,
            name=_MakeThreadName(Function, ThreadName),
            daemon=Daemon,
        )
        
        if ThreadGroup is not None :
            ThreadGroup.Add(self)
        
        if AutoStart :
            self.Start()
    
    def Start(self) -> None :
        self.__InternalThread.start()
    
    def __Run(self) -> None :
        self.__Running = True
        try :
            Output = self.__Function.Function(
                *self.__Function.Arguments,
                **self.__Function.Kwarguments
            )
        except Exception as e :
            self.__Failed = True
            self.__Exception = e
            if not self.__HandleExceptions :
                raise
        else :
            self.__Failed = False
            self.__Output = Output
        finally :
            self.__Running = False
    
    @property
    def IsAlive(self) -> bool :
        if self.HasStarted :
            return self.__Running
        else :
            return False
    
    @property
    def HasStarted(self) -> bool :
        return hasattr(self, '__Running')
    
    @property
    def Failed(self) -> bool :
        if hasattr(self, '__Failed') :
            return self.__Failed
        
        return False
    
    @property
    def Exception(self) -> Optional[BaseException] :
        if not self.Failed :
            return None
        
        return self.__Exception
    
    @property
    def Output(self) -> object :
        if not self.HasStarted :
            raise RuntimeError('The thread has not started yet.')
        
        if self.IsAlive :
            raise RuntimeError('The thread is still running.')
        
        if self.Failed :
            return self.Exception
        
        return self.__Output
    
    def Join(self, Timeout : Optional[float] = None) -> None :
        if not self.HasStarted :
            raise RuntimeError('The thread has not started yet.')
        
        self.__InternalThread.join(Timeout)