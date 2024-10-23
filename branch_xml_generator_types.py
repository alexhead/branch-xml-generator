from typing import TypedDict, Required, NotRequired


class CoordinatesType(TypedDict):
    latitude: Required[str]
    longitude: Required[str]

class UrlsType(TypedDict):
    url: Required[str]
    add_url: NotRequired[str]
    info_page: NotRequired[str]

class BranchType(TypedDict):
    # required fields
    id: Required[str]
    name: Required[str]
    address: Required[str]
    country: Required[str]
    actualization_date: Required[str]
    coordinates: Required[CoordinatesType]
    rubric_id: Required[str]
    # optional fields
    phone: NotRequired[str]
    email: NotRequired[str]
    urls: NotRequired[UrlsType]
    working_time: NotRequired[str]
