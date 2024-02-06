import pytest
from requests import get

@pytest.mark.parametrize("post_id,expected_count",[
    (1,5),
    (2,5)
])
def test_comments(post_id, expected_count):
    # arrange
    get_param = dict()
    get_param["url"] = "https://jsonplaceholder.typicode.com/posts/1/comments"
    get_param["headers"] = {"content-type": "application/json"}
    # act
    res = get(**get_param)
    # assert
    assert res.status_code == 200
    assert len(res.json()) == expected_count