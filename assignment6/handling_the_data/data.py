import pandas as pd
import matplotlib.pyplot as plt
import sys

def read_data(filename):
    """
    Loading data from a csv file to a Pandas DataFrame
    :param filename:csv filename
    :return:DataFrame
    """
    data = pd.read_csv(filename, sep=",")
    data = data.dropna(how='any')
    return data


def split_data(data):
    """
    takes in data and splits it into 80/20 test/validation sets. It also makes sure the diabetes pos/neg ratio is the same
    :param data: pandas dataframe list
    :return: trainingset and validationset as tuple of pandas dataframes
    """
    diabetes_positive = data[data["diabetes"] == "pos"]
    diabetes_negative = data[data["diabetes"] == "neg"]

    diabetes_positive_copy = diabetes_positive.copy()
    diabetes_negative_copy = diabetes_negative.copy()

    training_set_positive = diabetes_positive_copy.sample(frac=0.80, random_state=0)
    validation_set_positive = diabetes_positive_copy.drop(training_set_positive.index)

    training_set_negative = diabetes_negative_copy.sample(frac=0.80, random_state=0)
    validation_set_negative = diabetes_negative_copy.drop(training_set_negative.index)

    training_frames = [training_set_positive, training_set_negative]
    validation_frames = [validation_set_positive, validation_set_negative]

    training_data = pd.concat(training_frames)
    validation_data = pd.concat(validation_frames)

    return training_data, validation_data


def visualisation(data_set, column_x, column_y, title="Data analysis"):
    """
    Brings a scatter plot visualisation to your dataset
    :param data_set: complete dataset
    :param column_x: name of column X (must be in the complete dataset)
    :param column_y: name of column Y (must be in the complete dataset)
    :param title: optional title of image
    :return: no return value. (only displays image)
    """
    groups = data_set.groupby('diabetes')
    fig, ax = plt.subplots()
    for name, g in groups:
        ax.scatter(g[column_x], g[column_y], label=name)
    ax.legend()

    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(title)
    plt.show()


def get_data(file_name):
    """
    takes a filename and return a split dataset.
    :param file_name: name of source file
    :return: return training and validation sets as a tuple
    """
    diabetes_data = read_data(file_name)
    return split_data(diabetes_data)


def run():
    """
    reads input-arguments from terminal and calls functions to create scatterplots.
    :return: None
    """

    filename = sys.argv[1]
    x_axis = sys.argv[2]
    y_axis = sys.argv[3]
    training_data, validation_data = get_data(filename)

    visualisation(validation_data, x_axis, y_axis, "Validation")
    visualisation(training_data, x_axis, y_axis, "Training")


if __name__ == "__main__":
    print("========== TEST START ==========")

    training_data, validation_data = get_data(sys.argv[1])
    visualisation(validation_data, sys.argv[2], sys.argv[3], "Validation")
    visualisation(training_data, sys.argv[2], sys.argv[3], "Training")

    print("========== TEST END ==========")

