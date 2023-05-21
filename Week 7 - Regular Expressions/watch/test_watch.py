# Jesus Carlos Martinez Gonzalez
# 19/05/2023
# Watch on Youtube

from watch import parse


# Empty string
def test_no_string():
    assert parse('') == None


# Garbage string
def test_garbage():
    assert parse('Nlia3oM2XMs1FpCP5pvW') == None


# iframe but no youtube link within
def test_not_yt():
    assert parse('''<iframe width="560" height="315" src="https://www.twitch.tv/embed/xvFZjo5PgG0"
                 title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
                 encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''') == None


# iframe with youtube link within
def test_yt_url():
    assert parse('''<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
                 title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
                 encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''') == 'https://youtu.be/xvFZjo5PgG0'