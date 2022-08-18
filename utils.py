import pickle
import json
import numpy as np
import config

class SpeciesPrediction():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_model(self):
        with open (config.Model_file_path,"rb") as f:
            self.logistic_model = pickle.load(f)

        with open (config.json_file_path,"r") as f:
            self.json_data = json.load(f)

    def get_predicted_species(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data["columns"]))
        
        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalLengthCm
        test_array[3] = self.PetalWidthCm

        pred_species = self.logistic_model.predict([test_array])
        return pred_species


if __name__ == "__main__":

    SepalLengthCm = 5.7
    SepalWidthCm  = 4.4
    PetalLengthCm = 1.5
    PetalWidthCm  = 0.4

    Species_pred = SpeciesPrediction(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    Species_pred.get_predicted_species()


