## 왜 성능을 생각해야 하는가?

### CPU 관점
1. CPU의 IPC(Instruction Per Cycle)과 Clock의 증가
2. IPC의 성능이 좋아질수록, Vectorized level이 증가 -> Flynn SIMD(Simple Instruction Multiple Data stream)
3. Multithreading
4. Hyperthreading: 가상의 CPU를 인식시켜서 단일 CPU에 두 스레드를 번갈아 실행하는 기법 (by Intel)
5. Out-of-order execution
6. Multi-core Architecture

> Amdahl's Law
>  $$S_{latency}(s) = \frac{1}{(1-p)+ \frac{p}{s}}$$
>  - $S_{latency}$ = theoretical speed-up of the execution of the whole task
>  - $s$ = speed-up of the part of the task that benefits from imporved system resources
>  - $p$ = the propotion of execution time that the part benefiting from improved resources originally occupied   
>    $$S_{latency}(s) \leq \frac{1}{1-p}$$   
>    $$\displaystyle\lim_{s \rarr \infin} S_{latency}(s) = \frac{1}{1-p}$$  
>    $p$(전체에서 병렬 가능 부분)와 $s$(병렬화 개수)에 따라 성능 향상 최댓값이 병목으로 작용
>
> Example:
>  1. 100명을 대상으로 각 1분이 소요되는 설문조사 시행 -> 100분 소요
>  2. 조사원 1명의 경우: $p = \frac{1}{100} = 0.01, s = 1$  
> $S_{latency}(s) = \frac{1}{(1-p)+ \frac{p}{s}} = \frac{1}{(1-0.01)+ \frac{0.01}{1}} = \frac{1}{0.99+ {0.01}} = 1$ -> 기준
>  3. 조사원 2명의 경우: $p = \frac{50}{100} = 0.5, s = 2$  
> $S_{latency}(s) = \frac{1}{(1-p)+ \frac{p}{s}} = \frac{1}{(1-0.5)+ \frac{0.5}{2}} = \frac{1}{0.5+ {0.25}} = 1.3333...$ -> 1.3배 증가 (약 50분 소요)
>  4. 조사원 100명의 경우: $p = \frac{100}{100} = 1, s = 100$  
> $S_{latency}(s) = \frac{1}{(1-p)+ \frac{p}{s}} = \frac{1}{(1-1)+ \frac{1}{100}} = \frac{1}{0+ {0.01}} = 100$ -> 100배 증가 (1분이면 끝냄!)
>  5. 조사원 200명의 경우:  $p = \frac{200}{100} = 2, s = 200$  
> $S_{latency}(s) = \frac{1}{(1-p)+ \frac{p}{s}} = \frac{1}{(1-2)+ \frac{1}{200}} = \frac{1}{-1 + {0.005}} = \frac{1}{-0.995}$ -> 의미가 없음!  
> 설문조사 소요시간을 줄이는 수 밖에 없음!
>
> 
> Reference:
> 1. Bryant, Randal E.; David, O'Hallaron (2016), Computer Systems: A Programmer's Perspective (3 ed.), Pearson Education, p. 58, ISBN 978-1-488-67207-1
> 2. https://www3.cs.stonybrook.edu/~rezaul/Spring-2012/CSE613/reading/Amdahl-1967.pdf

#### 해결책
- GIL(Global Interpreter Lock): 코어가 몇 개든, 한 번에 명령 하나만 실행하도록 강제
- Amdahl's Law에서 조사원 100명이 있어도 한 번에 한 사람만 설문 조사가 가능하다는 말
- 다수의 코어를 사용하는 것이 골치 아픔
- 대안으로, multiprocessing module, numpy, numexpr, CPython, Clustering 등을 사용해야 함

### Memory 관점
1. Random access, Sequence access
2. Latency (HDD < SSD < RAM < Cache)

#### 해결책
- Asynchronus I/O
- Non-preemptive cache

### Bus 관점
1. CPU's Front-Side Bus(FSB), Ultra Path Interconnect(UPI)
2. Bus width, frequency

#### 해결책
- Interface

