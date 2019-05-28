import pickle


def put_pickle(file, params):
    try:
        with open(file, 'wb') as f:
            pickle.dump(params, f)
    finally:
        f.close()


def get_pickle(file):
    try:
        with open(file, 'rb') as f:
            res = pickle.load(f)
    finally:
        f.close()
    return res
