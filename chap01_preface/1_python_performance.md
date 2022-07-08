## 파이썬과 성능

### PVM (Python Virtual Machine)
- Python interpreter는 Computer's component 추상화 제공
- Profiling 필요

### Library
- Scikit-learn: LIBLINEAR, LIBSVM (written C), Scipy
- Numpy: BLAS, C, PORTRAN
- Scipy: C, PORTRAN
- Pandas: Scipy, Numpy
- Asyncio: Asynchronous I/P
- Pytorch, Tensorflow: GPU 사용
- ...

### 개발 방법
0. 코딩하기 전 계획 (Plan)
1. 폐기한다는 가정하에 일단 만들자 (Prototype)
2. 더 나은 구조 적용
    > Measure twice, cut once!
3. 테스트와 문서로 뒷받침 (Test, Documentation)
4. Fast! (Profiling, Compile, Parallelization)

### 핵심
1. Documentation
   - TOP_LEVEL/README.md 작성
   - /docs/ 추가 후 작성
   - 소스코드에 docstring 작성
2. Testing (TDD 활용)
   - tests/ 추가
   - pytest.unittest module 활용
3. Good structure
   - Refactoring
4. Source control
5. PEP8
6. Virtual environment (Docker, Anaconda, ...)
7. Continous Integration & Automated deployment
   