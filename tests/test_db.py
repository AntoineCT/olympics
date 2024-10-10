from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100

def test_countries_id():
    rows = db.get_countries(15)
    assert len(rows) == 1

def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 10000

def test_athletes_id():
    rows = db.get_athletes(16)
    assert len(rows) == 1

def test_disciplines():
    rows = db.get_disciplines()
    assert len(rows) > 40

def test_disciplines_id():
    rows = db.get_disciplines(20)
    assert len(rows) == 1

def test_teams():
    rows = db.get_teams()
    assert len(rows) > 1500

def test_teams_id():
    rows = db.get_teams(150)
    assert len(rows) == 1

def test_events():
    rows = db.get_events()
    assert len(rows) > 250

def test_events_id():
    rows = db.get_events(150)
    assert len(rows) == 1

def test_medals():
    rows = db.get_medals()
    assert len(rows) > 50

def test_medals_id():
    rows = db.get_medals(21)
    assert len(rows) == 1

def test_discipline_athletes():
    rows = db.get_discipline_athletes(45)
    assert len(rows) > 8

def test_collective_medals():
    rows = db.get_collective_medals(13)
    assert len(rows) > 10

def test_top_collective():
    rows = db.get_top_collective(5)
    assert len(rows) > 3

def test_individual_medals():
    rows = db.get_individual_medals()
    assert len(rows) > 14

def test_individual_medals_id():
    rows = db.get_individual_medals(4857)
    assert len(rows) > 3

def test_top_individual_():
    rows = db.get_top_individual()
    assert len(rows) > 5
