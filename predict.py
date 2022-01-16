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
        if abspoint in self.points_events:
            if event.uid in self.points_events[abspoint]:
                return None # не надо предсказывать уже известное
        if abspoint not in self.points_predictions:
            return event.p # по нему нет предсказаний
        if event.uid not in self.points_predictions[abspoint]:
            return event.p # по нему нет предсказаний
        corrected_p = self.points_predictions[abspoint][event.uid]
        return corrected_p # для него есть корректировка









