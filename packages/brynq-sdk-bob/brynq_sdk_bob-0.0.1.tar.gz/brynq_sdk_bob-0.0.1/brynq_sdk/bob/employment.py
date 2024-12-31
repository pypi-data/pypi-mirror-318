import pandas as pd
import requests
from src.bob.schemas.employment import EmploymentSchema
from src.utils.validation_tracker import enhanced_validate_data, ValidationTracker
from typing import Tuple

class Employment:
    def __init__(self, bob):
        self.bob = bob

    def get(self) -> Tuple[pd.DataFrame, ValidationTracker]:
        request = requests.Request(method='GET',
                                   url=f"{self.bob.base_url}bulk/people/employment")
        data = self.bob.get_paginated_result(request)
        df = pd.json_normalize(
            data,
            record_path='values',
            meta=['employeeId']
        )
        df = self.bob.rename_camel_columns_to_snake_case(df)
        valid_contracts, invalid_contracts, tracker = enhanced_validate_data(df=df, schema=EmploymentSchema, debug=True)

        return valid_contracts, tracker