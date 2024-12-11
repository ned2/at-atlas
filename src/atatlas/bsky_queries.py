from atproto import models


def get_feed_all(actor: str) -> list[models.AppBskyFeedDefs.FeedViewPost]:
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


def get_follows_all(actor: str) -> list[models.AppBskyActorDefs.ProfileView]:
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
