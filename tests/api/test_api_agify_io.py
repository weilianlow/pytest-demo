import pytest
from requests import get

@pytest.mark.parametrize("name,age,count", 
[("Adam", 36, "123000<{0}<124000"), 
 ("Betty", 60, "33900<{0}<34000")])
def test_get_age(name,age,count):
    # arrange
    uri = "https://api.agify.io/?name={0}"
    # act
    res = get(uri.format(name))
    # assert
    assert res.status_code ==   200
    assert res.json().get("age") , age
    assert eval(count.format(res.json().get("count")))