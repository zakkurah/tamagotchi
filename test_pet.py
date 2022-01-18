from tamagotchi import Pet


def test_init_pet():
    t = Pet(name="Fluffi", animal_type="Fisch")

    assert t.name == "Fluffi"
    assert t.animal_type == "Fisch"


def test_teach_pet():
    t = Pet(name="Fluffi", animal_type="Fisch")
    t.teach(word="rote Haare")

    assert "rote Haare" in t.vocab
    assert len(t.vocab) == 3

    assert t.__str__() == "I'm Fluffi, I feel bored."

def test_