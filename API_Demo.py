import json

import ibm_cloud_sdk_core
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

# authenticator = IAMAuthenticator('{apikey}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01'
)

natural_language_understanding.set_service_url('https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/a493cc01-e1ed-4846-8afb-e7324c948070')


with open('products.txt', 'r') as fd:
    for line in fd.readlines():
        url = line.strip()
        print(f"URL: {url}")

        try:
            response = natural_language_understanding.analyze(
                url=url,
                features=Features(categories=CategoriesOptions(limit=3))).get_result()
            print(json.dumps(response, indent=2))
        except ibm_cloud_sdk_core.api_exception.ApiException:
            print("ibm_cloud_sdk_core.api_exception.ApiException")

        print("#" * 60)

