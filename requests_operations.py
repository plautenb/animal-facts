from typing import List, Union


from my_dataclasses import CatFact

class DataOperations:

    @staticmethod
    def from_data(data: Union[dict, List[dict]])-> Union['CatFact', List['CatFact']]:
        data = data if isinstance(data, list) else [data]
        cat_facts = []
        for single_data in data:
            cat_facts.append(CatFact.from_dict(single_data))
        return cat_facts[0] if len(cat_facts) == 1 else cat_facts
