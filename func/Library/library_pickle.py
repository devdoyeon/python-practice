import pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.

#= Dictionary Object인 data를 그대로 파일에 저장하는 방법
with open('test.txt', 'wb') as f1:
    data = {1: 'python', 2: 'java'}
    pickle.dump(data, f1)

#= pickle.dump로 저장한 파일을 pickle.load를 사용해 원래 있던 Dictionary Object 상태 그대로 불러오는 방법
with open('test.txt', 'rb') as f2:
    data = pickle.load(f2)
    print(data) # {1: 'python', 2: 'java'}