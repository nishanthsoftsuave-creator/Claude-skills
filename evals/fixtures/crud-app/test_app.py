import app


def test_add_and_list(tmp_path, monkeypatch):
    monkeypatch.setattr(app, "DB", str(tmp_path / "t.db"))
    app.init()
    app.add("bolt", 5)
    assert app.list_items() == [(1, "bolt", 5)]
