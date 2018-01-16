import numpy as np
from collections import defaultdict

import pkg_resources
import os

DATA_PATH = pkg_resources.resource_filename('grader', 'data/')
MODEL_PATH = os.path.join(DATA_PATH, 'baseline_weights.npy')

feature_list = ['goout', 'school', 'schoolsup', 'failures', 'higher', 'subject', 'intercept']
    
class Model(object):

    def __init__(self, ):
        self.load_weights(MODEL_PATH)

    def load_weights(self, path):
        with open(path, 'rb') as f:
            model_weights = np.load(f)
        self.check_weights(model_weights)
        self.weights = model_weights
    
    def check_weights(self, weights):
        assert weights.shape == (3, len(feature_list))

    def predict(self, X):
        assert(isinstance(X, Student))
        prediction = np.dot(self.weights, X)
        return {'G1':prediction[0], 'G2':prediction[1], 'G3':prediction[2]}

class Student(list):
    
    def __init__(self, **kwargs):
        student_ = defaultdict(lambda : 0)
        for feature_name, feature_value in kwargs.items():
            assert(feature_name in feature_list)
            student_[feature_name] = float(feature_value[0])
        for feature_name in feature_list[:-1]:
            self.append(student_[feature_name])
        self.append(1)
    
