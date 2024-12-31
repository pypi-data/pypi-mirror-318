import pandas as pd
from brynq_sdk.functions import Functions

from src.bob.bank import Bank
from src.bob.employment import Employment
from src.bob.salaries import Salaries
from src.bob.schemas.people import PeopleSchema
from src.bob.work import Work


class People:
    def __init__(self, bob):
        self.bob = bob
        self.salaries = Salaries(bob)
        self.employment = Employment(bob)
        self.bank = Bank(bob)
        self.work = Work(bob)

    def get(self) -> pd.DataFrame:
        resp = self.bob.session.get(url=f"{self.bob.base_url}profiles")
        # Bob sucks with default fields so you need to do a search call to retrieve additional fields.
        additional_fields = [
            "personal.birthDate",
            "address.city",
            "address.postCode",
            "address.line1",
            "address.line2",
            "address.activeEffectiveDate",
            # "address.fullAddress",
            "address.country",
            "home.legalGender",
            "home.spouse.firstName",
            "home.spouse.surname",
            "home.spouse.birthDate",
            "home.spouse.gender",
            "internal.terminationReason",
            "internal.terminationDate",
            "internal.terminationType",
            "employee.lastDayOfWork"
        ]
        resp_additional_fields = self.bob.session.post(url=f"{self.bob.base_url}people/search",
                                                       json={
                                                           "fields": ["root.id"] + additional_fields,
                                                           "filters": []
                                                       })
        df_extra_fields = pd.json_normalize(resp_additional_fields.json()['employees'])
        resp.raise_for_status()
        data = resp.json()
        df = pd.json_normalize(data['employees'])
        df = pd.merge(df, df_extra_fields[["id"] + additional_fields], left_on='id', right_on='id')
        df = self.bob.rename_camel_columns_to_snake_case(df)
        valid_people, invalid_people = Functions.validate_data(df=df, schema=PeopleSchema, debug=True)

        return valid_people
