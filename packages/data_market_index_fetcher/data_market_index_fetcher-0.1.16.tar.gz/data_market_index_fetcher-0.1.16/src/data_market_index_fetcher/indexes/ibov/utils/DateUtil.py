import pandas as pd

class DateUtil:
    @staticmethod
    def is_valid_date(date_string):
      try:
        # Tenta converter a string para datetime no Pandas
        pd.to_datetime(date_string, format="%Y-%m-%d", errors="raise")
        return True
      except ValueError:
        return False