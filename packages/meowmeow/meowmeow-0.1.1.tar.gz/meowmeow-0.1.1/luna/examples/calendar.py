import json
import logging
import sys
from datetime import date, datetime
from pathlib import Path

import click
import pendulum

# from ics import Calendar, Event
import requests
from google.auth.transport.requests import AuthorizedSession

# import functions_framework
from google.oauth2.credentials import Credentials as Oauth2Credentials

# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
from ical.calendar import Calendar
from ical.calendar_stream import IcsCalendarStream
from ical.timezone import IcsTimezoneInfo


@click.group()
def cli():
    pass


# from ms_graph.client import MsGraphClient

log = logging.getLogger(__name__)

CURRENT_DIR = Path(__file__).parent

google_creds_path = CURRENT_DIR / "duan.leu@aliz.ai.json"
# ms_cache_path = CURRENT_DIR / "ms_graph_token_cache.json"
creds = Oauth2Credentials.from_authorized_user_info(json.load(open(google_creds_path)))
# service = build("calendar", "v3", credentials=creds)
session = AuthorizedSession(credentials=creds)
# ms_client = MsGraphClient(
#     application_id="1cb2b3e0-591a-41f7-a01c-2eb78b3c0f20",
#     token_cache_path=ms_cache_path,
# )


class GoogleService:
    def __init__(self, base_url: str, creds: "Oauth2Credentials"):
        self.base_url = base_url
        self.session = AuthorizedSession(creds)

    def _make_url(self, path: str):
        return self.base_url.rstrip("/") + "/" + path.lstrip("/")

    def request(self, method: str, path: str, **kwargs):
        res = self.session.request(method, self._make_url(path), **kwargs)
        res.raise_for_status()
        return res

    def get(self, path: str, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs):
        return self.request("POST", path, **kwargs)

    def delete(self, path: str, **kwargs):
        return self.request("DELETE", path, **kwargs)


calendar_service = GoogleService("https://www.googleapis.com/calendar/v3", creds)

# Parse the URL
url = "https://outlook.office365.com/owa/calendar/cc393df0754e4615b8876eb165ca9abc@flyscoot.com/725a89a19e4b4d36bd110609207daca914238869776473547957/calendar.ics"  # noqa


CALENDAR_ID = "duan.leu@aliz.ai"


@cli.command()
def next_events():
    # for event in service.events().list(calendarId=CALENDAR_ID).execute()["items"]:
    #     print(json.dumps(event, indent=2))

    for event in calendar_service.get(f"calendars/{CALENDAR_ID}/events").json()["items"]:
        print(json.dumps(event, indent=2))


@cli.command()
def sync_calendar():
    do_sync_calendar_2()


def naive(dt: datetime | date):
    if type(dt) is date:
        return dt
    tz = dt.tzinfo
    if isinstance(tz, IcsTimezoneInfo):
        name = str(tz)
        if name == "Singapore Standard Time":
            return pendulum.instance(dt).replace(tzinfo=pendulum.timezone("Asia/Singapore"))
        elif name == "SE Asia Standard Time":
            return pendulum.instance(dt).replace(tzinfo=pendulum.timezone("Asia/Ho_Chi_Minh"))
        else:
            raise RuntimeError("timzeon %s" % name)
    return dt.replace(tzinfo=None)


def _create_google_event_body(event: "Event"):  # noqa
    prefix = "x000"
    event_id: str = prefix + event.uid
    event_id = event_id.lower()
    for c in set(event_id):
        if not ("0" < c < "9" or "a" < c < "v"):
            event_id = event_id.replace(c, "")
    google_event = {
        "id": event_id,
        "summary": "MS: " + event.name,
        "colorId": "3",
    }
    google_event["location"] = event.location
    google_event["description"] = event.description.replace("\r\n", "")  # "<br>")
    print(event.begin.datetime, event.end.datetime)
    google_event["start"] = {
        "dateTime": naive(event.begin.datetime).isoformat(),
        "timeZone": "Asia/Ho_Chi_Minh",  # event.begin.timezone,
    }
    google_event["end"] = {
        "dateTime": naive(event.end.datetime).isoformat(),
        "timeZone": "Asia/Ho_Chi_Minh",  # event.end.timezone,
    }
    google_event["organizer"] = event.organizer
    return event_id, google_event


def do_sync_calendar_2():
    url = "https://outlook.office365.com/owa/calendar/cc393df0754e4615b8876eb165ca9abc@flyscoot.com/725a89a19e4b4d36bd110609207daca914238869776473547957/calendar.ics"
    cal = IcsCalendarStream.calendar_from_ics(requests.get(url).text)
    now = pendulum.now(pendulum.UTC)

    for event in cal.events:
        start = event.start
        start_date = pendulum.Date(start.year, start.month, start.day)

        if start_date > now.add(months=1).date() or start_date < now.subtract(days=1).date():
            continue
        if event.rrule:
            log.warning("skipping recurring event %s", event.summary)
            continue

        log.info("processing event %s", event.summary)
        log.info("  start at %s", event.start)
        log.info("  end at %s", event.end)
        # create google event
        prefix = "x000"
        event_id: str = prefix + event.uid
        event_id = event_id.lower()
        for c in set(event_id):
            if not ("0" < c < "9" or "a" < c < "v"):
                event_id = event_id.replace(c, "")

        to_delete = start_date < now.subtract(months=3).date() and 0
        if to_delete:
            try:
                # service.events().delete(calendarId=CALENDAR_ID, eventId=event.uid).execute()
                # continue
                req = session.delete(
                    f"https://www.googleapis.com/calendar/v3/calendars/{CALENDAR_ID}/events/{event.uid}"
                )
                req.raise_for_status()
            except Exception:
                continue

        google_event = {
            "id": event_id,
            "summary": "MS: " + event.summary,
            "colorId": "2",
        }
        google_event["location"] = event.location
        google_event["description"] = event.description.replace("\r\n", "")  # "<br>")
        # print(event.begin.datetime, event.end.datetime)
        google_event["start"] = {
            "timeZone": "Asia/Ho_Chi_Minh",  # event.begin.timezone,
        }
        if isinstance(event.start, datetime):
            google_event["start"]["dateTime"] = naive(event.start).isoformat()
        else:
            google_event["start"]["date"] = event.start.isoformat()
        google_event["end"] = {
            "timeZone": "Asia/Ho_Chi_Minh",  # event.end.timezone,
        }
        if isinstance(event.end, datetime):
            google_event["end"]["dateTime"] = naive(event.end).isoformat()
        else:
            google_event["end"]["date"] = event.end.isoformat()
        google_event["organizer"] = event.organizer
        is_canceled = event.summary.startswith("Canceled: ")
        handle_event(event_id=event_id, event=google_event, is_canceled=is_canceled)


def do_sync_calendar():
    now = pendulum.now(pendulum.UTC)
    cal = Calendar(requests.get(url).text)
    events = list(cal.events)
    events = sorted(events, key=lambda e: e.begin)
    for event in events:
        # continue.
        if event.begin.datetime < now.subtract(days=1):
            continue
        event_id, google_event = _create_google_event_body(event)
        print(json.dumps(google_event, indent=2))
        # continue
        # import sys
        # sys.exit(0)
        is_cancelled = event.name.startswith("Canceled: ")
        if is_cancelled:
            # delete the event
            try:
                service.events().delete(calendarId="duan.leu@aliz.ai", eventId=event_id).execute()
                log.info("event deleted %s", event["subject"])
                continue
            except HttpError as err:
                if err.resp.status in (410, 404):
                    # ignore
                    continue
                print(err.content.decode("utf8"))
                raise err

        # insert event to google calendar
        try:
            # # delete the event
            # service.events().delete(calendarId="duan.leu@aliz.ai", eventId=event_id).execute()
            # continue
            log.info("creating event %s", event_id)
            google_event = (
                service.events().insert(calendarId=CALENDAR_ID, body=google_event, sendUpdates="none").execute()
            )
            log.info("event created %s", google_event)
        except HttpError as err:
            if err.resp.status == 409:
                # update instead
                google_event = (
                    service.events()
                    .update(
                        calendarId=CALENDAR_ID,
                        eventId=event_id,
                        body=google_event,
                        sendUpdates="none",
                    )
                    .execute()
                )
                log.info("event updated %s", event)
                continue
            if err.resp.status == 404:
                # ignore
                continue
            print(err.content.decode("utf8"))
            raise err


# Register a CloudEvent function with the Functions Framework
# @functions_framework.http
# def http_entry(request):
#     sync_calendar()
#     log.info("done")
#     return "OK You are good"

from requests import HTTPError


def handle_event(*, event_id: str, event: dict, is_canceled: bool):
    # print(json.dumps(event, indent=2))
    if is_canceled:
        # delete the event
        try:
            calendar_service.delete(f"calendars/{CALENDAR_ID}/events/{event_id}")
            log.info("event deleted %s", event["summary"])
            return
        except HTTPError as err:
            if err.resp.status in (410, 404):
                # ignore
                return
            print(err.content.decode("utf8"))
            raise err

    # insert event to google calendar
    try:
        # # delete the event
        # service.events().delete(calendarId="duan.leu@aliz.ai", eventId=event_id).execute()
        # continue
        log.info("creating event")
        # google_event = service.events().insert(calendarId=CALENDAR_ID, body=event, sendUpdates="none").execute()
        raise NotImplementedError()
        log.info("event created")
    except HTTPError as err:
        resp = err.response
        if resp.status == 409:
            # update instead
            calendar_service.put(
                f"calendars/{CALENDAR_ID}/events/{event_id}",
                body=event,
                params={"sendUpdates": "none"},
            )

            log.info("event updated")
        elif err.resp.status == 404:
            # ignore
            return
        else:
            log.error(err.content.decode("utf8"))
            log.error("response %s %s", err.resp, type(err.resp))
            raise err


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stderr,
        format="%(asctime)s %(name)s %(levelname)s - %(message)s",
    )
    cli()
