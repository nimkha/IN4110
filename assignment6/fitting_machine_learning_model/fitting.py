import handling_the_data.data as data_handler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression


def log_reg_prediction(x_tr, y_tr, x_val, y_val):
    """
    Performs Logistic Regression training on given dataset
    :param x_tr: training values
    :param y_tr: training target values
    :param x_val: validation values
    :param y_val: validation target values
    :return: the accuracy score
    """
    lr = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr', max_iter=200).fit(x_tr, y_tr)
    lr_prediction = lr.predict(x_val)
    score = round(accuracy_score(lr_prediction, y_val), 2)

    print(f"logistic regression prediction: {score}")
    return score


def k_near_prediction(x_tr, y_tr, x_val, y_val):
    """
    Performs K neighbor training on given dataset
    :param x_tr: training values
    :param y_tr: training target values
    :param x_val: validation values
    :param y_val: validation target values
    :return: the accuracy score
    """
    knn = KNeighborsClassifier(n_neighbors=2).fit(x_tr, y_tr)
    knn_prediction = knn.predict(x_val)
    score = round(accuracy_score(knn_prediction, y_val), 2)

    print(f"knn prediction: {score}")
    return score


def svm_prediction(x_tr, y_tr, x_val, y_val):
    """
    Performs Support vector machine training on given dataset
    :param x_tr: training values
    :param y_tr: training target values
    :param x_val: validation values
    :param y_val: validation target values
    :return: the accuracy score
    """
    super_vec_machine = svm.SVC(decision_function_shape="ovo", gamma="auto").fit(x_tr, y_tr)
    svc_prediction = super_vec_machine.predict(x_val)
    score = round(accuracy_score(svc_prediction, y_val), 2)

    print(f"svm prediction: {score}")
    return score


if __name__ == "__main__":
    print("========== TEST START ==========\n")

    training_data, validation_data = data_handler.get_data("../diabetes.csv")
    y_training_values = training_data.iloc[:, 9]
    y_validation_values = validation_data.iloc[:, 9]

    # Training set with all features
    all_training_values = training_data.iloc[:, 1:9]
    all_validation_values = validation_data.iloc[:, 1:9]

    # Training set with 3 features
    three_training_values = training_data.iloc[:, 1:4]
    three_validation_values = validation_data.iloc[:, 1:4]

    # Training set with 5 features
    five_training_values = training_data.iloc[:, 2:7]
    five_validation_values = validation_data.iloc[:, 2:7]

    print("Testing with all features")
    k_near_prediction(all_training_values, y_training_values, all_validation_values, y_validation_values)
    svm_prediction(all_training_values, y_training_values, all_validation_values, y_validation_values)
    log_reg_prediction(all_training_values, y_training_values, all_validation_values, y_validation_values)
    print()

    print("Testing with 3 features")
    k_near_prediction(three_training_values, y_training_values, three_validation_values, y_validation_values)
    svm_prediction(three_training_values, y_training_values, three_validation_values, y_validation_values)
    log_reg_prediction(three_training_values, y_training_values, three_validation_values, y_validation_values)
    print()

    print("Testing with 5 features")
    k_near_prediction(five_training_values, y_training_values, five_validation_values, y_validation_values)
    svm_prediction(five_training_values, y_training_values, five_validation_values, y_validation_values)
    log_reg_prediction(five_training_values, y_training_values, five_validation_values, y_validation_values)
    print()

    print("========== TEST END ==========")