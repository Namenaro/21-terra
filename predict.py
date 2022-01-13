class Prediction:
    def __init__(self):
        self.index_in_context
        self.step_memorzed
        self.action_set
        self.onevent_uid
        self.event_uid_probability



class PredictionsRegisterInSession: #in abs coords 28x28 (В ск, не связанной с ни одной из программ)
    def __init__(self):
        pass

    def register_corrector(self, nontrivial_predictions, context):
        pass

    def _register_new_nontrivial_prediction(self, x_abs,y_abs, step, distr_on_events_uids):
        pass

    def is_event_rare_by_current_prediction(self, x_abs, y_abs, step, event_uid):
        return probability_of_event_uid_in_current_situation

    def _make_default_prediction_for_event(self):
        pass

    def _gather_stat_for_binary_events(self):
        pass
