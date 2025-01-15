from smolagents import Tool


class N8nPostTool(Tool):
    name = "post_to_social_media"
    description = """
    This is a tool that returns boolean value true if a post is successfully made to social media.
    It returns bool value false otherwise."""
    inputs = {
        "body": {
            "type": "string",
            "description": "the body of the social media post",
        },
        "link": {
            "type": "string",
            "description": "link to be shared with the social media post",
        },
        "thumbnail_url": {
            "type": "string",
            "description": "the thumbnail url to use with the social media post",
        },
    }
    output_type = "boolean"

    def forward(self, body: str, link: str, thumbnail_url: str) -> bool:
        # Code to post the social media post goes here
        return (
            True  # Replace this with actual logic to check if the post was successful
        )


post_to_social_media_tool = N8nPostTool()
