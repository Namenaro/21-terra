class Prediction:
    def __init__(self, event_uid, corrected_p):
        self.event_uid = event_uid
        self.corrected_p = corrected_p


class PredictionsSession:
    def __init__(self):
        self.points_events={}      # {abspoint: [uid]}
        self.points_predictions={} # {abspoint: {event_uid: corrected_p}}

    def register_prediction(self, prediction, abspoint):
        if abspoint not in self.points_predictions:
            self.points_predictions[abspoint]= {prediction.event_uid: prediction.corrected_p}
        else:
            self.points_predictions[abspoint][prediction.event_uid] = prediction.corrected_p

    def register_event(self, event, abspoint):
        if abspoint not in self.points_events:
            self.points_events[abspoint]= [event.uid]
        else:
            self.points_events[abspoint].append(event.uid)

    def check_predicted_probability_of_event(self, event, abspoint):



class HypoPrediction:
    def __init__(self, test_uid, test_point, base_uid, context, test_uid_default_p):
        self.test_uid = test_uid
        self.base_uid = base_uid
        self.test_uid_defauil_p = test_uid_default_p

    def evaluate(self):
        ...
        prediction = Prediction(...)
        actual_p = ....
        significance = abs(self.test_uid_defauil_p - actual_p)
        return prediction, significance




