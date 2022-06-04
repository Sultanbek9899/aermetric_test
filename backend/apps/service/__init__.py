from django.db.models import TextChoices


class EventType(TextChoices):
    TYPE_PRE_LEGEND = "PRE_LEGEND", "PreLegend"
    TYPE_REPEAT_LEGEND = "REPEAT_LEGEND", "Repeat Legend"
    TYPE_LEGEND = "LEGEND", "Legend"
    TYPE_UPPER_A = "UPPER_A", "Upper A"
    TYPE_PAIRED_B = "PAIRED_B", "Paired B"
    TYPE_PAIRED_A = "PAIRED_A", "Paired A"
    TYPE_LOWER_A = "LOWER_A", "Lower A"
    TYPE_LOWER_B = "LOWER_B", "Lower B"
    TYPE_WARNING = "WARNING", "Warning"

