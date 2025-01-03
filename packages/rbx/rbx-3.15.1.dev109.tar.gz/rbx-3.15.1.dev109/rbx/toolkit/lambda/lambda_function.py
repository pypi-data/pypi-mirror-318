import logging

from rbx.toolkit import Options, run

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger("sh").setLevel(logging.ERROR)


def handler(event, context):
    payload = event["payload"]

    run(
        options=Options(
            url=payload["url"],
            width=payload["width"],
            height=payload["height"],
            format=payload["format"],
            duration=int(payload.get("duration", 0)),
            output=payload.get(
                "output", "s3://474071279654-eu-west-1-dev/creatives/exports/"
            ),
            filename=payload.get("filename"),
        )
    )

    return "OK"
