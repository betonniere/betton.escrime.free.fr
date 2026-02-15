
class Language:
    pool = []

    # ------------------------------------------------------------
    def __init__(self, code, name, title, subtitle):
        self.code     = code
        self.name     = name
        self.icon     = '/static/images/languages/' + code + '.gif'
        self.title    = title
        self.subtitle = subtitle

        Language.pool.append(self)
