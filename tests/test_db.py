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