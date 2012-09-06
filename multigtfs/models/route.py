"""
Define Route model for rows in routes.txt

Google documentation from
https://developers.google.com/transit/gtfs/reference

routes.txt is required

- route_id (required)
The route_id field contains an ID that uniquely identifies a route. The
route_id is dataset unique.

- agency_id (optional)
The agency_id field defines an agency for the specified route. This value is
referenced from the agency.txt file. Use this field when you are providing data
for routes from more than one agency.

- route_short_name (required)
The route_short_name contains the short name of a route. This will often be a
short, abstract identifier like "32", "100X", or "Green" that riders use to
identify a route, but which doesn't give any indication of what places the
route serves. If the route does not have a short name, please specify a
route_long_name and use an empty string as the value for this field.

See a Google Maps screenshot highlighting the route_short_name:
  http://bit.ly/yIS1sa

- route_long_name (required)
The route_long_name contains the full name of a route. This name is generally
more descriptive than the route_short_name and will often include the route's
destination or stop. If the route does not have a long name, please specify a
route_short_name and use an empty string as the value for this field.

See a Google Maps screenshot highlighting the route_long_name:
  http://bit.ly/wZw5yH

- route_desc (optional)
The route_desc field contains a description of a route. Please provide useful,
quality information. Do not simply duplicate the name of the route. For
example, "A trains operate between Inwood-207 St, Manhattan and Far
Rockaway-Mott Avenue, Queens at all times. Also from about 6AM until about
midnight, additional A trains operate between Inwood-207 St and Lefferts
Boulevard (trains typically alternate between Lefferts Blvd and Far Rockaway)."

- route_type (required)
The route_type field describes the type of transportation used on a route.
Valid values for this field are:

    0 - Tram, Streetcar, Light rail. Any light rail or street level system
        within a metropolitan area.
    1 - Subway, Metro. Any underground rail system within a metropolitan area.
    2 - Rail. Used for intercity or long-distance travel.
    3 - Bus. Used for short- and long-distance bus routes.
    4 - Ferry. Used for short- and long-distance boat service.
    5 - Cable car. Used for street-level cable cars where the cable runs
        beneath the car.
    6 - Gondola, Suspended cable car. Typically used for aerial cable cars
        where the car is suspended from the cable.
    7 - Funicular. Any rail system designed for steep inclines.

See a Google Maps screenshot highlighting the route_type:
  http://bit.ly/wSt2h0

- route_url (optional)
The route_url field contains the URL of a web page about that particular route.
This should be different from the agency_url.

The value must be a fully qualified URL that includes http:// or https://, and
any special characters in the URL must be correctly escaped. See
  http://www.w3.org/Addressing/URL/4_URI_Recommentations.html
for a description of how to create fully qualified URL values.

- route_color (optional)
In systems that have colors assigned to routes, the route_color field defines a
color that corresponds to a route. The color must be provided as a
six-character hexadecimal number, for example, 00FFFF. If no color is
specified, the default route color is white (FFFFFF).

The color difference between route_color and route_text_color should provide
sufficient contrast when viewed on a black and white screen. The W3C Techniques
for Accessibility Evaluation And Repair Tools document offers a useful
algorithm for evaluating color contrast:
  http://www.w3.org/TR/AERT#color-contrast

There are also helpful online tools for choosing contrasting colors, including
the snook.ca Color Contrast Check application:
  http://snook.ca/technical/colour_contrast/colour.html

- route_text_color (optional)
The route_text_color field can be used to specify a legible color to use for
text drawn against a background of route_color. The color must be provided as a
six-character hexadecimal number, for example, FFD700. If no color is
specified, the default text color is black (000000).

The color difference between route_color and route_text_color should provide
sufficient contrast when viewed on a black and white screen.
"""

from csv import DictReader

from django.db import models

from multigtfs.models import Agency


class Route(models.Model):
    """A transit route"""

    feed = models.ForeignKey('Feed')
    route_id = models.CharField(
        max_length=255, db_index=True,
        help_text="Unique identifier for route.")
    agency = models.ForeignKey(
        'Agency', null=True, help_text="Agency for this route.")
    short_name = models.CharField(
        max_length=10,
        help_text="Short name of the route")
    long_name = models.CharField(
        max_length=255,
        help_text="Long name of the route")
    desc = models.TextField(
        blank=True,
        help_text="Long description of a route")
    rtype = models.IntegerField(
        choices=((0, 'Tram, Streetcar, or Light rail'),
                 (1, 'Subway or Metro'),
                 (2, 'Rail'),
                 (3, 'Bus'),
                 (4, 'Ferry'),
                 (5, 'Cable car'),
                 (6, 'Gondola or Suspended cable car'),
                 (7, 'Funicular')),
        help_text='Type of transportation used on route')
    url = models.URLField(
        verify_exists=False, blank=True,
        help_text="Web page about for the route")
    color = models.CharField(
        max_length=6, blank=True,
        help_text="Color of route in hex")
    text_color = models.CharField(
        max_length=6, blank=True,
        help_text="Color of route text in hex")

    def __unicode__(self):
        return u"%d-%s" % (self.feed.id, self.route_id)

    class Meta:
        db_table = 'route'
        app_label = 'multigtfs'

    _rel_to_feed = 'feed'  # TODO: Delete when I'm based on GTFSModel


def import_routes_txt(routes_file, feed):
    """Import routes.txt into Route records for feed

    Keyword arguments:
    routes_file -- A open routes.txt for reading
    feed -- the Feed to associate the records with
    """
    reader = DictReader(routes_file)
    name_map = dict(route_short_name='short_name', route_long_name='long_name',
                    route_desc='desc', route_type='rtype', route_url='url',
                    route_color='color', route_text_color='text_color')
    for row in reader:
        fields = dict((name_map.get(k, k), v) for k, v in row.items())
        agency_id = fields.pop('agency_id', None)
        if agency_id:
            agency = Agency.objects.get(feed=feed, agency_id=agency_id)
        else:
            agency = None
        Route.objects.create(feed=feed, agency=agency, **fields)