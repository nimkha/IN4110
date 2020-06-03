import pylab as pl
import numpy as np
import sys
from matplotlib.colors import ListedColormap
import handling_the_data.data as data_handler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


def plot_classifier(classifier, dataset, target, first_feat, second_feat):
    """
    Visualizes the result for two features. Added feature that stores the image
    :param classifier: which classifier you wish to use
    :param dataset: the complete dataset
    :param target: target values. (in our case its the diabetes column)
    :param first_feat: the first feature
    :param second_feat: the second feature
    :return: no return value
    """
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

    X = dataset[[first_feat, second_feat]]
    y = target.replace(['pos', 'neg'], [1, 0])
    lable = ["neg", "pos"]
    classifier.fit(X, y)

    x_min, x_max = X.iloc[:, 0].min() - .1, X.iloc[:, 0].max() + .1
    y_min, y_max = X.iloc[:, 1].min() - .1, X.iloc[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)
    pl.figure()
    pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    pl.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap=cmap_bold)
    formatter = pl.FuncFormatter(lambda i, *args: lable[int(i)])
    pl.colorbar(ticks=[0, 1], format=formatter)

    pl.xlabel(first_feat)
    pl.ylabel(second_feat)
    pl.axis('tight')
    fig = pl.gcf()
    pl.show()
    fig.savefig(f"../visualization_through_web_app/static/{first_feat}X{second_feat}.png")


if __name__ == "__main__":
    training_data, validation_data = data_handler.get_data("../diabetes.csv")
    y_training_values = training_data.iloc[:, 9]
    x_training_values = training_data.iloc[:, 1:9]
    y_validation_values = validation_data.iloc[:, 9]
    x_validation_values = validation_data.iloc[:, 1:9]

    plot_classifier(KNeighborsClassifier(n_neighbors=5), x_training_values, y_training_values, "insulin", "age")
    plot_classifier(SVC(gamma='scale'), x_training_values, y_training_values, "glucose", "pregnant")
    plot_classifier(LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=200), x_training_values,
                    y_training_values, "triceps", "pressure")
