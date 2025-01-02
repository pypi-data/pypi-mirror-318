def first():
    print("""import random
import csv
data = []
with open ('enjoysport.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
print(data)
n = len(data[0])-1
hypothesis = data[0].copy()[:-1]
print('Initial hypothesis', hypothesis)
for i in range (0, len(data)):
    if data[i][n] == 'Y':
        for j in range (0, n):
            if hypothesis[j] != '?' and hypothesis[j] != data[i][j]:
                hypothesis[j] = '?'
    print('Hypothesis after {} iteration {}'.format(i+1, hypothesis))
print('Final Hypothesis : ', hypothesis)""")

def second():
    print("""import numpy as np
import pandas as pd
import csv
X = []
y = []
with open ('enjoysport.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        X.append(row[:-1])
        y.append(row[-1])
def learn (X, y):
    n = len(X[0])
    specific = X[0].copy()
    general = [['?' for _ in range(n)] for _ in range(n)]
    for i, h in enumerate(X):
        if y[i] == 'Y':
            for x in range (n):
                if h[x] != specific[x]:
                    specific[x] = '?'
                    general[x][x] = '?'
        elif y[i] == 'N':
            for x in range (n):
                if h[x] != specific[x]: general[x][x] = specific[x]
                else: general[x][x] = '?'
    indices = [i for i, val in enumerate(general) if val == (['?'] * n)]
    for _ in indices: general.remove(['?'] * n)
    return specific, general
specific, general = learn(X,y)
print('Specific hypothesis', specific, sep='\n')
print()
print('General hypothesis', general, sep='\n')""")

def third():
    print("""import math
import csv
import pandas as pd
import numpy as np
def load_dataset():
    reader = csv.reader(open('PlayTennis.csv', 'r'))
    data = list(reader)
    header = data.pop(0)
    return data, header
class Node:
    def __init__ (self, attribute):
        self.attribute = attribute
        self.children = []
        self.answer = ""
def subtables (data, col, delete):
    dic = {}
    colData = [row[col] for row in data]
    attr = list(set(colData))
    for k in attr: dic[k] = []
    for y in range (len(data)):
        key = data[y][col]
        if delete: del data[y][col]
        dic[key].append(data[y])
    return attr, dic
def entropy (S):
    attr = list(set(S))
    if len(attr) == 1: return 0
    counts = [0] * len(attr)
    for i in range (len(attr)): counts[i] = sum( [1 for x in S if x == attr[i]]) / (len(S) * 1.0)
    sums = 0
    for cnt in counts: sums += -1 * cnt * math.log(cnt,2)
    return sums
def compute_gain (data, col):
    attr, dic = subtables (data, col, delete=False)
    total_entropy = entropy([row[-1] for row in data])
    for x in range (len(attr)):
        ratio = len(dic[attr[x]]) / (len(data) * 1.0)
        entro = entropy([ row[-1] for row in dic[attr[x]] ])
        total_entropy -= ratio * entro
    return total_entropy
def build_tree (data, header):
    y = [row[-1] for row in data]
    if len(set(y)) == 1:
        node = Node("")
        node.answer = y[0]
        return node
    n = len(data[0])-1
    gains = [compute_gain(data, col) for col in range(n)]
    split = gains.index(max(gains))
    node = Node(header[split])
    fea = header[:split] + header[split+1:]
    attr, dic = subtables(data, split, delete=True)
    for x in range (len(attr)):
        child = build_tree(dic[attr[x]], fea)
        node.children.append((attr[x], child))
    return node
def print_tree (node, level):
    if node.answer != "":
        print("---"*level, node.answer)
        return
    print("---"*level, node.attribute)
    for value, n in node.children:
        print("---"*(level+1), value)
        print_tree(n, level+2)
data, header = load_dataset()
node = build_tree(data, header)
print_tree(node, 0)""")

def fourth():
    print("""import numpy as np
from numpy import random as rand
X = np.array(( [2,9], [1,5], [3,6] ), dtype=float)
y = np.array(( [92], [86], [89] ), dtype=float)
X = X / np.amax(X, axis=0)
y = y / 100
def sigmoid (x):
    return 1 / (1 + np.exp(-x))
def sigmoid_grad (x):
    return x * (1 - x)
epoch = 1000
eta = 0.2

input_neurons = len(X[0])
hidden_neurons = 3
output_neurons = len(y[0])

wh = rand.uniform(size = (input_neurons, hidden_neurons))
bh = rand.uniform(size = (1, hidden_neurons))

wout = rand.uniform(size = (hidden_neurons, output_neurons))
bout = rand.uniform(size = (1, output_neurons))

for _ in range (epoch):
    
    h_ip = np.dot(X, wh) + bh
    h_act = sigmoid(h_ip)
    
    o_ip = np.dot(h_act, wout) + bout
    o_act = sigmoid(o_ip)
    
    e_o = y - o_act
    out_grad = sigmoid_grad(o_act)
    d_output = e_o * out_grad
    
    e_h = d_output.dot(wout.T)
    hidden_grad = sigmoid_grad(h_act)
    d_hidden = e_h * hidden_grad
    
    wout += h_act.T.dot(d_output) * eta
    wh += X.T.dot(d_hidden) * eta
print("Normalised Input", X, sep='\n')
print()
print("Actual Output", y, sep='\n')
print()
print("Predicted Output", o_act, sep='\n')""")

def fifth():
    print("""import pandas as pd
from sklearn.model_selection import train_test_split as split
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn import metrics
data = pd.read_csv('data6.csv', names=['message', 'result'])
data.shape
data['target'] = data.result.map({'pos':1, 'neg':0})
X = data['message']
y = data['target']
x_train, x_test, y_train, y_test = split(X, y)
print(x_train.shape)
print(x_test.shape)
vect = CV()
x_train_dtm = vect.fit_transform(x_train)
x_test_dtm = vect.transform(x_test)
print('Features extracted using CV', x_train_dtm.shape[1])
df = pd.DataFrame(x_train_dtm.toarray(), columns=vect.get_feature_names_out())
print(df)
clf = MNB().fit(x_train_dtm, y_train)
predicted = clf.predict(x_test_dtm)
for x, y in zip(x_test, predicted):
    print(x, y)

print('Accuracy Metrics\n')
print('Accuracy', metrics.accuracy_score(y_test, predicted))
print('Recall', metrics.recall_score(y_test, predicted))
print('Precision', metrics.precision_score(y_test, predicted))
print('Confusion Matrix\n')
print(metrics.confusion_matrix(y_test, predicted))""")

def sixth():
    print("""import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

data = pd.read_csv("data6.csv")
heart_disease = pd.DataFrame(data)

print(heart_disease)

model = BayesianModel([
    ('age', 'Lifestyle'),
    ('Gender', 'Lifestyle'),
    ('Family', 'heartdisease'),
    ('diet', 'cholestrol'),
    ('Lifestyle', 'diet'),
    ('cholestrol', 'heartdisease')
])

model.fit(heart_disease, estimator=MaximumLikelihoodEstimator)

HeartDisease_infer = VariableElimination(model)

print('For Age enter SuperSeniorCitizen:0, SeniorCitizen:1, MiddleAged:2, Youth:3, Teen:4')
print('For Gender enter Male:0, Female:1')
print('For Family History enter Yes:1, No:0')
print('For Diet enter High:0, Medium:1')
print('For LifeStyle enter Athlete:0, Active:1, Moderate:2, Sedentary:3')
print('For Cholesterol enter High:0, BorderLine:1, Normal:2')

q = HeartDisease_infer.query(variables=['heartdisease'], evidence = {
    'age': 3,          
    'Gender': 1,      
    'Family': 1,       
    'diet': 0,         
    'Lifestyle': 0,   
    'cholestrol': 2 
})

print(q)""")

def seventh():
    print("""import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture as GM
iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y = pd.DataFrame(iris.target)
y.columns = ['Target']
model = KMeans(n_clusters=3)
model.fit(X)
scaler = preprocessing.StandardScaler()
scaler.fit(X)
xsa = scaler.transform(X)
xs = pd.DataFrame(xsa, columns = X.columns)
gmm = GM(n_components=3)
gmm.fit(xs)
gmm_y = gmm.predict(xs)
plt.figure(figsize=(14,5))
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1,3,1)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y.Target], s=40)
plt.title('Real Clusters')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.subplot(1,3,2)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('KMeans Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.subplot(1,3,3)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[gmm_y], s=40)
plt.title('GMM Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()""")

def eighth():
    print("""from sklearn.model_selection import train_test_split as split
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn import datasets
iris = datasets.load_iris()
x_train, x_test, y_train, y_test = split(iris.data, iris.target, test_size=0.2)
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)
print('Target names', iris.target_names)
classifier = KNN(n_neighbors=1)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print('Accuracy', classifier.score(x_test, y_test))""")

def ninth():
    print("""import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def kernel (point, x_mat, k):
    m, n = np.shape(x_mat)
    weights = np.asmatrix(np.eye(m))
    for j in range (m):
        diff = point - X[j]
        weights[j,j] = np.exp(diff * diff.T / (-2.0 * k**2))
    return weights

def local_weight (point, x_mat, y_mat, k):
    weight = kernel(point, x_mat, k)
    return (X.T * (weight*X)).I * (X.T * (weight * y_mat.T))
def local_weight_regression (x_mat, y_mat, k):
    m, n = np.shape(x_mat)
    y_pred = np.zeros(m)
    for i in range (m):
        y_pred[i] = x_mat[i] * local_weight(x_mat[i], x_mat, y_mat, k)
    return y_pred
def graph_plot (X, y_pred):
    sort_index = X[:,1].argsort(0)
    x_sort = X[sort_index][:,0]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(bill, tip, color='green')
    ax.plot(x_sort[:,1], y_pred[sort_index], color='red', linewidth=5)
    plt.xlabel('Total bill')
    plt.ylabel('Tip')
    plt.show()
    
data = pd.read_csv('tips.csv')
bill = np.array(data.total_bill)
tip = np.array(data.tip)
m_bill = np.asmatrix(bill)
m_tip = np.asmatrix(tip)
m = np.shape(m_bill)[1]
one = np.asmatrix(np.ones(m))
X = np.hstack((one.T, m_bill.T))
y_pred = local_weight_regression(X, m_tip, 3)
graph_plot(X, y_pred)""")
