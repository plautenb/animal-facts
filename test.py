import pytest

from cat_facts import CatFacts

class TestAnimalFacts:

    def test_get_one_fact(self):
        cat_facts = CatFacts(animal_type="cat",
                             amount=1)
        fact = cat_facts.get_cats_facts()
        assert fact.text, "No fact about cat received."


    @pytest.mark.parametrize("animal, amount",[
        ("cat", 2),
        ("dog", 3)],
        ids=["cat, 2 facts", "dog, 3 facts"])
    def test_get_many_facts(self, animal, amount):
        cat_facts = CatFacts(animal_type=animal,
                             amount=amount)
        facts = cat_facts.get_cats_facts()
        assert len(facts) == amount, "Wrong number of animal facts received."
        for fact in facts:
            assert fact.type == animal, "Fact about wrong animal received."


