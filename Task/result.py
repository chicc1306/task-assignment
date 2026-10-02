from Task.generation import chia 

def build (a,b):
    return {
        "cong": chia(a, b)
    }

if __name__ == "__main__":
    print (build (7,3))