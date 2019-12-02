class Treatments:
    def __init__(self, treat_id, treat_surgery, surgery_date, medication, med_start, med_end, responsible_abuse,
                 responsible_abandoned):
        self.treat_id = treat_id
        self.treat_surgery = treat_surgery
        self.surgery_date = surgery_date
        self.medication = medication
        self.med_start = med_start
        self.med_end = med_end
        self.responsible_abuse = responsible_abuse
        self.responsible_abandoned = responsible_abandoned

    def __str__(self):
        return_str = "Sanctuary Identification: " + self.treat_id + "|"
        return_str += "Surgery: " + self.treat_surgery + "|"
        return_str += "Surgery date: " + self.surgery_date + "|"
        return_str += "Medication: " + self.medication + "|"
        return_str += "Medication start: " + self.med_start + "|"
        return_str += "Medication end: " + self.med_end + "|"
        return_str += "Responsible for abuse: " + self.responsible_abuse + "|"
        return_str += "Responsible for abandoned: " + self.responsible_abandoned + "|"
        return return_str
