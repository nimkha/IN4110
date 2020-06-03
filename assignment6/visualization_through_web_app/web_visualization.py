from flask import Flask, render_template
from fitting_machine_learning_model import fitting
from handling_the_data import data

app = Flask(__name__)


@app.route("/docs")
def get_docs():
    """
    Get the documentation page created by sphinx
    :return: a rendered sphinx_docs.html
    """
    return render_template("docs.html")


@app.route("/")
def show_images():
    """
    Displays 3 different plot images and 3x3 score of different AI learning methods
    :return: a rendered docs.html
    """
    training_data, validation_data = data.get_data("../diabetes.csv")
    y_training_values = training_data.iloc[:, 9]
    all_training_values = training_data.iloc[:, 1:9]
    y_validation_values = validation_data.iloc[:, 9]
    all_validation_values = validation_data.iloc[:, 1:9]
    three_training_values = training_data.iloc[:, 1:4]
    three_validation_values = validation_data.iloc[:, 1:4]
    five_training_values = training_data.iloc[:, 2:7]
    five_validation_values = validation_data.iloc[:, 2:7]

    k_one = fitting.k_near_prediction(all_training_values, y_training_values, all_validation_values, y_validation_values)
    s_one = fitting.svm_prediction(all_training_values, y_training_values, all_validation_values, y_validation_values)
    l_one = fitting.log_reg_prediction(all_training_values, y_training_values, all_validation_values, y_validation_values)

    k_two = fitting.k_near_prediction(three_training_values, y_training_values, three_validation_values, y_validation_values)
    s_two = fitting.svm_prediction(three_training_values, y_training_values, three_validation_values, y_validation_values)
    l_two = fitting.log_reg_prediction(three_training_values, y_training_values, three_validation_values, y_validation_values)

    k_three = fitting.k_near_prediction(five_training_values, y_training_values, five_validation_values, y_validation_values)
    s_three = fitting.svm_prediction(five_training_values, y_training_values, five_validation_values, y_validation_values)
    l_three = fitting.log_reg_prediction(five_training_values, y_training_values, five_validation_values, y_validation_values)

    return render_template("index.html",
                           first_image="static/glucoseXpregnant.png",
                           second_image="static/insulinXage.png",
                           third_image="static/tricepsXpressure.png",
                           knn_score_one=k_one, svm_score_one=s_one, lg_score_one=l_one,
                           knn_score_two=k_two, svm_score_two=s_two, lg_score_two=l_two,
                           knn_score_three=k_three, svm_score_three=s_three, lg_score_three=l_three)


if __name__ == "__main__":
    app.run(port=5001)
