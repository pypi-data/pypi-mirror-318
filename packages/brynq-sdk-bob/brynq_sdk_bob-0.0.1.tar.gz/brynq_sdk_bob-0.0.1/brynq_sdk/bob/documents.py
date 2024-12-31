from datetime import datetime
import pandas as pd
from brynq_sdk.functions import Functions


class Documents:
    def __init__(self, bob):
        self.bob = bob
        # self.headers_upload = self.bob.headers.copy()
        # self.headers_upload['Content-Type'] = 'multipart/form-data'
        # self.headers_upload['Accept'] = 'application/json'

    def get(self, person_id: datetime) -> pd.DataFrame:
        resp = self.bob.session.get(url=f"{self.bob.base_url}docs/people/{person_id}")
        resp.raise_for_status()
        data = resp.json()['documents']
        df = pd.DataFrame(data)
        # data = self.bob.get_paginated_result(request)
        # df = pd.json_normalize(
        #     data,
        #     record_path='changes',
        #     meta=['employeeId']
        # )
        df = self.bob.rename_camel_columns_to_snake_case(df)
        valid_documents, invalid_documents = Functions.validate_data(df=df, schema=DocumentsSchema, debug=True)

        return valid_documents

    def create_confidential(self,
                            person_id: datetime,
                            file_name: str,
                            file_path: str):
        files = {"file": (file_name, open(file_path, "rb"), "application/pdf")}
        resp = self.bob.session.post(url=f"{self.bob.base_url}people/{person_id}/confidential/upload",
                                     files=files)
        resp.raise_for_status()

    # def create_shared(self, person_id: datetime):
    #     resp = self.bob.session.post(url=f"{self.bob.base_url}people/{person_id}/shared/upload")
    #     resp.raise_for_status()
