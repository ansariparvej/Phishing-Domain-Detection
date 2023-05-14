
from phishing_domain_detection.utils.main_utils import load_numpy_array_data
from phishing_domain_detection.exception import PhishingException
from phishing_domain_detection.logger import logging
from phishing_domain_detection.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from phishing_domain_detection.entity.config_entity import ModelTrainerConfig
import os
import sys
from sklearn.ensemble import RandomForestClassifier
from phishing_domain_detection.ml.metric.classification_metric import get_classification_score
from phishing_domain_detection.ml.model.estimator import PhishingModel
from phishing_domain_detection.utils.main_utils import save_object, load_object


class ModelTrainer:

    def __init__(self, model_trainer_config: ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact

            # Hyper Parameters
            self.n_estimators = self.model_trainer_config.n_estimators
            self.max_features = self.model_trainer_config.max_features
            self.max_depth = self.model_trainer_config.max_depth
            self.min_samples_split = self.model_trainer_config.min_samples_split
            self.min_samples_leaf = self.model_trainer_config.min_samples_leaf
        except Exception as e:
            raise PhishingException(e, sys)

    def train_model(self, x_train, y_train):
        try:
            rf_clf = RandomForestClassifier(n_estimators=self.n_estimators, max_features=self.max_features, max_depth=self.max_depth, min_samples_split=self.min_samples_split, min_samples_leaf=self.min_samples_leaf)
            rf_clf.fit(x_train, y_train)
            return rf_clf
        except Exception as e:
            raise e
    
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            # loading training array and testing array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )

            model = self.train_model(x_train, y_train)
            y_train_pred = model.predict(x_train)
            classification_train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)
            
            if classification_train_metric.f1_score <= self.model_trainer_config.expected_accuracy:
                raise Exception("Trained model is not good to provide expected accuracy")
            
            y_test_pred = model.predict(x_test)
            classification_test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            # Over-fitting and Under-fitting
            diff = abs(classification_train_metric.f1_score-classification_test_metric.f1_score)
            
            if diff > self.model_trainer_config.over_fitting_under_fitting_threshold:
                raise Exception("Model is not good try to do more experimentation.")

            preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            
            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path,exist_ok=True)
            sensor_model = PhishingModel(preprocessor=preprocessor,model=model)
            save_object(self.model_trainer_config.trained_model_file_path, obj=sensor_model)

            # model trainer artifact

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path, 
            train_metric_artifact=classification_train_metric,
            test_metric_artifact=classification_test_metric)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise PhishingException(e, sys)