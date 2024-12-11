from atproto import Client, models, CAR


def get_feed_all(
    client: Client, actor: str
) -> list[models.AppBskyFeedDefs.FeedViewPost]:
    """Get all posts by an author."""
    cursor = None
    feed_view_posts = []
    while True:
        response = client.get_author_feed(actor=profile.did, cursor=cursor)
        feed_view_posts.extend(response.feed)
        if response.cursor is None:
            break
        cursor = response.cursor
    return feed_view_posts


def get_follows_all(
    client: Client, actor: str
) -> list[models.AppBskyActorDefs.ProfileView]:
    """Get all actors an actor follows."""
    cursor = None
    profile_views = []
    while True:
        response = client.get_follows(actor=profile.did, cursor=cursor)
        profile_views.extend(response.follows)
        if response.cursor is None:
            break
        cursor = response.cursor
    return profile_views


def get_pds_car(client: Client, did: str) -> CAR:
    """Get the complete PDS of a DID as a CAR object."""
    repo = client.com.atproto.sync.get_repo(
        params=models.com.atproto.sync.get_repo.Params(did=did)
    )
    return CAR.from_bytes(repo)
