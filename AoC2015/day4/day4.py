from hashlib import md5
import multiprocessing
from joblib import Parallel, delayed
input = "iwrupvqb"

N = 50
def check_hash(num: str) -> bool:
    encode_input = (input+num).encode()
    return md5(encode_input).hexdigest().startswith('000000')

def checker(i: int) -> int:
    j = i
    while True:
        if check_hash(str(j)):
            return j
        j += N

parallel = Parallel(n_jobs=N)
results = parallel(delayed(checker)(i) for i in range(1,N+1))
for result in results:
    print(result)
print("-"*50)
print(min(results))

