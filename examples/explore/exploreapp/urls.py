from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from multigtfs.models import (
    Agency, Block, Fare, FareRule, Feed, FeedInfo, Route, Service, ServiceDate,
    Shape, ShapePoint, Stop, StopTime, Trip, Zone)

from exploreapp.views import (
    ByFeedListView, FareRuleByFareListView, FareRuleByRouteListView,
    FrequencyByTripListView, ServiceDateByServiceListView,
    ShapePointByShapeListView, StopTimeByStopListView, StopTimeByTripListView,
    TripByBlockListView, TripByRouteListView, TripByServiceListView,
    TripByShapeListView)


urlpatterns = patterns(
    '',
    url(r'feed/$', ListView.as_view(model=Feed), name='feed_list'),
    url(r'feed/(?P<pk>\d+)/$', DetailView.as_view(model=Feed),
        name='feed_detail'),
    url(r'feed/(?P<feed_id>\d+)/agency/$',
        ByFeedListView.as_view(model=Agency),
        name='agency_list'),
    url(r'feed/(?P<feed_id>\d+)/agency/(?P<pk>\d+)/$',
        DetailView.as_view(model=Agency), name='agency_detail'),
    url(r'feed/(?P<feed_id>\d+)/stop/$',
        ByFeedListView.as_view(model=Stop),
        name='stop_list'),
    url(r'feed/(?P<feed_id>\d+)/stop/(?P<pk>\d+)/$',
        DetailView.as_view(model=Stop), name='stop_detail'),
    url(r'feed/(?P<feed_id>\d+)/stop/(?P<stop_id>\d+)/stoptime/$',
        StopTimeByStopListView.as_view(), name='stoptime_by_stop_list'),
    url(r'feed/(?P<feed_id>\d+)/stoptime/(?P<pk>\d+)/$',
        DetailView.as_view(model=StopTime), name='stoptime_detail'),
    url(r'feed/(?P<feed_id>\d+)/trip/(?P<pk>\d+)/$',
        DetailView.as_view(model=Trip), name='trip_detail'),
    url(r'feed/(?P<feed_id>\d+)/trip/(?P<trip_id>\d+)/frequency/$',
        FrequencyByTripListView.as_view(), name='frequency_by_trip_list'),
    url(r'feed/(?P<feed_id>\d+)/trip/(?P<trip_id>\d+)/stoptime/$',
        StopTimeByTripListView.as_view(), name='stoptime_by_trip_list'),
    url(r'feed/(?P<feed_id>\d+)/route/(?P<route_id>\d+)/farerule/$',
        FareRuleByRouteListView.as_view(), name='farerule_by_route_list'),
    url(r'feed/(?P<feed_id>\d+)/route/(?P<route_id>\d+)/trip/$',
        TripByRouteListView.as_view(), name='trip_by_route_list'),
    url(r'feed/(?P<feed_id>\d+)/route/$',
        ByFeedListView.as_view(model=Route),
        name='route_list'),
    url(r'feed/(?P<feed_id>\d+)/route/(?P<pk>\d+)/$',
        DetailView.as_view(model=Route), name='route_detail'),
    url(r'feed/(?P<feed_id>\d+)/service/$',
        ByFeedListView.as_view(model=Service),
        name='service_list'),
    url(r'feed/(?P<feed_id>\d+)/service/(?P<pk>\d+)/$',
        DetailView.as_view(model=Service), name='service_detail'),
    url(r'feed/(?P<feed_id>\d+)/service/(?P<service_id>\d+)/servicedate/$',
        ServiceDateByServiceListView.as_view(),
        name='servicedate_by_service_list'),
    url(r'feed/(?P<feed_id>\d+)/service/(?P<service_id>\d+)/trip/$',
        TripByServiceListView.as_view(), name='trip_by_service_list'),
    url(r'feed/(?P<feed_id>\d+)/servicedate/(?P<pk>\d+)/$',
        DetailView.as_view(model=ServiceDate), name='servicedate_detail'),
    url(r'feed/(?P<feed_id>\d+)/shape/$',
        ByFeedListView.as_view(model=Shape),
        name='shape_list'),
    url(r'feed/(?P<feed_id>\d+)/shape/(?P<pk>\d+)/$',
        DetailView.as_view(model=Shape), name='shape_detail'),
    url(r'feed/(?P<feed_id>\d+)/shape/(?P<shape_id>\d+)/shapepoint/$',
        ShapePointByShapeListView.as_view(), name='shapepoint_by_shape_list'),
    url(r'feed/(?P<feed_id>\d+)/shape/(?P<shape_id>\d+)/trip/$',
        TripByShapeListView.as_view(), name='trip_by_shape_list'),
    url(r'feed/(?P<feed_id>\d+)/shapepoint/(?P<pk>\d+)$',
        DetailView.as_view(model=ShapePoint), name='shapepoint_detail'),
    url(r'feed/(?P<feed_id>\d+)/fare/$',
        ByFeedListView.as_view(model=Fare),
        name='fare_list'),
    url(r'feed/(?P<feed_id>\d+)/fare/(?P<pk>\d+)/$',
        DetailView.as_view(model=Fare), name='fare_detail'),
    url(r'feed/(?P<feed_id>\d+)/fare/(?P<fare_id>\d+)/farerule$',
        FareRuleByFareListView.as_view(), name='farerule_by_fare_list'),
    url(r'feed/(?P<feed_id>\d+)/farerule/(?P<pk>\d+)/$',
        DetailView.as_view(model=FareRule), name='farerule_detail'),
    url(r'feed/(?P<feed_id>\d+)/feedinfo/$',
        ByFeedListView.as_view(model=FeedInfo),
        name='feedinfo_list'),
    url(r'feed/(?P<feed_id>\d+)/feedinfo/(?P<pk>\d+)/$',
        DetailView.as_view(model=FeedInfo), name='feedinfo_detail'),
    url(r'feed/(?P<feed_id>\d+)/zone/$',
        ByFeedListView.as_view(model=Zone),
        name='zone_list'),
    url(r'feed/(?P<feed_id>\d+)/zone/(?P<pk>\d+)/$',
        DetailView.as_view(model=Zone), name='zone_detail'),
    url(r'feed/(?P<feed_id>\d+)/block/$',
        ByFeedListView.as_view(model=Block),
        name='block_list'),
    url(r'feed/(?P<feed_id>\d+)/block/(?P<pk>\d+)/$',
        DetailView.as_view(model=Block), name='block_detail'),
    url(r'feed/(?P<feed_id>\d+)/block/(?P<block_id>\d+)/trip/$',
        TripByBlockListView.as_view(), name='trip_by_block_list'),
)